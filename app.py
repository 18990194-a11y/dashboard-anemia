import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# CONFIGURACIÓN DE LA PÁGINA

st.set_page_config(
    page_title="Dashboard Bibliométrico",
    layout="wide"
)

# CARGAR DATASET

df = pd.read_csv("dataset_limpio.csv")

# SIDEBAR

st.sidebar.title("📊 Panel de Control")

st.sidebar.write(
    "Utilice estos filtros para explorar la bibliografía científica."
)

# FILTRO POR PALABRA
busqueda = st.sidebar.text_input(
    "🔍 Buscar palabra clave"
)

# FILTRO POR AÑO
anio = st.sidebar.selectbox(
    "📅 Seleccione un año",
    sorted(df['Year'].unique())
)

# FILTRO POR CITAS
min_citas = st.sidebar.slider(
    "⭐ Mínimo de citas",
    0,
    int(df['Cited by'].max()),
    0
)
# INFORMACIÓN CLÍNICA EN SIDEBAR

st.sidebar.markdown("---")

st.sidebar.markdown("## 🩺 Información Clínica")

st.sidebar.info("""
### 🩸 La Anemia

Datos relevantes:

🌎 La anemia afecta a millones de personas en el mundo.

👩 Mujeres y niños presentan mayor riesgo.

🧠 La inteligencia artificial ayuda en diagnósticos tempranos.

📊 El análisis de datos médicos mejora la prevención.

🏥 La detección temprana reduce complicaciones de salud.
""")

st.sidebar.markdown("### 🎯 Objetivo del Dashboard")

st.sidebar.write("""
Analizar investigaciones científicas relacionadas con anemia,
machine learning e inteligencia artificial utilizando datos de Scopus.
""")

st.sidebar.markdown("---")

st.sidebar.markdown("ℹ️ Sobre el Dashboard")

st.sidebar.write("""
🔬 Datos: Scopus · Ciencia de Datos · Dashboard Bibliométrico
""")


# FILTRAR DATOS

df_filtrado = df[
    (df['Year'] == anio) &
    (df['Cited by'] >= min_citas)
]

if busqueda:
    df_filtrado = df_filtrado[
        df_filtrado['Title'].str.contains(
            busqueda,
            case=False,
            na=False
        )
    ]

# TÍTULO PRINCIPAL

st.title("🏥 Dashboard Bibliométrico sobre Anemia e Inteligencia Artificial")

# INTEGRANTE

st.markdown("### 👩‍💻 Integrante")

st.write("""
- Rosa María Flores Echeverría
""")

# MENSAJES

st.success(
    "Bienvenido al dashboard bibliométrico sobre anemia e inteligencia artificial."
)

st.info(
    "Los datos fueron obtenidos desde Scopus y analizados utilizando Python, Pandas y Streamlit."
)

# DESCRIPCIÓN

st.write("""
Este dashboard presenta un análisis bibliométrico de artículos científicos
relacionados con anemia, machine learning e inteligencia artificial.
""")

# SEPARADOR

st.markdown("---")
# MÉTRICAS

st.subheader("📊 Métricas Generales")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📚 Cantidad de artículos", df.shape[0])

with col2:
    st.metric("👨‍🔬 Total de autores", df['Authors'].nunique())

with col3:
    st.metric("📅 Año más frecuente", df['Year'].mode()[0])

# SEPARADOR

st.markdown("---")

# DATASET

st.subheader("🗂 Dataset Científico Filtrado")

st.dataframe(df_filtrado)
# SEPARADOR

st.markdown("---")

# GRÁFICO 1
st.subheader("📈 Cantidad de Publicaciones por Año")

articulos_por_anio = df['Year'].value_counts().sort_index()

fig1, ax1 = plt.subplots(figsize=(10,5))

articulos_por_anio.plot(
    kind='bar',
    ax=ax1
)

plt.xlabel("Año")
plt.ylabel("Cantidad")
plt.title("Publicaciones por Año")

st.pyplot(fig1)

# SEPARADOR

st.markdown("---")

# GRÁFICO 2

st.subheader("👨‍🔬 Autores con Más Publicaciones")

top_autores = df['Authors'].value_counts().head(10)

fig2, ax2 = plt.subplots(figsize=(10,5))

top_autores.plot(
    kind='barh',
    ax=ax2
)

plt.xlabel("Cantidad")
plt.ylabel("Autores")
plt.title("Top 10 Autores")

st.pyplot(fig2)

# SEPARADOR

st.markdown("---")

# GRÁFICO 3

st.subheader("⭐ Artículos Más Citados")

top_citados = df.sort_values(
    by='Cited by',
    ascending=False
).head(10)

fig3, ax3 = plt.subplots(figsize=(10,6))

ax3.barh(
    top_citados['Title'],
    top_citados['Cited by']
)

plt.xlabel("Cantidad de citas")
plt.ylabel("Artículos")
plt.title("Top Artículos Más Citados")

st.pyplot(fig3)

# SEPARADOR

st.markdown("---")

# GRÁFICO DONUT

st.subheader("📚 Distribución de Publicaciones por Año")

tipos = df['Year'].value_counts()

fig4, ax4 = plt.subplots(figsize=(8,8))

ax4.pie(
    tipos,
    labels=tipos.index,
    autopct=lambda p: '\n'.join(list(f'{p:.1f}%')),
    startangle=90,
    pctdistance=0.75,
    labeldistance=1.05,
    textprops={'fontsize': 6}
)

# LEYENDA PEQUEÑA
ax4.legend(
    tipos.index,
    title="Años",
    loc="center left",
    bbox_to_anchor=(1, 0.5),
    fontsize=6,
    title_fontsize=7
)
# AGUJERO CENTRAL
centro = plt.Circle((0,0), 0.70, fc='white')

fig4.gca().add_artist(centro)

plt.title("Distribución de Publicaciones")

st.pyplot(fig4)

# AGUJERO CENTRAL
centro = plt.Circle((0,0), 0.70, fc='white')

fig4.gca().add_artist(centro)

plt.title("Distribución de Publicaciones")

st.pyplot(fig4)

# SEPARADOR

st.markdown("---")

# CONCLUSIÓN

st.subheader("📝 Conclusión")

st.write("""
La inteligencia artificial y el machine learning han incrementado su presencia
en investigaciones relacionadas con anemia y salud. El análisis bibliométrico
permite identificar tendencias científicas, autores relevantes y artículos
de alto impacto académico.
""")

# PIE DE PÁGINA

st.markdown("---")

st.caption(
    "Proyecto desarrollado con Streamlit, Python, Pandas y Scopus"
)
# RECOMENDACIONES

st.markdown("---")

st.subheader("🏥 Recomendaciones para la Práctica Clínica")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("""
    ✅ Para pacientes

    • Realizar controles médicos periódicos.

    • Mantener una alimentación rica en hierro.

    • Detectar síntomas tempranos de anemia.
    """)

with col2:
    st.info("""
    🤖 Para profesionales

    • Utilizar herramientas de IA como apoyo diagnóstico.

    • Analizar datos clínicos para prevención temprana.

    • Mejorar estrategias de atención médica.
    """)

with col3:
    st.warning("""
    📊 Para investigadores

    • Continuar investigaciones sobre IA y anemia.

    • Desarrollar modelos predictivos más precisos.

    • Promover análisis bibliométricos en salud.
    """)