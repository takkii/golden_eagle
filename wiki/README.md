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

※ Windows Terminalなど端末上で、ctrl+cで終了してください。

#### .env

```ruby
# before picture path.
single_param = "./Images/scan/myself.gif"
# all picture path.
all_param = "./Images/run/"
# Yourself before picture image.
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
# use bakachon path.
picture_images = "./images/face.jpg"
# face name
name = "Takayuki Kamiyama"
```

> 更新履歴: 2026/01/10
