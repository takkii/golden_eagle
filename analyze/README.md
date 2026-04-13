# Python3を利用したデータ分析の検証と考察。

※ Windows (推奨) flakey.py golden-eagle.py wing-coverts.py recognition.py recognition_ga.py security.py security_ga.py

### recognition_ga.py | recognition.pyのWSL2対応について

```markdown
[ WARN:0@1.269] global cap_v4l.cpp:914 open VIDEOIO(V4L2:/dev/video1): can't open camera by index
[ WARN:0@1.269] global cap.cpp:438 open VIDEOIO(FFMPEG): raised OpenCV exception:
...
[ERROR:0@1.269] global obsensor_uvc_stream_channel.cpp:163 getStreamChannelGroup Camera index out of range
```

_※ dlibのGoogle検索でWindowsビルドは出来ました。 golden-eagle.pyなどは動作します。_

> WSL2/RockyLinux10、Webcamの動作確認ができませんでした。

#### security.pyの仕様

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

#### python recongnition.py

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

```shell
# before picture path.
single_param = "../Images/scan/myself.gif"
# all picture path.
all_param = "../Images/run/"
# Yourself before picture image (Using recognition.py ...etc)
before_param = "../Images/run/face_1.gif"
# Yourself after picture image.
after_param = "../Images/run/face_2.gif"
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
picture_images = "../images/face.jpg"
# My Family picture path.
two_params = "../Images/keiko/keiko.gif"
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
match_word = './recognition.log'
# Default, effect.txt
effect = 'effect.txt'
# Regex match pattern
regex = '(([AEIOUKSTNHMYRWGZDBCFJ][tshy]?[aeiou]?)([kstnhmyrwgzdbcfj]?[tshy]?[aeiou]n?){2,8})'
```

[picture](https://github.com/takkii/picture) | [bakachon](https://github.com/takkii/bakachon) | [sheltered-girl](https://rubygems.org/gems/sheltered-girl)

> 上記のプロジェクトを使い、比較元の顔写真を.envに設定し繋いでください。

> python .\flakey.py

```markdown
  0%|                                                                   | 0/2 [00:00<?, ?it/s] before picture path ./Images/scan/myself.gif
❎️ failed: 0.442 < hyoka_accuracy: 0.469 all picture path Images\run\face_1.gif
 50%|█████████████████████████████▌                             | 1/2 [00:22<00:22, 22.71s/it] before picture path ./Images/scan/myself.gif
⭕️ success: 0.442 > hyoka_accuracy: 0.441 all picture path Images\run\face_2.gif
100%|███████████████████████████████████████████████████████████| 2/2 [00:57<00:00, 28.69s/it]
```

> gem install sheltered-girl
>
> aqua -z ./analyze/analyze_result.txt ⭕️

```markdown
 8 : ⭕️ success: 0.442 > hyoka_accuracy: 0.441 all picture path Images\run\face_2.gif
```

> aqua -z ./analyze/analyze_result.txt ❎️

```markdown
 6 : ❎️ failed: 0.442 < hyoka_accuracy: 0.469 all picture path Images\run\face_1.gif
```

※ 精度評価の結果をエクセルシートにコピー＆ペーストする。

> 精度評価の結果(ファイル名.xlsx) / 顔認識分析.xlsx

#### 来客.xlsx

> recognition.pyで書き出したrecognition.logを集計、来客数を関数で計算。
>
> または、golden-eagle/bin: meteor/flare/holyなどのUNIXシェルで来客数合計を換算する。

※ 但し、顔写真を登録していない人はカウントしないものとする。

> 更新履歴: 2026/04/14
