## 顔認識システムのコンソール版

#### 日本語に英語を混合し表現していきます。

> pip wheel --no-deps -w dist .

_プロジェクト内、Python3パッケージをビルドします。_

### 防犯カメラ機能の説明

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
python security.py
```

#### ...

```python
# security.py/24行目
# 1日経過後、breakを実行 (days=2)など変更可
# t1 = datetime.timedelta(days=1)
# 1時間経過後、breakを実行 (hours=2)など変更可
t1 = datetime.timedelta(hours=1)
# 1分経過後、breakを実行 (mininutes=2)など変更可
# t1 = datetime.timedelta(mininutes=1)
# 1秒経過後、breakを実行 (seconds=2)など変更可
# t1 = datetime.timedelta(seconds=1)
```

_※ 初期値は1時間、手動で時間数を設定できます。その都度、タイマーの時間を考慮してください。_

#### ./recongnition.py

> 起動時のqで終了することを有効化しました。何回か終了するまで、押してみてください。

※ それでも終了しないとき、Windows Terminalなど端末上でctrl+cで終了してください。

> 2人、認識出来るようにしました。名前とPATH(画像)を変えて使用してみてください。

※ 画像の保存機能、1人の緑枠と名前のみ表示します。

> 2人分の緑枠と名前を取りたいときは、
>
> スクリーンショット(Prt Scボタン)を押し、
>
> 範囲を選択後、ペイントなどに貼り付け画像として保存してください。

### touch .env

_※ golden_eagle/.env になるように設置する。_

### .envに下記内容を貼り付けます。

```ruby
# before picture path.
single_param = "./Images/scan/myself.gif"
# all picture path.
all_param = "./Images/run/"
# Yourself before picture image (Using recognition.py ...etc)
before_param = "./Images/run/face_1.gif"
# Yourself after picture image.
after_param = "./Images/run/face_2.gif"
# Using, facecompare.py
ga_num = 0.32
# Using, facecompare.py
before_param_face = "../Images/run/face_1.gif"
# Using, facecompare.py
after_param_face = "../Images/run/face_2.gif"
# Using, golden-eagle.py
ga_num_run = 0.32
# Using, analyze.py
lo_num = 0.442
# Using, recognition.py
picture_images = "./images/face.jpg"
# My Family picture path.
two_params = "./Images/keiko/keiko.gif"
# First Name, Takayuki.
one_name = "Takayuki"
# First Name, Keiko.
two_name = "Keiko"
# Use, recognition.py
fl_num = 0.4
# Default settings, 100KB recognition.py
int_num = 100
# Webcam Built-in camera (0 or 1) | security_ga.py or recognition.py
int_conn = 0
# Webcam Built-in camera (0 or 1) | main.py
int_conn_main = 0
# clock is timer (security_ga.py)
int_clock = 1
# DEBUG LOG.
debug_log = './debug.log'
# open file.
match_word = 'recognition.log'
# Default, effect.txt
effect = 'effect.txt'
# Regex match pattern
regex = '(([AEIOUKSTNHMYRWGZDBCFJ][tshy]?[aeiou]?)([kstnhmyrwgzdbcfj]?[tshy]?[aeiou]n?){2,8})'
```

[picture](https://github.com/takkii/picture) | [bakachon](https://github.com/takkii/bakachon) | [sheltered-girl](https://rubygems.org/gems/sheltered-girl)

> 上記のプロジェクトを使い、比較元の顔写真を.envに設定し繋いでください。

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

### WSL2の対応について

```markdown
[ WARN:0@1.269] global cap_v4l.cpp:914 open VIDEOIO(V4L2:/dev/video1): can't open camera by index
[ WARN:0@1.269] global cap.cpp:438 open VIDEOIO(FFMPEG): raised OpenCV exception:
...
[ERROR:0@1.269] global obsensor_uvc_stream_channel.cpp:163 getStreamChannelGroup Camera index out of range
```

_dlibのGoogle検索で手動ビルドは出来ました。 golden-eagle.py / analyze.py / inuwashi.pyは動作します。_

> ※ WSL2/RockyLinux10、Webcamの動作確認ができませんでした。 (recognition_ga.py / recognition.py)

### CLIの使い方

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

### エラー表示

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
```

※ clarify、railseiden、flare、meteor、holyはUNIX環境のみ対応しています。

#### clarify effect.txt 0 2

```markdown
# 出力結果
Takayuki (11)
Keiko (5)
```

_※ # 名前を先頭から2行目まで、指定の行数出力します。_

### UserWarningの対応

> C:\Users\user\scoop\apps\python313\current\Lib\site-packages\face_recognition_models\__init__.py

```markdown
# __version__ = '0.1.0'の空白を含んで下に追加。
# 7行目 ~ 11行目に貼り付け
import os
import warnings

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
warnings.simplefilter('ignore', UserWarning)
# ... 下記の記述があるところ。
# from pkg_resources import resource_filename
```

※ analyze.py/golden-eagle.py/inuwashi.pyの実行時UserWarningが非表示に出来る。気になる人はどうぞ。

> 更新履歴: 2026/04/13
