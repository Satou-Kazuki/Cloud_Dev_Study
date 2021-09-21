# 最近流行りのクラウド仮想開発環境を構築しよう。
git,github,Docker,Vscode,クラウドサービス？なんですかそれは？という状態から、\
それぞれの要点を掻い摘んで、なんとか形にしていった時の流れと参考にしたことをまとめました。


◆目的◆
- ローカル環境に、github,Docker,VScodeを用いて、仮想開発環境を構築。
- クラウドサービス上に仮想マシンを起動させ、クラウド上に同じような仮想開発環境を構築。


◆ローカルマシン環境でのメリット◆
- パソコンごとに環境の選択やライブラリの選択や細々とした設定インストールをする必要がなくなります。
- コンテナ単位で環境を構築するので、問題が生じた環境の破棄及び再生成が容易になります。
- 先人が作成してくれた環境のパッケージを用いることにより、最小の労力で環境構築が行えます。


◆クラウドマシン環境でのメリット◆
- クラウド上にて仮想マシンに環境を構築しているので、RDPで接続するだけで同一環境で作業ができます。
- 環境を常時稼働させることが出来ます。（従量課金制なのでお金はかかります。1h10円くらい・・？）
- 耐障害性が高い。
- 仮想マシンの破棄、再生成が容易。
- 仮想マシンなので、何個でも生成できますし、複数稼働もできます。（従量課金制・・・・以下略
- クラウド上のマシンリソースを利用してるので、ローカル環境には負担がほぼかかりません。\


 →慣れたら仮想マシン作成、立ち上げから、開発環境一通り揃えるのに1時間ほどで行える。とても速い。


# Githubのアカウント作成 
- 参考:https://www.sejuku.net/blog/73468


# gitインストール
- https://git-scm.com/
- 参考:https://kitsune.blog/engineer/git


# VSCodeインストール 
- https://azure.microsoft.com/ja-jp/products/visual-studio-code/
- 参考github連携：https://breezegroup.co.jp/202102/vscode-github-windows/
- 参考Docker連携：https://qiita.com/Yuki_Oshima/items/d3b52c553387685460b0


# Dockerインストール
- https://www.docker.com/
- 参考：https://www.pasonatech.co.jp/workstyle/column/detail.html?p=2675
- 使ってるイメージファイル：https://hub.docker.com/r/jupyter/datascience-notebook/tags?page=1&ordering=last_updated
- 補足：DockerがBIOSのCPUの仮想化設定がDisableだとかで起動しない場合。https://mrkmyki.com/docker%E3%82%92%E8%B5%B7%E5%8B%95%E3%81%97%E3%82%88%E3%81%86%E3%81%A8%E3%81%97%E3%81%9F%E3%82%89%E3%80%8Chardware-assisted-virtualization-and-data-execution-protection-must-be-enabled-in-the-bios
- ちなみに、AMDのCPUの場合BIOS設定でSVMをEnableにすると動くかもしれないし動かないかもしれない。


# 上記インストールが終わったら、下記参考ページ
- Docker + VSCode + Remote Containerで作る快適Jupyter Lab(Python)分析環境
- https://qiita.com/sho-hata/items/02ad47f67bce6816a69a
- VSCode Remote Containerが良い
- https://qiita.com/d0ne1s/items/d2649801c6f804019db7
- docker-compose.yml の内容を理解しよう（Dockerで作るコンテナの設定ファイル）
- https://futureys.tokyo/lets-understand-contents-of-docker-compose-yml/
- dockerfileの作り方
- https://kitsune.blog/dockerfile-summary
- Python, pipでrequirements.txtを使ってパッケージ一括インストール
- https://note.nkmk.me/python-pip-install-requirements/
- Linuxを体系的に勉強するまとめ（linuxがからんでくるので、都度確認する用）
- https://kitsune.blog/engineer/linux


# ゼロから環境構築
◆Git、Docker、VSCodeインストール、Githubのアカウント作成◆\
VSCode内、下記拡張機能インストールを行う。\
【Japanese Language Pack , Python , Remote Development , Docker】\
◆githubのリポジトリからローカル環境へクローンする。◆\
https://github.com/Satou-Kazuki/Cloud_Dev_Study.git


◆リポジトリのクローン方法◆\
1.git bashから、コマンド入力で行う。\
2.VSCodeのフォルダ管理から行う。\
今回は2の方法を利用する。
  
  
◆クローン後の流れ◆\
クローンをすると、指定したフォルダ配下にローカルリポジトリが作成されて、まるまるコピーが作成される。\
クローンしたCloud_Dev_Studyには、Dockerのコンテナファイルが入っているので、\
VSCode内にて、コンテナ作成の案内が来る。OKすると、イメージを元にコンテナが作成されていくのでしばし待つ。\
→今回使うイメージはjupyter/datascience-notebookでDockerHubに公開されているものを利用。


◆コンテナについて◆\
LinuxOSを元に、必要なアプリをインストールした仮想環境といった感じの物と思われる。


◆今回使っているイメージ◆\
OS:Linuxのubuntu-20.04\
anaconda, python:3.9.6 , JupyterLab ,各種ライブラリ】がインストールされているもの。\
上記マイクロOSのようなものがホストOS（ローカルのWINDOWS）上でゲストOSとして稼働しているようなイメージ。\
コンテナの作成及び実行が問題なく行われれば、VScodeとコンテナの相互が連携している状態になる。


◆VSCode Docker,Github連携について◆\
VSCode下部タスクバーみたいなところに><のようなアイコンがあり、\
【><】の横にDev Container:Jupyter Projectと表示される。\
【><】のアイコンからコンテナを停止させる等操作が行える。\
※このタスクバーみたいなところに、現在利用してるインタプリタ等表示される。\
※タスクバー内、玉紐と↑↓はgithubへpull,commit,pushするための物。

◆連携の流れ◆\
コンテナ内Linux環境下あるJupyterLabとpythonインタプリタへ、ローカルのVScodeからリモートでアクセスを行い、\
ローカルで作業している感覚と変わらず作業が行える。\
/opt/conda/bin/pythonのPython 3.9.6のインタプリタが選択できれば、うまく連携できている。\
/opt/conda/bin/pythonというディレクトリはコンテナLinux内ディレクトリとなる。


◆表示されない場合◆\
色々案内が出てくるので、それに従って、インストールやらボタン連打していたら、そのうち使えるようになっている・・はず。

# ここまでくればgithub　リポジトリからコードもらったり上げたり、チームでの開発が行えるようになっている・・・はず。


# クラウドコンピューティングサービス利用（Azure）
- azureへアカウント作成：クレジットカードの登録が必要になります。
- なしで利用する場合・・・https://www.acrovision.jp/service/azure/?p=1258
- Azureでクラウド上リソースの利用に際して、従量課金制となり、お金はかかります。（Azureは30日$200分無料）
- 参考：標準的な仮想マシン、1H毎10円 1ヵ月フル稼働で9000円ほど（リソースの利用具合によっても変わります）


# Azure Portalでクラウド上にLinux仮想マシンを作成（windows環境とかもある）
◆注意点◆\
作成の流れ自体はその辺のサイトに書いている内容で問題ないが、注意する点というか引っかかった点として以下がある。\
初期設定でSSH:22、RDP:3389のポート開放をチェックしとく。→　あとで設定はできるがちょっとめんどい。\
ポート番号22：SSH接続で使うポート\
ポート番号3389：こちら側から仮想マシンへリモートデスクトップするために使うポート


◆SSH接続について◆\
【******(設定したユーザー名).pem】という秘密鍵がダウンロードされるが、これがパスワードの代わりのようなものになる。\
→なくしたらめんどくさそうなので、しっかりと保存する。\
最初Linux環境にパスワードが設定されていない状態なので、SSHで接続を行う。\
Azure CLIか Tera Termのようなもので接続する必要がある。
・Teratarm:端末へSSH接続を行うためのソフト。インストールしておく。


# Azure PortalとTeraterm
◆Azure Portal　仮想マシンページ◆\
仮想マシンが立ち上がると、Azure Portalに表示された状態になり、開始、再起動、停止やその他設定が行える。\
基本内パブリックIPアドレス、仮想ネットワーク／サブネットと続き、その下の未設定みたいなところを押下。\
ここでDNS（ドメインネームシステム）を設定が出来るので、設定しておく。
```
DNSとは・・IPアドレスに名前を付けて、その名前を元に接続を行えるようにする物。WEBのURLみたいなもの。
これなしでパブリックIPアドレスからRDP接続を行っていると、マシンを起動しなおす毎にアドレスが振りなおされるので
一々確認して入れなおさなければいけなくなって、とてもめんどくさい。
```


◆Teratermでの接続について◆\
Teratermに設定したDNS名（パブリックIPアドレスでも構わない）を入力して、SSHで接続を行う。\
何か表示されるが、そのままOKして設定したSSH接続で設定した【ユーザー名】入力と、\
→Teratermは初期画面でSSH ポート番号22になっているはずだけども、なってない場合は入力する。\
認証方式で【RSA/DSA/ECDSA/ED25519鍵を使う】を選択し、【******(設定したユーザー名).pem】を選択してSSH接続を行う。


【Install and configure xrdp to use Remote Desktop with Ubuntu】\
 https://docs.microsoft.com/en-us/azure/virtual-machines/linux/use-remote-desktop


# クラウドマシンへ接続のち下記実施
Azure CLIインストール（詳細はよくわからないが入れた・・）\
Linux側リモート接続するためのアプリをコマンドでインストールする。
```
sudo apt-get update
sudo apt-get -y install xfce4
sudo apt install xfce4-session
sudo apt-get -y install xrdp
sudo systemctl enable xrdp
echo xfce4-session >~/.xsession
sudo service xrdp restart
```
- 仮想マシンにパスワードを設定する。\
→sudo passwd (入れたいパスワード）下記いれるとazureuserというパスワードが設定される。
```
sudo passwd azureuser
```
- Azure CLIインストールした後、windows powershellで下記コマンド実施（・・いるのかよくわからない\
 【myResourceGroup】に自分のリソースグループ名、【myVM】に自分の仮想マシン名をいれる。
```
az vm open-port --resource-group myResourceGroup --name myVM --port 3389
```
以上、ubuntuデスクトップへのリモート接続の準備完了。


# ローカルマシンからクラウドマシンへリモート接続
◆注意点◆\
Azure PortalからRDP接続用ショートカットのようなものがダウンロード出来、それから接続を行えるが、\
何故かうまく接続が行えなかった。（勘違いかもしれないが特に困らないので放置）\


◆Windowsリモートデスクトップ接続◆\
例：111.111.111.111:3389　（111.111.111.111)の部分には仮想マシンのパブリックIPか設定したDNS名を入れる。\
これで、問題なければ、ubuntu認証画面が起動するので、下記内容にてログインする。
```
【Login to my Xdrp】
【Session】:Xorg
【username】:仮想マシン作成SSH接続の時に入力したユーザー名
【password】:自分で設定したやつ
```


# Ubuntuへデスクトップ接続出来た後、下記各種設定行う。
- VM起動後の開発環境セットアップ(Linux)
- https://dotnetdevelopmentinfrastructure.osscons.jp/index.php?VM%E8%B5%B7%E5%8B%95%E5%BE%8C%E3%81%AE%E9%96%8B%E7%99%BA%E7%92%B0%E5%A2%83%E3%81%AE%E3%82%BB%E3%83%83%E3%83%88%E3%82%A2%E3%83%83%E3%83%97%EF%BC%88Linux%EF%BC%89
- Azure VMでLinuxインスタンスを起動したら最初にやっておくべき設定
- https://www.buildinsider.net/pr/microsoft/azure/dictionary04


# 参考
- Azure で Linux 仮想マシンを作成する
- https://docs.microsoft.com/ja-jp/learn/modules/create-linux-virtual-machine-in-azure/
- Azure VM (Ubuntu Server 20.04 LTS) に GNOME + TigerVNC + xrdp を導入、リモート デスクトップ接続を行う
- https://kogelog.com/2020/05/12/20200512-01/
- WindowsのRDPを使ってクラウド上のLinuxインスタンスに接続する
- https://qiita.com/yamada-hakase/items/a8efe626f598c5eb6f8c
- Install and configure xrdp to use Remote Desktop with Ubuntu
- https://docs.microsoft.com/en-us/azure/virtual-machines/linux/use-remote-desktop


# Linux関連
- bashで始めるシェルスクリプト基礎の基礎
- https://atmarkit.itmedia.co.jp/ait/articles/0202/05/news001.html
- シェルスクリプトを定期実行してみよう
- https://note.com/goldnanoparticle/n/nb9bd20d18f37
- Cronの使い方とテクニックと詰まったところ
- https://qiita.com/UNILORN/items/a1a3f62409cdb4256219
- UbuntuにVSCodeをインストールする3つの方法
- https://qiita.com/yoshiyasu1111/items/e21a77ed68b52cb5f7c8
- UbuntuにGitをインストールする
- https://qiita.com/tommy_g/items/771ac45b89b02e8a5d64
- Ubuntu 20.04へのDockerのインストールおよび使用方法
- https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04-ja
- Ubuntu20.04で日本語入力(Mozc)を可能にする方法
- https://novicengineering.com/ubuntu_mozc_install/
- DockerもいいけどLXDもね 1 〜LXDEデスクトップ環境の構築〜
- https://zenn.dev/tantan_tanuki/articles/7796a4f1d6d1b0
- Ubuntu 20 .04にVNC をインストールして構成 する方法
- https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-vnc-on-ubuntu-20-04-ja
- 第683回　LXDコンテナ上にUbuntuのフルデスクトップ環境を構築する
- https://gihyo.jp/admin/serial/01/ubuntu-recipe/0683
