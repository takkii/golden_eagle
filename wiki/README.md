### 顔認識システムのコンソール版 (データ分析を利用)

#### プロジェクト内、Python3パッケージをビルドします。

> pip wheel --no-deps -w dist .

※ 忘れないようにします。

### 防犯カメラ機能の説明

```markdown
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

```python
# security.py/24行目

# ...

# 1日経過後、breakを実行 (days=2)など変更可
# t1 = datetime.timedelta(days=1)
# 1時間経過後、breakを実行 (hours=2)など変更可
t1 = datetime.timedelta(hours=1)
# 1分経過後、breakを実行 (mininutes=2)など変更可
# t1 = datetime.timedelta(mininutes=1)
# 1秒経過後、breakを実行 (seconds=2)など変更可
# t1 = datetime.timedelta(seconds=1)

# ...
```

※ 初期値は1時間、手動で時間数を設定できます。その都度、タイマーの時間を考慮してください。

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

※ golden_eagle/.env になるように設置する。

```ruby
# ↓ paste in .env ↓

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

※ WSL2/RockyLinux10、Webcamの動作確認ができませんでした。 (recognition_ga.py / recognition.py)

- 但し、dlibの手動ビルドは出来ました。 golden-eagle.py / analyze.py / inuwashi.pyは動作します。

### CLIの使い方

```markdown
# WSL2(UNIX推奨) ~/.zshrc
export PATH="/mnt/c/Users/users/GitHub/golden_eagle/bin:$PATH"

# golden_eagle
git clone git@github.com:takkii/golden_eagle.git
cd golden_eagle

# UNIX環境 (railseiden/golden_eagle)
flare recognition.log

# railseidenから生成
./effect.txt

# UNIX環境 (meteor)
meteor recognition.log effect.txt '(([AEIOUKSTNHMYRWGZDBCFJ][tshy]?[aeiou]?)([kstnhmyrwgzdbcfj]?[tshy]?[aeiou]n?){2,8})'

# UNIX環境 (clarify)
clarify effect.txt 0 2
```

```markdown
# CRLF → LFに改行コードを変換し保存してください。
/usr/bin/env: `python3\r': そのようなファイルやディレクトリはありません
/usr/bin/env: shebang 行でオプションを渡すには -[v]S を使ってください
```

※ clarify、railseiden、flare、meteorが対象です。

#### 出力結果

```markdown
# 名前を先頭から2行目まで、指定の行数出力。
Takayuki (11)
Keiko (5)

 Done, processed target file.
```

> 更新履歴: 2026/04/11
