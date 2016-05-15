#!/usr/bin/env python
# -*- coding:utf-8 -*-
import  sys,json,logging,prettytable
#定义日志级别、格式、输出位配置
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %Y-%m-%d %H:%M:%S',
                    filename='log/test.log',
                    filemode='a',
                    )

def login():
    with open('conf/userinfo.txt', 'r') as f:
        userpass = json.load(f)
    print(userpass)
    #userpass={'jwh':'123456','wenhui':'654321','test':'test','test01':'abcd1234'}
    counter=0#定义登录次数（初始值是0）
    a=[]
    try:
        with open('conf/suouser.txt') as f:#从文件读取已经锁定的用户


                for i in f:
                        i=i.strip('\n')
                        a.append(i.strip())
    except FileNotFoundError:
        pass
    while True:
        user=input("请输入要登录的用户名:")
        if user in a:#判断用户是否被锁
                print ("此用户已经被锁")
                logging.error('error message,user:%s bei suo le ')#记录错误日志
                jiesuo=input("是否需要解锁账户y/n:")
                if jiesuo=='y':

                        while True:
                            adminuser=input('请输入管理员帐号:')
                            if adminuser !='root':
                                    print ("管理员帐号不对")
                                    logging.error('error message,user:guan li yuan zhanghao bu dui ')#记录错误日志
                                    continue
                            else:

                                    while True:
                                            adminpwd=input('请输入管理员密码:')
                                            if adminpwd != '123456':
                                                    print("管理员密码不对")
                                                    logging.error('error message,adminpassword bu dui ')#记录错误日志
                                                    continue
                                            else:
                                                    break
                                    break
                        while True:
                            jiesuouser=input('请输入你要解锁的帐号:')

                            if jiesuouser in a:
                                a.remove(jiesuouser)
                                f=open('conf/suouser.txt','w')
                                f.write('')
                                f.close()
                                for line in a:
                                        f=open('conf/suouser.txt','a')
                                        f.write('%s\n'%line)
                                        f.close()


                                print ("帐号%s已经被解锁,请重新去用此用户登录" % jiesuouser)
                                logging.error('error message,user:%s bu zai suo ding de list '%user)#记录错误日志
                                sys.exit()
                            else:
                                tuichu=input('此帐号不存在或已经被解锁。是否要继续解锁其他帐号y/n:')
                                logging.error('error message,user:%s bu zai suo ding de list '%user)#记录错误日志
                                if tuichu=='y':
                                  continue
                                else:
                                        sys.exit()


                else:
                        continue
        if user not  in userpass.keys():
                print ("用户名不存在")
                logging.error('error message,user:%s bu zai  '%user)#记录错误日志
                continue
        else:
                pass
                break


    while True:
            if counter<3:
                    password=input("输入密码:").strip()
                    if len(password)==0:
                            print ("\033[36m密码不能为空\033[0m")
                            counter+=1
                            continue
                    elif password==userpass[user]:
                            pass
                    else:
                            print ("\033[37m用户名为 %s的这个用户的密码不对\033[0m" % user)
                            logging.error('error message,user:%s password error '%user)#记录错误日志
                            counter+=1
                            continue
                    break
            else:
                    print ("\033[32m输入密码错误3次，用户已经被锁定了\033[0m")
                    logging.error('error message,user:%s enter password > 3 ci, bei suo le '%user)#记录错误日志
                    f=open('conf/suouser.txt','a')
                    f.write('\n%s' %(user))#锁定用户并写入到文件
                    f.close()
                    sys.exit()

    print("\033[34m-----------------用户%s密码验证通过,欢迎进入系统----------------\033[1m"%user)
    return user


def yhzx(user):
    x = prettytable.PrettyTable(["\033[32m编号\033[0m","\033[33m名称\033[0m"])
    x.add_row(['1','\033[32m修改密码\033[0m'])
    x.add_row(['2','\033[32m购物记录\033[0m'])
    x.add_row(['3','\033[32m我的账单\033[0m'])
    x.add_row(['4','\033[32mquit\033[0m'])

    while True:
        print(x)
        shuru=input("输入编号：")
        if shuru=="1":
            while True:
                new_password=input("输入新的密码：")
                new_password1=input("再次输入新的密码：")
                if new_password!=new_password1:
                    print("两次输入的密码不一致，请重新输入：")
                    logging.error('error message,liang ci enter de password bu yi yang ')#记录错误日志
                    continue
                else:
                    with open('conf/userinfo.txt', 'r') as f:
                        userpass = json.load(f)
                    userpass[user]=new_password
                    with open('conf/userinfo.txt', 'w') as f:
                            json.dump(userpass,f)
                    print("密码修改成功！")
                    break

        if shuru=="2":
            p = prettytable.PrettyTable(["\033[32mdatetime\033[0m","\033[33mgoods名称\033[0m","rmb"])
            startdate=input("输入开始日期：格式如：2016-01-01 ：")
            enddate=input("输入结束日期：格式如：2016-01-01 ：")
            with open("jilu/jilu.txt") as f:
                for i in f:
                    dateshijian,liushuiuser,goods,price=i.split("--")
                    if user in liushuiuser:
                        riqi,sjtime=dateshijian.split(" ")
                        riqi=riqi.replace("-","")
                        #print(riqi)
                        if int(riqi)>int(startdate.replace("-","")) and int(riqi)<int(enddate.replace("-","")):
                            #print("datetime:%s,goods:%s,rmb%s"%(dateshijian,goods,price))
                            p.add_row([dateshijian,goods,price])
            print(p)
            input("请按回车继续！")


        if shuru=="3":
            y = prettytable.PrettyTable(["\033[32m日期\033[0m","\033[33m信用卡卡号\033[0m","\033[34m银行流水号\033[0m","\033[36m交易金额\033[0m","\033[36m交易类型\033[0m"])
            startdate=input("输入开始日期：格式如：2016-01-01 ：")
            enddate=input("输入结束日期：格式如：2016-01-01 ：")

            with open('conf/xykinfo.txt', 'r') as f:
                data = json.load(f)
                print(data)
                #print( type(data))
            kahao=input("请输入你的卡号:")

            with open("jilu/liushui.txt") as f:
                for i in f:
                    dateshijian,liushuikahao,liushuihao,price,xiaofeitype=i.split("--")
                    if kahao in liushuikahao:
                        riqi,sjtime=dateshijian.split(" ")
                        riqi=riqi.replace("-","")
                        if int(riqi)>int(startdate.replace("-","")) and int(riqi)<int(enddate.replace("-","")):
                            y.add_row([dateshijian,liushuikahao,liushuihao,price,xiaofeitype])
                print(y)
            input("请按回车继续！")

        if shuru=="4":
            break



if __name__=="__main__":
    user=login()
    if user:
        yhzx(user)
