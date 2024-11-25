import matplotlib.pyplot as plt


class Menu:

    def show_consumption_by_month(self, months, consumptions):
        plt.ion()
        fig, ax = plt.subplots(figsize=(10, 6))

        ax.set_title("Consumo de energía mensual", fontsize=16)
        ax.set_xlabel("Meses", fontsize=14)
        ax.set_ylabel("Consumo (kWh)", fontsize=14)
        ax.grid(True, linestyle="--", alpha=0.6)
        ax.set_xticks(range(len(months)))
        ax.set_xticklabels(months, rotation=45, fontsize=12)
        ax.set_xlim(-1, len(months))

        for i in range(len(months)):
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

            plt.pause(0.5)

        plt.ioff()
        plt.show()

    def show_consumption_by_month_whit_panel(
        self, months, consumptions, consumptions_whit_panel
    ):
        plt.ion()
        fig, ax = plt.subplots(figsize=(10, 6))

        ax.set_title("Consumo de energía mensual", fontsize=16)
        ax.set_xlabel("Meses", fontsize=14)
        ax.set_ylabel("Consumo (kWh)", fontsize=14)
        ax.grid(True, linestyle="--", alpha=0.6)
        ax.set_xticks(range(len(months)))
        ax.set_xticklabels(months, rotation=45, fontsize=12)
        ax.set_xlim(-1, len(months))

        for i in range(len(months)):
            ax.clear()
            # Graficar consumptions
            ax.plot(
                months[: i + 1],
                consumptions[: i + 1],
                marker="o",
                color="b",
                label="Consumo sin panel (kWh)",
            )
            # Graficar consumptions_whit_panel
            ax.plot(
                months[: i + 1],
                consumptions_whit_panel[: i + 1],
                marker="x",
                color="g",
                label="Consumo con panel (kWh)",
            )

            # Configuración de la gráfica
            ax.set_title("Consumo de energía mensual", fontsize=16)
            ax.set_xlabel("Meses", fontsize=14)
            ax.set_ylabel("Consumo (kWh)", fontsize=14)
            ax.grid(True, linestyle="--", alpha=0.6)
            ax.set_xticks(range(len(months)))
            ax.set_xticklabels(months, rotation=45, fontsize=12)
            ax.set_xlim(-1, len(months))
            ax.legend(fontsize=12)

            plt.pause(0.5)

        plt.ioff()
        plt.show()
