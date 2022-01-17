from db import db_handler


def withdraw_interface(username, money):
    user_dic = db_handler.select(username)
    balance = int(user_dic.get("balance"))
    money = int(money)
    money2 = money * 1.05

    if balance < money:
        return False, f"【{username}】用户余额不足！"

    user_dic['balance'] = balance - money2
    db_handler.save(user_dic)

    return True, f"【{username}】成功提现金额【{money}】！"
