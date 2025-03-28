import random
import tkinter as tk
from tkinter import messagebox
from diccionario import obtener_palabra_aleatoria

class JuegoAdivinarPalabras:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de Adivinar Palabras")
        self.iniciar_juego()

    def iniciar_juego(self):
        self.palabra = obtener_palabra_aleatoria()
        self.vidas = 6
        self.letras_adivinadas = ["_"] * len(self.palabra)
        self.letras_usadas = set()

        # Configuración de la interfaz
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        self.label_palabra = tk.Label(self.frame, text=" ".join(self.letras_adivinadas), font=("Arial", 16))
        self.label_palabra.pack()

        self.label_vidas = tk.Label(self.frame, text=f"Vidas restantes: {self.vidas}", font=("Arial", 12))
        self.label_vidas.pack()

        self.label_usadas = tk.Label(self.frame, text="Letras usadas: ", font=("Arial", 12))
        self.label_usadas.pack(pady=5)

        self.entry_letra = tk.Entry(self.frame, font=("Arial", 14), width=5, justify="center")
        self.entry_letra.pack(pady=10)

        self.boton_adivinar = tk.Button(self.frame, text="Adivinar", command=self.adivinar_letra, font=("Arial", 12))
        self.boton_adivinar.pack()

        self.canvas = tk.Canvas(self.frame, width=200, height=200, bg="white")
        self.canvas.pack(pady=10)
        self.dibujar_base()

    def dibujar_base(self):
        self.canvas.create_line(50, 180, 150, 180, width=2)  # Base
        self.canvas.create_line(100, 180, 100, 20, width=2)  # Poste
        self.canvas.create_line(100, 20, 150, 20, width=2)   # Brazo superior
        self.canvas.create_line(150, 20, 150, 40, width=2)   # Cuerda

    def dibujar_parte(self):
        partes = [
            lambda: self.canvas.create_oval(140, 40, 160, 60, width=2),  # Cabeza
            lambda: self.canvas.create_line(150, 60, 150, 120, width=2),  # Cuerpo
            lambda: self.canvas.create_line(150, 70, 130, 90, width=2),  # Brazo izquierdo
            lambda: self.canvas.create_line(150, 70, 170, 90, width=2),  # Brazo derecho
            lambda: self.canvas.create_line(150, 120, 130, 150, width=2),  # Pierna izquierda
            lambda: self.canvas.create_line(150, 120, 170, 150, width=2)   # Pierna derecha
        ]
        if 6 - self.vidas < len(partes):
            partes[6 - self.vidas]()  # Dibuja la parte correspondiente

    def adivinar_letra(self):
        letra = self.entry_letra.get().lower()
        self.entry_letra.delete(0, tk.END)

        if len(letra) != 1 or not letra.isalpha():
            messagebox.showerror("Error", "Por favor, introduce una sola letra válida.")
            return

        if letra in self.letras_usadas:
            messagebox.showwarning("Advertencia", "Ya has usado esa letra. Intenta con otra.")
            return

        self.letras_usadas.add(letra)
        self.label_usadas.config(text=f"Letras usadas: {', '.join(sorted(self.letras_usadas))}")

        if letra in self.palabra:
            for i, l in enumerate(self.palabra):
                if l == letra:
                    self.letras_adivinadas[i] = letra
            self.label_palabra.config(text=" ".join(self.letras_adivinadas))
            if "_" not in self.letras_adivinadas:
                messagebox.showinfo("¡Felicidades!", "¡Has adivinado la palabra!")
                self.reiniciar_juego()
        else:
            self.vidas -= 1
            self.label_vidas.config(text=f"Vidas restantes: {self.vidas}")
            self.dibujar_parte()  # Llama a dibujar_parte para agregar la parte correspondiente
            if self.vidas == 0:
                messagebox.showerror("Game Over", f"Te has quedado sin vidas. La palabra era '{self.palabra}'.")
                self.reiniciar_juego()

    def reiniciar_juego(self):
        self.frame.destroy()
        self.iniciar_juego()

if __name__ == "__main__":
    root = tk.Tk()
    app = JuegoAdivinarPalabras(root)
    root.mainloop()
