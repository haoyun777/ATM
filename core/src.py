"""
用户视图层
"""

from interface import user_interface


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
    pass


# 3. 查看余额
def check_balance():
    pass


# 4. 提现功能
def withdraw():
    pass


# 5. 还款功能
def repay():
    pass


# 6. 转账功能
def transfer():
    pass


# 7. 查看流水
def check_flow():
    pass


# 8. 购物功能
def shopping():
    pass


# 9. 查看购物车
def check_shop_car():
    pass


# 10. 管理员功能
def admin():
    pass


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