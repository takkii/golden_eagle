#### 実行時、警告文に対応するには。

```markdown
# Windows, default:user use scoop/python313.
C:/Users/user/scoop/apps/python313/current/Lib/site-packages/face_recognition_models/__init__.py
C:/Users/user/golden_eagle/patch/__init__.py

# Example, patch Applicable
cd /golden_eagle/patch
patch /home/user/.anyenv/envs/pyenv/versions/3.13.14/lib/python3.13/site-packages/face_recognition_models/__init__.py < init.patch
```

_winmergeでマージまたは、patchの適用など対応してください。_

> 更新履歴: 2026/06/12