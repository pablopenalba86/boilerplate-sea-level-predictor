import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Importar datos
    df = pd.read_csv("epa-sea-level.csv")

    # Crear figura
    plt.figure(figsize=(10, 6))

    # Dispersión de datos históricos
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], color="blue", label="Datos históricos")

    # Regresión con todos los datos
    res_full = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x_full = pd.Series(range(1880, 2051))
    y_full = res_full.intercept + res_full.slope * x_full
    plt.plot(x_full, y_full, color="red", label="Tendencia 1880–2050")

    # Regresión desde el año 2000
    df_recent = df[df["Year"] >= 2000]
    res_recent = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    x_recent = pd.Series(range(2000, 2051))
    y_recent = res_recent.intercept + res_recent.slope * x_recent
    plt.plot(x_recent, y_recent, color="green", label="Tendencia 2000–2050")

    # Etiquetas y título
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()
    plt.grid(True, alpha=0.3)

    # Guardar gráfico
    plt.savefig("sea_level_plot.png")

    # Devolver el eje para los tests
    return plt.gca()
