
from db import db_handler
from lib import common


def register_interface(username, password, balance=15000):

    user_dic = db_handler.select(username)
    if user_dic:
        return False, '用户名已存在！'

    password = common.get_pwd_md5(password)
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


def login_interface(username, password):

    user_dic = db_handler.select(username)

    if not user_dic:
        return False, f"【{username}】用户不存在！"

    if user_dic.get("locked"):
        return False, f"【{username}】用户已锁定！"

    password = common.get_pwd_md5(password)
    if password == user_dic.get('password'):

        return True, f"【{username}】登陆成功！"

    else:
        return False, f"【{username}】密码错误！"


def check_bal_interface(username):
    user_dic = db_handler.select(username)
    if not user_dic:
        return False, f"【{username}】用户不存在！"

    return True, f"【{username}】的账户余额为：{user_dic.get('balance')}"


def lock_user_interface(username):
    user_dic = db_handler.select(username)
    if not user_dic:
        return False, '该用户不存在！'

    user_dic["locked"] = True

    db_handler.save(user_dic)

    return True, f"【{username}】用户冻结成功！"

