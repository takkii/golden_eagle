### Golden-eagleは、顔写真でデータ分析を行うプロジェクトです。

#### プロジェクト内、Python3パッケージをビルドします。

> pip wheel --no-deps -w dist .

※ 忘れないようにします。

### 防犯カメラ機能の説明

> cd golden_eagle
>
> pip3 install -r requirements.txt
>
> python security.py

```python
# ... security.py/24行目付近

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

※ 初期値は1時間、手動でタイマーを設定できます。その都度、時間設定を考慮してください。

#### recongnition.py

> 起動時のqで終了することを有効化しました。何回か終了するまで、押してみてください。

※ それでも終了しないとき、Windows Terminalなど端末上でctrl+cで終了してください。

> 2人、認識出来るようにしました。名前とPATH(画像)を変えて使用してみてください。

※ 画像の保存機能、1人の緑枠と名前のみ表示します。

> 2人分の緑枠と名前を取りたいときは、
>
> スクリーンショット(Prt Scボタン)を押し、
>
> 範囲を選択後、ペイントなどに貼り付け画像として保存してください。

#### .env

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
# Name, takayuki.
one_name = "Takayuki Kamiyama"
# Name, keiko.
two_name = "Keiko Kamiyama"
# Use, recognition.py
fl_num = 0.4
# Default settings, 100KB (recognition.py)
int_num = 100
# connect number
int_conn = 0
# before/after and 1days calc
str_calc = "hour"
# clock is timer.
int_clock = 1
```

> 更新履歴: 2026/01/25
