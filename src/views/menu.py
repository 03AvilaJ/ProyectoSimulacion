import matplotlib.pyplot as plt
import tkinter as tk


class Menu:

    # def show_consumption_by_month(
    #     self, months, consumptions, solar_generation, energy_covered, energy_uncovered
    # ):
    #     # Crear la figura con 3 subgráficas (1 fila, 3 columnas)
    #     fig, axes = plt.subplots(3, 1, figsize=(10, 18))  # 3 filas, 1 columna

    #     # Primer gráfico: Consumo de energía mensual
    #     axes[0].plot(
    #         months,
    #         consumptions,
    #         marker="o",
    #         color="b",
    #         label="Consumo de energía (kWh)",
    #     )
    #     axes[0].set_title("Consumo de energía mensual", fontsize=16)
    #     axes[0].set_xlabel("Meses", fontsize=14)
    #     axes[0].set_ylabel("Consumo (kWh)", fontsize=14)
    #     axes[0].grid(True, linestyle="--", alpha=0.6)
    #     axes[0].legend(fontsize=12)

    #     # Segundo gráfico: Generación de energía solar mensual
    #     axes[1].plot(
    #         months,
    #         solar_generation,
    #         marker="o",
    #         color="g",
    #         label="Generación de energía solar (kWh)",
    #     )
    #     axes[1].set_title("Generación de energía solar mensual", fontsize=16)
    #     axes[1].set_xlabel("Meses", fontsize=14)
    #     axes[1].set_ylabel("Generación (kWh)", fontsize=14)
    #     axes[1].grid(True, linestyle="--", alpha=0.6)
    #     axes[1].legend(fontsize=12)

    #     # Tercer gráfico: Cobertura de consumo por panel solar (en kWh)
    #     bar_width = 0.5
    #     axes[2].bar(
    #         months,
    #         energy_uncovered,
    #         color="r",
    #         label="Energía no cubierta (kWh)",
    #         width=bar_width,
    #     )
    #     axes[2].bar(
    #         months,
    #         energy_covered,
    #         bottom=energy_uncovered,
    #         color="g",
    #         label="Energía cubierta (kWh)",
    #         width=bar_width,
    #     )
    #     axes[2].set_title("Cobertura de consumo por panel solar (en kWh)", fontsize=16)
    #     axes[2].set_xlabel("Meses", fontsize=14)
    #     axes[2].set_ylabel("Energía (kWh)", fontsize=14)
    #     axes[2].grid(True, linestyle="--", alpha=0.6)
    #     axes[2].legend(fontsize=12)

    #     # Ajustar el espacio entre las subgráficas
    #     plt.tight_layout()

    #     # Mostrar la ventana con las tres gráficas
    #     plt.show()

    # Funciones para los botones
    def boton1_click():
        print("Grafica abierta: ", consume_grafic)

    def boton2_click():
        print("¡Botón 2 presionado!")

    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Interfaz Sencilla")
    ventana.geometry("300x200")  # Tamaño de la ventana

    # Crear los botones
    boton1 = tk.Button(ventana, text="Botón 1", command=boton1_click)
    boton1.pack(pady=20)  # Añadir el botón 1 con un espacio vertical

    boton2 = tk.Button(ventana, text="Botón 2", command=boton2_click)
    boton2.pack(pady=20)  # Añadir el botón 2 con un espacio vertical

    # Mostrar la ventana
    ventana.mainloop()
