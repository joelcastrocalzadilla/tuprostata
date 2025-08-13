import streamlit as st
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# ░░ 1. DEFINICIÓN DE VARIABLES ░░
frecuencia = ctrl.Antecedent(np.arange(0, 6.1, 0.1), 'frecuencia')
chorro = ctrl.Antecedent(np.arange(0, 11.1, 0.1), 'chorro')
edad = ctrl.Antecedent(np.arange(40, 91, 1), 'edad')
actividad_fisica = ctrl.Antecedent(np.arange(0, 11, 1), 'actividad_fisica')
alcohol = ctrl.Antecedent(np.arange(0, 11, 1), 'alcohol')
vida_sexual = ctrl.Antecedent(np.arange(0, 11, 1), 'vida_sexual')
dolor_miccional = ctrl.Antecedent(np.arange(0, 11, 1), 'dolor_miccional')
dolor_abdomen = ctrl.Antecedent(np.arange(0, 11, 1), 'dolor_abdomen')
grado_hpb = ctrl.Consequent(np.arange(0, 11.1, 0.1), 'grado_hpb')

# ░░ 2. FUNCIONES DE PERTENENCIA ░░
frecuencia['baja'] = fuzz.trapmf(frecuencia.universe, [0, 0, 1.2, 2])
frecuencia['moderada'] = fuzz.trimf(frecuencia.universe, [1.5, 2.8, 4.2])
frecuencia['alta'] = fuzz.trapmf(frecuencia.universe, [3.5, 4.5, 6, 6])

chorro['fuerte'] = fuzz.trapmf(chorro.universe, [6, 7.5, 10, 11])
chorro['medio'] = fuzz.trimf(chorro.universe, [3.5, 5, 6.5])
chorro['debil'] = fuzz.trapmf(chorro.universe, [0, 0, 2.5, 4.5])

edad['media'] = fuzz.trapmf(edad.universe, [40, 45, 55, 60])
edad['mayor'] = fuzz.trimf(edad.universe, [55, 65, 75])
edad['avanzada'] = fuzz.trapmf(edad.universe, [70, 75, 90, 90])

actividad_fisica['sedentario'] = fuzz.trapmf(actividad_fisica.universe, [0, 0, 3, 4])
actividad_fisica['moderado'] = fuzz.trimf(actividad_fisica.universe, [3, 5, 7])
actividad_fisica['activo'] = fuzz.trapmf(actividad_fisica.universe, [6, 8, 10, 10])

alcohol['nulo'] = fuzz.trapmf(alcohol.universe, [0, 0, 2, 3])
alcohol['ocasional'] = fuzz.trimf(alcohol.universe, [2, 5, 7])
alcohol['frecuente'] = fuzz.trapmf(alcohol.universe, [6, 8, 10, 10])

vida_sexual['plena'] = fuzz.trapmf(vida_sexual.universe, [7, 8.5, 10, 10])
vida_sexual['moderada'] = fuzz.trimf(vida_sexual.universe, [4, 6, 8])
vida_sexual['alterada'] = fuzz.trapmf(vida_sexual.universe, [0, 0, 3, 5])

dolor_miccional['ausente'] = fuzz.trapmf(dolor_miccional.universe, [0, 0, 2, 3])
dolor_miccional['moderado'] = fuzz.trimf(dolor_miccional.universe, [2.5, 5, 7])
dolor_miccional['intenso'] = fuzz.trapmf(dolor_miccional.universe, [6, 8, 10, 10])

dolor_abdomen['inexistente'] = fuzz.trapmf(dolor_abdomen.universe, [0, 0, 2, 3])
dolor_abdomen['molesto'] = fuzz.trimf(dolor_abdomen.universe, [2.5, 5, 7])
dolor_abdomen['pronunciado'] = fuzz.trapmf(dolor_abdomen.universe, [6, 8, 10, 10])

grado_hpb['leve'] = fuzz.trimf(grado_hpb.universe, [0, 1.5, 3])
grado_hpb['moderada'] = fuzz.trimf(grado_hpb.universe, [2.5, 4.5, 6.5])
grado_hpb['severa'] = fuzz.trimf(grado_hpb.universe, [6, 8, 10])

# ░░ 3. REGLAS DIFUSAS ░░
reglas = [
    ctrl.Rule(frecuencia['alta'] & chorro['debil'], grado_hpb['severa']),
    ctrl.Rule(frecuencia['moderada'] & chorro['medio'], grado_hpb['moderada']),
    ctrl.Rule(frecuencia['baja'] & chorro['fuerte'], grado_hpb['leve']),
    ctrl.Rule(edad['avanzada'] & frecuencia['alta'], grado_hpb['moderada']),
    ctrl.Rule(edad['media'] & chorro['medio'], grado_hpb['leve']),
    ctrl.Rule(actividad_fisica['sedentario'] & alcohol['frecuente'], grado_hpb['moderada']),
    ctrl.Rule(vida_sexual['alterada'] & edad['avanzada'], grado_hpb['severa']),
    ctrl.Rule(alcohol['frecuente'] & chorro['medio'], grado_hpb['moderada']),
    ctrl.Rule(actividad_fisica['activo'] & vida_sexual['plena'], grado_hpb['leve']),
    ctrl.Rule(dolor_miccional['intenso'] & edad['mayor'], grado_hpb['severa']),
    ctrl.Rule(dolor_abdomen['pronunciado'] & frecuencia['alta'], grado_hpb['severa']),
    ctrl.Rule(dolor_miccional['moderado'] & chorro['debil'], grado_hpb['moderada']),
    ctrl.Rule(edad['mayor'] | frecuencia['moderada'], grado_hpb['moderada'])
]

# ░░ 4. SISTEMA DE CONTROL ░░
sistema_ctrl = ctrl.ControlSystem(reglas)
sistema = ctrl.ControlSystemSimulation(sistema_ctrl)# ░░ 5. INTERFAZ STREAMLIT ░░
st.title("🧔 Diagnóstico Preliminar de HPB")
st.markdown("Sistema experto creado por **Joel**, educador y desarrollador de herramientas digitales para la salud comunitaria.")

# Sliders para entrada de datos
f = st.slider("Frecuencia urinaria nocturna (0 a 6)", 0.0, 6.0, 2.0)
c = st.slider("Fuerza del chorro urinario (0 a 10)", 0.0, 10.0, 5.0)
e = st.slider("Edad del paciente (40 a 90)", 40, 90, 60)
a = st.slider("Nivel de actividad física (0=sedentario / 10=activo)", 0, 10, 5)
alc = st.slider("Consumo de alcohol (0=nulo / 10=frecuente)", 0, 10, 3)
vs = st.slider("Función sexual / vida en pareja (0=mala / 10=plena)", 0, 10, 7)
dm = st.slider("¿Dolor o ardor al orinar? (0=nada / 10=intenso)", 0, 10, 2)
da = st.slider("¿Dolor bajo vientre o hipogastrio? (0=nada / 10=fuerte)", 0, 10, 2)

# Botón para ejecutar diagnóstico
if st.button("Evaluar"):
    sistema.input['frecuencia'] = f
    sistema.input['chorro'] = c
    sistema.input['edad'] = e
    sistema.input['actividad_fisica'] = a
    sistema.input['alcohol'] = alc
    sistema.input['vida_sexual'] = vs
    sistema.input['dolor_miccional'] = dm
    sistema.input['dolor_abdomen'] = da

    sistema.compute()
    resultado = sistema.output['grado_hpb']
    st.subheader(f"🔍 Diagnóstico difuso (grado HPB): {resultado:.2f}")

    # Interpretación del resultado
    if resultado < 3:
        st.success("✅ Evaluación: HPB Leve")
        st.markdown("**Análisis:** Síntomas mínimos. Estilo de vida saludable.")
        st.markdown("**Recomendación:** Seguimiento anual, promover ejercicio, PSA si hay antecedentes.")
    elif resultado < 6:
        st.warning("⚠️ Evaluación: HPB Moderada")
        st.markdown("**Análisis:** Síntomas urinarios intermedios o factores de riesgo presentes.")
        st.markdown("**Recomendación:** PSA + ecografía prostática. Revisión de estilo de vida. Considerar tratamiento farmacológico.")
    else:
        st.error("🚨 Evaluación: HPB Severa")
        st.markdown("**Análisis:** Posible obstrucción significativa, síntomas progresivos y alteración de calidad de vida.")
        st.markdown("**Recomendación:** Tacto rectal, PSA urgente, ecografía, flujometría. Evaluar función sexual y dolor pélvico. Derivación urológica.")

    st.markdown("---")

    st.markdown("🧠 *Sistema creado por Joel, educador y desarrollador de herramientas digitales. Compartelo con tus familiares y amigos.*")
with st.expander("📘 Más información sobre la próstata"):
    st.markdown("""
    <div style="background-color:#f0f8ff;padding:20px;border-radius:10px;">
        <h2 style="text-align:center;">🌍 Estadísticas Globales sobre el Cáncer de Próstata</h2>
        <p style="font-size:16px;">
            <em>“Más de <strong>1.4 millones</strong> de hombres son diagnosticados con cáncer de próstata cada año, y cerca de <strong>375,000</strong> fallecen por esta causa.”</em><br>
            <span style="font-size:14px;">— Globocan 2020, OMS</span>
        </p>
        <ul style="font-size:16px;">
            <li>🧍‍♂️ <strong>1 de cada 8 hombres</strong> será diagnosticado en algún momento de su vida.</li>
            <li>🧪 La <strong>detección temprana</strong> puede aumentar la tasa de curación hasta el <strong>75%</strong>.</li>
            <li>📉 La <strong>mortalidad ha disminuido</strong> significativamente en países con campañas de prevención.</li>
        </ul>
        <hr>
        <h3>🧠 Reflexión Educativa</h3>
        <p style="font-size:16px;">
            La próstata no solo es una glándula: es un símbolo de salud masculina, de cuidado preventivo, de diálogo intergeneracional.<br>
            Desde la adolescencia, el cuerpo masculino merece atención, ciencia y rituales de autocuidado.
        </p>
        <blockquote style="font-size:16px;color:#555;">
            En este espacio, promovemos el conocimiento como herramienta de transformación.<br>
            Cada clic, cada lectura, cada test es un paso hacia una comunidad más sana y consciente.
        </blockquote>
        <hr>
        <h4>🔗 Fuentes consultadas:</h4>
        <ul style="font-size:14px;">
            <li><a href="https://gco.iarc.fr/today/data/factsheets/cancers/27-Prostate-fact-sheet.pdf" target="_blank">Globocan 2020 – Prostate Cancer</a></li>
            <li><a href="https://www.cancer.org/cancer/prostate-cancer/about/key-statistics.html" target="_blank">American Cancer Society – Prostate Cancer Statistics</a></li>
            <li><a href="https://www.minsalud.gov.co" target="_blank">Ministerio de Salud de Colombia – Estadísticas Oncológicas</a></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
