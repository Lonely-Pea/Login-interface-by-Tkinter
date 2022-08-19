# 导入tkinter相关模块
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
from time import sleep


# 常量
TITLE = "Tkinter登录界面"
WIDTH, HEIGHT = 240, 180
UserInfo_list = [0, 0]  # 用户信息列表


class Window(tk.Tk):  # 主窗口
    def __init__(self, title, width, height):
        super(Window, self).__init__()

        self.title(title)  # 设置窗口标题

        # 设置窗口的大小和位置(geometry)
        self.width, self.height = width, height
        self.screenwidth, self.screenheight = self.winfo_screenwidth(), self.winfo_screenheight()
        self.size = "%dx%d+%d+%d" % (self.width, self.height, (self.screenwidth - self.width) / 2, (self.screenheight - self.height) / 2)
        self.geometry(self.size)

        self.resizable(False, False)  # 设置窗口大小不可更改


class Main(tk.Frame):  # 窗口的主要内容
    def __init__(self, master):
        super(Main, self).__init__(master)
        self.master = master

        self.login_desktop = None  # 登录框架
        self.register_desktop = None  # 注册框架

        self.pack(fill=tk.BOTH, expand=True)  # 放置对象

        # 变量
        self.login_var = tk.StringVar()
        self.password_var = tk.StringVar()

        self.desktop()

    def desktop(self):  # 桌面内容
        # print(self.get_user_info())
        if self.get_user_info():  # 已经记录了登录文件
            self.Login()  # 进入登录界面

        else:  # 没有记录登录文件
            self.register_()  # 进入注册界面

    def get_user_info(self) -> bool:  # 获取用户信息
        global UserInfo_list
        f1 = open("UserLogin.txt", "r")
        f2 = open("UserPassword.txt", "r")
        if f1.read() == "" or f2.read() == "":  # 没有记录登陆信息
            f1.close()
            f2.close()
            return False
        else:  # 记录了登录信息
            # f1.seek(0)  # 将游标至于开头
            # f2.seek(0)
            UserInfo_list[0] = f1.read()
            UserInfo_list[1] = f2.read()
            print(UserInfo_list)
            f1.close()
            f2.close()
            return True

    def Login(self):  # 登录界面
        # 新建一个Frame框架以承接登录界面的所有内容
        self.login_desktop = tk.Frame(self)
        self.login_desktop.place(x=0, y=0, width=WIDTH, height=HEIGHT)

        # 界面主要内容
        tk.Label(self.login_desktop, text="登录", font=("微软雅黑", 20)).pack()

        tk.Label(self.login_desktop, text="账号：").place(x=0, y=50, width=70, height=25)
        ttk.Entry(self.login_desktop, textvariable=self.login_var).place(x=70, y=50, width=100, height=25)
        ttk.Button(self.login_desktop, text="X", cursor="hand2", command=lambda: self.login_var.set("")).place(x=175, y=50, width=30, height=25)

        tk.Label(self.login_desktop, text="密码：").place(x=0, y=80, width=70, height=25)
        ttk.Entry(self.login_desktop, textvariable=self.password_var).place(x=70, y=80, width=100, height=25)
        ttk.Button(self.login_desktop, text="X", cursor="hand2", command=lambda: self.login_var.set("")).place(x=175, y=80, width=30, height=25)

        ttk.Button(self.login_desktop, text="登录", cursor="hand2", command=self.login_in).place(x=5, y=110, width=(WIDTH - 20) / 3, height=25)
        ttk.Button(self.login_desktop, text="注册", cursor="hand2", command=lambda: self.register_in(True)).place(x=(WIDTH - 20) / 3 + 10, y=110, width=(WIDTH - 20) / 3, height=25)
        ttk.Button(self.login_desktop, text="退出", cursor="hand2", command=lambda: self.master.destroy()).place(x=(WIDTH - 20) / 3 * 2 + 15, y=110, width=(WIDTH - 20) / 3, height=25)

    def login_in(self):  # 登录
        if self.login_var.get() == UserInfo_list[0] and self.password_var.get() == UserInfo_list[1]:  # 登录信息无误
            msg.showinfo("提示", "登陆成功！将在3秒后关闭！")
            for i in range(6):
                self.master.update()
                sleep(0.5)
            self.master.destroy()
        else:
            self.move_window()
            msg.showerror("错误", "账号或密码错误！")

    def register_in(self, InLogin=False):  # 注册：
        if self.login_var.get() != "" and self.password_var.get() != "":
            if InLogin:  # 在登录环境下注册
                answer = msg.askyesno("提示", "确定注册？注册将销毁之前注册过的账号！")
                if answer:  # 确定注册
                    f1 = open("UserLogin.txt", "w")
                    f2 = open("UserPassword.txt", "w")
                    f1.write(self.login_var.get())
                    f2.write(self.password_var.get())
                    f1.close()
                    f2.close()
                else:
                    msg.showinfo("提示", "用户已取消注册！")
            else:
                f1 = open("UserLogin.txt", "w")
                f2 = open("UserPassword.txt", "w")
                f1.write(self.login_var.get())
                f2.write(self.password_var.get())
                f1.close()
                f2.close()
                msg.showinfo("提示", "注册成功！将在三秒后关闭！")
                for i in range(6):
                    self.master.update()
                    sleep(0.5)
                self.master.destroy()
        else:
            self.move_window()
            msg.showerror("错误", "账号或密码不能为空！")

    def register_(self):
        # 新建一个Frame框架以承接注册界面的所有内容
        self.register_desktop = tk.Frame(self)
        self.register_desktop.place(x=0, y=0, width=WIDTH, height=HEIGHT)

        # 界面主要内容
        tk.Label(self.register_desktop, text="注册", font=("微软雅黑", 20)).pack()

        tk.Label(self.register_desktop, text="账号：").place(x=0, y=50, width=70, height=25)
        ttk.Entry(self.register_desktop, textvariable=self.login_var).place(x=70, y=50, width=100, height=25)
        ttk.Button(self.register_desktop, text="X", cursor="hand2", command=lambda: self.login_var.set("")).place(x=175,
                                                                                                               y=50,
                                                                                                               width=30,
                                                                                                               height=25)

        tk.Label(self.register_desktop, text="密码：").place(x=0, y=80, width=70, height=25)
        ttk.Entry(self.register_desktop, textvariable=self.password_var).place(x=70, y=80, width=100, height=25)
        ttk.Button(self.register_desktop, text="X", cursor="hand2", command=lambda: self.login_var.set("")).place(x=175,
                                                                                                               y=80,
                                                                                                               width=30,
                                                                                                               height=25)

        ttk.Button(self.register_desktop, text="注册", cursor="hand2", command=lambda: self.register_in(False)).place(x=5, y=110, width=(WIDTH - 15) / 2, height=25)
        ttk.Button(self.register_desktop, text="退出", cursor="hand2", command=lambda: self.master.destroy()).place(x=(WIDTH - 15) / 2 + 10, y=110, width=(WIDTH - 15) / 2, height=25)

    def move_window(self):  # 震动窗口
        x = self.master.winfo_x()  # 获取窗口横坐标
        y = self.master.winfo_y()
        for i in range(2):
            for i2 in range(4):
                if i2 // 2 == 0:
                    move_value = 50
                else:
                    move_value = 0
                self.master.geometry(f"+{x + move_value}+{y}")
                self.master.update()
                sleep(0.02)


if __name__ == "__main__":
    win = Window(title=TITLE, width=WIDTH, height=HEIGHT)  # 生成对象win
    main = Main(master=win)

    win.mainloop()  # 显示窗口
