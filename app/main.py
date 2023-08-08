"""doc
"""

from pathlib import Path

# import cv2
import responder


class Application:
    """doc
    """

    def __init__(self, address='0.0.0.0', port=80):
        self.api = responder.API()
        self.address = address
        self.port = port

        self.index_html = Path('app/index.html').read_text(encoding='utf-8')

        self.api.add_route("/", self.get_page)
        self.api.add_route("/health", self.health_check)
        self.api.add_route("/echo/{hoge}", self.echo)

        self.api.add_route("/images", self.post_image)

    def start(self):
        """doc
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

    async def post_image(self, req, _resp):
        """doc
        """
        assert req.method == 'post'

        # 画像の受け取り
        data = await req.media(format='files')
        print(type(data))
        print(data.keys())

        # サーバーでの画像保存場所 TODO) あとで見直す
        storage = Path('var/server_cache')
        storage.mkdir(exist_ok=True, parents=True)

        # 保存
        def save_image(file):
            filename = file['filename']
            content = file['content']
            ctype = file['content-type']
            print(ctype)
            if not ctype.startswith('image/'):
                return
            (storage/filename).write_bytes(content)

        for _, file in data.items():
            save_image(file)


if __name__ == '__main__':
    Application(address='0.0.0.0', port=80).start()
