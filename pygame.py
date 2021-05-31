'''___________________________________________________________________________
Wszystkie importy'''

from  tkinter import *
from tkinter import messagebox

'''___________________________________________________________________________
Wszystkie funkcje'''

def przycisk_instrukcja():
    messagebox.showinfo("Instrukcja gry","Gra zamkowe sprzataczki dzieli sie na 3 etapy:\n W pierwszym etapie trzeba ułożyć puzzle w taki sposób aby tworzyły spójną ścieżkę. \n Następnie poruszając się za pomocą strzałek należy przejść postacią po ścieżce\n przez zamek do miejsca docelowego, zanim zapadnie się podłoga.")


'''___________________________________________________________________________
okono gry'''
okno_gry = Tk()
okno_gry.title("Gra zamkowe sprzataczki")
okno_gry.geometry("350x300")


#wczytanie obrazu tła
#plotno.pack()
tlo_zamek=PhotoImage(file="castle.png")
tlo=Label(okno_gry, image=tlo_zamek)
tlo.place(x=0,y=0)
#plotno.create_image(350, 200,image=background_imageTk)

#wczytanie grafiki protagonisty gry
#protag_image=Image.open('protag.png')
#protag_imageTk=PhotoImage(protag_image)
#plotno.create_image(20, 8,image=protag_imageTk)

#wyswietlenie okienka z instrukcje gry

instrukcja = Button(okno_gry, text = "Instrukcja gry", command =  przycisk_instrukcja)
instrukcja.pack(side=LEFT)


okno_gry.mainloop()
