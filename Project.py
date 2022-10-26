from tkinter import *
import tkinter as tk
import base64
from turtle import width

class welcomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='gray19')

        welcome = tk.Label(self, text =('welcome'),font=("Bangna New",60),fg='white',bg='gray19').place(x=285, y = 110)
        to_en_de = tk.Label(self,font = ('Bangna New',20), text ='to Encrypting - Decrypting message',fg='white',bg='gray19').place(x=220, y = 210)

        Button = tk.Button(self,font = ('Bangna New',20), text="Let's start!",bg='gray8',fg='black',width=15, command=lambda: controller.show_frame(firstPage))
        Button.place(x=295, y=280)

class firstPage(tk.Frame):
    def __init__(self, parent, controller):
        def Exit():
            self.quit()

        tk.Frame.__init__(self, parent)
        self.configure(bg='gray19')

        Button = tk.Button(self, text="en-code", font=("Bangna New", 40), command=lambda: controller.show_frame(encodePage))
        Button.place(x=190, y=180)

        Button = tk.Button(self, text="de-code", font=("Bangna New", 40), command=lambda: controller.show_frame(decodePage))
        Button.place(x=450, y=180)

        exit = tk.Button(self, font = ('Bangna New',30),text= 'EXIT' , width = 10, command = Exit)
        exit.place(x=310,y=290)

class encodePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='gray19')

        Text = StringVar()
        private_key = StringVar()
        mode = StringVar()
        Result = StringVar()

        def Encode(key,message):
            enc=[]

            for i in range(len(message)):
                key_c = key[i % len(key)]
                enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
            return base64.urlsafe_b64encode("".join(enc).encode()).decode()

        def Mode():
            Result.set(Encode(private_key.get(), Text.get()))
                
        def Exit():
            self.quit()

        def Reset():
            Text.set("")
            private_key.set("")
            mode.set("")
            Result.set("")

        Label(self,font=('Bangena new',20),text='en - code Page',fg='white',bg='gray19').place(x=350,y=60)

        Label(self,font=('Bangena new',20),text='RESULT',fg='white',bg='gray19').place(x=370,y=320)

        Label(self, font= ('Bangena new',25), text='MESSAGE : ',fg='white',bg='gray19').place(x= 180,y=130)
        Entry(self, font = ('Bangena new',20), textvariable = Text,fg='Black', bg = 'CadetBlue1').place(x=330, y = 130,height = 40,width = 330)

        Label(self, font = ('Bangena new',25), text ='KEY : ',fg='white',bg='gray19').place(x=248, y = 190)
        Entry(self, font = ('Bangena new',20), textvariable = private_key ,fg='Black', bg ='CadetBlue1').place(x=330, y = 190,height=40,width = 330)

        Entry(self, font = ('Bangena new',20), textvariable = Result, bg ='CadetBlue1',fg='black').place(x=240, y = 375 , height = 40, width = 330)

        Button(self, font = ('Bangena new',20), text = 'ENCODE'  ,padx =2,bg ='LightGray' ,command = Mode).place(x=260, y = 260)

        Button(self, font = ('Bangena new',20) ,text ='RESET' ,width =6, command = Reset,bg = 'LimeGreen', padx=2).place(x=450, y = 260)

        Button(self, font = ('Bangena new',15),text= 'EXIT' , width = 6, command = Exit,bg = 'OrangeRed', padx=2, pady=2).place(x=640, y = 450)

        Buttona = tk.Button(self, text="HOME", font=('Bangena new',15), padx=2, pady=2, command=lambda: controller.show_frame(firstPage))
        Buttona.place(x=70, y=450)



class decodePage(tk.Frame):
 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='gray19')

        Text = StringVar()
        private_key = StringVar()
        mode = StringVar()
        Result = StringVar()

        def Decode(key,message):
            dec=[]
            message = base64.urlsafe_b64decode(message).decode()

            for i in range(len(message)):
                key_c = key[i % len(key)]
                dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))
            return "".join(dec)

        def Mode():
            Result.set(Decode(private_key.get(), Text.get()))

        def Exit():
            self.quit()

        def Reset():
            Text.set("")
            private_key.set("")
            mode.set("")
            Result.set("")
    
        Label(self,font=('Bangena new',20),text='de - code Page',fg='white',bg='gray19').place(x=350,y=60)

        Label(self,font=('Bangena new',20),text='RESULT',fg='white',bg='gray19').place(x=370,y=320)

        Label(self, font= ('Bangena new',25), text='MESSAGE : ',fg='white',bg='gray19').place(x= 180,y=130)
        Entry(self, font = ('Bangena new',20), textvariable = Text,fg='Black', bg = 'CadetBlue1').place(x=330, y = 130,height = 40,width = 330)

        Label(self, font = ('Bangena new',25), text ='KEY : ',fg='white',bg='gray19').place(x=248, y = 190)
        Entry(self, font = ('Bangena new',20), textvariable = private_key ,fg='Black', bg ='CadetBlue1').place(x=330, y = 190,height=40,width = 330)

        Entry(self, font = ('Bangena new',20), textvariable = Result, bg ='CadetBlue1',fg='black').place(x=240, y = 375 , height = 40, width = 330)

        Button(self, font = ('Bangena new',20), text = 'ENCODE'  ,padx =2,bg ='LightGray' ,command = Mode).place(x=260, y = 260)

        Button(self, font = ('Bangena new',20) ,text ='RESET' ,width =6, command = Reset,bg = 'LimeGreen', padx=2).place(x=450, y = 260)

        Button(self, font = ('Bangena new',15),text= 'EXIT' , width = 6, command = Exit,bg = 'OrangeRed', padx=2, pady=2).place(x=640, y = 450)

        Buttona = tk.Button(self, text="HOME", font=('Bangena new',15), padx=2, pady=2, command=lambda: controller.show_frame(firstPage))
        Buttona.place(x=70, y=450)

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        window = tk.Frame(self)
        window.pack()

        window.grid_rowconfigure(0, minsize=500)
        window.grid_columnconfigure(0, minsize=800)

        self.frames = {}
        for F in (welcomePage, firstPage, encodePage, decodePage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(welcomePage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Application")


app = Application()
app.maxsize(1000, 800)
app.mainloop()
