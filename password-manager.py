import tkinter as tk
import random
import string
from tkinter.constants import BOTH, EW, GROOVE, LEFT, NS, NSEW, RIGHT, TOP, W
import pyperclip

VERSION = "0.0.1"

class Main():
    def __init__(self):
        self.root = tk.Tk()
        #self.root.geometry('1000x500')
        self.root.option_add('*font','Consolas 14')
        self.root.title(f'password-manager VER.{VERSION}')
        self._create_widgets()

    def _create_widgets(self):
        frame = tk.Frame(self.root, bd=4, relief=GROOVE)
        # frameListの作成
        frameList = tk.Frame(frame, bd=2, relief=GROOVE)
        # labelの作成
        self.lb_list = tk.Label(frameList,text="パスワード一覧")
        self.lb_list.grid(row=0, column=0)
        self.sb_passList = tk.Scrollbar(frameList)
        self.sb_passList.grid(row=1, column=1, sticky=NS)
        self.lst_pass = tk.Listbox(frameList, yscrollcommand=self.sb_passList.set)
        self.lst_pass.grid(row=1, column=0, sticky=NS)

        # framePassの作成
        framePass = tk.Frame(frame, bd=2, relief=GROOVE)
        # lanelの作成
        self.lb_pass = tk.Label(framePass, text="Password")
        self.lb_pass.grid(row=0,column=0,padx=5,pady=5)
        # テキストボックスの作成
        self.tb_pass = tk.Entry(framePass)
        self.tb_pass.grid(row=0,column=1,padx=5,pady=5)
        # クリップボードへのコピーボタン
        self.bt_copy = tk.Button(framePass, text="コピー",command=self.bt_copy_clicked)
        self.bt_copy.grid(row=0,column=2,padx=5,pady=5)
        # ボタンの作成
        self.bt_exe = tk.Button(framePass, text="実行",command=self.bt_exe_clicked)
        self.bt_exe.grid(row=1,column=1,padx=5,pady=5)

        frameList.grid(row=0, column=0, sticky=NS)
        framePass.grid(row=0, column=1, sticky=NSEW)
        frame.pack(expand=0,fill=BOTH)

    def bt_copy_clicked(self):
        pyperclip.copy(self.tb_pass.get())

    def bt_exe_clicked(self):
        symbollst = '!"#$%&()=~|<>'
        randlst = [random.choice(string.ascii_letters + string.digits + symbollst) for i in range(32)]
        ans = ''.join(randlst)
        self.tb_pass.delete(0,tk.END)
        self.tb_pass.insert(tk.END,ans)

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    main = Main()
    main.run()
