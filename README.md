# Airline Passenger Satisfaction Analysis

## Objetivo

Analizar la satisfacción de pasajeros de aerolíneas e identificar los factores que influyen en la experiencia del cliente.
Respondemos estas preguntas principales:
- ¿Influye la clase del vuelo en la satisfacción?
- ¿Afectan los retrasos a la experiencia del pasajero?
- ¿Qué servicios reciben mejores valoraciones?
- ¿Los clientes leales están más satisfechos?
---

## Dataset

Airline Passenger Satisfaction Dataset.

El proyecto utiliza los archivos:

- `train.csv`
- `test.csv`

---

## Tecnologías

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## Pipeline

1. Carga de datos
2. Unión de datasets
3. Limpieza de datos
4. Feature engineering
5. Análisis exploratorio (EDA)
6. Visualización de datos
7. Exportación del dataset limpio

---

## Ejecución

Ejecutar el pipeline principal:

```bash
python main.py
```

---

## Notebook

El notebook principal se encuentra en:

```text
notebooks/eda.ipynb
```

Contenido del notebook:

1. Introducción
2. Imports
3. Objetivo
4. Carga de datos
5. Exploración inicial
6. Limpieza de datos
7. Feature engineering
8. Visualizaciones
9. Conclusiones
10. Exportación de datos

---

## Estructura del proyecto

```text
project/
├── main.py
├── data/
│   ├── raw/
│   │   ├── train.csv
│   │   └── test.csv
│   └── processed/
│       └── clean_airline_passenger_satisfaction.csv
│
├── notebooks/
│   └── eda.ipynb
│
├── src/
│   ├── __init__.py
│   ├── io.py
│   ├── cleaning.py
│   ├── config.py
│   ├── features.py
│   ├── viz.py
│   └── utils.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Resultados principales

- Los pasajeros de clase Business presentan mayor satisfacción.
- Los retrasos afectan negativamente a la experiencia del cliente.
- Los servicios mejor valorados son:
  - Seat comfort
  - Inflight entertainment
  - Cleanliness
- Los clientes leales muestran mejores niveles de satisfacción.

---

## Autor

Proyecto desarrollado para práctica de Data Science & AI.
