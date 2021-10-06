# 最近流行りのVPS or クラウドで仮想開発環境を構築しよう。
# Let's build a virtual development environment with VPS or Cloud, which is popular these days.
git,github,Docker,Vscode,クラウドサービス？なんですかそれは？という状態から、<br>
それぞれの要点を掻い摘んで、なんとか形にしていった時の流れと参考にしたことをまとめました。<br><br>
<strong>
git,Github,docker,vscode,cloud services? This is a summary of the process and references\
I used it when I went from knowing almost nothing to summarizing and shaping the key points of each.
</strong>


◆目的◆<strong>Purpose</strong>
- ローカル環境に、github,Docker,VScodeを用いて、仮想開発環境を構築。<br>
<strong>Build a virtual development environment in the local environment using Github, Docker, and VScode.</strong>
- クラウドサービス上に仮想マシンを起動させ、クラウド上に同じような仮想開発環境を構築。<br>
<strong>Start a virtual machine on the cloud service and build a similar virtual development environment in the cloud.</strong>



◆ローカルマシン環境側でのメリット◆<strong>Benefits on the local machine environment side</strong>
- パソコンごとに環境の選択やライブラリの選択や細々とした設定インストールをする必要がなくなります。<br>
<strong>You no longer need to choose an environment, select a library, and install detailed settings for each computer.</strong>
- コンテナ単位で環境を構築するので、問題が生じた環境の破棄及び再生成が容易になります。<br>
<strong>Since the environment is built-in containers, it is easy to destroy and regenerate the environment if a problem occurs.</strong>
- 先人が作成してくれた環境のパッケージを用いることにより、最小の労力で環境構築が行えます。<br>
<strong>By using the environment packages created by our predecessors, we can build the environment with minimal effort.</strong>



◆クラウドマシン環境側でのメリット◆<strong>Benefits on the cloud machine environment side</strong>
- クラウド上にて仮想マシンに環境を構築しているので、RDPで接続するだけで同一環境で作業ができます。<br>
<strong>The environment is built on a virtual machine in the cloud, so you can work in the same environment just by connecting via RDP.</strong>
- 環境を常時稼働させることが出来ます。（従量課金制なのでお金はかかります。1h10円程）<br>
<strong>You can run the environment all the time. (It's a pay-as-you-go system, so you will have to pay for it, about 10 yen per hour.</strong>
- 耐障害性が高い。<br>
<strong>High fault tolerance.</strong>
- マシンリソースのグレードアップが容易。<br>
<strong>Easy to upgrade machine resources</strong>
- クラウド上のリソースを用いることが出来る。（画像分析やテキスト分析等）<br>
<strong>Resources in the cloud can be used. (Image analysis, text analysis, etc.)</strong>


 →慣れたら仮想マシン作成、立ち上げから、開発環境一通り揃えるのに1時間ほどで行えます。とても速い。<br>
 <strong>
 Once you get used to it, it takes about an hour to create a virtual machine, 
 start it up, and set up the entire development environment. Very fast.
 </strong>

※追記<br>
先にクラウドのサービス無料で使えるというので、それで進めてしまいましたが、仮想マシンに限定すれば\
VPSサービスのほうが費用を抑えられます。\
ただ、クラウドサービスにはAIのデータセット等あり、それらのリソースを利用することが出来ます。<br>
<strong>
I went ahead and used the free cloud service, but if you limit yourself to virtual machines, the VPS service is more cost-effective.
However, the cloud service has AI data sets and other resources that can be used.
</strong>


# Githubのアカウント作成 
# Create a Github account 
- 参考:https://www.sejuku.net/blog/73468


# gitインストール
# git install
- https://git-scm.com/
- 参考:https://kitsune.blog/engineer/git


# VSCodeインストール
# VSCode installation 
- https://azure.microsoft.com/ja-jp/products/visual-studio-code/
- 参考github連携：https://breezegroup.co.jp/202102/vscode-github-windows/
- 参考Docker連携：https://qiita.com/Yuki_Oshima/items/d3b52c553387685460b0


# Dockerインストール
# Docker installation
- https://www.docker.com/
- 参考：https://www.pasonatech.co.jp/workstyle/column/detail.html?p=2675
- 使ってるイメージファイル：https://hub.docker.com/r/jupyter/datascience-notebook/tags?page=1&ordering=last_updated
- 補足：DockerがBIOSのCPUの仮想化設定がDisable等で起動しない場合。https://mrkmyki.com/docker%E3%82%92%E8%B5%B7%E5%8B%95%E3%81%97%E3%82%88%E3%81%86%E3%81%A8%E3%81%97%E3%81%9F%E3%82%89%E3%80%8Chardware-assisted-virtualization-and-data-execution-protection-must-be-enabled-in-the-bios
- AMDのCPUの場合BIOS設定でSVMをEnableにします。


# 上記インストールが終わったら、下記参考ページ
# Reference page
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

<strong></strong><br>
# ゼロから環境構築
# Build an environment from scratch
◆Git、Docker、VSCodeインストール、Githubのアカウント作成◆<br>
VSCode内、下記拡張機能インストールを行う。<br>
<strong>
Install Git, Docker, VSCode, and create a Github account.
Install the following extensions in VSCode.
</strong><br>
【Japanese Language Pack , Python , Remote Development , Docker】<br>
◆githubのリポジトリからローカル環境へクローンする。◆<br>
<strong>Clone from the github repository to the local environment.</strong><br>
https://github.com/Satou-Kazuki/Cloud_Dev_Study.git


◆リポジトリのクローン方法◆<strong>How to clone the repository</strong><br>
1.git bashから、コマンド入力で行う。\
2.VSCodeのフォルダ管理から行う。\
今回は2の方法を利用します。<br>
<strong>
1.Do this by entering commands from git bash.
2.Do this from the folder management of VSCode.
In this case, we will use method 2.
<strong>
  
  
◆クローン後の流れ◆<strong>Flow after cloning</strong><br>
クローンを行うと、指定したフォルダ配下にローカルリポジトリが作成され、リモートリポジトリのコピーが作成されます。<br>
クローンしたCloud_Dev_Studyには、Dockerのコンテナファイルが入っていますので、<br>
VSCode内にて、コンテナ作成の案内が来ます。OK押下しますと、イメージを元にコンテナ作成が行われます。<br>
→今回使うイメージはjupyter/datascience-notebookでDockerHubに公開されているものを利用。<br>
<strong>
When you clone, a local repository is created under the specified folder and a copy of the remote repository is created.
The cloned Cloud_Dev_Study contains a Docker container file, so you will be prompted to create a container in VSCode
→The image we will use is jupyter/datascience-notebook, which is available on DockerHub.
</strong>


◆コンテナについて◆<strong>About containers</strong><br>
LinuxOSを元に、最小単一の機能で、必要なアプリをインストールした仮想環境という感じの物になります。<br>
<strong>
It is a virtual environment based on the Linux operating system, with a minimum of a single function, and the necessary applications installed.
</strong>


◆今回使っているイメージ◆<strong>Image used in this project</strong><br>
OS:Linuxのubuntu-20.04\
anaconda, python:3.9.6 , JupyterLab ,Various libraries


◆VSCode Docker,Github連携について◆<strong>About VSCode Docker and Github integration</strong><br>
VSCode下部タスクバーみたいなところに><のようなアイコンがあり、<br>
【><】の横にDev Container:Jupyter Projectと表示されます。<br>
【><】のアイコンからコンテナを停止させる等操作が行えます。<br>
※このタスクバーみたいなところに、現在利用してるインタプリタ等表示されます。<br>
※タスクバー内、玉紐と↑↓はgithubへpull,commit,pushするための物になります。<br>
<strong>
There is a '><' like icon on the taskbar at the bottom of VSCode, with Dev Container:Jupyter Project next to '><'.
You can stop the container from the '><' icon.
This taskbar-like area will display the interpreter you are currently using.
In the taskbar, the ball and ↑↓ are for pulling, committing, and pushing to github.
</strong>


◆連携の流れ◆\Flow of collaboration
コンテナ内Linux環境下あるJupyterLabとpythonインタプリタへ、ローカルのVScodeからリモートでアクセスを行い、\
ローカルで作業している感覚と変わらず作業が行えます。\
/opt/conda/bin/pythonのPython 3.9.6のインタプリタが選択できれば、うまく連携出来ています。\
/opt/conda/bin/pythonというディレクトリはコンテナLinux内ディレクトリとなります。
You can remotely access JupyterLab and the python interpreter in the Linux environment in the container from your local VScode, and work as if you were working locally.
If you can select the Python 3.9.6 interpreter in /opt/conda/bin/python, you have a good connection.
The directory /opt/conda/bin/python is the directory in the container Linux.


# ここまでくればgithub　リポジトリからコードを貰ったり上げたり、チーム開発を行えるようになっています。
# You can now get code from the github repository, raise it, and do team development.


# クラウドコンピューティングサービス利用（Azure）
# Use of cloud computing services (Azure)
- azureへアカウント作成：クレジットカードの登録が必要になります。
- なしで利用する場合・・・https://www.acrovision.jp/service/azure/?p=1258
- Azureでクラウド上リソースの利用に際して、従量課金制となり、お金はかかります。（Azureは30日$200分無料）
- 参考：標準的な仮想マシン、1H毎10円 1ヵ月フル稼働で9000円ほど（リソースの利用具合によっても変わります）
<strong>
- Create an account with azure: You will need to register a credit card.
- To use it without... https://www.acrovision.jp/service/azure/?p=1258
- When you use resources in the cloud with Azure, you will be charged on a pay-as-you-go basis. (Azure is free for 30 days and $200 minutes)
- Reference: Standard virtual machine, 10 yen per 1 hour, about 9,000 yen per month of full operation (depending on how the resources are used)
</strong>

# Azure Portalでクラウド上にLinux仮想マシンを作成（windows環境とかもあります）
# Create a Linux virtual machine in the cloud with Azure Portal (windows environment is also available)
◆注意点◆\Points to note
作成の流れ自体はその辺のサイトに書いている内容で問題ありませんが、下記注意点あり。\
初期設定でSSH:22、RDP:3389のポート開放をチェック→　あとで設定はできますが、最初にしてるほうが楽。\
ポート番号22：SSH接続で使うポート\
ポート番号3389：こちら側から仮想マシンへリモートデスクトップするために使うポート
The creation process itself is fine as described in those sites, but there are some cautions below.
Check the SSH:22 and RDP:3389 port openings in the default settings → You can set this later, but it is easier to do it first.
Port number 22: Port used for SSH connection
Port number 3389: Port used for remote desktop from our side to the virtual machine.


◆SSH接続について◆\About SSH connection
【******(設定したユーザー名).pem】という秘密鍵がダウンロードされますが、これがパスワードの代わりのようなものになります。\
→しっかりと保存する。\
最初Linux環境にパスワードが設定されていない状態なので、SSHで接続を行います。\
Azure CLIか Tera Termのようなもので接続する必要があります。
・Teratarm:端末へSSH接続を行うためのソフト。インストールします。
A private key named [******(username you set).pem] will be downloaded, which is a kind of password substitute.
Since there is no password set in the Linux environment at first, we will use SSH to connect.
You will need to use Azure CLI or something like Tera Term to connect.
Teratarm: A software for SSH connection to the terminal. Install it.


# Azure PortalとTeraterm
◆Azure Portal◆\
仮想マシンが立ち上がると、Azure Portalに表示された状態になり、開始、再起動、停止やその他設定が行えます。\
基本ページ、パブリックIPアドレス、仮想ネットワーク／サブネットと続き、その下の未設定みたいなところを押下。\
ここでDNS（ドメインネームシステム）を設定が出来るので、設定します。
```
DNSとは・・IPアドレスに名前を付けて、その名前を元に接続を行えるようにする物。WEBのURLみたいなもの。
これなしでパブリックIPアドレスからRDP接続を行っていると、マシンを起動しなおす毎にアドレスが振りなおされ
一々確認して入力する必要が生じ、面倒です。
```
Once the virtual machine is up and running, it will appear in the Azure Portal, where you can start, restart, stop and configure other settings.
Press down on the basic page, followed by public IP address, virtual network/subnet, and then something like unconfigured underneath.
This is where you can configure the DNS (Domain Name System) setting
```
DNS is a system for naming IP addresses so that connections can be made based on those names, much like URLs on the web.
If you are using RDP connections from a public IP address without DNS, the address will be reassigned every time you reboot the machine.
If you are using RDP connections from a public IP address without this, the address will be reassigned every time you reboot the machine, and you will have to check and enter the address every time.
```


◆Teratermでの接続について◆\About the connection with Teraterm
Teratermに設定したDNS名（パブリックIPアドレスでも構わない）を入力して、SSHで接続を行います。\
何か表示されますが、そのままOKして設定したSSH接続で設定した【ユーザー名】入力と、\
→Teratermは初期画面でSSH ポート番号22を指定します。\
認証方式で【RSA/DSA/ECDSA/ED25519鍵を使う】を選択し、【******(設定したユーザー名).pem】を選択してSSH接続を行う。
Enter the DNS name (or public IP address) that you configured on Teraterm, and connect to the server via SSH.
You will be prompted something, OK as it is and enter the [User name] configured in the SSH connection you set up.
→Teraterm specifies the SSH port number 22 in the initial screen.
Select [Use RSA/DSA/ECDSA/ED25519 key] for the authentication method and select [******(username you set).pem] to connect to SSH.


【Install and configure xrdp to use Remote Desktop with Ubuntu】\
 https://docs.microsoft.com/en-us/azure/virtual-machines/linux/use-remote-desktop


# クラウドマシンへ接続のち下記実施
# Connect to the cloud machine and do the following
Azure CLIインストール\
Linux側リモート接続するためのアプリをコマンドでインストールします。
Azure CLI installation
Install the application for remote connection on the Linux side using the command.
```
sudo apt-get update
sudo apt-get -y install xfce4
sudo apt install xfce4-session
sudo apt-get -y install xrdp
sudo systemctl enable xrdp
echo xfce4-session >~/.xsession
sudo service xrdp restart
```
- 仮想マシンにパスワードを設定します。\
→sudo passwd (入れたいパスワード）下記いれるとazureuserというパスワードが設定されます。
- Set a password for the virtual machine.
→sudo passwd (the password you want to enter) Enter the following to set the password as azureuser.
```
sudo passwd azureuser
```
- Azure CLIインストールした後、windows powershellで下記コマンド実施します。\
 【myResourceGroup】に自分のリソースグループ名、【myVM】に自分の仮想マシン名をいれます。
- After installing Azure CLI, execute the following command in windows powershell.
 Enter your resource group name in [myResourceGroup] and your virtual machine name in [myVM].
```
az vm open-port --resource-group myResourceGroup --name myVM --port 3389
```
以上、ubuntuデスクトップへのリモート接続の準備完了となります。
This completes the preparation for remote connection to the ubuntu desktop.


# ローカルマシンからクラウドマシンへリモート接続
◆Windowsリモートデスクトップ接続◆\
例：111.111.111.111:3389　（111.111.111.111)の部分には仮想マシンのパブリックIPか設定したDNS名を入れます。\
これで、問題がなければ、ubuntu認証画面が起動しますので、下記内容にてログインします。
```
【Login to my Xdrp】
【Session】:Xorg
【username】:仮想マシン作成SSH接続の時に入力したユーザー名
【password】:自分で設定したやつ
```


# Ubuntuへデスクトップ接続出来た後、下記各種設定行う。
# Once you have a desktop connection to Ubuntu, configure the following settings.
- VM起動後の開発環境セットアップ(Linux)
- https://dotnetdevelopmentinfrastructure.osscons.jp/index.php?VM%E8%B5%B7%E5%8B%95%E5%BE%8C%E3%81%AE%E9%96%8B%E7%99%BA%E7%92%B0%E5%A2%83%E3%81%AE%E3%82%BB%E3%83%83%E3%83%88%E3%82%A2%E3%83%83%E3%83%97%EF%BC%88Linux%EF%BC%89
- Azure VMでLinuxインスタンスを起動したら最初にやっておくべき設定
- https://www.buildinsider.net/pr/microsoft/azure/dictionary04


# 参考
# Reference
- Azure で Linux 仮想マシンを作成する
- https://docs.microsoft.com/ja-jp/learn/modules/create-linux-virtual-machine-in-azure/
- Azure VM (Ubuntu Server 20.04 LTS) に GNOME + TigerVNC + xrdp を導入、リモート デスクトップ接続を行う
- https://kogelog.com/2020/05/12/20200512-01/
- WindowsのRDPを使ってクラウド上のLinuxインスタンスに接続する
- https://qiita.com/yamada-hakase/items/a8efe626f598c5eb6f8c
- Install and configure xrdp to use Remote Desktop with Ubuntu
- https://docs.microsoft.com/en-us/azure/virtual-machines/linux/use-remote-desktop


# Linux関連
# Linux related
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
- 【Azure VM】CentOSにrootユーザでログインする方法
- https://coeure.co.jp/blog/infrastructure/microsoft-azure/azure-centos-root-210212
- CentOS7にデスクトップ環境としてGNOMEをインストールする方法
- https://qiita.com/yasushi-jp/items/cc40e404d2fa15114802
- WindowsのリモートデスクトップでCentOS 7に接続してみた
- https://www.bing.com/search?q=github&form=ANNTH1&refig=1ea1c6befe73420d885d577f90824c53

#VPS関連
#VPS related
- ご利用ガイド マンガで学ぶConoHa
- https://support.conoha.jp/v/study-03/?btn_id=v-study-02-sidebar_v-study-03
- ネコでもわかる！さくらのVPS講座 〜第一回：VPSてなんだろう？〜
- https://knowledge.sakura.ad.jp/7938/?_gl=1*l665d4*_gcl_aw*R0NMLjE2MzI0MzM2MzAuQ2p3S0NBand5N0NLQmhCTUVpd0EwRWI3YW9QZDZBYWxJLTUtT2lzNUJub3ZIMGNqZGZOUEZkTmlvSklZR01uLVNvSXZmUXMzTkpaZFd4b0M2cVVRQXZEX0J3RQ..&_ga=2.149153907.492133002.1632429434-1377883743.1625409629&_gac=1.90834408.1632433630.CjwKCAjwy7CKBhBMEiwA0Eb7aoPd6AalI-5-Ois5BnovH0cjdfNPFdNioJIYGMn-SoIvfQs3NJZdWxoC6qUQAvD_BwE
- ConoHa VPSにGitHubのPrivateリポジトリをCloneする
- https://create-it-myself.com/know-how/clone-github-private-ripogitory-on-conoha-vps/
- VPS + Docker で トレンド技術を使いこなす【 第1回： コマンド1行でアプリが動く Docker 
- https://www.kagoya.jp/howto/cloud/container/vps-docker-01/
- ssh接続先のdockerコンテナにVSCodeのRemote Developmentで繋ぐ
- https://qiita.com/kanosawa/items/07e26edb19c86091fa48
- Django♪VPSサーバーでDjangoを始めてみたシリーズ
- https://snowtree-injune.com/django-series-dj000/
- VSCodeをフロントにしたPython開発環境の個人的ベストプラクティス
- https://qiita.com/yoichi_t/items/c42639d7700089a9eedb
- VSCodeを使ってAWS EC2のソースコードを編集する
- https://qiita.com/takao-takass/items/9f81d5095924280966ae
- デスクトップ環境 : VNC サーバーの設定
- https://www.server-world.info/query?os=Ubuntu_21.04&p=desktop&f=5
