from dbhelper import db
import hashlib

def sign_in():
    while True:
        username = input("登录：请输入用户名：")
        if db.where(username=username).select():
            password = input("登录：请输入密码：")
            hash_password = hashlib.sha1(password.encode("utf-8")).hexdigest()
            print(db.fields("password").where(username=username).select())
            tmp = db.fields("password").where(username=username).select()
            if hash_password == tmp[0]['password']:
                print("登录成功")
                break
            else:
                print("登录失败")
                break
        else:
            print("该账户不存在")
            continue
