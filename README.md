# SpaceX Interactive Dashboard

## Descripción

Este proyecto consiste en el desarrollo de un dashboard interactivo para explorar y analizar datos históricos de lanzamientos de SpaceX mediante Python, Plotly y Dash.

El objetivo es identificar patrones en los resultados de los lanzamientos y facilitar la exploración de variables como el sitio de lanzamiento, la masa de carga y la versión del propulsor.

La aplicación permite interactuar con los datos mediante filtros dinámicos y visualizar los resultados a través de gráficos.

## Objetivos

- Analizar el desempeño histórico de los lanzamientos de SpaceX.

- Comparar los resultados entre diferentes sitios de lanzamiento.

- Explorar la relación entre la masa de carga y el resultado del lanzamiento.

- Examinar el desempeño según la versión del propulsor.
  
-  Construir un dashboard interactivo utilizando Plotly Dash.

## Tecnologías utilizadas

- Python
- Pandas
- Plotly Express
- Dash
- Git y GitHub
- Render

## Funcionalidades

- Visualización de lanzamientos exitosos y fallidos.
- Filtro interactivo por sitio de lanzamiento.
- Filtro por rango de masa de carga útil.
- Gráfico de dispersión para analizar la relación entre la masa de carga y los resultados.
- Comparación de resultados según la versión del propulsor.

## Resultados del análisis

El análisis se realizó sobre 56 registros de lanzamientos.

**Por sitio de lanzamiento:**

| Sitio | Lanzamientos | Exitosos | Tasa de éxito |
|---|---:|---:|---:|
| KSC LC-39A | 13 | 10 | 76.92% |
| CCAFS SLC-40 | 33 | 10 | 30.30% |
| VAFB SLC-4E | 10 | 4 | 40.00% |

**Por masa de carga:**

- Mayor tasa de éxito: 3000–4000 kg (72.73%).
- Menor tasa de éxito con registros: 6000–7000 kg (0%).

**Por versión del propulsor:**

- B5: 100% (1 lanzamiento).
- FT: 66.67% (24 lanzamientos).
- B4: 54.55% (11 lanzamientos).
- v1.1: 6.67% (15 lanzamientos).
- v1.0: 0% (5 lanzamientos).

## Conclusiones

El análisis de los datos permitió identificar diferencias en el desempeño histórico de los lanzamientos según el sitio, la masa de carga y la versión del propulsor.

KSC LC-39A presentó la mayor tasa de éxito entre los sitios analizados, con un 76,92 %. Por otra parte, CCAFS SLC-40 concentró el mayor volumen de operaciones, con 33 lanzamientos.

En cuanto a la masa de carga, el intervalo de 3000 a 4000 kg obtuvo la mayor tasa de éxito, con un 72,73 %. Respecto a las versiones de los propulsores, FT registró 66,67 % de éxito en 24 lanzamientos.

Estos resultados permiten explorar patrones históricos y comparar el desempeño de los lanzamientos. Sin embargo, las tasas observadas son descriptivas y no demuestran por sí mismas relaciones causales.

## Estructura del proyecto

```text
SpaceX-Interactive-Dashboard/
│
├── data/
│   └── spacex_launch_dash.csv
│
├── app.py
├── analysis.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Instalación y ejecución

Clonar el repositorio:

```bash
https://github.com/Julianlo11/SpaceX-Interactive-Dashboard
```

Ingresar al proyecto:

```bash
https://spacex-interactive-dashboard.onrender.com/
```

Crear y activar el entorno virtual:

```bash
python -m venv venv
```

En Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar el dashboard:

```bash
python app.py
```

Abrir en el navegador:

```text
http://127.0.0.1:8050/
```

Ejecutar el análisis exploratorio:

```bash
python analysis.py
```

## Autor

**Julian Daniel Lopez Cano**

Economista | Data Science | Python | SQL | Data Analytics

Proyecto desarrollado como parte de mi formación en Ciencia de Datos, aplicando técnicas de análisis, procesamiento y visualización interactiva de datos.
