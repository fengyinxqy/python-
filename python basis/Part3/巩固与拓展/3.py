dict = {"username": "xiaoqiyan", "password": 123456}
username = input("请输入用户名:")
password = int(input("请输入密码:"))
if username == dict["username"]:
    if password == dict["password"]:
        print("用户名，密码正确!")
