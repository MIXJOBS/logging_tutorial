import logging


def do_log_test():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.info('test info')
    logger.debug('debug test')
