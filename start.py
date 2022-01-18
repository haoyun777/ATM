"""
程序的入口
"""

import sys
import os


if not os.path.exists('log'):
    os.mkdir('log')

if not os.path.exists('db/user_data'):
    os.mkdir('db/user_data')

from core import src

# 添加解释器的环境变量
sys.path.append(
    os.path.dirname(__file__)
    )


# 开始执行项目函数
if __name__ == '__main__':

    # 1. 先执行用户视图层
    src.run()
