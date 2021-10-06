#!/usr/bin/env python
# coding: utf-8
import time
import re
import MeCab
import twint
import emoji
import nlplot
import sqlite3
import unicodedata
import numpy as np
import nest_asyncio
import pandas as pd
import pandas.io.sql as psql
from PIL import Image
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime
from collections import Counter
import matplotlib.pyplot as plt
from datetime import datetime, timedelta, timezone
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer

#時刻の取得し文字列で返す
def time_get(since,until,before):
    #今の時間
    now = datetime.now()
    #時間
    jh = timedelta(hours=9) 
    thb = timedelta(hours=int(before))
    #期間指定
    dt_since = datetime.strptime(since, '%Y-%m-%d %H:%M:%S')
    dt_until = datetime.strptime(until, '%Y-%m-%d %H:%M:%S')
    dt_since_thb = dt_until - thb
    dt_since_str = dt_since.strftime('%Y-%m-%d %H:%M:%S')
    dt_since_thb_str = dt_since_thb.strftime('%Y-%m-%d %H:%M:%S')
    dt_until_str = dt_until.strftime('%Y-%m-%d %H:%M:%S')
    # 基準がJSTの場合-9でUTC、逆は+9
    jst_until = now + jh
    jst_since = jst_until - thb
    utc_until = now
    utc_since = now - thb
    
    #時間を文字列へ変換
    jst_nowday_str = jst_until.strftime('%Y-%m-%d')
    jst_since_str = jst_since.strftime('%Y-%m-%d %H:%M:%S')
    jst_until_str = jst_until.strftime('%Y-%m-%d %H:%M:%S')
    utc_since_str = utc_since.strftime('%Y-%m-%d %H:%M:%S')
    utc_until_str = utc_until.strftime('%Y-%m-%d %H:%M:%S')
    return dt_since_str,dt_since_thb_str,dt_until_str,jst_nowday_str,jst_since_str,jst_until_str,utc_since_str,utc_until_str


#STOPリストの読み込み
def stop_word(text):
    with open(text, 'r') as f:
        stop_list = f.read().split(",")
    #STOPWORD強化
    for i,stop in enumerate(stop_list):
        STOPWORDS.add(stop)
    return STOPWORDS


#キーワード検索（日時指定）
def twint_word(word,like,filename,since,until):
    nest_asyncio.apply()
    c = twint.Config()
    c.Search = word
    c.Store_csv = True
    c.Output = filename
    c.Since = since
    c.Until = until
    c.Count = True
    c.Min_likes = like
    c.Hide_output = True
    twint.run.Search(c)

#ユーザー検索
def twint_user(data,numst,numen,like,filename,since,until):
    nest_asyncio.apply()
    for i,twi in enumerate(data.loc[numst:numen, "username"]):
        try:
            c = twint.Config()
            c.Username = twi
            c.Store_csv = True
            c.Output = filename
            c.Since = since
            c.Until = until
            c.Count = True
            c.Min_likes = like
            c.Hide_output = True
            twint.run.Search(c)
        except ValueError:
            continue

#プロフ検索
def twint_info(data,filename):
    nest_asyncio.apply()
    for i,twi in enumerate(data["username"]):
        try:
            c = twint.Config()
            c.Username = twi
            c.Pandas = True
            c.User_full = True
            c.Hide_output = False
            twint.run.Lookup(c)
        except KeyError:
            continue
    Users_df = twint.storage.panda.User_df

def inport_db(name,filename):
    try:
        dbname = "twint.db"
        db = sqlite3.connect(dbname)
        cur = db.cursor()
        df = pd.read_csv(filename, encoding="utf-8")
        df.to_sql(name, db, if_exists='append', index=None, method='multi', chunksize=1000)
        db.commit()
    except:
        db.close()

def export_db(table):
    try:
        dbname = "twint.db"
        db = sqlite3.connect(dbname)
        cur = db.cursor()
        df = pd.read_sql_query('SELECT * FROM ' + table, db)
        db.commit()
    except:
        db.close()
    return df

def sentence_clean(text):
    #絵文字削除
    result = ''.join(c for c in text if c not in emoji.UNICODE_EMOJI)
    #URL削除
    result = re.sub('https?://[\da-zA-Z!\?/\+\-_~=;\.,\*&@#\$%\(\)\'\[\]]+', '', result)
    #記号の削除
    code_regex = re.compile('[\t\s!"#$%&\\\\()*+-./:;；：<=>?@[\\]^_`{|}~○｢｣「」〔〕“”〈〉'    '『』【】＆＊（）＄＃＠？！｀＋￥¥％♪…◇→←↓↑｡･ω･｡ﾟ´∀｀ΣДｘ⑥◎©︎♡★☆▽※ゞノ〆εσ＞＜┌┘]')
    result = code_regex.sub(' ', result)
    return result

def sentence_tokenizer(text):
    # 分かち書きの中で使うオブジェクト生成
    # #tagger = MeCab.Tagger("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
    tagger = MeCab.Tagger() #設定ファイルに指定されてる。
    # ひらがなのみの文字列にマッチする正規表現
    kana_re = re.compile("^[ぁ-ゖ]+$")
    # ユニコード正規化
    text = unicodedata.normalize("NFKC", text)
    # 分かち書き
    parsed_lines = tagger.parse(text).split("\n")[:-2]
    surfaces = [l.split('\t')[0] for l in parsed_lines]
    features = [l.split('\t')[1] for l in parsed_lines]
    # 原型を取得
    bases = [f.split(',')[6] for f in features]
    # 品詞を取得
    pos = [f.split(',')[0] for f in features]
    # 各単語を原型に変換する
    token_list = [b if b != '*' else s for s, b in zip(surfaces, bases)]
    # 名詞,動詞,形容詞のみに絞り込み
    #target_pos = ["名詞","形容詞"]
    #target_pos = ["名詞"]
    #token_list = [t for t, p in zip(token_list, pos) if (p in target_pos)]
    # ひらがなのみの単語を除く
    # token_list = [t for t in token_list if not kana_re.match(t)]
    # アルファベットを小文字に統一
    token_list = [t.lower() for t in token_list]
    # 半角スペースを挟んで結合する。
    result = " ".join(token_list)
    # 念のためもう一度ユニコード正規化
    result = unicodedata.normalize("NFKC", result)
    return result

def string_clean(data,columns):
    text = ""
    for i,tweet in enumerate(data[columns]):
        text = text + ',' + tweet
    #文章前処理
    def text_clean(text):
        #絵文字削除
        result = ''.join(c for c in text if c not in emoji.UNICODE_EMOJI)
        #URL削除
        result = re.sub('https?://[\da-zA-Z!\?/\+\-_~=;\.,\*&@#\$%\(\)\'\[\]]+', '', result)
        #記号の削除
        code_regex = re.compile('[\t\s!"#$%&\\\\()*+-./:;；：<=>?@[\\]^_`{|}~○｢｣「」〔〕“”〈〉'    '『』【】＆＊（）＄＃＠？！｀＋￥¥％♪…◇→←↓↑｡･ω･｡ﾟ´∀｀ΣДｘ⑥◎©︎♡★☆▽※ゞノ〆εσ＞＜┌┘]')
        result = code_regex.sub(' ', result)
        return result
    result = text_clean(text)
    def mecab_tokenizer(text):
        # 分かち書きの中で使うオブジェクト生成
        # #tagger = MeCab.Tagger("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
        tagger = MeCab.Tagger() #設定ファイルに指定されてる。
        # ひらがなのみの文字列にマッチする正規表現
        kana_re = re.compile("^[ぁ-ゖ]+$")
        # ユニコード正規化
        text = unicodedata.normalize("NFKC", text)
        # 分かち書き
        parsed_lines = tagger.parse(text).split("\n")[:-2]
        surfaces = [l.split('\t')[0] for l in parsed_lines]
        features = [l.split('\t')[1] for l in parsed_lines]
        # 原型を取得
        bases = [f.split(',')[6] for f in features]
        # 品詞を取得
        pos = [f.split(',')[0] for f in features]
        # 各単語を原型に変換する
        token_list = [b if b != '*' else s for s, b in zip(surfaces, bases)]
        # 名詞,動詞,形容詞のみに絞り込み
        #target_pos = ["名詞","形容詞"]
        target_pos = ["名詞"]
        token_list = [t for t, p in zip(token_list, pos) if (p in target_pos)]
        # ひらがなのみの単語を除く
        # token_list = [t for t in token_list if not kana_re.match(t)]
        # アルファベットを小文字に統一
        token_list = [t.lower() for t in token_list]
        # 半角スペースを挟んで結合する。
        result = " ".join(token_list)
        # 念のためもう一度ユニコード正規化
        result = unicodedata.normalize("NFKC", result)
        return result
    result = mecab_tokenizer(result)
    return result

def con_list(filename,stop,text):
    token = text.split()
    con = Counter(token)
    count_list = []
    for word in con.most_common():
        count_list.append(word)
    con_df = pd.DataFrame(data=count_list, columns=['word',"count"])
    con_df.to_csv(filename, encoding='utf_8_sig')
    con_df = con_df[~con_df["word"].isin(stop)]
    con_df.to_csv("stopword+" + filename, encoding='utf_8_sig')

'''
#文章前処理
def text_clean(text):
    #絵文字削除
    result = ''.join(c for c in text if c not in emoji.UNICODE_EMOJI)
    #URL削除
    result = re.sub('https?://[\da-zA-Z!\?/\+\-_~=;\.,\*&@#\$%\(\)\'\[\]]+', '', result)
    #記号の削除
    code_regex = re.compile('[\t\s!"#$%&\\\\()*+-./:;；：<=>?@[\\]^_`{|}~○｢｣「」〔〕“”〈〉'    '『』【】＆＊（）＄＃＠？！｀＋￥¥％♪…◇→←↓↑｡･ω･｡ﾟ´∀｀ΣДｘ⑥◎©︎♡★☆▽※ゞノ〆εσ＞＜┌┘]')
    result = code_regex.sub(' ', result)
    return result

def mecab_tokenizer(text):
    # 分かち書きの中で使うオブジェクト生成
    # #tagger = MeCab.Tagger("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
    tagger = MeCab.Tagger() #設定ファイルに指定されてる。
    # ひらがなのみの文字列にマッチする正規表現
    kana_re = re.compile("^[ぁ-ゖ]+$")
    # ユニコード正規化
    text = unicodedata.normalize("NFKC", text)
    # 分かち書き
    parsed_lines = tagger.parse(text).split("\n")[:-2]
    surfaces = [l.split('\t')[0] for l in parsed_lines]
    features = [l.split('\t')[1] for l in parsed_lines]
    # 原型を取得
    bases = [f.split(',')[6] for f in features]
    # 品詞を取得
    pos = [f.split(',')[0] for f in features]
    # 各単語を原型に変換する
    token_list = [b if b != '*' else s for s, b in zip(surfaces, bases)]
    # 名詞,動詞,形容詞のみに絞り込み
    #target_pos = ["名詞","形容詞"]
    target_pos = ["名詞"]
    token_list = [t for t, p in zip(token_list, pos) if (p in target_pos)]
    # ひらがなのみの単語を除く
    # token_list = [t for t in token_list if not kana_re.match(t)]
    # アルファベットを小文字に統一
    token_list = [t.lower() for t in token_list]
    # 半角スペースを挟んで結合する。
    result = " ".join(token_list)
    # 念のためもう一度ユニコード正規化
    result = unicodedata.normalize("NFKC", result)

    return result
'''
def n_gram(text,x,y):
    vectrizer = CountVectorizer(tokenizer = mecab_tokenizer, ngram_range = (x, y))
    vectrizer.fit(sentence)
    print(vectrizer.vocabulary_)


#ワードクラウド化
def wd_cloud(token,font,back,wid,hei,maxw,color,png):
#マスク化処理
#mask_array = np.array(Image.open('python_wordcloud_mask_01.jpg'))
#image_color = ImageColorGenerator(mask_array)
    wordcloud = WordCloud(font_path=font,
                          #mask=mask_array,
                          background_color=back,
                          #max_font_size=200,
                          width=wid,
                          height=hei,
                          max_words=maxw,
                          #stopwords=stop,
                          colormap=color,
                          collocations=False).generate(token)
    wordcloud.to_file(png)



# %%
