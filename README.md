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

Airline Passenger Satisfaction Dataset de Kaggle:
https://www.kaggle.com/datasets/teejmahal20/airline-passenger-satisfaction?resource=download

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
- Streamlit
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
Para lanzar el dashboard interactivo:

```bash
streamlit run src/app.py
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
│   ├── app.py                     
│   │
│   ├── pages/                     
│   │   ├── 1_Distribucion.py
│   │   ├── 2_Clases.py
│   │   └── 3_Correlaciones.py
│   │
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

¿Influye la clase del vuelo en la satisfacción?

Sí. Los pasajeros que viajan en clase Business presentan los mayores niveles de satisfacción. Aproximadamente el 69% de ellos se declaran satisfechos, frente a valores cercanos al 19% en Economy y al 25% en Economy Plus.

¿Afectan los retrasos a la experiencia del pasajero?

Sí. Los pasajeros insatisfechos acumulan más minutos de retraso que los satisfechos. Los resultados muestran una relación negativa entre el retraso total y la satisfacción del cliente.

¿Qué servicios reciben mejores valoraciones?

Los servicios mejor valorados son:

- Seat Comfort
- Inflight Entertainment
- Cleanliness

Además, estos servicios muestran diferencias claras entre pasajeros satisfechos e insatisfechos, lo que indica que son factores importantes en la percepción de calidad.

¿Los clientes leales están más satisfechos?

Sí. Los clientes leales presentan mayores tasas de satisfacción que los clientes ocasionales, lo que sugiere una relación positiva entre fidelización y experiencia de viaje.


## Conclusión

La satisfacción de los pasajeros está principalmente relacionada con la calidad de la experiencia ofrecida por la aerolínea. La clase del vuelo y la fidelidad del cliente están asociadas a mayores niveles de satisfacción, mientras que los retrasos afectan negativamente a la percepción del servicio. Entre todos los factores analizados, la comodidad del asiento, el entretenimiento a bordo y la limpieza destacan como los aspectos con mayor impacto en la experiencia del pasajero.
---

## Autor
Andy Vacas
Proyecto desarrollado para práctica de Data Science & AI.
