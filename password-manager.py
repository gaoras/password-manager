import tkinter as tk
import random
import string
import pyperclip

VERSION = "0.0.1"

class Main():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('400x200')
        self.root.option_add('*font','Consolas 14')
        self.root.title(f'password-manager VER.{VERSION}')
        self._create_widgets()

    def _create_widgets(self):
        frame = tk.Frame(self.root)
        # lanelの作成
        self.lb_pass = tk.Label(frame, text="Password")
        self.lb_pass.grid(row=0,column=0,padx=5,pady=5)
        # テキストボックスの作成
        self.tb_pass = tk.Entry(frame)
        self.tb_pass.grid(row=0,column=1,padx=5,pady=5)
        # ボタンの作成
        self.bt_exe = tk.Button(frame, text="実行",command=self.bt_exe_clicked)
        self.bt_exe.grid(row=1,column=1,padx=5,pady=5)

        frame.pack()

    def bt_exe_clicked(self):
        symbollst = '!"#$%&()=~|<>'
        randlst = [random.choice(string.ascii_letters + string.digits + symbollst) for i in range(32)]
        ans = ''.join(randlst)
        self.tb_pass.delete(0,tk.END)
        self.tb_pass.insert(tk.END,ans)
        pyperclip.copy(ans)

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    main = Main()
    main.run()
