from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image
import math
import re

#Importar módulos propios
from ConstanteDeEquilibrio import calculoK, criterio
from DensidadRelativaGas import rog, miSum

global elemsList, zList

componentes = ["Metano" , "Etano" , "Propano" , "Isobutano" , "n-Butano" , "Isopentano" , "n-Pentano" , "n-Hexano" , "n-Heptano" , "n-Octano" , "n-Nonano" , "n-Decano" , "CO2" , "H2S" , "H2" , "O2" , "N2" , "HCl"]
zList = []

class Menu():

    def __init__(self):
        
        self.root = Tk()
        self.root.config(bg = "AntiqueWhite1")
        self.root.title("Método de constante K")
        listas = []

        frm = Frame(self.root)
        scroll = Scrollbar(self.root , orient = VERTICAL)

        listbox = Listbox(self.root, yscrollcommand = scroll.set, selectmode = MULTIPLE) #,selectmode = 'multiple',exportselection=0, cursor = 'man', selectforeground = 'red')
        scroll.config(command = listbox.yview)
        #scroll.pack(side = RIGHT, fill = Y) 
        scroll.grid(column = 1, row = 0)
        #listbox.pack()
        listbox.grid(column = 0, row = 0)

        global rex

        rex = Label(self.root, text = '')
        rex.config(bg = "NavajoWhite2")
        rex.grid(column = 0, row = 3)


        self.T = StringVar()
        self.P = StringVar()
        self.C1 = StringVar()
        self.C2 = StringVar()
        self.C3 = StringVar()
        self.C4 = StringVar()
        self.nC4 = StringVar()
        self.C5 = StringVar()
        self.nC5 = StringVar()
        self.C6 = StringVar()
        self.C7 = StringVar()
        self.C8 = StringVar()
        self.C9 = StringVar()
        self.C10 = StringVar()
        self.CO2 = StringVar()
        self.H2S = StringVar()
        self.SO2 = StringVar()
        self.H2 = StringVar()
        self.O2 = StringVar()
        self.N2 = StringVar()
        self.HCl = StringVar()
        self.kf = StringVar()
        self.Tf = StringVar()

        def IngresarDatos():

            if self.C1 != '':
                self.c1Val = float(self.C1.get())
                zList.append(self.c1Val)

                
            else:

                #self.C1 == '':
                self.c1Val = 0


            if self.C2 != '':

                self.c2Val = float(self.C2.get())
                zList.append(self.c2Val)
                

            else:
                self.c2Val = 0

                

            self.c3Val = float(self.C3.get())
            zList.append(self.c3Val)
            self.c4Val = float(self.C4.get())
            zList.append(self.c4Val)
            self.nc4Val = float(self.nC4.get())
            zList.append(self.nc4Val)
            self.c5Val = float(self.C5.get())
            zList.append(self.c5Val)
            self.nc5Val = float(self.nC5.get())
            zList.append(self.nc5Val)
            self.c6Val = float(self.C6.get())
            zList.append(self.c6Val)
            self.c7Val = float(self.C7.get())
            zList.append(self.c7Val)
            self.c8Val = float(self.C8.get())
            zList.append(self.c8Val)
            self.c9Val = float(self.C9.get())
            zList.append(self.c9Val)
            self.c10Val = float(self.C10.get())
            zList.append(self.c10Val)
            self.co2Val = float(self.CO2.get())
            zList.append(self.co2Val)
            self.h2sVal = float(self.H2S.get())
            zList.append(self.h2sVal)
            self.so2Val = float(self.SO2.get())
            zList.append(self.so2Val)
            self.h2Val = float(self.H2.get())
            zList.append(self.h2Val)
            self.o2Val = float(self.O2.get())
            zList.append(self.o2Val)
            self.n2Val = float(self.N2.get())
            zList.append(self.n2Val)
            self.hclVal = float(self.HCl.get())
            zList.append(self.hclVal)

            rog(zList)

        TLabel = Label(self.root, text = "Temperatura [°C]: ")
        TLabel.config(bg = "AntiqueWhite1")
        TLabel.grid(column = 3, row = 0)

        TEntry = Entry(self.root)
        TEntry.config(textvariable = self.T)
        TEntry.grid(column = 4, row = 0, padx = 5)

        PLabel = Label(self.root, text = "Presión [MPa]: ")
        PLabel.config(bg = "AntiqueWhite1")
        PLabel.grid(column = 3, row = 1, padx = 5)

        PEntry = Entry(self.root)
        PEntry.config(textvariable = self.P)
        PEntry.grid(column = 4, row = 1)

        compsLabel = Label(self.root, text = "Componente")
        compsLabel.config(bg = "AntiqueWhite1")
        compsLabel.grid(column = 5, row = 0)

        zLabel = Label(self.root, text = "Z")
        zLabel.config(bg = "AntiqueWhite1")
        zLabel.grid(column = 6, row = 0)

        metanoLabel = Label(self.root, text = "Metano")
        metanoLabel.config(bg = "AntiqueWhite1")
        metanoLabel.grid(column = 5, row = 1)

        metanoZEntry = Entry(self.root)
        metanoZEntry.config(textvariable = self.C1)
        metanoZEntry.grid(column = 6, row = 1)

        etanoLabel = Label(self.root, text = "Etano")
        etanoLabel.config(bg = "AntiqueWhite1")
        etanoLabel.grid(column = 5, row = 2)

        etanoZEntry = Entry(self.root)
        etanoZEntry.config(textvariable = self.C2)
        etanoZEntry.grid(column = 6, row = 2)

        propanoLabel = Label(self.root, text = "Propano")
        propanoLabel.config(bg = "AntiqueWhite1")
        propanoLabel.grid(column = 5, row = 3)

        propanoZEntry = Entry(self.root)
        propanoZEntry.config(textvariable = self.C3)
        propanoZEntry.grid(column = 6, row = 3)


        isobutanoLabel = Label(self.root, text = "Isobutano")
        isobutanoLabel.config(bg = "AntiqueWhite1")
        isobutanoLabel.grid(column = 5, row = 4)

        isobutanoZEntry = Entry(self.root)
        isobutanoZEntry.config(textvariable = self.C4)
        isobutanoZEntry.grid(column = 6, row = 4)

        nbutanoLabel = Label(self.root, text = "n-Butano")
        nbutanoLabel.config(bg = "AntiqueWhite1")
        nbutanoLabel.grid(column = 5, row = 5)

        nbutanoZEntry = Entry(self.root)
        nbutanoZEntry.config(textvariable = self.nC4)
        nbutanoZEntry.grid(column = 6, row = 5)

        isopentanoLabel = Label(self.root, text = "Isopentano")
        isopentanoLabel.config(bg = "AntiqueWhite1")
        isopentanoLabel.grid(column = 5, row = 6)

        isopentanoZEntry = Entry(self.root)
        isopentanoZEntry.config(textvariable = self.C5)
        isopentanoZEntry.grid(column = 6, row = 6)

        npentanoLabel = Label(self.root, text = "n-Pentano")
        npentanoLabel.config(bg = "AntiqueWhite1")
        npentanoLabel.grid(column = 5, row = 7)

        npentanoZEntry = Entry(self.root)
        npentanoZEntry.config(textvariable = self.nC5)
        npentanoZEntry.grid(column = 6, row = 7)

        nhexanoLabel = Label(self.root, text = "n-Hexano")
        nhexanoLabel.config(bg = "AntiqueWhite1")
        nhexanoLabel.grid(column = 5, row = 8)

        nhexanoZEntry = Entry(self.root)
        nhexanoZEntry.config(textvariable = self.C6)
        nhexanoZEntry.grid(column = 6, row = 8)

        nheptanoLabel = Label(self.root, text = "n-Heptano")
        nheptanoLabel.config(bg = "AntiqueWhite1")
        nheptanoLabel.grid(column = 5, row = 9)

        nheptanoZEntry = Entry(self.root)
        nheptanoZEntry.config(textvariable = self.C7)
        nheptanoZEntry.grid(column = 6, row = 9)

        noctanoLabel = Label(self.root, text = "n-Octano")
        noctanoLabel.config(bg = "AntiqueWhite1")
        noctanoLabel.grid(column = 5, row = 10)

        noctanoZEntry = Entry(self.root)
        noctanoZEntry.config(textvariable = self.C8)
        noctanoZEntry.grid(column = 6, row = 10)

        nnonanoLabel = Label(self.root, text = "n-Nonano")
        nnonanoLabel.config(bg = "AntiqueWhite1")
        nnonanoLabel.grid(column = 5, row = 11)

        nnonanoZEntry = Entry(self.root)
        nnonanoZEntry.config(textvariable = self.C9)
        nnonanoZEntry.grid(column = 6, row = 11)

        ndecanoLabel = Label(self.root, text = "n-Decano")
        ndecanoLabel.config(bg = "AntiqueWhite1")
        ndecanoLabel.grid(column = 5, row = 12)

        ndecanoZEntry = Entry(self.root)
        ndecanoZEntry.config(textvariable = self.C10)
        ndecanoZEntry.grid(column = 6, row = 12)

        co2Label = Label(self.root, text = "CO2")
        co2Label.config(bg = "AntiqueWhite1")
        co2Label.grid(column = 5, row = 13)

        co2ZEntry = Entry(self.root)
        co2ZEntry.config(textvariable = self.CO2)
        co2ZEntry.grid(column = 6, row = 13)

        h2sLabel = Label(self.root, text = "H2S")
        h2sLabel.config(bg = "AntiqueWhite1")
        h2sLabel.grid(column = 5, row = 14)

        h2sZEntry = Entry(self.root)
        h2sZEntry.config(textvariable = self.H2S)
        h2sZEntry.grid(column = 6, row = 14)

        so2Label = Label(self.root, text = "SO2")
        so2Label.config(bg = "AntiqueWhite1")
        so2Label.grid(column = 5, row = 15)

        so2ZEntry = Entry(self.root)
        so2ZEntry.config(textvariable = self.SO2)
        so2ZEntry.grid(column = 6, row = 15)

        h2Label = Label(self.root, text = "H2")
        h2Label.config(bg = "AntiqueWhite1")
        h2Label.grid(column = 5, row = 16)

        h2ZEntry = Entry(self.root)
        h2ZEntry.config(textvariable = self.H2)
        h2ZEntry.grid(column = 6, row = 16)

        o2Label = Label(self.root, text = "O2")
        o2Label.config(bg = "AntiqueWhite1")
        o2Label.grid(column = 5, row = 17)

        o2ZEntry = Entry(self.root)
        o2ZEntry.config(textvariable = self.O2)
        o2ZEntry.grid(column = 6, row = 17)

        n2Label = Label(self.root, text = "N2")
        n2Label.config(bg = "AntiqueWhite1")
        n2Label.grid(column = 5, row = 18)

        n2ZEntry = Entry(self.root)
        n2ZEntry.config(textvariable = self.N2)
        n2ZEntry.grid(column = 6, row = 18)

        hclLabel = Label(self.root, text = "HCl")
        hclLabel.config(bg = "AntiqueWhite1")
        hclLabel.grid(column = 5, row = 19)

        hclZEntry = Entry(self.root)
        hclZEntry.config(textvariable = self.HCl)
        hclZEntry.grid(column = 6, row = 19)

        kflagLabel = Label(self.root, text = "K")
        kflagLabel.grid(column = 0, row = 4)

        kLabel = Label(self.root, textvariable = self.kf)
        kLabel.grid(column = 1, row = 4)
        kLabel.config(bg = "firebrick1")

        TflagLabel = Label(self.root, text = "T[°F]")
        TflagLabel.grid(column = 0, row = 5)
        
        TfLabel = Label(self.root, textvariable = self.Tf)
        TfLabel.grid(column = 1, row = 5)
        TfLabel.config(bg = "firebrick1")
        
        sendButton = Button(self.root, text = "ɣg", command = IngresarDatos)
        sendButton.grid(column = 6, row = 20)

        for i in range(len(componentes)):
            listbox.insert(END , componentes[i])

        def selecn():
            resul = ''
            #print(listbox.curselection())
            global elemsList, pVal, tVal
            elemsList = list(listbox.curselection())
            print(elemsList)
            for g in listbox.curselection():
                resul = resul + str(listbox.get(g)) + '\n'
                #print(listbox.get(g))
            #print(type(resul))
            rex.config(text=resul)
            print(resul)
            miSum(elemsList)

            pVal = float(self.P.get())
            tVal = float(self.T.get())
            tVal = (tVal * 1.8) + 32
            pVal = (pVal/0.006895)

            if re.search("Metano", resul):

                calculoK(1,pVal,tVal,zList)

                #print(6+10)

            if re.search("Etano", resul):
                calculoK(2,pVal,tVal,zList)

            if re.search("Propano", resul):
                calculoK(3,pVal,tVal,zList)
            #print(listas[0])

        def Kfun():

            c = criterio(pVal, tVal, zList, elemsList)
            print("c: ",c)
            print(c[1])
            self.kf.set(c[0])
            self.Tf.set(c[1])

        #calculaRog = Button(self.root, text = "Calcular densidad", command = calculoRog)
        #calculaRog.grid(column = 0, row = 3) 
        #10:37

        botn = Button(self.root, text = "Seleccionar", command = selecn)
        botn.grid(column = 0, row = 2)

        kButton = Button(self.root, text = "K", command = Kfun)
        kButton.grid(column = 1, row = 2)

        def graphF():
            self.g = Toplevel()
            self.g.title("GPSA Graph")

            self.graph = PhotoImage(file = "GPSA.png")
            self.graph1 = Label(self.g , image = self.graph)

            self.graph1.grid(column = 0, row = 0)
            #graph1.config(bg = "AntiqueWhite1") 
        
        gButton = Button(self.root, text = "Gráfica", command = graphF)
        gButton.grid(column = 2, row = 2)


        self.root.mainloop()

        
def main():

    GPSA = Menu()

if __name__ == '__main__':
    main()