"""
CRITICAL
ERROR
WARNING
INFO
DEBUG
"""

# loggingの使い方
import logging

# import logtest

# ロガー
# メインのコード意外でlogを表示したい場合に使用する
logging.basicConfig(level=logging.INFO)
logging.info('info')


# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
# logging.debug('debug')

# ロギングのフィルタ
class NoPassFilter(logging.Filter):
    def filter(self, record):
        log_message = record.getMessage()
        # 'password'という単語をフィルタ
        return 'password' not in log_message


logger = logging.getLogger(__name__)
logger.addFilter(NoPassFilter())
logger.info('from main')
logger.info('from main password = "test"')

# logtestのメソッドを使用
# logtest.do_log_test()

# ロギングの出力をformatしたい場合
# ロギングのフォーマットはドキュメントに記載されている
# https://docs.python.org/ja/3/library/logging.html?highlight=logging
# formatter = '%(asctime)s:%(levelname)s:%(message)s'
# logging.basicConfig(level=logging.DEBUG, format=formatter)

# ログ情報をファイルに書き出したい場合
# logging.basicConfig(filename='test.log', level=logging.DEBUG)

# # ロギングのログレベルはデフォルトでwarningまでなので指定してログレベルを変更する
# logging.basicConfig(level=logging.DEBUG)
#
# # ロギングの各種表示方法
# logging.critical('critical')
# logging.error('error')
# logging.warning('warning')
# logging.info('info')
# logging.debug('debug')

# ロギング内での表記方法
# (%s, 代入したい文)
# logging.info('info %s', 'test')
# logging.debug('debug %s', 'test')
