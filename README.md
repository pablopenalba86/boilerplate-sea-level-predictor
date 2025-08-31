# 🌊 Sea Level Predictor / Predicción del Nivel del Mar

This project analyzes global sea level changes since 1880 using data from the US EPA. It applies linear regression to predict sea level rise through the year 2050.

Este proyecto analiza los cambios en el nivel del mar desde 1880 utilizando datos de la EPA de EE.UU. Aplica regresión lineal para predecir el aumento del nivel del mar hasta el año 2050.

---

## 📊 Tools Used / Herramientas Utilizadas

- Python  
- pandas  
- matplotlib  
- scipy.stats.linregress  

---

## 📈 Results / Resultados

The script generates a plot (`sea_level_plot.png`) showing:

- A regression line using all available data (1880–2014)
- A second regression line using only data from the year 2000 onward
- Both lines extended to predict sea level in 2050

El script genera un gráfico (`sea_level_plot.png`) que muestra:

- Una línea de regresión usando todos los datos disponibles (1880–2014)  
- Una segunda línea de regresión usando solo datos desde el año 2000  
- Ambas líneas extendidas para predecir el nivel del mar en 2050

---

## 🧪 Testing / Pruebas

All unit tests in `test_module.py` pass successfully.

Todas las pruebas unitarias en `test_module.py` se ejecutan correctamente.

---

## 📁 Dataset Source / Fuente del Dataset

- [EPA Global Sea Level Data](https://www.epa.gov/climate-indicators/climate-change-indicators-sea-level)  
- Data from CSIRO (2015) and NOAA (2015)

Datos de CSIRO (2015) y NOAA (2015), publicados por la EPA.

---

## 🚀 How to Run / Cómo Ejecutar

```bash
python main.py
