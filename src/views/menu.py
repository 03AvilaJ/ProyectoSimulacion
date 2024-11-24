import matplotlib.pyplot as plt


class Menu:

    def show_consumption_by_month(self, months, consumptions):
        plt.figure(figsize=(10, 6))
        plt.plot(
            months,
            consumptions,
            marker="o",
            color="b",
            label="Consumo de energía (kwh)",
        )

        plt.title("Consumo de energía mensual", fontsize=16)
        plt.xlabel("Meses", fontsize=14)
        plt.ylabel("Consumo (kWh)", fontsize=14)
        plt.grid(True, linestyle="--", alpha=0.6)
        plt.xticks(rotation=45, fontsize=12)
        plt.yticks(fontsize=12)
        plt.legend(fontsize=12)
        plt.tight_layout()

        plt.show()
