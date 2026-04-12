> python .\analyze.py

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
> または、meteorなどのUNIXシェルで正規表現を扱い対象を絞る。

※ 但し、顔写真を登録していない人はカウントしないものとする。