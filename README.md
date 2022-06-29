# KEIO_AUTO_LOGIN
Pythonとchromedriverを使ってkeio.jpのログインを自動で行います。

# Requirement

* Anaconda4(Python3.9)

# Installation

- 好きな階層でプロジェクトフォルダーをcloneする

```:bash
git clone https://github.com/mando0520/keio_auto_login_python.git
```

- [Anaconda](https://www.anaconda.com/products/distribution)をインストールし、Anaconda環境を立ち上げる。
  - Macの場合、ターミナルで、`conda activate`
  - Windowsの場合、AnacondaPromptを起動
- Anaconda環境で、ライブラリのselenium, dotenvをインストールする(pipでも可)

```:bash
conda install selenium
conda install dotenv
```

- chromeのバージョンと同じchromedriverをダウンロードし、実行ファイルを同階層に配置する
  - chromeバージョン確認 : chrome右上の[︙] > [ ヘルプ ] > [ Google Chrome について ]
  - [chromedriverダウンロード](https://chromedriver.chromium.org/downloads)
  - Windowsの場合、`chromedriver.exe`となるので、`keio.py`の17行目を編集する

# Usage

プロジェクトフォルダー配下(keio.pyと同じ階層)に、「.env」ファイルを作成する。
そこに以下を記入し、右辺を自分のアカウント情報に編集する。

```
KEIO_LOGIN_ID=xxxxx
KEIO_LOGIN_PASSWORD=xxxxx
```

Anacondaでプロジェクトフォルダーの階層に行き、keio.pyを実行

```:bash
python keio.py
```