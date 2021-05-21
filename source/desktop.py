import eel
import sys
import socket

# 定数
ENTRY_POINT = 'index.html'
CHROME_ARGS = [
    '--incognit',  # シークレットモード
    '--disable-http-cache',  # キャッシュ無効
    '--disable-plugins',  # プラグイン無効
    '--disable-extensions',  # 拡張機能無効
    '--disable-dev-tools',  # デベロッパーツールを無効にする
]
ALLOW_EXTENSIONS = ['.html', '.css', '.js', '.ico']


def start(appName, endpoint,size):  # 画面生成
    eel.init(appName, allowed_extensions=ALLOW_EXTENSIONS)
    # 未使用ポート取得
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 0))
    port = s.getsockname()[1]
    s.close()
    options = {
        'mode': "chrome",
        'close_callback': exit,
        'port': port,
        'cmdline_args': CHROME_ARGS,
        'size': (1000, 700)
    }
    eel.start(endpoint, options=options,
        size=size, suppress_error=True)

def exit(arg1, arg2):  # 終了時の処理
    sys.exit(0)