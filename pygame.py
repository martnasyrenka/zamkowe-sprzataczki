#okono gry w gui:
from  tkinter import
okno_gry = Tk()
okno_gry.title("Gra zamkowe sprzataczki")
okno_gry.geometry("350x300")


#wczytanie obrazu tła
plotno.pack()
background_image=Image.open('lava.jpg')
background_imageTk=ImageTk.Photoimage(background_image)
plotno.create_image(350, 200,image=background_imageTk)


okno_gry.mainloop()
