#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys,prettytable,logging

#定义日志级别、格式、输出位配置
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %Y-%m-%d %H:%M:%S',
                    filename='log/test.log',
                    filemode='a',
                    )

def zhu():
    user=''
    while True:
        x = prettytable.PrettyTable(["\033[32m编号\033[0m","\033[33m名称\033[0m"])
        x.add_row(['1','\033[32m进入商店\033[0m'])
        x.add_row(['2','\033[33m登录系统\033[0m'])
        x.add_row(['3','\033[34m信用卡管理\033[33m'])
        x.add_row(['4','\033[33m后台管理\033[0m'])
        x.add_row(['5','\033[33m用户管理\033[0m'])
        x.add_row(['6','exit'])
        print(x)
        a=input("enter 编号:")

        if a=='1':
            import shangpin
            rmb=shangpin.sp()

        elif a=="2":
            if not user:
                import denglu
                user=denglu.login()

            else:
                print("已经登录了！")
                logging.error('error message,enter username:%s yi jing login! '%user)#记录错误日志
            enter=input("请按回车继续：")
            continue

        elif a=="3":
            import xyk
            xyk.xingyongka()

        elif a=="4":
            import houtai
            houtai.houtaiguanli()

        elif a=="5":
            if not  user:
                import denglu
                user=denglu.login()
                if user:
                    denglu.yhzx(user)
            else:
                denglu.yhzx(user)
            enter=input("请按回车继续：")
        elif a=="6":
            sys.exit()

        else:
            print("输入的编号不存在！")
            logging.error('error message, enter bianhao bu cun zai!')#记录错误日志

if __name__=="__main__":
    zhu()
