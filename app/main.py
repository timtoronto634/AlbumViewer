"""エントリーポイント
"""
import log_setting  # noqa: F401
from api_router import ApiServer


if __name__ == '__main__':
    ApiServer(address='0.0.0.0', port=80).start()
