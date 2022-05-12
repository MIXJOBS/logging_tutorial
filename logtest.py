import logging

if __name__ == '__main__':
    print("mainとして実行します")
else:
    print("importされて実行します")

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# logtest.logのハンドルをloggerに渡す
# loggerがだすlogのみがlogtest.logに記述される
h = logging.FileHandler('logtest.log')
logger.addHandler(h)


def do_log_test():
    logger.info('test info')
    logger.debug('debug test')
