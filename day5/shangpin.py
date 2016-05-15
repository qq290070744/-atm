#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys,prettytable,json,logging,datetime

#定义日志级别、格式、输出位配置
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %Y-%m-%d %H:%M:%S',
                    filename='log/test.log',
                    filemode='a',
                    )

dic= {
    "手机通讯":{
        "苹果6S":{
            "16G":["price",5000],
            "32G":["price",6000],
            "64G":["price",7000]
            },
        "小米":{
            "16G":["price",1000],
            "32G":["price",2000],
            "64G":["price",3000]
        }
    },
    "图书音像":{
        "<<Python指南>>":{
             "1本":["price",5000],
            "2本":["price",6000],
            "3本":["price",7000]
        },
        "<<我的Python成长之路>>":{
             "1本":["price",5000],
            "2本":["price",6000],
            "3本":["price",7000]
        }
    }
}
new_dic={}
new_dic2={}
new_dic3={}
def sp():
    user=''
    rmb=0
    while True:
        x = prettytable.PrettyTable(["编号","名称"])
        for k,v in enumerate(dic):
            new_dic[k]=v
            x.add_row(['%s'%k,v])
        x.add_row(["3","查看购物车"])
        x.add_row(["4","购物结算"])
        x.add_row(["5","登录系统"])
        x.add_row(["6","exit"])


        print(x)
        shuru=int(input("请输入编号:"))


        if shuru in   new_dic.keys():
            print("你选择了[%s]"%new_dic[shuru])
            #print(dic[new_dic[shuru]])
            x = prettytable.PrettyTable(["编号","名称"])
            for k,v in enumerate(dic[new_dic[shuru]]):
                new_dic2[k]=v
                x.add_row(['%s'%k,v])
            print(x)

            shuru1=int(input("请输入编号:"))
            if shuru1 in   new_dic2.keys():
                print("你选择了[%s]"%new_dic2[shuru1])
                #print(dic[new_dic[shuru]][new_dic2[shuru1]])
                x = prettytable.PrettyTable(["编号","品名"])
                for k,v in enumerate (dic[new_dic[shuru]][new_dic2[shuru1]]):
                    new_dic3[k]=v
                    x.add_row(['%s'%k,v])

                print(x)

            shuru2=int(input("请输入编号:"))
            if shuru2 in new_dic3.keys():
                print("你选择了[%s]"%new_dic3[shuru2])
                #print(dic[new_dic[shuru]][new_dic2[shuru1]][new_dic3[shuru2]])
                print("需要[%s]元"%dic[new_dic[shuru]][new_dic2[shuru1]][new_dic3[shuru2]][1])
                gwcdict={}

                import denglu
                if not user:
                    print(",请登录：")
                    user=denglu.login()
                gwcdict[user]=['%s%s'%(new_dic[shuru],new_dic2[shuru1]),dic[new_dic[shuru]][new_dic2[shuru1]][new_dic3[shuru2]][1]]
                with open('conf/goods.txt', 'a',encoding="utf-8") as f:
                        json.dump(gwcdict,f)
                        f.write("\n")
                print("%s:%s:%s元，已经加入购物车！"%(new_dic2[shuru1],new_dic3[shuru2],dic[new_dic[shuru]][new_dic2[shuru1]][new_dic3[shuru2]][1]))
                shijian=datetime.datetime.now()
                with open("jilu/jilu.txt","a") as f:
                    f.write("%s--%s--%s:%s--%s\n"%(shijian,user,new_dic2[shuru1],new_dic3[shuru2],dic[new_dic[shuru]][new_dic2[shuru1]][new_dic3[shuru2]][1]))
                fh=input("请按回车继续：")

                #return dic[new_dic[shuru]][new_dic2[shuru1]][new_dic3[shuru2]][1]

        elif shuru==3:
            if user:

                with open("conf/goods.txt","r",encoding="utf-8") as f:
                    charmb=0
                    x = prettytable.PrettyTable(["\033[32m商品名\033[0m","\033[33m价格\033[0m"])
                    for i in f:
                        i=i.strip()
                        if len(i)>1:
                            #print("i=%s"%i)
                            #print(type(i))
                            chakan=json.loads(i)
                            x.add_row([chakan.get(user)[0],chakan.get(user)[1]])
                            #print(chakan.get(user))
                            charmb=charmb+float (chakan.get(user)[1])
                print(x)
                print("所购买的商品的总价钱%s"%charmb)
                fh=input("请按回车返回：")
            else:
                import denglu
                user=denglu.login()

                pass
        elif shuru==4:
            if user:
                with open("conf/goods.txt","r",encoding="utf-8") as f:
                    for i in f:
                        i=i.strip()
                        if len(i)>1:
                            #print("i=%s"%i)
                            #print(type(i))
                            chakan=json.loads(i)
                            #print(chakan.get(user))
                            rmb=rmb+float (chakan.get(user)[1])
                import xyk
                xyk.zhifu(rmb)#调用信用卡支付模块扣款


                fh=input("请按回车返回：")
                continue

            else:
                import denglu
                user=denglu.login()
                panduan=input("是否继续y/n:")
                if panduan=='y':
                    continue
                else:
                    break

        elif shuru==5:
            import denglu
            user=denglu.login()
        elif shuru==6:
            #flag=False
            break
        else:
            logging.error('error message, enter de bianhao bu cun zai!')#记录错误日志
if __name__=="__main__":
    sp()