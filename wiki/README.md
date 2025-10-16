### 顔写真でデータ分析を行うプロジェクトです。

#### Python3 Package Build

> pip wheel --no-deps -w dist .

※ Don't forget.

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
