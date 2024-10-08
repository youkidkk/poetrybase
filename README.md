# poetrybase

Poetry のベースプロジェクト

## 前提

- pyenv
- poetry

### Windows

PowerShell を開き、以下を実行

```shell
# pyenv-win のインストール
Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"

# Python 3.12 のインストール
pyenv install 3.12.5
pyenv global 3.12.5

# poetry のインストール
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -

# 環境変数Pathへの追加と再読込
[Environment]::SetEnvironmentVariable("Path", "${ENV:APPDATA}\pypoetry\venv\Scripts;"+$ENV:Path, "User")
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

# Python仮想環境をプロジェクトディレクトリ内に作成するように設定
poetry config virtualenvs.in-project true
```

---

## プロジェクトの仮想環境を作成

- ディレクトリ名の変更

  - プロジェクトディレクトリを [プロジェクト名] に変更
  - `poetrybase` ディレクトリを [プロジェクト名] に変更

- `pyproject.toml` の以下を変更

```toml
name = "[プロジェクト名]"
version = "0.1.0"
```

- Python 仮想環境を作成

```shell
poetry install
```
