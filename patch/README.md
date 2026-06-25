### Python3の依存ライブラリにパッチを適用するには

```markdown
# Windows (scoop/python313)
C:/Users/user/scoop/apps/python313/current/Lib/site-packages/face_recognition_models/__init__.py
C:/Users/user/golden_eagle/patch/__init__.py

# WSL2環境、golden_eagle/patch
cd /mnt/c/Users/user/golden_eagle/patch

# パッチを生成します (WSL2)
diff -u /mnt/c/Users/user/scoop/apps/python313/current/Lib/site-packages/face_recognition_models/__init__.py ./__init__.py > init.patch

# パッチを生成します (UNIX/anyenv)
diff -u ~/.anyenv/envs/pyenv/versions/3.13.14/lib/python3.13/site-packages/face_recognition_models/__init__.py ./__init__.py > init.patch

# パッチを適用します (WSL2)
patch -u /mnt/c/Users/user/scoop/apps/python313/current/Lib/site-packages/face_recognition_models/__init__.py < ./init.patch

# パッチを適用します (UNIX/anyenv)
patch -u ~/.anyenv/envs/pyenv/versions/3.13.14/lib/python3.13/site-packages/face_recognition_models/__init__.py < ./init.patch

# パッチを元に戻します (WSL2)
patch -u -R /mnt/c/Users/user/scoop/apps/python313/current/Lib/site-packages/face_recognition_models/__init__.py < ./init.patch

# パッチを元に戻します (UNIX/anyenv)
patch -u -R ~/.anyenv/envs/pyenv/versions/3.13.14/lib/python3.13/site-packages/face_recognition_models/__init__.py < ./init.patch
```

※ コマンドプロンプトで実行するPATHは省略します。❎️

_WSL2側から、各環境ごとにパッチの適用を検討してください。_✅️

> 更新履歴: 2026/06/25
