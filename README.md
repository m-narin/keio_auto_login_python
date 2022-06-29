# KEIO_AUTO_LOGIN
Pythonとchromedriverを使ってkeio.jpのログインを自動で行います。

# Requirement

* Anaconda4(Python3.9)

# Installation

- Anacondaをインストール。
- Anaconda環境で、ライブラリのselenium, dotenvをインストールする(conda, pipどちらも可)
- chromeのバージョンと同じchromedriverをダウンロードして実行ファイルを同階層に配置する
  - [chromeバージョン確認](chrome://settings/help)
  - [chromedriverダウンロード](https://chromedriver.chromium.org/downloads)

# Usage

.envファイルを作成し、以下を記入。右辺を編集する。

```
KEIO_LOGIN_ID=xxxxx
KEIO_LOGIN_PASSWORD=xxxxx
```

Anacondaで、keio.pyを実行

```:bash
python keio.py
```