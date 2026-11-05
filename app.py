import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# 1. La página y el título

st.set_page_config(
    page_title="Inmigración Italiana a EE.UU. (1855-1900)",  # Aca le doy forma a la pestaña del navegador.
    page_icon="🚢",
    layout="wide"
)

st.title("🚢 Explorador del Flujo de Inmigración Italiana (1855 - 1900)")  # Aca le pongo titulo a la pagina.
st.markdown("Aplicación interactiva desarrollada para analizar los registros históricos de pasajeros.") # Y una breve descripción de la misma en formato markdown.


# 2. Cargar los datos limpios, con `@st.cache_data`

@st.cache_data                                     # Utilizo el @st.cache_data para que la función de carga de datos se ejecute una sola vez y no cada vez que se actualiza la app.
def cargar_datos():
    return pd.read_csv("datos/datos_limpios.csv")

df = cargar_datos()


# 3. Los filtros, en la barra de la izquierda

st.sidebar.header("🔍 Filtros de Búsqueda")                  # Aca creo la barra izquierda despegable donde voy a poner los filtros, de sexo, años y tipo de pasaje.

# Filtro por Sexo
sexos_disponibles = df["sexo"].dropna().unique().tolist()     # Aca selecciono la columna de sexo, y le saco los valores nulos, y le saco los duplicados, para que quede una lista de sexos disponibles.
sexo_seleccionado = st.sidebar.multiselect(                   # Utilizo en .multiselect para que el usuario pueda seleccionar uno o varios sexos, y si no selecciona ninguno, se muestran todos.
    "Seleccioná el Sexo:", 
    options=sexos_disponibles, 
    default=sexos_disponibles
)

# Filtro por Rango de Años
min_año = int(df["año"].min())                             # Defini el minimo y maximo de años para el slider, y lo pongo en la barra lateral.
max_año = int(df["año"].max())
rango_años = st.sidebar.slider(                            # Aca hago el .slider para que se pueda ajustar el minimo y maximo de años, moviendo los puntos desde el minimo o desde el maximo.
    "Seleccioná el Rango de Años:", 
    min_value=min_año, 
    max_value=max_año, 
    value=(min_año, max_año)
)

# Filtro por Tipo de Pasaje (opcional para enriquecer)
tipos_pasaje = df["tipo_pasaje"].dropna().unique().tolist()   # Aca selecciono la columna tipo_pasaje, le saco los nulos, extraigo los valores unicos y armo una lista de py.
pasaje_seleccionado = st.sidebar.multiselect(                 # Utilizo nuevamente el .multiselect para que el ususario elija los tipos de pasajes.
    "Tipo de Pasaje:", 
    options=tipos_pasaje, 
    default=tipos_pasaje
)
# Filtro de Edad

edad_min = float(df["edad"].min())      # Coloco el filtro de edad, con valores decimales ya que tengo numeros con decimales.
edad_max = float(df["edad"].max())
if edad_min > 0:
    edad_min = 0.0

rango_edad = st.sidebar.slider(
    "Selecciona el rango de edad",    # Aca hago el .slider para que se pueda ajustar el minimo y maximo de edades, moviendo los puntos desde el minimo o desde el maximo.
    min_value= edad_min,            
    max_value= edad_max,
    value=(edad_min,edad_max)
)

# 4. Filtrar la tabla

df_filtrado = df[
    (df["sexo"].isin(sexo_seleccionado)) &                    # Aca lo que hago es tomar el df original y se va actualizando y cambiando a medida que el usuario aplica los filtros.
    (df["año"] >= rango_años[0]) & 
    (df["año"] <= rango_años[1]) &                            # meto los rangos de la edad.
    (df["tipo_pasaje"].isin(pasaje_seleccionado)) &
    (((df["edad"] >= rango_edad[0]) & (df["edad"] <= rango_edad[1])) | (df["edad"].isna()))  # Aca coloco el rango de las edades y meto a los valores nulos tambien, osea las personas que no tienen edad.
]

# 5. Si no queda nada, avisar y parar

if df_filtrado.empty:
    st.warning("⚠️ No hay registros que coincidan con los filtros seleccionados. Por favor, amplía los criterios en la barra lateral.") #aviso
    st.stop()  # Detiene la ejecución para que no rompa en los siguientes pasos  # Aqui meto un .stop para cuando no se encuentren resultados por los filtros aplicados.


# 6. Las métricas

st.subheader("📊 Indicadores Principales")                             
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total de Pasajeros", f"{len(df_filtrado):,}")              # Aca vamos a sacar la metricas, total de pasajero, edad media y años.
col2.metric("Edad Promedio", f"{df_filtrado['edad'].mean():.1f} años")
col3.metric("Año Inicial", rango_años[0])
col4.metric("Año Final", rango_años[1])

st.markdown("---")


# 7. Las pestañas: la tabla, los gráficos 

pestaña_tabla, pestaña_graficos = st.tabs(["📋 Tabla de Datos", "📈 Gráficos y Tendencias"])  # Organizamos en solapas limpias. Y vamos a dividir en una la tabla y en la otra el grafico.

with pestaña_tabla:
    st.subheader("Listado de Inmigrantes Filtrados")
    st.dataframe(df_filtrado, use_container_width=True)

with pestaña_graficos:
    st.subheader("Evolución Anual del Flujo Migratorio")
    migracion_anual = df_filtrado["año"].value_counts().sort_index()     # ordenamos el df por año de menor a mayor.

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(migracion_anual.index, migracion_anual.values, marker="o", color="#2b5c8f", linewidth=2) # Meti en el eje de la x la migracion en años y en la y la cantidad de pasajeros x año.
    ax.set_title("Cantidad de Inmigrantes por Año")
    ax.set_xlabel("Año")
    ax.set_ylabel("Cantidad de Pasajeros")           # En este grafico se puede ver la cantidad de inmigrantes por año, que va en una solapa a parte.
    ax.grid(True, linestyle="--", alpha=0.5)
    st.pyplot(fig) # lo enseño en la pagina.


# 8. Una pregunta para el usuario

st.markdown("---")
st.subheader(" Consulta Interactiva para el Investigador")   # Aca planteo una pregunta para el usuario implementando un boton para que "se envia la respuesta del usuario". Se utiliza el st.radio para pooder hacer un conjunto de botones.

pregunta_usuario = st.radio(
    "Si tuvieras que emigrar en este período (1855-1900), ¿en qué año te hubiera gustado zarpar según el flujo migratorio?",
    options=[
        "A finales del siglo XIX (1895-1900) con mayor movimiento",
        "A mitad del período (1875-1880) con flujo moderado",
        "En los inicios (1855-1860) con menor densidad de pasajeros"
        ]
)

if st.button("Enviar respuesta"):
    st.success(f"¡Excelente elección! Has seleccionado: *'{pregunta_usuario}'*. Esta perspectiva ayuda a comprender el comportamiento histórico de los datos analizados.")