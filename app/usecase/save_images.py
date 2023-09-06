"""画像を保存
"""

import logging


logger = logging.getLogger(__name__)
logger.info('loaded usecase/save_images.py')


def _save(storage, datas):
    """画像を保存する関数
    """
    for file in datas:
        (storage/file['filename']).write_bytes(file['content'])
        logger.info('saved :'+str(file['filename']))


def save(storage, datas, wrapper=lambda f: f):
    if wrapper is not None:
        wrapper(_save)(storage, datas)
    else:
        _save(storage, datas)
