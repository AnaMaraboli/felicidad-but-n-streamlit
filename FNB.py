import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Índice de Felicidad Nacional Bruta", page_icon="🌸", layout="centered")

st.markdown(
    """
    <h1 style='text-align: center; color: black;'>🌸 Índice de Felicidad Nacional Bruta (FNB)</h1>
    <h4 style='text-align: center; color: black;'>Creado por Ana Maraboli</h4>
    """,
    unsafe_allow_html=True
)
st.write("Este test está inspirado en el modelo de Bután para medir el bienestar integral.")


# Dominios del FNB
dominios = {
    "Bienestar psicológico": "¿Qué tan satisfecho/a te sientes emocionalmente y mentalmente?",
    "Salud": "¿Qué tan saludable te consideras actualmente?",
    "Educación": "¿Qué tan satisfecho/a estás con tu acceso a educación o aprendizaje?",
    "Uso del tiempo": "¿Qué tan equilibrado sientes tu tiempo entre trabajo, descanso y ocio?",
    "Vitalidad comunitaria": "¿Qué tan conectado/a te sientes con tu comunidad y entorno social?",
    "Diversidad cultural": "¿Qué tanto disfrutas y participas en actividades culturales o tradiciones?",
    "Resiliencia ecológica": "¿Qué tan responsable eres con el medio ambiente y naturaleza?",
    "Nivel de vida": "¿Qué tan satisfecho/a estás con tus condiciones materiales (ingresos, vivienda)?",
    "Gobernanza": "¿Qué tanto confías en las instituciones y reglas de tu sociedad?"
}

resultados = {}

st.subheader("📝 Responde cada dominio del 1 al 5")
st.caption("1 = Muy insatisfecho/a | 5 = Muy satisfecho/a")

for dominio, pregunta in dominios.items():
    resultados[dominio] = st.slider(pregunta, 1, 5, 3)

if st.button("Calcular mi índice de felicidad"):
    df = pd.DataFrame(list(resultados.items()), columns=["Dominio", "Puntaje"])
    puntaje_total = df["Puntaje"].sum()
    max_puntaje = len(df) * 5
    indice_felicidad = (puntaje_total / max_puntaje) * 100

    # Interpretación
    if indice_felicidad >= 80:
        interpretacion = "🌟 Alta felicidad, mantén ese equilibrio."
    elif indice_felicidad >= 60:
        interpretacion = "😊 Moderada felicidad, hay espacio para mejorar."
    elif indice_felicidad >= 40:
        interpretacion = "⚠️ Riesgo de insatisfacción, revisa tus prioridades."
    else:
        interpretacion = "💔 Baja felicidad, busca apoyo y cambios significativos."

    st.metric("Índice de Felicidad Nacional Bruta", f"{indice_felicidad:.1f}%")
    st.write(interpretacion)

    # Gráfico de barras
    fig = px.bar(df, x="Dominio", y="Puntaje", color="Puntaje", 
                 title="Distribución de tu felicidad por dominios",
                 range_y=[0,5])
    st.plotly_chart(fig, use_container_width=True)

    st.success("✅ Tu evaluación se basa en el modelo original de Bután, adaptado para uso personal.")

    with st.expander("📖 ¿Cómo se calcula este índice?"):
        st.write("""
        Este índice está inspirado en la **Felicidad Nacional Bruta (FNB)** de Bután, que considera 9 dominios esenciales:

        1. Bienestar psicológico
        2. Salud
        3. Educación
        4. Uso del tiempo
        5. Vitalidad comunitaria
        6. Diversidad cultural
        7. Resiliencia ecológica
        8. Nivel de vida
        9. Gobernanza

        Cada dominio se evalúa en una escala del **1 al 5**. Luego, se suman las puntuaciones y se convierten en un porcentaje sobre el máximo posible.

        Este método busca reflejar el **bienestar integral** más allá de lo económico, valorando tanto lo material como lo emocional, social y ambiental.
        """)
