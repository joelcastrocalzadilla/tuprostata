import streamlit as st

st.set_page_config(page_title="¿Cómo está tu azúcar?", page_icon="🍬")

st.title("🍬 ¿Cómo está tu azúcar?")
st.markdown("Este test educativo te ayuda a reflexionar sobre tu metabolismo del azúcar. No diagnostica, pero orienta con empatía y ciencia.")

st.markdown("---")
st.header("📝 Responde con sinceridad")

# Preguntas
p1 = st.slider("¿Sientes sed con frecuencia, incluso sin hacer ejercicio?", 0, 10, 0)
p2 = st.slider("¿Has notado visión borrosa, especialmente al final del día?", 0, 10, 0)
p3 = st.slider("¿Te sientes cansado/a después de comer, como si te bajara la energía?", 0, 10, 0)
p4 = st.slider("¿Tienes antecedentes familiares de diabetes?", 0, 10, 0)
p5 = st.slider("¿Consumes alimentos azucarados o harinas refinadas con frecuencia?", 0, 10, 0)
p6 = st.slider("¿Has tenido infecciones frecuentes o heridas que tardan en sanar?", 0, 10, 0)
p7 = st.slider("¿Has notado cambios en tu peso sin explicación clara?", 0, 10, 0)
p8 = st.slider("¿Sientes hormigueo o entumecimiento en manos o pies?", 0, 10, 0)
p9 = st.slider("¿Te cuesta concentrarte o te sientes mentalmente lento/a?", 0, 10, 0)
p10 = st.slider("¿Has tenido resultados de glucosa cercanos al límite o te han hablado de prediabetes?", 0, 10, 0)

# Botón de evaluación
if st.button("📊 Evaluar"):
    total = p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10

    st.markdown("---")
    st.header("📋 Resultado educativo")

    if total <= 30:
        st.success("🌿 Dulce equilibrio\n\nTu perfil indica un metabolismo glucémico estable. Sigue cuidando tus hábitos, moviéndote con alegría y escuchando tu cuerpo.")
    elif 31 <= total <= 50:
        st.warning("🌥️ Zona de alerta\n\nTu perfil sugiere un riesgo leve. Podrías estar en una zona de transición. Revisa tus hábitos, reduce azúcares simples y considera chequeos preventivos.")
    elif 51 <= total <= 70:
        st.error("🔥 Azúcar encendida\n\nTu perfil es compatible con prediabetes. Es momento de actuar con cariño: alimentación consciente, movimiento regular y revisión médica.")
    else:
        st.error("🌪️ Tormenta glucémica\n\nTu perfil muestra señales compatibles con diabetes. No te alarmes, pero sí toma acción. Consulta con profesionales, revisa tu alimentación y acompáñate con cuidado.")

    st.markdown("---")
    st.caption("Este test no guarda tus respuestas ni emite diagnósticos. Es una herramienta educativa para la escucha corporal.")