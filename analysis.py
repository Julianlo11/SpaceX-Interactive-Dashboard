
import pandas as pd

# ============================================
# 1. CARGAR LOS DATOS
# ============================================

df = pd.read_csv("data/spacex_launch_dash.csv")

# Estandarizar nombres de los sitios de lanzamiento
df["Launch Site"] = df["Launch Site"].replace({
    "CCAFS LC-40": "CCAFS SLC-40"
})

# ============================================
# 2. PREGUNTA 1 Y 2:
# ANALISIS POR SITIO DE LANZAMIENTO
# ============================================

site_analysis = (
    df.groupby("Launch Site")["class"]
    .agg(
        total_lanzamientos="count",
        lanzamientos_exitosos="sum",
        tasa_exito="mean"
    )
    .reset_index()
)

site_analysis["tasa_exito"] *= 100

print("\n===== ANALISIS POR SITIO =====")
print(site_analysis.sort_values(
    "lanzamientos_exitosos",
    ascending=False
).to_string(index=False))

print("\nMayor cantidad de lanzamientos exitosos:")
print(site_analysis.loc[
    site_analysis["lanzamientos_exitosos"].idxmax()
])

print("\nMayor tasa de exito:")
print(site_analysis.loc[
    site_analysis["tasa_exito"].idxmax()
])


# ============================================
# 3. PREGUNTAS 3 Y 4:
# ANALISIS POR RANGO DE MASA
# ============================================

bins = list(range(0, 11000, 1000))

labels = [
    f"{i}-{i + 1000} kg"
    for i in range(0, 10000, 1000)
]

df["Payload Range"] = pd.cut(
    df["Payload Mass (kg)"],
    bins=bins,
    labels=labels,
    right=False
)

payload_analysis = (
    df.groupby("Payload Range", observed=False)["class"]
    .agg(
        total_lanzamientos="count",
        lanzamientos_exitosos="sum",
        tasa_exito="mean"
    )
    .reset_index()
)

payload_analysis["tasa_exito"] *= 100

print("\n===== ANALISIS POR MASA DE CARGA =====")
print(payload_analysis.to_string(index=False))

print("\nMayor tasa de exito por masa:")
print(payload_analysis.loc[
    payload_analysis["tasa_exito"].idxmax()
])

print("\nMenor tasa de exito por masa:")
print(payload_analysis.loc[
    payload_analysis["tasa_exito"].idxmin()
])


# ============================================
# 4. PREGUNTA 5:
# ANALISIS POR VERSION DEL PROPULSOR
# ============================================

booster_analysis = (
    df.groupby("Booster Version Category")["class"]
    .agg(
        total_lanzamientos="count",
        lanzamientos_exitosos="sum",
        tasa_exito="mean"
    )
    .reset_index()
)

booster_analysis["tasa_exito"] *= 100

print("\n===== ANALISIS POR VERSION DEL PROPULSOR =====")
print(booster_analysis.sort_values(
    "tasa_exito",
    ascending=False
).to_string(index=False))

print("\nVersion con mayor tasa de exito:")
print(booster_analysis.loc[
    booster_analysis["tasa_exito"].idxmax()
])
