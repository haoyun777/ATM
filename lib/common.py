"""存放公共方法"""

import hashlib
import logging.config
from core import src
from conf import settings


def get_pwd_md5(password):
    md5_obj = hashlib.md5()
    md5_obj.update(password.encode('utf-8'))
    salt = '一二三四五'
    md5_obj.update(salt.encode('utf-8'))

    return md5_obj.hexdigest()


def login_auth(func):

    def warppers(*args, **kwargs):
        if not src.login_user:
            print('请先登陆！')
            src.login()
        res = func(*args, **kwargs)
        return res

    return warppers


def get_logger(log_type):
    """
    :param log_type: 比如是user日志，bank日志，购物商城日志
    :return:
    """

    logging.config.dictConfig(
        settings.LOGGING_DIC
    )

    logger = logging.getLogger(log_type)

    return logger
