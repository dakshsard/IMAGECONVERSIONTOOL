import os
import wget
import tkinter as tk
from PIL import Image
from tkinter import filedialog
from tkinter import messagebox
import time

root=tk.Tk()
root.title("Daksh's Tool")
canvas1=tk.Canvas(root,width=300,height=375,bg='lightsteelblue2', relief = 'raised')
canvas1.pack()
label1 = tk.Label(root, text='File Conversion Tool', bg = 'lightsteelblue2')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)


cnt=0
imagelist=[]


def getbyFile():
    global im1,imagelist,cnt
    import_file_path=filedialog.askopenfilename()
    try:
        image1=Image.open(import_file_path)
        if cnt==0:
            im1 = image1.convert('RGB')
        else:
            imagelist.append(image1.convert('RGB'))
        cnt+=1
    except:
        messagebox.showinfo('Warning','Atleast select something')

browseButton = tk.Button(text="     Select Image     ", command=getbyFile, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=browseButton)


res=-1
rem=[]
def byurl():
    global res
    root1=tk.Tk()
    root1.title("Enter url of image")
    cn=tk.Canvas(root1,width=350,height=300, bg= 'lightsteelblue2', relief = 'raised')
    cn.pack()
    lab=tk.Label(root1,text='Enter URL to insert image in PDF',bg='lightsteelblue2')
    lab.config(font=('helvetica',10))
    cn.create_window(110,60,window=lab)
    s=tk.Entry(root1)
    cn.create_window(280,60,window=s)
    def down():
        global res,cnt,im1,rem
        url=str(s.get())
        if url=='':
            mp=messagebox.showinfo('Warning','URL cannot be empty',icon='warning')
            if mp=='ok':
                root1.destroy()
        else:
            try:
                res=wget.download(url)
            except:
                res=-1
            if res!=-1:
                ms1=messagebox.showinfo('Success','Image added successfully')
                if ms1=='ok':
                    root1.destroy()
                import_file_path=str(os.getcwd())
                import_file_path+=str('\\')
                import_file_path+=str(res)
                image1=Image.open(import_file_path)
                rem.append(import_file_path)
                if cnt==0:
                    im1=image1.convert('RGB')
                else:
                    imagelist.append(image1.convert('RGB'))
                cnt+=1
            else:
                ms=messagebox.showinfo('Error','Incorrect url',icon='error')
                if ms=='ok':
                    root1.destroy()
    sub=tk.Button(root1,text='Submit',command=down)
    cn.create_window(130,110,window=sub)
    def close():
        root1.destroy()
    cl=tk.Button(root1,text='Close',command=close)
    cn.create_window(250,110,window=cl)
    
    
urlbut=tk.Button(text="     Add from url     ",command=byurl,bg='green',fg='white',font=('helvetica', 12, 'bold'))
canvas1.create_window(150,180,window=urlbut)

def convertToPdf():
    global im1,cnt,imagelist,rem
    if cnt!=0:
        export_file_path=filedialog.asksaveasfilename(defaultextension='.pdf')
        im1.save(export_file_path,save_all=True,append_images=imagelist)
        messagebox.showinfo('Success','Images converted to PDF')
        imagelist=[]
        cnt=0
        try:
            for i in (rem):
                if os.path.exists(i):
                    os.remove(i)
        except:
            bv=0
    else:
        messagebox.showinfo('Warning','No images selected')


saveAsButton = tk.Button(text='Convert to PDF', command=convertToPdf, bg='gold', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 230, window=saveAsButton)


def exitApplication():
    global rem
    MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application ?',icon = 'warning')
    if MsgBox == 'yes':
        root.destroy()

exitButton = tk.Button (root, text='Exit Application',command=exitApplication, bg='brown', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 280, window=exitButton)

root.mainloop()
