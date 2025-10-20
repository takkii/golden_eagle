> python analyze.py

```markdown
C:\Users\sudok\scoop\apps\python313\current\Lib\site-packages\face_recognition_models\__init__.py:7: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  from pkg_resources import resource_filename
  0%|                                                         | 0/2 [00:00<?, ?it/s] before picture path ./Images/scan/myself.gif
C:\Users\sudok\GitHub\golden_eagle\analyze.py:69: DeprecationWarning: Conversion of an array with ndim > 0 to a scalar is deprecated, and will error in future. Ensure you extract a single element from your array before performing this operation. (Deprecated NumPy 1.25.)
  hyoka_fl = float(hyoka)
❎️ failed: 0.442 < hyoka_accuracy: 0.469 all picture path Images\run\face_1.gif
 50%|████████████████████████▌                        | 1/2 [00:30<00:30, 30.17s/it] before picture path ./Images/scan/myself.gif
⭕️ success: 0.442 > hyoka_accuracy: 0.441 all picture path Images\run\face_2.gif
100%|█████████████████████████████████████████████████| 2/2 [01:00<00:00, 30.06s/it]

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