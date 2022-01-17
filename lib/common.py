"""存放公共方法"""

import hashlib
from core import src


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
