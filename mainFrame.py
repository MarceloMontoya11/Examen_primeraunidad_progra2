
# -*- coding: utf-8 -*-



from tkinter import Frame,Label,StringVar,IntVar,Checkbutton,PhotoImage,Button,Entry,DoubleVar

import serial
import time
import mysql.connector

import threading

class MainFrame(Frame):
    
    def __init__(self,master=None):
        super().__init__(master,width=1000,height=1000)
        self.master=master
        self.master.protocol('WM_DELETE_WINDOW',self.askQuit)
        self.pack()
        self.hilo1=threading.Thread(target=self.getSensorValues,daemon=True)
        self.hilo2=threading.Thread(target=self.Enviar_db,daemon=True)
        self.arduino=serial.Serial("COM7",9600,timeout=1.0)
        time.sleep(1)
        self.cnn=mysql.connector.connect(host="localhost",user="root",passwd="m7475",database="proyecto")
        print(self.cnn)
        self.value_temp =StringVar()
        self.value_lum =StringVar()
        self.value_temp_1 =IntVar()
        self.value_lum_1 =IntVar()
        
        self.value_foco=IntVar()
        self.value_cale=IntVar()
        self.min_temp=StringVar()
        self.min_lum=StringVar()
        self.ayuda=IntVar()
        self.muestras=StringVar()
        self.create_widgets()
    
     
        self.isRun=True
        self.isRun_1=True
        self.hilo1.start()
        self.hilo2.start()
        
        
    def askQuit(self):
        self.isRun=False
        self.isRun_1=False
        self.arduino.write('cale:0'.encode('ascii'))
        time.sleep(1.1)
        self.arduino.write('foco:0'.encode('ascii'))
        
        self.arduino.close()
        self.hilo1.join(0.1)
        self.hilo2.join(0.1)
        self.master.quit()
        self.master.destroy()
        print("****Finalizando.....")
    
   
    def Enviar_db(self):
        
         while self.isRun_1:
            cur=self.cnn.cursor()
            sql="INSERT INTO datos (temperatura,luminosidad)VALUES('{}','{}')".format(self.value_temp_1,self.value_lum_1)
            cur.execute(sql)
            self.cnn.commit()
            time.sleep(1)
            cur.close()
        
            
    
    
    def getSensorValues(self):
        while self.isRun:
            cad=self.arduino.readline().decode('ascii').strip()
            if cad:
                pos=cad.index(":")
                label=cad[:pos]
                value=cad[pos+1:]
                if label =='temp':
                    self.value_temp.set(value +" °C")
                    self.value_temp_1=float(value)
                if label =='lum':
                    self.value_lum.set(value +" lux")
                    self.value_lum_1=float(value)
                
    
    def calefaccion(self):
        cad='cale:' + str(self.value_cale.get()) 
        self.arduino.write(cad.encode('ascii'))
    
    def foco(self):
        cad='foco:' + str(self.value_foco.get()) 
        self.arduino.write(cad.encode('ascii'))
    
    def control_calefaccion(self):
        if self.value_temp_1<int(self.min_temp.get()):
            cad='c_1:' + str(0)+"/n" 
            
        
        else :
            
            cad='c_1:' + str(1)+"/n"
            
        self.arduino.write(cad.encode('ascii'))
        
    def control_foco(self):
        
        if self.value_lum_1<int(self.min_lum.get()):
            cad='c_2:' + str(0)+"/n" 
            
        
        else :
            
            cad='c_2:' + str(1)+"/n"
            
        self.arduino.write(cad.encode('ascii'))
        
    def create_widgets(self):
        Label(self,text="Temperatura:",font=("Verdana,20")).place(x=50,y=20)
        Label(self,width=6,textvariable=self.value_temp,font=("Verdana,20")).place(x=150,y=20)
        
        Label(self,text="Luminosidad:",font=("Verdana,20")).place(x=50,y=50)
        Label(self,width=6,textvariable=self.value_lum,font=("Verdana,20")).place(x=150,y=50)
        
        Checkbutton(self,text="Encender/Apagar Calefacción",variable=self.value_cale,onvalue=0,offvalue=1,command=self.calefaccion).place(x=700,y=0)
        Checkbutton(self,text="Encender/Apagar Foco",variable=self.value_foco,onvalue=0,offvalue=1,command=self.foco).place(x=470,y=0)
        self.imagen_1=PhotoImage(file="foco-0.png")
        Label(self,image=self.imagen_1).place(x=400,y=20)
        self.imagen_2=PhotoImage(file="Ventilador-0 .png")
        Label(self,image=self.imagen_2).place(x=700,y=70)
        
        Label(self,text="Temperatura mínima deseada",font=("Verdana,20")).place(x=132,y=120)
        Entry(self,textvariable=self.min_temp,width=35).place(x=132,y=140)
        
       
        self.btn_tmin=Button(self,text="ENVIAR TEMPERATURA ", width=30 ,command=self.control_calefaccion,bg='#FEEECF')
        self.btn_tmin.place(x=132,y=160)
        
        
        Label(self,text="Luminosidad mínima deseada",font=("Verdana,20")).place(x=132,y=180)
        Entry(self,textvariable=self.min_lum,width=35).place(x=132,y=200)
        
        self.btn_lmin=Button(self,text="ENVIAR LUMINOSIDAD ", width=30,command=self.control_foco,bg='#FEEECF')
        self.btn_lmin.place(x=132,y=220)
       
       