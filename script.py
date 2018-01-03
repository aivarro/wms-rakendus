import webbrowser
from tkinter import *
from tkinter import messagebox

master = Tk()
Label(master, text="vasak alumine x").grid(row=0)
Label(master, text="vasak alumine y").grid(row=1)
Label(master, text="ülemine parem x").grid(row=2)
Label(master, text="ülemine parem y").grid(row=3)
Label(master, text="laius").grid(row=4)
Label(master, text="kõrgus").grid(row=5)

llx = Entry(master)
lly = Entry(master)
urx = Entry(master)
ury = Entry(master)
width = Entry(master)
height = Entry(master)

llx.grid(row=0, column=1, padx=1, pady=1)
lly.grid(row=1, column=1, padx=1, pady=1)
urx.grid(row=2, column=1, padx=1, pady=1)
ury.grid(row=3, column=1, padx=1, pady=1)
width.grid(row=4, column=1, padx=1, pady=1)
height.grid(row=5, column=1, padx=1, pady=1)

# näidisväärtused llx=525000 lly=6530000 urx=526000 ury=6531000 width=1000 height=1000
def main():
   if (len(llx.get())*len(lly.get())*len(urx.get())*len(ury.get())*len(width.get())*len(height.get())) < 1:
       messagebox.showinfo( "Veateade", "Ükski sisend ei tohi olla tühi!")
   elif int(llx.get())>int(urx.get()):
       messagebox.showinfo( "Veateade", "Vasak alumine x peab olema väiksem kui ülemine parem x")
   elif int(lly.get())>int(ury.get()):
       messagebox.showinfo( "Veateade", "Vasak alumine y peab olema väiksem kui ülemine parem y")
   elif ((int(llx.get())*int(lly.get())*int(urx.get())*int(ury.get())*int(width.get())*int(height.get())) > 1):
       webbrowser.open('http://kaart.maaamet.ee/wms/alus?SERVICE=WMS&VERSION=1.1.1&REQUEST=GetMap&LAYERS=of10000&SRS=EPSG%3A3301&BBOX='
       +llx.get()+','
       +lly.get()+','
       +urx.get()+','
       +ury.get()
       +'&width='+width.get()
       +'&height='+height.get()
       +'&FORMAT=image%2Fpng')
   else:
        messagebox.showinfo( "Veateade", "Valed sisendid!")

Button(master, text='Ava link', command=main).grid(row=6, column=0, sticky=W, padx=4, pady=4)
mainloop()
