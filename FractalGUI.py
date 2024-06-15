import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser
from TrianguloSierpinsky import TrianguloSierpinsky

class GUISimple:
    def __init__(self):
        self.ventana = tk.Tk()

        self.mar_con = tk.Frame(self.ventana)
        self.mar_con.pack()

        self.cbbox_prof = ttk.Combobox(self.mar_con, values=list(range(11)))
        self.cbbox_prof.set(0)  #defecto
        self.cbbox_prof.pack(side=tk.LEFT)

        self.boton_color = tk.Button(self.mar_con, text='Seleccionar color', command=self.seleccionar_color)
        self.boton_color.pack(side=tk.LEFT)

        self.color_label = tk.Label(self.mar_con, text='Color seleccionado', bg='#FFFFFF')
        self.color_label.pack(side=tk.LEFT)

        self.boton_dibujar = tk.Button(self.mar_con, text='Dibujar', command=self.dibujar_fractal)
        self.boton_dibujar.pack(side=tk.LEFT)

        self.canvas = tk.Canvas(self.ventana, width=800, height=800)
        self.canvas.pack()
        self.color_seleccionado = "#000000"  
    
    def seleccionar_color(self):
        color = colorchooser.askcolor()
        if color[1] is not None:
            self.color_seleccionado = color[1]
            self.color_label.config(bg=self.color_seleccionado)

    def dibujar_fractal(self):
        self.canvas.delete("all")

        prof = int(self.cbbox_prof.get())

        color = self.color_seleccionado

        puntos = [(400, 200), (200, 600), (600, 600)]  
        fractal = TrianguloSierpinsky(puntos, color)

        fractal.dibujar(self.canvas, prof)

    def ejecutar(self):
        self.ventana.mainloop()

def main():
    interfaz = GUISimple()
    interfaz.ejecutar()

if __name__ == "__main__":
    main()