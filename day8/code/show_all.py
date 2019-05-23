from dbhelper import db


def show_all():
    datas = db.select()
    for data in datas:
        if data['usertype']=='0':
            usertype = "普通用户"
        else:
            usertype = "管理员"
        str='''
        %s %s %s %s %s
        '''%(data['username'],usertype,data['password'],data['regtime'],data['email'])
        print(str)


show_all()