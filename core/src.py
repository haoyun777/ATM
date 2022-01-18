"""
用户视图层
"""

from interface import user_interface
from lib.common import login_auth
from interface import bank_interface
from interface import shop_interface


login_user = None


# 1. 注册功能
def register():
    while True:
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()
        re_password = input('请输确认密码：').strip()
        if password != re_password:
            print('两次输入的密码不一样，请重新输入！')
            continue

        flag, msg = user_interface.register_interface(username, password)

        print(msg)
        if flag:
            break


# 2. 登陆功能
def login():
    while True:
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()

        flag, msg = user_interface.login_interface(username, password)

        print(msg)
        if flag:
            global login_user
            login_user = username
            break


# 3. 查看余额
@login_auth
def check_balance():
    flag, msg = user_interface.check_bal_interface(login_user)
    print(msg)


# 4. 提现功能
@login_auth
def withdraw():
    while True:
        input_money = input("请输入提现金额：").strip()
        if not input_money.isdigit():
            print("请重新输入！")
            continue

        flag, msg = bank_interface.withdraw_interface(login_user, input_money)
        print(msg)
        break


# 5. 还款功能
@login_auth
def repay():
    while True:
        input_money = input("请输入需要还款的金额：").strip()
        if not input_money.isdigit():
            print("请重新输入！")
            continue

        flag, msg = bank_interface.repay_interface(login_user, input_money)
        print(msg)
        break


# 6. 转账功能
@login_auth
def transfer():
    while True:
        to_user = input("请输入转账目标用户：").strip()
        input_money = input("请输入转账金额：").strip()
        if not input_money.isdigit():
            print("请重新输入！")
            continue

        flag, msg = bank_interface.transfer_interface(
            login_user, to_user, input_money
        )
        print(msg)
        break


# 7. 查看流水
@login_auth
def check_flow():
    flow_list = bank_interface.check_flow_interface(login_user)

    if not flow_list:
        print("当前用户没有流水！")

    for flow in flow_list:
        print(flow)


# 8. 购物功能
@login_auth
def shopping():
    shop_list = [
        ['南京灌汤包', 30],
        ['老北京烤鸭', 199],
        ['广东凤爪', 28],
        ['MacBook pro', 2000],
        ['水杯', 66],
    ]
    shopping_car = {}
    while True:
        for index, shop in enumerate(shop_list):
            print(index, ":", shop[0], shop[1])

        shop_choice = input("请输入商品编号：").strip()

        if not shop_choice.isdigit():
            print("请输入正确的编号！")
            continue
        shop_choice = int(shop_choice)
        if shop_choice not in range(len(shop_list)):
            print("请输入正确的编号！")
            continue
        shop_name, shop_price = shop_list[shop_choice]

        if shop_name in shopping_car:
            shopping_car[shop_name][1] += 1
        else:
            shopping_car[shop_name] = [shop_price, 1]

        option_choice = input("是否直接下单输入 y or n : ").strip()

        if option_choice == 'y':
            flag, msg = shop_interface.pay_interface(login_user, shopping_car)
            if flag:
                print("购买成功，准备发货！")
                break
            else:
                print(msg)
                continue

        elif option_choice == 'n':

            exit_choice = input("是否退出商城输入 y or n : ").strip()

            if exit_choice == 'y':
                shop_interface.shop_car_save_interface(login_user, shopping_car)
                break


# 9. 查看购物车
@login_auth
def check_shop_car():
    shop_car = shop_interface.shop_car_check_interface(login_user)

    if not shop_car:
        print("购物车空空如也，快去添加吧！")
        return

    for k, v in shop_car.items():
        print(f"商品：【{k}】，单价：【{v[0]}】，数量【{v[1]}】")

    option_choice = input("是否全部下单输入 y or n : ").strip()
    if option_choice == "y":
        flag, msg = shop_interface.shop_car_pay_interface(login_user)
        if flag:
            print("购买成功，准备发货！")
        else:
            print(msg)


# 10. 管理员功能
@login_auth
def admin():
    from core import admin
    admin.admin_run()


# 创建函数功能字典
func_dic = {
    '1': register,
    '2': login,
    '3': check_balance,
    '4': withdraw,
    '5': repay,
    '6': transfer,
    '7': check_flow,
    '8': shopping,
    '9': check_shop_car,
    '10': admin,
}


# 视图层主程序
def run():
    while True:
        print("""
        ====== ATM + 购物车 ======
            1. 注册功能
            2. 登陆功能
            3. 查看余额
            4. 提现功能
            5. 还款功能
            6. 转账功能
            7. 查看流水
            8. 购物功能
            9. 查看购物车
            10. 管理员功能
        ========== end ==========
        """)
        choice = input("请输入功能编号：").strip()
        if choice not in func_dic:
            print("请输入正确的功能编号！")
            continue

        func_dic.get(choice)()
