#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys,prettytable,json,logging

#定义日志级别、格式、输出位配置
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %Y-%m-%d %H:%M:%S',
                    filename='log/test.log',
                    filemode='a',
                    )

def houtaiguanli():
    with open('conf/userinfo.txt', 'r') as f:
        data = json.load(f)

    a=[]
    try:
        with open('conf/suouser.txt') as f:#从文件读取已经锁定的用户

                for i in f:
                        i=i.strip('\n')
                        a.append(i.strip())
    except FileNotFoundError:

        pass

    try:
        with open("conf/xykinfo.txt","r") as f:
            data1=json.load(f)
    except json.decoder.JSONDecodeError:

        data1={"0":["0",0,0]}
        with open("conf/xykinfo.txt","w") as f:
            json.dump(data1,f)
    useradmin=input("输入管理员帐号:")
    password=input("输入管理员密码:")
    while True:

        if useradmin!="root" or  password!="123456":
            print("你的权限不够")
            logging.error('error message, user or password not admin!')#记录错误日志
        else:
            x = prettytable.PrettyTable(["\033[32m菜单编号\033[0m","\033[33m菜单名称\033[0m"])
            x.add_row(['1','\033[32m创建用户\033[0m'])
            x.add_row(['2','\033[32m删除用户\033[0m'])
            x.add_row(['3','\033[32m解锁用户\033[0m'])
            x.add_row(['4','\033[32m发行信用卡用户\033[0m'])
            x.add_row(['5','\033[32m冻结信用卡\033[0m'])
            x.add_row(['6','\033[32mexit\033[0m'])
            print(x)
            shuru=input("请输入编号:")
            if shuru=="1":

                print(data)
                useradd=input("输入用户名:")
                if  data.get(useradd):
                    print("[%s]这个用户名存在"%useradd)
                    logging.error('error message, enter username bu cun zai!')#记录错误日志
                else:
                    useraddpassword=input("请输入密码：")
                    data[useradd]=useraddpassword

                    print("用户名%s已经创建"%useradd)
                    enter=input("请按回车继续：")
                    continue
            if shuru=="2":
                userdel=input("输入要删除的用户:")
                if userdel in data.keys():
                    del data[userdel]
                    print("用户%s已经被删除"%userdel)
                else:
                    print("不存在这个用户")
            if shuru=="3":
                suouser=input("输入要解锁的用户：")
                if suouser in a:
                    a.remove(suouser)
                    print(a)
                    with open("suouser.txt","w") as f:
                        for i in a:
                            i=i.strip()
                            f.write(i)
                    print("用户%s已经解除锁定"%suouser)
                else:
                    print("输入的用户不在锁定用户的列表")
            if shuru=="4":
                kahao=input("请输入卡号：")
                if kahao not in data1.keys():
                    kapassword=input("输入卡的密码：")
                    kaed=float(input("输入卡的额度："))
                    data1[kahao]=[kapassword,kaed,0]
                    print("已经发行了一张信用卡，卡号是%s,额度为%s元"%(kahao,kaed))
                    enter=input("请按回车继续：")
                else:
                    print("已经存在此卡号")
            if shuru=="5":
                suokahao=input("请输入要冻结的卡号：")
                if suokahao in data1.keys():
                    print("卡号%s,额度%s"%(suokahao,data1.get(suokahao)[1]))
                    queren=input("确认冻结吗？y/n：")
                    if queren=="y":
                        data1.get(suokahao)[2]=4
                        print("卡号%s已经被冻结了"%suokahao)

                else:
                    print("卡号不存在")
                    logging.error('error message, enter kahao bu cun zai!')#记录错误日志

            if shuru=="6":
                break
                pass
        with open('conf/userinfo.txt', 'w') as f:
            json.dump(data,f)
        with open('conf/xykinfo.txt', 'w') as f:
            json.dump(data1,f)


if __name__=="__main__":
    houtaiguanli()

