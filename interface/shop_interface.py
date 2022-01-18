from db import db_handler
from interface import bank_interface


def pay_interface(username, car):

    money = 0

    for k, v in car.items():
        money += v[0] * v[1]

    flag, msg = bank_interface.shop_pay_interface(username, money)

    if flag:
        return True, "支付成功！"
    else:
        return flag, msg


def shop_car_check_interface(username):
    user_dic = db_handler.select(username)
    return user_dic.get('shop_car')


def shop_car_save_interface(username, shopping_car):
    user_dic = db_handler.select(username)
    shop_car = user_dic.get('shop_car')
    for k, v in shopping_car.items():
        if k in shop_car:
            shop_car[k][1] += v[1]
        else:
            shop_car[k] = v
    db_handler.save(user_dic)


def shop_car_pay_interface(username):
    user_dic = db_handler.select(username)
    shop_car = user_dic.get('shop_car')
    flag, msg = pay_interface(username, shop_car)
    if flag:
        return True, "支付成功！"
    else:
        return flag, msg
