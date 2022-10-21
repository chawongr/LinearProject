from tkinter import *
import base64

root = Tk()
root.geometry('720x500')
root.resizable(0,0)
root.title("Encrypting-Decrypting message")
Label(root, text ='Encrypting-Decrypting message', font = 'arial 20 bold').pack()
Label(root, text ='KMITL', font = 'arial 20 bold',bg = 'Orange').pack(side =BOTTOM)
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

def CheckInput(input):
    if len(input.get()) > 9:
        input.set(input.get()[:-1])

def Decode(key,message):
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()

    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))
    return "".join(dec)

def Mode():
    if(mode.get() == 'e'):
        Result.set(Encode(private_key.get(), Text.get()))
    elif(mode.get() == 'd'):
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set('Invalid Mode')
        
def Exit():
    root.destroy()

def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")
    
Label(root, font= 'arial 12 bold', text='MESSAGE').place(x= 80,y=80)
Entry(root, font = 'arial 10', textvariable = Text, bg = 'ghost white' ).place(x=360, y = 80)

Label(root, font = 'arial 12 bold', text ='KEY').place(x=80, y = 110)
Entry(root, font = 'arial 10', textvariable = private_key , bg ='ghost white').place(x=360, y = 110)

Label(root, font = 'arial 12 bold', text ='MODE(e-encode, d-decode)').place(x=80, y = 140)
Entry(root, font = 'arial 10', textvariable = mode , bg= 'ghost white').place(x=360, y = 140)
Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='ghost white').place(x=360, y = 170)

Button(root, font = 'arial 10 bold', text = 'RESULT'  ,padx =2,bg ='LightGray' ,command = Mode).place(x=80, y = 170)

Button(root, font = 'arial 10 bold' ,text ='RESET' ,width =6, command = Reset,bg = 'LimeGreen', padx=2).place(x=110, y = 210)

Button(root, font = 'arial 10 bold',text= 'EXIT' , width = 6, command = Exit,bg = 'OrangeRed', padx=2, pady=2).place(x=200, y = 210)

private_key.trace("w" ,lambda *args: CheckInput(private_key))
root.mainloop()
