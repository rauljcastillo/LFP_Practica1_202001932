import re
from tkinter import filedialog
from tkinter.ttk import Treeview
from turtle import bgcolor, width
from Agregar import Agregar
from Objeto import Objeto
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
__clase=Agregar()

def credHasta1(sem, in3,in4,in5):
    if sem>10 or sem<=0:
        messagebox.showerror(title="Semestre invalido", message="El semestre que ingresó no es valido")
        return 
    (c1,c2,c3)=__clase.sumarCred2(sem)
    in3.delete(0,"end")
    in4.delete(0,"end")
    in5.delete(0,"end")
    in3.insert(0, c1)
    in4.insert(0, c2)
    in5.insert(0, c3)
    c1=""
    c2=""
    c3=""
    sem=""

def credHasta(sem,in1):
    if sem and in1:
        sum4=__clase.credHasta(int(sem))
        if sum4:
            in1.delete(0,"end")
            in1.insert(0,sum4)
        else:
            messagebox.showerror(title="Semestre", message="El semestre no es válido")
    else:
        return 
       
def conteoCreditos():
    conteo=Toplevel()
    conteo.geometry("500x400")
    root.withdraw()
    (c1,c2,c3)=__clase.credito()
    
    btr=Button(conteo,text="Regresar",command= lambda:[root.deiconify(),conteo.destroy()])
    btr.place(x=2,y=2)

    lb1=Label(conteo,text="Calificacion1: ",font=("Times New Roman",14,"bold"))
    lb1.place(relx=0.12,rely=0.09)
    lb2=Label(conteo,text="Créditos cursando: ",font=("Times New Roman",14,"bold"))
    lb2.place(relx=0.12,rely=0.2)
    lb3=Label(conteo,text="Creditos pendientes: ",font=("Times New Roman",14,"bold"))
    lb3.place(relx=0.12,rely=0.31)

    lb4=Label(conteo,text=c1,font=("Times New Roman",16,"bold"))
    lb4.place(relx=0.5,rely=0.09)
    lb5=Label(conteo,text=c2,font=("Times New Roman",16,"bold"))
    lb5.place(relx=0.5,rely=0.20)
    lb6=Label(conteo,text=c3,font=("Times New Roman",16,"bold"))
    lb6.place(relx=0.5,rely=0.31)

    lb7=Label(conteo,text="Créditos hasta semestre N:",font=("Times New Roman",14,"bold"))
    lb7.place(relx=0.12,rely=0.42)
    in1=Entry(conteo,font=("Times New Roman",14,"bold"),justify=CENTER)
    in1.place(relx=0.6,rely=0.42, width=38)

    lb8=Label(conteo, text="Semestre:",font=("Times New Roman",14,"bold"))
    lb8.place(x=130,y=210)
    in2=Entry(conteo,font=("Times New Roman",14,"bold"),justify=CENTER)
    in2.place(x=220,y=214, width=35)
    btn1=Button(conteo,text="Contar", command=lambda:credHasta(in2.get(),in1))
    btn1.place(x=270,y=209,width=70)

    lb9=Label(conteo,text="Créditos del semestre:",font=("Times New Roman",14,"bold"))
    lb9.place(x=20,y=260)
    in3=Entry(conteo,font=("Times New Roman",14,"bold"),justify=CENTER)
    in3.place(x=220,y=260,width=35)

    lb10=Label(conteo,text="Créditos asignados:",font=("Times New Roman",14,"bold"))
    lb10.place(x=275,y=260)
    in4=Entry(conteo,font=("Times New Roman",14,"bold"),justify=CENTER)
    in4.place(x=450,y=260,width=35)

    lb11=Label(conteo,text="Créditos pendientes:",font=("Times New Roman",14,"bold"))
    lb11.place(x=110,y=310)
    in5=Entry(conteo,font=("Times New Roman",14,"bold"),justify=CENTER)
    in5.place(x=290,y=310,width=35)    

    lb12=Label(conteo, text="Semestre:",font=("Times New Roman",14,"bold"))
    lb12.place(x=130,y=360)
    in6=Entry(conteo,font=("Times New Roman",14,"bold"),justify=CENTER)
    in6.place(x=220,y=360, width=35)
    btn2=Button(conteo,text="Contar", command= lambda:credHasta1(int(in6.get()), in3,in4,in5))
    btn2.place(x=270,y=360,width=70)

def listarCurso(gestionar):
    listar=Toplevel()
    listar.geometry("1200x500")
    btn=Button(listar,text="Regresar",command=lambda:[gestionar.deiconify(),listar.destroy()])

    #Tabla de referecias
    tabla1=Treeview(listar,show="headings" ,columns=("c1","c2"),height=3)
    tabla1.place(x=3,y=120)
    tabla1.heading("c1", text="Estado")
    tabla1.heading("c2",text="Representacion")
    tabla1.column("c1", width=90,anchor=CENTER)
    tabla1.column("c2",width=135,anchor=CENTER)
    tabla1.insert("",END,values=("Aprobado","0"))
    tabla1.insert("",END,values=("Cursando","1"))
    tabla1.insert("",END,values=("Pendiente","-1"))

    #Tabla de referencias 2
    tabla2=Treeview(listar,show="headings" ,columns=("c1","c2"),height=2)
    tabla2.place(x=3,y=280)
    tabla2.heading("c1", text="Obligatorio")
    tabla2.heading("c2",text="Representacion")
    tabla2.column("c1", width=95,anchor=CENTER)
    tabla2.column("c2",width=130,anchor=CENTER)
    tabla2.insert("",END,values=("Obligatorio","1"))
    tabla2.insert("",END,values=("Opcional","0"))

    #Tabla de datos 
    btn.place(x=5, y=5)
    tabla=Treeview(listar,show="headings",columns=("col1","col2","col3","col4","col5","col6","col7"),height=20)
    tabla.place(x=242,y=20, relwidth=0.8)
    tabla.heading("col1",text="Código",anchor=CENTER)
    tabla.heading("col2",text="Nombre",anchor=CENTER)
    tabla.heading("col3",text="Pre Requisito",anchor=CENTER)
    tabla.heading("col4",text="Obligatorio",anchor=CENTER)
    tabla.heading("col5",text="Semestre",anchor=CENTER)
    tabla.heading("col6",text="Créditos",anchor=CENTER)
    tabla.heading("col7",text="Estado",anchor=CENTER)

    tabla.column("col1", anchor=CENTER, width=15)
    tabla.column("col2", anchor=CENTER, width=210)
    tabla.column("col3", anchor=CENTER,width=120)
    tabla.column("col4", anchor=CENTER,width=15)
    tabla.column("col5", anchor=CENTER,width=15)
    tabla.column("col6", anchor=CENTER,width=15)
    tabla.column("col7",anchor=CENTER,width=15)


    style=ttk.Style()
    style.theme_use('clam')
    style.configure(
    'Treeview',
    foreground="black",
    background="old lace",
    font=("Arial ",12,"bold"),
    rowheight=30)

    style.configure(
    'Treeview.Heading',
    font=("Arial",12,"bold"),
    rowheight=30,
    background="gray78")    


    arreglo=__clase.getArreglo()

    #Este for recorre todo la lista de objeto y los añade a la tabla 
    for element in arreglo:
        pre=" , ".join(element.getpre()) #Uno el arreglo del pre requisito
        tabla.insert("",END,values=(element.getcodigo(),element.getnombre(),pre,element.getobli(),element.getsemestre(),element.getcredito(),element.getestado()))

def elimina(codigo,in1):
    objeto=__clase.buscar(codigo)
    if objeto:
        dec=messagebox.askyesno("Eliminar", "¿Estás seguro que deseas eliminar?")
        if dec:     
            __clase.eliminar(codigo)
            messagebox.showinfo(title="Curso eliminado", message="Curso eliminado con éxito")
            in1.delete(0,"end")
    else:
        messagebox.showerror(title="Error",message="No existe el curso")

def eliminarCurso(gestionar):
    eliminar=Toplevel(gestionar)
    #eliminar.geometry("300x180")
    eliminar.maxsize(300,180)
    eliminar.minsize(300,180)
    lbl1=Label(eliminar,text="Codigo de curso",font="Arial 16")
    lbl1.place(x=10,y=15)


    in1=Entry(eliminar)
    in1.place(x=200,y=15, height=30,relwidth=0.15)
    in2=Button(eliminar,text="Eliminar", command=lambda: elimina(in1.get(),in1))
    in2.place(x=60,y=65, height=30,relwidth=0.3)
    in3=Button(eliminar,text="Regresar",command=lambda:[gestionar.deiconify(),eliminar.destroy()])
    in3.place(x=160,y=65, height=30,relwidth=0.3)

def Buscar1(codigo,in1,in2):
    objeto=__clase.buscar(codigo)
    if objeto:
        in2.insert(0,objeto.getnombre())
        messagebox.showinfo(title="Exito",message="Si existe el curso")
    else:
        messagebox.showerror(title="Error",message="El curso no existe")
        in1.delete(0,"end")

def editarCurso(gestionar):
    editar=Toplevel(gestionar)
    editar.geometry("500x420")
    lbl1=Label(editar,text="Codigo",font="Arial 16")
    lbl1.place(x=15,y=15)

    buscar=Button(editar, text="Buscar",command=lambda:[Buscar1(in1.get(),in1,in2)])
    buscar.place(x=400,y=15)
    lbl2=Label(editar,text="Nombre",font="Arial 16")
    lbl2.place(x=15,y=65)
    lbl3=Label(editar,text="Pre requisito",font="Arial 16")
    lbl3.place(x=15,y=115)
    lbl4=Label(editar,text="Obligatorio", font="Arial 16")
    lbl4.place(x=15,y=165)
    lbl5=Label(editar,text="Semestre",font="Arial 16")
    lbl5.place(x=15,y=215)
    lbl6=Label(editar,text="Creditos",font="Arial 16")
    lbl6.place(x=15,y=265)
    lbl7=Label(editar,text="Estado",font="Arial 16")
    lbl7.place(x=15,y=315)

    in1=Entry(editar)
    in1.place(x=145,y=15, height=30,relwidth=0.5)
    in2=Entry(editar)
    in2.place(x=145,y=65, height=30,relwidth=0.5)
    in3=Entry(editar)
    in3.place(x=145,y=115, height=30,relwidth=0.5)
    in4=Entry(editar)
    in4.place(x=145,y=165, height=30,relwidth=0.5)
    in5=Entry(editar)
    in5.place(x=145,y=215, height=30,relwidth=0.5)
    in6=Entry(editar)
    in6.place(x=145,y=265, height=30,relwidth=0.5)
    in7=Entry(editar)
    in7.place(x=145,y=315, height=30,relwidth=0.5)

    aceptar=Button(editar,text="Editar",command=lambda:agregarNuevo(in1.get(),in2.get(),in3.get(),in4.get(),int(in5.get()),in6.get(),in7.get()))
    aceptar.place(x=125,y=360,width=120 )
    regresar=Button(editar,text="Regresar",command=lambda:[gestionar.deiconify(),editar.destroy()])
    regresar.place(x=255, y=360,width=120)

def Busqueda(codigo,in2):
    objeto=__clase.buscar(codigo)
    if objeto:
        in2.insert(0,objeto.getnombre())
        messagebox.showwarning(title="Ya existe",message="El curso ya existe")
        
def agregarNuevo(codigo,nombre,pre,obliga,semest,creditos,estado):
    if semest<=10 and semest>0:
        __clase.agregar(Objeto(codigo,nombre,pre,obliga,semest,creditos,estado))
        messagebox.showinfo(title="Agregado",message="Curso agregado con éxito")
    else:
        messagebox.showerror(title="Semestre invalido", message="El semestre que ingresó no es válido")

def agregarCurso(gestionar):
    agregar=Toplevel()
    agregar.geometry("500x420")
    lbl1=Label(agregar,text="Codigo",font="Arial 16")
    lbl1.place(x=15,y=15)

    buscar=Button(agregar, text="Buscar",command=lambda:Busqueda(in1.get(),in2))
    buscar.place(x=400,y=15)
    lbl2=Label(agregar,text="Nombre",font="Arial 16")
    lbl2.place(x=15,y=65)
    lbl3=Label(agregar,text="Pre requisito",font="Arial 16")
    lbl3.place(x=15,y=115)
    lbl4=Label(agregar,text="Obligatorio",font="Arial 16")
    lbl4.place(x=15,y=165)
    lbl5=Label(agregar,text="Semestre",font="Arial 16")
    lbl5.place(x=15,y=215)
    lbl6=Label(agregar,text="Creditos",font="Arial 16")
    lbl6.place(x=15,y=265)
    lbl7=Label(agregar,text="Estado",font="Arial 16")
    lbl7.place(x=15,y=315)

    in1=Entry(agregar)
    in1.place(x=145,y=15, height=30,relwidth=0.5)
    in2=Entry(agregar)
    in2.place(x=145,y=65, height=30,relwidth=0.5)
    in3=Entry(agregar)
    in3.place(x=145,y=115, height=30,relwidth=0.5)
    in4=Entry(agregar)
    in4.place(x=145,y=165, height=30,relwidth=0.5)
    in5=Entry(agregar)
    in5.place(x=145,y=215, height=30,relwidth=0.5)
    in6=Entry(agregar)
    in6.place(x=145,y=265, height=30,relwidth=0.5)
    in7=Entry(agregar)
    in7.place(x=145,y=315,height=30,relwidth=0.5)

    aceptar=Button(agregar,text="Aceptar",command=lambda:agregarNuevo(in1.get(),in2.get(),in3.get().split(","),in4.get(),int(in5.get()),int(in6.get()),in7.get()))
    aceptar.place(x=125,y=360,width=120 )
    regresar=Button(agregar,text="Regresar",command=lambda:[gestionar.deiconify(),agregar.destroy()])
    regresar.place(x=255, y=360,width=120)

def gestionar():
    gestionar=Toplevel(root)
    gestionar.geometry("300x350")
    root.withdraw()
    btn=Button(gestionar, text="Listar cursos",font="Arial 12",command=lambda:[gestionar.withdraw(),listarCurso(gestionar)])
    btn.place(relx=0.5, rely=0.1 , anchor=CENTER, width=150,height=50)
    btn1=Button(gestionar,text="Agregar curso",font="Arial 12",command= lambda:[gestionar.withdraw() , agregarCurso(gestionar)])
    btn1.place(relx=0.5, rely=0.3 , anchor=CENTER, width=150,height=50)
    btn2=Button(gestionar,text="Editar curso",font="Arial 12",command=lambda:[gestionar.withdraw(), editarCurso(gestionar)])
    btn2.place(relx=0.5, rely=0.5 , anchor=CENTER, width=150,height=50)
    btn3=Button(gestionar,text="Eliminar curso",font="Arial 12" ,command= lambda:[gestionar.withdraw(),eliminarCurso(gestionar)])
    btn3.place(relx=0.5, rely=0.7 , anchor=CENTER, width=150,height=50)
    btn4=Button(gestionar,text="Regresar",font="Arial 12",command=lambda:[root.deiconify(),gestionar.destroy()])
    btn4.place(relx=0.5, rely=0.9 , anchor=CENTER, width=150,height=50)

def leerarchivo(valor):
    try:
        quest=re.findall(".lfp$",valor)
        if quest:
            file=open(valor,"r",encoding="utf-8")
            arreglo=file.readlines()

            for elem in arreglo:
                array=elem.split(",")
                codigo=array[0]
                nombre=array[1]
                pre=array[2]
                oblig=array[3]
                semes=array[4]
                credi=array[5]
                estad=array[6]
                __clase.agregar(Objeto(codigo,nombre,pre.split(";"),oblig,semes,int(credi),estad))
            messagebox.showinfo(title="Satisfactorio",message="El archivo se cargo correctamente")
            del arreglo[:]
        else:
            messagebox.showerror(title="Error de formato", message="Solo se aceptan archivos con extension .lfp")
            return 
        
    except:
        messagebox.showerror(title="Error en el archivo",message="Ocurrio un error al leer el archivo")

def openfile():
    file=filedialog.askopenfile()
    if file:
        leerarchivo(file.name)
    

def cargarArchivo():
    ventana2=Toplevel(root)
    root.withdraw()
    ventana2.geometry("500x300")
    ventana2.title("Cargar Archivo")

    btnRegre=Button(ventana2,text="Regresar",command=lambda:[root.deiconify(), ventana2.destroy()])
    btnRegre.place(x=5,y=5)
    bt=Button(ventana2,text="Abrir archivo",command=openfile)
    bt.place(width=200,height=50,x=160,y=20)
    input=Entry(ventana2, justify=CENTER, font=("Times New Roman",16))
    input.place(relx=0.5,rely=0.35, relwidth=0.8,height=40,anchor=CENTER)
    btn= Button(ventana2,text="Aceptar",command=lambda: [leerarchivo(input.get()),input.delete(0,"end")])
    btn.place(relx=0.5,rely=0.55, anchor=CENTER, relwidth=0.8,height=40)


root=Tk()
root.geometry("300x300")
root.title("Pantalla inicial")
btn=Button(root, text="Cargar archivo",font="Arial 12", command=cargarArchivo)
btn.place(relx=0.5, rely=0.1 , anchor=CENTER, width=150,height=50)
btn1=Button(root,text="Gestionar cursos",font="Arial 12",command=gestionar)
btn1.place(relx=0.5, rely=0.3 , anchor=CENTER, width=150,height=50)
btn2=Button(root,text="Conteo de creditos",font="Arial 12", command=conteoCreditos)
btn2.place(relx=0.5, rely=0.5 , anchor=CENTER, width=150,height=50)
btn3=Button(root,text="Salir",font="Arial 12", command=root.destroy)
btn3.place(relx=0.5, rely=0.7 , anchor=CENTER, width=150,height=50)
root.mainloop()






