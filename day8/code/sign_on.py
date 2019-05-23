from dbhelper import db
import hashlib
import datetime

def sign_on():
    while True:
        username = input("注册：请输入用户名：")
        if db.where(username=username).select():
            print("输入有误，请重新输入")
            continue
        elif username.strip()=="" and len(username)<=2:
            print("输入有误，请重新输入")
            continue
        else:
            password = input("注册：请输入密码：")
            hash_password = hashlib.sha1(password.encode("utf-8")).hexdigest()
            email = input("注册：请输入邮箱")
            time_now = str(datetime.datetime.now())
            db.insert(username=username,password=hash_password,regtime=time_now,email=email)
            print("注册成功")
            break



