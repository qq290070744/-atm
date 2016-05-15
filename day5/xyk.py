#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys,prettytable,json,datetime,logging
#定义日志级别、格式、输出位配置
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %Y-%m-%d %H:%M:%S',
                    filename='log/test.log',
                    filemode='a',
                    )


def xingyongka():
    with open('conf/xykinfo.txt', 'r') as f:
        data = json.load(f)
    print(data)
    #print( type(data))

    def qian():
        while True:
            try:
                rmb=int(input("rmb:"))
                if rmb<0:
                    print("金额不能是负数！")
                    continue
            except ValueError:
                print("只能输入数字")
                logging.error('error message,rmb not enter num')#记录错误日志
                continue
            else:
                return rmb

    num=0
    flag=True
    while num<=3 and flag:
        kahao=input("输入卡号:")
        mima=input("输入密码:")


        #判断密码是否正确
        if kahao in data.keys() :
            if mima != data.get(kahao)[0]: #data[kahao][0]:
                print("密码不对！")
                logging.error('error message,kahao:%s password:%s error'%(kahao,mima))#记录错误日志
            else:
                 #判断是否锁定
                if int(data.get(kahao)[2]):
                    if int(data.get(kahao)[2])>=3:
                        print("此卡已锁定或冻结,请重新输入")
                        logging.error('error message,kahao:%s bei dong jie'%(kahao))#记录错误日志
                        continue
                while True:
                    x = prettytable.PrettyTable(["\033[32m编号\033[0m","\033[33m名称\033[0m"])
                    x.add_row(['1','\033[32m我的信用卡\033[0m'])
                    x.add_row(['2','\033[32m提现\033[0m'])
                    x.add_row(['3','\033[32m转账\033[0m'])
                    x.add_row(['4','\033[32m还款\033[0m'])
                    x.add_row(['5','\033[32mquit\033[0m'])
                    print(x)
                    a=input("输入编号")

                    if a=="1":
                        y = prettytable.PrettyTable(["\033[32m卡号\033[0m","\033[33m余额\033[0m"])
                        y.add_row([kahao,'%s'%data[kahao][1]])

                        print(y)
                        enter=input("请按回车继续：")
                    if a=="2":
                        while True:

                            print("请输入提现金额")
                            txje=qian()
                            #txje=int(input("请输入提现金额"))


                            if float (data[kahao][1])>float (txje):

                                sxf=txje*0.05
                                data[kahao][1]=float (data[kahao][1])-txje-sxf
                                print("提现金额%s,手续费%s,还剩余额%s"%(txje,sxf,data.get(kahao)[1]))
                                with open("jilu/liushui.txt","a") as f:#写入流水记录到文件
                                    shijian=datetime.datetime.now()
                                    liushuihao=str(shijian).replace("-",'')
                                    liushuihao=liushuihao.replace(":",'')
                                    liushuihao=liushuihao.replace(" ",'')
                                    liushuihao=liushuihao.replace(".",'')
                                    f.write("%s--%s--%s--%s--提现(包含%s手续费)\n"%(shijian,kahao,liushuihao,txje+sxf,sxf))
                                enter=input("请按回车继续：")
                                break
                            else:
                                print("余额不足,重新输入")
                                logging.error('error message,kahao:%s yue bu zu'%(kahao))#记录错误日志
                                continue

                    if a=="3":
                        while True:
                            duifangkahao=input("输入对方卡号:")
                            if duifangkahao not  in data.keys():
                                print("卡号不存在")
                                logging.error('error message,kahao:bu cun zai')#记录错误日志
                                continue

                            else:
                                while True:
                                    print("输入转账金额:")
                                    zzje=qian()
                                    #zzje=float (input("输入转账金额:"))

                                    if zzje>float (data.get(kahao)[1]):
                                        print("余额不足，转载失败")
                                        logging.error('error message,kahao:%s zhuan zhang, yue bu zu'%(kahao))#记录错误日志
                                        continue
                                    else:
                                        data.get(duifangkahao)[1]=float (data.get(duifangkahao)[1])+zzje
                                        data.get(kahao)[1]=float(data.get(kahao)[1])-zzje
                                        print("你转了[%s]元到[%s]账户"%(zzje,duifangkahao))
                                        with open("jilu/liushui.txt","a") as f:#写入流水记录到文件
                                            shijian=datetime.datetime.now()
                                            liushuihao=str(shijian).replace("-",'')
                                            liushuihao=liushuihao.replace(":",'')
                                            liushuihao=liushuihao.replace(" ",'')
                                            liushuihao=liushuihao.replace(".",'')
                                            f.write("%s--%s--%s--%s--转账\n"%(shijian,kahao,liushuihao,zzje))
                                        enter=input("请按回车继续：")
                                        break
                                break

                    if a=="4":
                        print("输入还款金额")
                        hkje=qian()
                        data.get(kahao)[1]=float(data.get(kahao)[1])+hkje
                        print("你还款了%s元,现在余额有%s元"%(hkje,data.get(kahao)[1]))
                        with open("jilu/liushui.txt","a") as f:#写入流水记录到文件
                            shijian=datetime.datetime.now()
                            liushuihao=str(shijian).replace("-",'')
                            liushuihao=liushuihao.replace(":",'')
                            liushuihao=liushuihao.replace(" ",'')
                            liushuihao=liushuihao.replace(".",'')
                            f.write("%s--%s--%s--%s--还款\n"%(shijian,kahao,liushuihao,hkje))
                        enter=input("请按回车继续：")
                    if a=="5":
                        flag=False
                        break
                    if a=="6":
                        import shangpin
                        #data.get(kahao)[1]=float(data.get(kahao)[1])-shangpin.sp()
        else:
            print("信用卡号或密码错误")
            logging.error('error message,kahao and password error')#记录错误日志
            data[kahao][2]+=1
            if data[kahao][2]>=3:
                break
            continue


    with open('conf/xykinfo.txt', 'w') as f:
        json.dump(data,f)
    return kahao
def zhifu(rmb):#信用卡支付模块
    with open('conf/xykinfo.txt', 'r') as f:
        data = json.load(f)
    print(data)
    num=0
    flag=True
    while num<=3 and flag:
        kahao=input("输入卡号:")
        mima=input("输入密码:")

        #判断是否锁定
        if int(data.get(kahao)[2]):
            if int(data.get(kahao)[2])>=3:
                print("此卡已锁定或冻结,请重新输入")
                logging.error('error message,kahao:%s bei dong jie'%(kahao))#记录错误日志
                continue
        #判断密码是否正确
        if kahao in data.keys() and mima == data.get(kahao)[0]:
            if float (data.get(kahao)[1])>float (rmb):
                data.get(kahao)[1]=float(data.get(kahao)[1])-rmb
                print("卡号%s,已经支付了%s元"%(kahao,rmb))
                if rmb>0:
                    with open("goods.txt","w") as f:
                        f.write("")
                    print("已清空了购物车！")
                    with open('xykinfo.txt', 'w') as f1:
                        json.dump(data,f1)
                    with open("jilu/liushui.txt","a") as f:#写入流水记录到文件
                        shijian=datetime.datetime.now()
                        liushuihao=str(shijian).replace("-",'')
                        liushuihao=liushuihao.replace(":",'')
                        liushuihao=liushuihao.replace(" ",'')
                        liushuihao=liushuihao.replace(".",'')
                        f.write("%s--%s--%s--%s--购物\n"%(shijian,kahao,liushuihao,rmb))
                    break
            else:
                print("余额不足,购买失败")
                logging.error('error message,kahao:%s yue bu zu,gou mai shi bai'%(kahao))#记录错误日志
                break
if __name__=="__main__":
    xingyongka()