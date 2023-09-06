"""doc
"""
import logging

import usecase.save_images


logger = logging.getLogger(__name__)
logger.info('loaded application.py')


class Application:

    def __init__(self, api, cache_root):
        self._api = api
        self.background_runner = api.background.task
        # データの保存場所
        self.storage = cache_root
        self.storage.mkdir(exist_ok=True, parents=True)

    def save(self, datas):
        """画像を保存
        """
        usecase.save_images.save(self.storage, datas,
                                 wrapper=self.background_runner)
