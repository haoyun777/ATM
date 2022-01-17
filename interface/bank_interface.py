from db import db_handler


def withdraw_interface(username, money):
    user_dic = db_handler.select(username)
    balance = int(user_dic.get("balance"))
    money = int(money)
    money2 = money * 1.05

    if balance < money:
        return False, f"【{username}】用户余额不足！"
    flow = f"【{username}】成功提现金额【{money}】！"
    user_dic['balance'] = balance - money2
    user_dic["flow"].append(flow)
    db_handler.save(user_dic)

    return True, flow


def repay_interface(username, money):
    user_dic = db_handler.select(username)
    money = int(money)

    if money <= 0:
        return False, "输入的金额不能小于0！"
    flow = f"【{username}】成功还款金额【{money}】！"
    user_dic['balance'] += money
    user_dic["flow"].append(flow)
    db_handler.save(user_dic)
    return True, flow


def transfer_interface(username, to_username, money):
    money = int(money)

    if money <= 0:
        return False, "输入的金额不能小于0！"

    login_user_dic = db_handler.select(username)
    to_user_dic = db_handler.select(to_username)

    if not to_user_dic:
        return False, f"【{to_username}】用户不存在！"

    if login_user_dic.get("balance") < money:
        return False, f"余额不足，请先充值！"

    login_user_dic["balance"] -= money
    to_user_dic["balance"] += money

    flow = f"【{username}】给【{to_username}】成功转账【{money}】！"

    login_user_dic["flow"].append(flow)
    to_user_dic["flow"].append(flow)

    db_handler.save(login_user_dic)
    db_handler.save(to_user_dic)

    return True, flow


def check_flow_interface(username):
    user_dic = db_handler.select(username)
    return user_dic.get("flow")
