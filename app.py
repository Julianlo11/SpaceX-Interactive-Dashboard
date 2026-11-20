
# ============================================
# 1. IMPORTAR BIBLIOTECAS
# ============================================

import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output


# ============================================
# 2. CARGAR EL DATASET
# ============================================

spacex_df = pd.read_csv("data/spacex_launch_dash.csv")

# Estandarizar nombres de los sitios de lanzamiento
spacex_df["Launch Site"] = spacex_df["Launch Site"].replace({
    "CCAFS LC-40": "CCAFS SLC-40"
})
# ============================================
# 3. CREAR LA APLICACIÓN DASH
# ============================================

app = Dash(__name__)


# ============================================
# 4. CREAR LAS OPCIONES DEL DROPDOWN
# ============================================

launch_sites = spacex_df["Launch Site"].unique()

# Obtener el peso mínimo y máximo de las cargas útiles
min_payload = spacex_df["Payload Mass (kg)"].min()
max_payload = spacex_df["Payload Mass (kg)"].max()

dropdown_options = [
    {"label": "All Sites", "value": "ALL"}
]

for site in launch_sites:
    dropdown_options.append({
        "label": site,
        "value": site
    })


# ============================================
# 5. DISEÑO DEL DASHBOARD
# ============================================

app.layout = html.Div([

    html.H1(
        "SpaceX Launch Records Dashboard",
        style={"textAlign": "center"}
    ),

    # Filtro por sitio de lanzamiento
    html.Label("Select a Launch Site:"),

    dcc.Dropdown(
        id="site-dropdown",
        options=dropdown_options,
        value="ALL",
        placeholder="Select a Launch Site here",
        searchable=True
    ),

    # Grafico circular
    dcc.Graph(id="success-pie-chart"),

    # Filtro por masa de carga util
    html.Label("Payload Mass Range (Kg):"),

    dcc.RangeSlider(
        id="payload-slider",
        min=0,
        max=10000,
        step=1000,
        marks={
            0: "0",
            1000: "1000",
            2000: "2000",
            3000: "3000",
            4000: "4000",
            5000: "5000",
            6000: "6000",
            7000: "7000",
            8000: "8000",
            9000: "9000",
            10000: "10000"
        },
        value=[min_payload, max_payload]
    ),
    # Grafico de dispersión
    dcc.Graph(id="success-payload-scatter-chart")
])


# ============================================
# 6. CALLBACK PARA EL GRAFICO CIRCULAR
# ============================================

@app.callback(
    Output("success-pie-chart", "figure"),
    Input("site-dropdown", "value")
)
def get_pie_chart(entered_site):

    if entered_site == "ALL":

        success_counts = (
            spacex_df.groupby("Launch Site")["class"]
            .sum()
            .reset_index()
        )

        fig = px.pie(
            success_counts,
            values="class",
            names="Launch Site",
            title="Successful Launches by Launch Site"
        )

    else:

        filtered_df = spacex_df[
            spacex_df["Launch Site"] == entered_site
        ]

        outcome_counts = (
            filtered_df["class"]
            .value_counts()
            .reindex([0, 1], fill_value=0)
            .reset_index()
        )

        outcome_counts.columns = ["Outcome", "Count"]

        outcome_counts["Outcome"] = outcome_counts["Outcome"].map({
            0: "Failed",
            1: "Successful"
        })

        fig = px.pie(
            outcome_counts,
            values="Count",
            names="Outcome",
            title=f"Launch Outcomes for {entered_site}"
        )

    return fig


# ============================================
# 7. EJECUTAR LA APLICACIÓN
# ============================================


# ============================================
# 7. CALLBACK PARA EL GRAFICO DE DISPERSION
# ============================================

@app.callback(
    Output("success-payload-scatter-chart", "figure"),
    [
        Input("site-dropdown", "value"),
        Input("payload-slider", "value")
    ]
)
def get_scatter_chart(entered_site, payload_range):

    # Filtrar los datos por el rango de masa seleccionado
    low, high = payload_range

    filtered_df = spacex_df[
        (spacex_df["Payload Mass (kg)"] >= low) &
        (spacex_df["Payload Mass (kg)"] <= high)
    ]

    # Comprobar si se seleccionaron todos los sitios
    if entered_site == "ALL":

        fig = px.scatter(
            filtered_df,
            x="Payload Mass (kg)",
            y="class",
            color="Booster Version Category",
            title="Payload Mass vs. Launch Outcome"
        )

    else:

        # Filtrar adicionalmente por el sitio seleccionado
        site_df = filtered_df[
            filtered_df["Launch Site"] == entered_site
        ]

        fig = px.scatter(
            site_df,
            x="Payload Mass (kg)",
            y="class",
            color="Booster Version Category",
            title=f"Payload Mass vs. Launch Outcome for {entered_site}"
        )

    return fig


# Exponer el servidor para el despliegue en Render
server = app.server

# Ejecutar la aplicación localmente
if __name__ == "__main__":
    app.run(
        debug=True,
        host="127.0.0.1",
        port=8050
    )
