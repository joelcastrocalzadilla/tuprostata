import streamlit as st

st.set_page_config(page_title="Test de Sedentarismo", layout="centered")

st.title("🏃‍♂️ ¿Tu estilo de vida es sedentario?")
st.markdown("""
Este test educativo te ayuda a reflexionar sobre tu nivel de actividad física y recibir recomendaciones personalizadas.  
Forma parte de tu ritual de autocuidado y activación corporal.
""")

# Datos básicos
st.subheader("📋 Datos personales")
peso = st.number_input("¿Cuál es tu peso en kg?", min_value=30.0, max_value=200.0, step=0.5)
talla = st.number_input("¿Cuál es tu estatura en metros?", min_value=1.0, max_value=2.5, step=0.01)

# Rutina diaria
st.subheader("🕰️ Rutina diaria")
hora_levantarse = st.time_input("¿A qué hora te levantas normalmente?")
trabajo = st.selectbox("¿Tu trabajo es principalmente…", [
    "🪑 Sedentario (escritorio, oficina, conducción)",
    "🚶‍♂️ Activo (ventas, docencia, atención al público)",
    "🛠️ Físico (construcción, agricultura, deporte)"
])

# Actividad física
st.subheader("🏋️ Actividad física")
actividad = st.selectbox("¿Realizas algún tipo de ejercicio físico?", [
    "Nunca",
    "1–2 veces por semana",
    "3–5 veces por semana",
    "Diariamente"
])
duracion = st.slider("¿Cuánto tiempo dedicas al ejercicio cada vez?", 0, 120, 30)

# Pantallas
st.subheader("📱 Tiempo frente a pantallas")
computador = st.slider("¿Cuántas horas al día usas el computador?", 0, 12, 4)
celular = st.slider("¿Cuántas horas al día usas el celular?", 0, 12, 3)

# Resultado
if st.button("🔍 Ver diagnóstico de sedentarismo"):
    imc = peso / (talla ** 2)
    nivel = ""
    recomendaciones = ""

    # Evaluación simple
    puntos = 0
    if trabajo == "🪑 Sedentario (escritorio, oficina, conducción)": puntos += 2
    if actividad == "Nunca": puntos += 3
    elif actividad == "1–2 veces por semana": puntos += 2
    elif actividad == "3–5 veces por semana": puntos += 1
    if computador + celular > 6: puntos += 2
    if imc >= 25: puntos += 1

    # Diagnóstico
    if puntos >= 7:
        nivel = "🚨 Sedentarismo alto"
        recomendaciones = """
        - Realiza pausas activas cada 60 minutos.
        - Camina al menos 30 minutos diarios.
        - Prueba rutinas breves de estiramiento o yoga.
        - Reduce el tiempo frente a pantallas en bloques.
        """
    elif puntos >= 4:
        nivel = "⚠️ Sedentarismo moderado"
        recomendaciones = """
        - Aumenta la frecuencia de actividad física semanal.
        - Incorpora caminatas conscientes o ejercicios suaves.
        - Evalúa tu postura y ergonomía.
        """
    else:
        nivel = "✅ Estilo de vida activo"
        recomendaciones = """
        - ¡Sigue así! Mantén tu rutina y escucha tu cuerpo.
        - Puedes explorar nuevas formas de movimiento: danza, natación, ciclismo.
        """

    st.subheader("🧭 Resultado")
    st.markdown(f"**Nivel de sedentarismo:** {nivel}")
    st.markdown("**Recomendaciones personalizadas:**")
    st.markdown(recomendaciones)

    st.markdown(f"📊 Tu IMC estimado es: **{imc:.1f}**")

# Footer
st.markdown("---")
st.caption("Este test es educativo y no sustituye una evaluación médica profesional.")