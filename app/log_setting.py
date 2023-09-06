"""logging の初期化

メインから最初に一度だけ呼び出す。

Python では同じモジュールに対して複数回 import しても
最初しかロード(実行)が入らないので複数回 import しても故障はしない。
"""
from logging import config
from pathlib import Path

import yaml


# TODO : 環境変数などに応じて yaml の中身を書き換える(ログファイルのルートディレクトリなど)
# TODO : ログファイル出力のディレクトリを作成する

# logging 設定ファイルの読み込み
config_file_path = (Path(__file__) / '../logconf.yaml').resolve()
dict_conf = yaml.load(config_file_path.read_text(), Loader=yaml.FullLoader)
config.dictConfig(dict_conf)
