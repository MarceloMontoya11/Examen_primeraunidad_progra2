# -*- coding: utf-8 -*-



from mainFrame import MainFrame
from tkinter import Tk,Button,Label,PhotoImage,Frame,Toplevel

def main():
    caratula=Tk()
    caratula.title("Monitoreo de temperatura y luminosidad")
    caratula.iconbitmap("UNT.ico")
    caratula.geometry('1010x498')
    caratula.config(bg='#36B0FF')
    
    imagen_0=PhotoImage(file="mecatronica.png")
    Label(caratula,image=imagen_0).place(x=0,y=0)
    
    frame_1=Frame(caratula,width=420,height=340,bg='white',borderwidth=4,relief="groove")
    frame_1.place(x=545,y=100)
    
    Comenzar=Button(frame_1,text='Comenzar',font=("Verdana,12"),bg='#36B0FF',command=control)
    Comenzar.place(x=280,y=250)
    
    Salir=Button(frame_1,text='Salir',font=("Verdana,12"),bg='red',command=caratula.destroy)
    Salir.place(x=20,y=250)
    
    Titulo=Label(caratula,text="SISTEMA DE MONITOREO Y CONTROL ",font=("Verdana",18),bg='#49A')
    Titulo.place(x=515,y=5)
    
    Titulo=Label(caratula,text=" DE TEMPERATURA Y LUMINOSIDAD",font=("Verdana",18),bg='#49A')
    Titulo.place(x=520,y=50)
    
    Label(frame_1,text='Curso:Programación II ',font=("Verdana,12")).place(x=20,y=20)
    Label(frame_1,text='Docente: Ing.E.Maximo Asto Rodriguez  ',font=("Verdana,12")).place(x=20,y=50) 
    Label(frame_1,text='Alumno:Marcelo Montoya Herrera ',font=("Verdana,12")).place(x=20,y=80)
    Label(frame_1,text='Carrera:Ingeniería Mecatrónica  ',font=("Verdana,12")).place(x=20,y=110)
    Label(frame_1,text='Ciclo: IV ',font=("Verdana,12")).place(x=20,y=140)
    Label(frame_1,text='Grupo:A',font=("Verdana,12"),).place(x=20,y=170)
    Label(frame_1,text='Matrícula:1513600919',font=("Verdana,12")).place(x=20,y=200)
    
    caratula.mainloop()
    
    
def control():
    root=Toplevel()
    root.wm_title("Monitoreo de temperatura y luminosidad")
    root.iconbitmap("UNT.ico")
    app=MainFrame(root)
    app.mainloop()
    
    
if __name__=="__main__":
    main()
    