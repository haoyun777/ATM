
from db import db_handler


def register_interface(username, password, balance=15000):

    user_dic = db_handler.select(username)
    if user_dic:
        return False, '用户名已存在！'

    user_dic = {
        'username': username,
        'password': password,
        'balance': balance,
        'flow': [],
        'shop_car': {},
        'locked': False
    }
    db_handler.save(user_dic)

    return True, f"{username}注册成功！"
