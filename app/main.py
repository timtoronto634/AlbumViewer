"""doc
"""

from pathlib import Path

import responder

from utils import Application


class ApiServer:
    """APIクラス
    """

    def __init__(self, address='0.0.0.0', port=80):
        self.api = responder.API()
        self.address = address
        self.port = port

        # TODO) サーバーでの画像保存場所をどこにするか、後で決める
        self.app = Application(self.api, cache_root=Path('var/server_cache'))

        self.index_html = Path('app/index.html').read_text(encoding='utf-8')

        self.api.add_route("/", self.get_page)
        self.api.add_route("/health", self.health_check)
        self.api.add_route("/echo/{hoge}", self.echo)

        self.api.add_route("/images", self.post_image)

    def start(self):
        """サーバーを開始する
        """
        self.api.run(address=self.address, port=self.port)

    def get_page(self, _, resp):
        """doc
        """
        resp.content = self.index_html
        resp.mimetype = 'text/html'

    def health_check(self, _, resp):
        """doc
        """
        resp.media = {"status": "ok"}
        resp.mimetype = 'application/json'

    def echo(self, _, resp, *, hoge):
        """doc
        """
        resp.media = {"content": hoge}
        resp.mimetype = 'application/json'

    async def post_image(self, req, resp):
        """画像を受け取って保存
        """
        assert req.method == 'post'

        # 画像の受け取り
        data = await req.media(format='files')
        resp.status_code = 201

        # データの保存
        self.app.save(data)


if __name__ == '__main__':
    ApiServer(address='0.0.0.0', port=80).start()
