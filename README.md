# poetrybase

Poetry のベースプロジェクト

## 前提

### Python のインストール

- pip をインストール
- Install Python 3.x for all users チェックしない
- Add Python to environment variables チェック

### Pyenv のインストール

```shell
pip install pyenv-win --target %USERPROFILE%\\.pyenv
```

### 開発用依存パッケージのインストール

```shell
pip install black flake8 mypy pyinstaller
```

#### 環境変数（Pyenv）

| 環境変数   | 値                                                                           |
| ---------- | ---------------------------------------------------------------------------- |
| PYENV      | %USERPROFILE%\.pyenv\pyenv-win                                               |
| PYENV_HOME | %USERPROFILE%\.pyenv\pyenv-win                                               |
| PYENV_ROOT | %USERPROFILE%\.pyenv\pyenv-win                                               |
| PATH       | %USERPROFILE%\.pyenv\pyenv-win\bin <br> %USERPROFILE%\.pyenv\pyenv-win\shims |

### Poetry のインストール

```shell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

#### 環境変数 (Poetry)

| 環境変数 | 値                       |
| -------- | ------------------------ |
| PATH     | %APPDATA%\Python\Scripts |

#### 設定

```shell
# 仮想環境をプロジェクトディレクトリ内に作成
poetry config virtualenvs.in-project true
```

## インストール

```shell
poetry install
```

### 問題

仮想環境の Python バージョンが pyproject.toml の指定と異なるものが設定される場合、  
.venv ディレクトリを削除後に以下を実行

```shell
pyenv local [対象のPythonバージョン]
python -m venv .venv
```
