from tkinter import Tk,Menu,Menubutton,Text,Scrollbar,Frame,Button,filedialog,messagebox,SOLID,END,INSERT
from Analizador import Analizador

analizador=None
rutaArchivo=''

def a():
    pass


def abrirArchivo():
    global rutaArchivo 
    rutaArchivo = filedialog.askopenfilename()
    if not(rutaArchivo==''):
        AbrirArchivo = open(rutaArchivo,'r+') #,encoding='utf8'
        DatosArchivo =  AbrirArchivo.read()
        AbrirArchivo.close()  
        cuadro_archivo.delete('1.0',END)
        cuadro_archivo.insert(INSERT,DatosArchivo)    

def analizarArchivo():
    global rutaArchivo 
    if not(rutaArchivo=='') and not((cuadro_archivo.get('1.0',END+'-1c')=='')):
        AbrirArchivo = open(rutaArchivo,'w+')
        AbrirArchivo.write(cuadro_archivo.get('1.0',END+'-1c'))
        AbrirArchivo.close()

        AbrirArchivo = open(rutaArchivo,'r')
        DatosArchivo = AbrirArchivo.read()
        AbrirArchivo.close()

        global analizador
        analizador = Analizador(rutaArchivo)
        analizador.analizar(DatosArchivo)
    else:
        messagebox.showinfo('Accion no valida','Cargue primero un archivo',detail='No ingreso la ruta del archivo o esta en blanco')


menu = Tk()
menu.title('Proyecto 1 - Lenguajes Formales A+')
menu.geometry("1700x1000")

opciones = Menubutton(menu,text='Opciones Archivo',width=15,height=3,font=('Arial',15),cursor='hand2',bg='#088BD1',relief=SOLID,activebackground='#2CAFF5')
opciones.place(relx=0.01,rely=0.02)
opcion =Menu(opciones,tearoff=0,font=('Arial',13),cursor='hand2',bd=15,bg='#2CAFF5',activebackground='#F78411',activeforeground='#000000')
opcion.add_command(label='Guardar',command=a)
opcion.add_separator()
opcion.add_command(label='Guardar Como',command=a)
opcion.add_separator()
opcion.add_command(label='Errores',command=a)
opcion.add_separator()
opcion.add_command(label='Salir',command=a)
opcion.add_separator()
opciones.config(menu=opcion)

ayuda = Menubutton(menu,text='Ayuda',width=12,height=3,font=('Arial',15),cursor='hand2',bg='#23BC0E',relief=SOLID,activebackground='#50DE3D')
ayuda.place(relx=0.13,rely=0.02)
opcion2 =Menu(ayuda,tearoff=0,font=('Arial',13),cursor='hand2',bd=15,bg='#50DE3D',activebackground='#F78411',activeforeground='#000000')
opcion2.add_command(label='Manual de Usuario',command=a)
opcion2.add_separator()
opcion2.add_command(label='Manual Técnico',command=a)
opcion2.add_separator()
opcion2.add_command(label='Temas de Ayuda',command=a)
opcion2.add_separator()
ayuda.config(menu=opcion2)

frame1 = Frame(menu)
frame1.place(relx=0.01,rely=0.12)
cuadro_archivo = Text(frame1,width=100,height=40,font='Arial')
cuadro_archivo.grid(row=0,column=0)
SC_archivo = Scrollbar(frame1, command=cuadro_archivo.yview)
cuadro_archivo['yscroll'] = SC_archivo.set
SC_archivo.grid(row=0,column=2)

frame2 = Frame(menu)
frame2.place(relx=0.58,rely=0.12)
cuadro_texto = Text(frame2,width=70,height=20,font='Arial')
cuadro_texto.grid(row=0,column=0)
SC_texto = Scrollbar(frame2, command=cuadro_texto.yview)
cuadro_texto['yscroll'] = SC_texto.set
SC_texto.grid(row=0,column=2)


frame3 = Frame(menu)
frame3.place(relx=0.58,rely=0.60)
cuadro_funcion = Text(frame3,width=70,height=20,font='Arial')
cuadro_funcion.grid(row=0,column=0)
SC_funcion = Scrollbar(frame3, command=cuadro_funcion.yview)
cuadro_funcion['yscroll'] = SC_funcion.set
SC_funcion.grid(row=0,column=2)




abrir=Button(menu,text='Abrir',width=15, height=2, font=('Arial',15), cursor='hand2', bg='#088BD1',activebackground='#2CAFF5', relief=SOLID, command=abrirArchivo)
abrir.place(relx=0.15,rely=0.87)
analizar=Button(menu,text='Analizar',width=15, height=2, font=('Arial',15),cursor='hand2',bg='#088BD1',activebackground='#2CAFF5',relief=SOLID, command=analizarArchivo)
analizar.place(relx=0.27,rely=0.87)

menu.resizable(0,0)
menu.mainloop()
