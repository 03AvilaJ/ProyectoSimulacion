import tkinter as tk
from gui import SimulacionRedInteligente  # Importar directamente la clase

if __name__ == "__main__":
    root = tk.Tk()
    app = SimulacionRedInteligente(root)  # Crear una instancia de la clase
    root.mainloop()
