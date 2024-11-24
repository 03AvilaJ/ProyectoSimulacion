import matplotlib.pyplot as plt


class Menu:

    def show_consumption_by_month(self, months, consumptions):
        plt.ion()  # Activa el modo interactivo
        fig, ax = plt.subplots(figsize=(10, 6))

        # Configuración inicial
        ax.set_title("Consumo de energía mensual", fontsize=16)
        ax.set_xlabel("Meses", fontsize=14)
        ax.set_ylabel("Consumo (kWh)", fontsize=14)
        ax.grid(True, linestyle="--", alpha=0.6)
        ax.set_xticks(range(len(months)))
        ax.set_xticklabels(months, rotation=45, fontsize=12)
        ax.set_xlim(-1, len(months))

        for i in range(len(months)):
            # Graficar solo los datos hasta el mes actual
            ax.clear()
            ax.plot(
                months[: i + 1],
                consumptions[: i + 1],
                marker="o",
                color="b",
                label="Consumo de energía (kWh)",
            )
            ax.set_title("Consumo de energía mensual", fontsize=16)
            ax.set_xlabel("Meses", fontsize=14)
            ax.set_ylabel("Consumo (kWh)", fontsize=14)
            ax.grid(True, linestyle="--", alpha=0.6)
            ax.set_xticks(range(len(months)))
            ax.set_xticklabels(months, rotation=45, fontsize=12)
            ax.set_xlim(-1, len(months))
            ax.legend(fontsize=12)

            # Actualizar la gráfica en tiempo real
            plt.pause(0.5)  # Pausar para dar sensación de tiempo real

        plt.ioff()  # Desactiva el modo interactivo
        plt.show()
