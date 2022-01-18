from core.src import register
from interface import user_interface


def admin_add_user():
    register()


def admin_check_balance():
    while True:
        check_balance_user = input("请输入您要查看的用户：").strip()
        flag, msg = user_interface.check_bal_interface(check_balance_user)
        print(msg)
        if flag:
            break


def admin_lock_user():
    while True:
        input_lock_user = input("请输入您要冻结的用户：").strip()
        flag, msg = user_interface.lock_user_interface(input_lock_user)
        print(msg)
        if flag:
            break


admin_func_dic = {
    '1': admin_add_user,
    '2': admin_check_balance,
    '3': admin_lock_user
}


def admin_run():
    while True:
        print("""
        ====== 管理员功能 ======
            1. 添加账户
            2. 用户额度
            3. 冻结账户
        ========== end ==========
        """)
        admin_choice = input("请输入管理员功能编号：").strip()
        if admin_choice not in admin_func_dic:
            print("请输入正确的管理员功能编号！")
            continue

        admin_func_dic.get(admin_choice)()
