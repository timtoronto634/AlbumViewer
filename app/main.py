import cv2
import responder


class Application:

    def __init__(self, port=80):
        self.api = responder.API()
        self.port = port

        self.api.add_route("/", self.get_page)
        self.api.add_route("/health", self.health_check)
        self.api.add_route("/echo/{hoge}", self.echo)

    def start(self):
        self.api.run(address='0.0.0.0', port=self.port)

    def get_page(self, _, resp):
        resp.content = "<body>hello, world</body>"
        resp.mimetype = 'text/html'

    def health_check(self, _, resp):
        resp.media = {"status": "ok"}
        resp.mimetype = 'application/json'

    def echo(self, req, resp, *, hoge):
        resp.media = {"content": hoge}
        resp.mimetype = 'application/json'


if __name__ == '__main__':
    Application().start()
