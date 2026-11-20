# SpaceX Interactive Dashboard

## Descripción

Proyecto de análisis y visualización de datos de lanzamientos de SpaceX mediante Python y Dash. Desarrollé un dashboard interactivo que permite explorar los resultados de los lanzamientos según el sitio, la masa de carga y la versión del propulsor.

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
cd SpaceX-Interactive-Dashboard
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
