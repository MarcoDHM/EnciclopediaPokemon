import tkinter as tk
from tkinter import messagebox
import random

class JuegoAhorcado:
    def __init__(self, master):
        self.master = master
        self.master.title("Juego del Ahorcado")

        # Configurar la pantalla completa
        self.pantalla_completa = False
        self.master.attributes("-fullscreen", False)

        # Color de fondo
        self.master.configure(bg="#2c3e50")

        self.palabra_secreta = self.obtener_palabra()
        self.letras_adivinadas = []

        self.intentos_maximos = 6
        self.intentos = 0

        self.label_palabra = tk.Label(master, text=self.mostrar_tablero(), font=("Helvetica", 16), bg="#2c3e50", fg="#ecf0f1")
        self.label_palabra.pack(pady=10)

        self.label_intentos = tk.Label(master, text=f"Intentos restantes: {self.intentos_maximos}", font=("Helvetica", 12), bg="#2c3e50", fg="#ecf0f1")
        self.label_intentos.pack(pady=5)

        self.canvas_ahorcado = tk.Canvas(master, width=150, height=150, bg="#2c3e50")
        self.canvas_ahorcado.pack()

        self.partes_ahorcado = [
            self.canvas_ahorcado.create_line(20, 140, 130, 140, width=2),  # Base horizontal
            self.canvas_ahorcado.create_line(75, 140, 75, 20, width=2),    # Poste vertical
            self.canvas_ahorcado.create_line(75, 20, 110, 20, width=2),    # Viga horizontal
            self.canvas_ahorcado.create_oval(100, 20, 120, 40, width=2),   # Cabeza
            self.canvas_ahorcado.create_line(110, 40, 110, 80, width=2),   # Cuerpo
            self.canvas_ahorcado.create_line(110, 50, 90, 60, width=2),    # Brazo izquierdo
            self.canvas_ahorcado.create_line(110, 50, 130, 60, width=2),   # Brazo derecho
            self.canvas_ahorcado.create_line(110, 80, 90, 100, width=2),   # Pierna izquierda
            self.canvas_ahorcado.create_line(110, 80, 130, 100, width=2)   # Pierna derecha
        ]

        self.entry_letra = tk.Entry(master, font=("Helvetica", 12))
        self.entry_letra.pack(pady=10)

        self.boton_adivinar_letra = tk.Button(master, text="Adivinar letra", command=self.adivinar_letra, bg="#3498db", fg="#ecf0f1", padx=10)
        self.boton_adivinar_letra.pack(side=tk.LEFT, padx=5)

        self.boton_adivinar_palabra = tk.Button(master, text="Adivinar palabra", command=self.adivinar_palabra, bg="#e74c3c", fg="#ecf0f1", padx=10)
        self.boton_adivinar_palabra.pack(side=tk.RIGHT, padx=5)

        self.boton_pista = tk.Button(master, text="Pista", command=self.dar_pista, bg="#2ecc71", fg="#ecf0f1", padx=10)
        self.boton_pista.pack()

        self.boton_pantalla_completa = tk.Button(master, text="Pantalla Completa", command=self.toggle_pantalla_completa, bg="#f39c12", fg="#ecf0f1", padx=10)
        self.boton_pantalla_completa.pack()

    def toggle_pantalla_completa(self):
        self.pantalla_completa = not self.pantalla_completa
        self.master.attributes("-fullscreen", self.pantalla_completa)

    def obtener_palabra(self):
        palabras = {
            "python": "Un lenguaje de programación interpretado de alto nivel.",
            "programacion": "El acto de escribir, probar, perfeccionar y mantener el código fuente de los programas informáticos.",
            "juego": "Una actividad que uno realiza para la diversión o el entretenimiento.",
            "ahorcado": "Un juego en el que se trata de adivinar una palabra antes de que se complete el dibujo de un ahorcado.",
            "desarrollo": "El proceso de concebir, especificar, diseñar, programar, documentar, probar y corregir errores de un software.",
            "ventana": "Una interfaz gráfica que permite la interacción entre el usuario y un programa.",
            "datos": "Información que se procesa y almacena en una computadora.",
            "tecnologia": "Conjunto de conocimientos y técnicas que permiten el aprovechamiento de los recursos naturales para satisfacer las necesidades humanas.",
            "inteligencia": "Capacidad mental que poseen los seres vivos para aprender, adaptarse y resolver problemas."
        }
        palabra = random.choice(list(palabras.keys())).lower()
        self.pista = palabras[palabra]
        return palabra

    def mostrar_tablero(self):
        resultado = ""
        for letra in self.palabra_secreta:
            if letra in self.letras_adivinadas:
                resultado += letra + " "
            else:
                resultado += "_ "
        return resultado.strip()

    def adivinar_letra(self):
        letra = self.entry_letra.get().lower()

        if letra.isalpha() and len(letra) == 1:
            if letra in self.letras_adivinadas:
                messagebox.showinfo("Aviso", "Ya has adivinado esa letra. Intenta con otra.")
            elif letra in self.palabra_secreta:
                self.letras_adivinadas.append(letra)
            else:
                self.intentos += 1
                self.label_intentos.config(text=f"Intentos restantes: {self.intentos_maximos - self.intentos}")
                self.mostrar_parte_ahorcado()

            self.label_palabra.config(text=self.mostrar_tablero())

            if set(self.letras_adivinadas) == set(self.palabra_secreta):
                messagebox.showinfo("Felicidades", "¡Has adivinado la palabra!")
                self.master.destroy()

            if self.intentos == self.intentos_maximos:
                messagebox.showinfo("Fin del juego", f"Te has quedado sin intentos. La palabra era '{self.palabra_secreta}'.")
                self.master.destroy()
        else:
            messagebox.showwarning("Error", "Ingresa una letra válida.")

    def adivinar_palabra(self):
        palabra_propuesta = self.entry_letra.get().lower()
        if palabra_propuesta == self.palabra_secreta:
            messagebox.showinfo("Felicidades", "¡Has adivinado la palabra!")
            self.master.destroy()
        else:
            self.intentos += 1
            self.label_intentos.config(text=f"Intentos restantes: {self.intentos_maximos - self.intentos}")
            self.mostrar_parte_ahorcado()

            if self.intentos == self.intentos_maximos:
                messagebox.showinfo("Fin del juego", f"Te has quedado sin intentos. La palabra era '{self.palabra_secreta}'.")
                self.master.destroy()

    def mostrar_parte_ahorcado(self):
        parte_actual = self.partes_ahorcado[self.intentos - 1]
        self.canvas_ahorcado.itemconfig(parte_actual, fill="#e74c3c")  # Cambiar el color de la parte dibujada

    def dar_pista(self):
        messagebox.showinfo("Pista", f"{self.pista}")

def main():
    root = tk.Tk()
    root.geometry("400x400")
    root.resizable(False, False)
    root.configure(bg="#2c3e50")  # Color de fondo general
    juego = JuegoAhorcado(root)
    root.mainloop()

if __name__ == "__main__":
    main()
