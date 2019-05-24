# -*- encoding:utf_8 -*-
from dbhelper import db


def show_all():
    datas = db.select()
    str = "{0:^8} {1:^4} {2:^40} {3:^28} {4:^23}".format("用户名", "用户类型", "用户密码", "创建时间","邮箱地址")
    print(str)
    for data in datas:
        if data['usertype']=='0':
            usertype = "普通用户"
        else:
            usertype = "管理员"

        if data['regtime']:
            time = data['regtime'].strftime('%x %X')
        else:
            time = "NONE"

        if data['email']:
            email = data['email']
        else:
            email = "NONE"
        # str="{0:^10} {1:^5} {2:^48} {3:^25} {4:^30}".format(data['username'],usertype,data['password'],data['regtime'],data['email'])
        str = "{0:^10} {1:^5} {2:^48} {3:^25} {4:^30}".format(data['username'],usertype,data['password'],time,email)
        print(str)
    a = input("按任意键返回")


