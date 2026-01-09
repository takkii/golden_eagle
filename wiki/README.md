### 顔写真でデータ分析を行うプロジェクトです。

#### Python3パッケージをビルドします。

> pip wheel --no-deps -w dist .

※ 忘れないようにします。

> python security.py

→ 起動すると録画を開始します。スクリーン上でqを押すと、保存後終了します。

※ 1時間を超えないように目安に動画を保存してください。自動でそれを超えると終了します。

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
```

> 更新履歴: 2025/10/17
