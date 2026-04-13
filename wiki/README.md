# 顔認識システムのコンソール版

_プロジェクト内、Python3パッケージを配布用ビルドします。_

> pip wheel --no-deps -w dist .

```shell
# ① 複製方法
git clone https://github.com/takkii/golden_eagle.git
# ② 複製方法
git clone git@github.com:takkii/golden_eagle.git

※ ①と②はどちらでもよい。

# ログフォルダを作成するときのPATH先
~/golden_eagle | $HOME/golden_eagle

# 実行
cd golden_eagle
pip3 install -r requirements.txt
```

#### 環境構築

```markdown
# Install
gem install sheltered-girl
heat branch picture takkii picture main
cd picture
pip3 install bakachon
pip3 install -r requirements.txt
python take.py
python convert.py
```

#### UNIX環境シェルの使い方

_※ WSL2 (推奨) clarify railseiden flare meteor holy pake_

```markdown
# ~/.zshrc
export PATH="/mnt/c/Users/users/GitHub/golden_eagle/bin:$PATH"

# golden_eagle
git clone git@github.com:takkii/golden_eagle.git
cd golden_eagle

# pake: UnitTest
pake

# Equal effect to meteor/flare project. (using .env)
holy

# railseiden: ver.golden_eagle
flare recognition.log

# create textfile: railseiden/flare/holy/meteor
./effect.txt

# meteor: origin railseiden
meteor recognition.log effect.txt '(([AEIOUKSTNHMYRWGZDBCFJ][tshy]?[aeiou]?)([kstnhmyrwgzdbcfj]?[tshy]?[aeiou]n?){2,8})'

# railseiden
git clone git@github.com:takkii/newworld.git
cd logs
railseiden newworld.log
```

#### Question & Answer

```markdown
# CRLF → LFに改行コードを変換し保存してください。
/usr/bin/env: `python3\r': そのようなファイルやディレクトリはありません
/usr/bin/env: shebang 行でオプションを渡すには -[v]S を使ってください

# 「許可がありません」に対応するには
cd golden_eagle/bin
chmod +x clarify
chmod +x railseiden
chmod +x flare
chmod +x meteor
chmod +x holy
chmod +x pake
```

_※ clarify、railseiden、flare、meteor、holy、pakeはUNIX環境シェルのみ対応しています。_

#### clarify effect.txt 0 2

```markdown
# 出力結果
Takayuki (20)
Keiko (5)
```

_※ 先頭から2行目まで、指定の行数出力します。_

#### 実行時、警告文に対応するには。

```markdown
# Windows, default:user use scoop/python313.
C:/Users/user/scoop/apps/python313/current/Lib/site-packages/face_recognition_models/__init__.py
# WSL2, default:user use anyenv/pyenv.
/home/user/.anyenv/envs/pyenv/versions/3.13.13/lib/python3.13/site-packages/face_recognition_models/__init__.py

# __version__ = '0.1.0'の空白を含んで下に追加。
# ↓ 7行目 ~ 11行目に貼り付け ↓
import os
import warnings

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
warnings.simplefilter('ignore', UserWarning)
# ↑ ... 下記の記述があるところ。↑
# from pkg_resources import resource_filename

# cd ./golden_eagle/analyze
# python flakey.py
# QFontDatabase: Cannot find font directory
# Note that Qt no longer ships fonts. Deploy some (from https://dejavu-fonts.github.io/ for example) or switch to fontconfig.

※ WSL2、flakey.pyなどを実行するとfontconfigに切り替えメッセージが流れます。Windowsで実行するとメッセージは流れません。
```

_警告文に対応したい方は、上記を参考にして下さい。_

> 更新履歴: 2026/04/14
