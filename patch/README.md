### Python3の依存ライブラリに適用するには

```markdown
# Windowsで、scoop/python313とwinmergeを使います。
C:/Users/user/scoop/apps/python313/current/Lib/site-packages/face_recognition_models/__init__.py
C:/Users/user/golden_eagle/patch/__init__.py

# WSL2環境で、golden_eagleプロジェクトに移動します。
cd /mnt/c/Users/user/golden_eagle/patch

# diffコマンドを使います。
diff -u ~/.anyenv/envs/pyenv/versions/3.13.14/lib/python3.13/site-packages/face_recognition_models/__init__.py 
./__init__.py > init.patch

# patchコマンドを使います。
cd /golden_eagle/patch patch -u ~/.anyenv/envs/pyenv/versions/3.13.14/lib/python3.13/site-packages/face_recognition_models/__init__.py < ./init.patch
```

_winmergeでマージまたは、patchの適用をしてください。_

> 更新履歴: 2026/06/13
