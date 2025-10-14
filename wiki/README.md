### Python3 Package Build

> pip wheel --no-deps -w dist .

※ Don't forget.

### facecompare.py

> .env

```ruby
# There's already a ./Images/run/face_2.gif
before_param = "./Images/run/face_1.gif"
all_param = "./Images/run/"
# before_param = "./Images/run/disabilit.gif"
# after_param = "./Images/run/mynumber.gif"
ga_num = 0.32
ga_num_run = 0.32
```

before_param、単一画像(face_1.gifのみを入れました)

all_param、複数画像(face_1.gif, face_2.gifを入れました)

1対多の顔認識、設定後facecompre.pyを実行した結果。

```ruby
# output
# golden-eagle_version: 1.0.5.5
# = Same picture / face_1.gif
# accuracy:[0.]
# ≠ Different picture / face_2.gif
# golden-eagle_version: 1.0.5.5
# accuracy:[0.255]
```

精度評価をみて、0.は全く同じ画像です。まさか0になるとは...