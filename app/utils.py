"""とりあえず
"""

import time
import logging


# サブプロセスが出力するログ
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(
    logging.FileHandler(filename="var/server_background.log",
                        encoding="utf-8"))


class Jobs:
    """バックグラウンド実行するつもりの関数をまとめておく
    """

    @staticmethod
    def _save(storage, data):
        """画像を保存する関数
        """
        for _, file in data.items():
            filename = file['filename']
            content = file['content']
            ctype = file['content-type']
            if not ctype.startswith('image/'):
                return
            (storage/filename).write_bytes(content)
            logger.info('saved :'+str(filename))


class Application:
    """メインの処理
    """

    def __init__(self, api, cache_root):
        self._api = api
        # データの保存場所
        self.storage = cache_root
        self.storage.mkdir(exist_ok=True, parents=True)

    def save(self, data):
        """画像を保存
        """
        self._api.background.task(Jobs._save)(self.storage, data)
