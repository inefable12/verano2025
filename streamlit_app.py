import streamlit as st

##############
st.sidebar.image("imagenes/img1.PNG",
                 caption="CICLO VERANO: BONIFATTI 2025")

st.title("Temario de Conceptos Básicos: Física, Química y Matemáticas")

st.header("Introducción")
st.info("Profesor Jesús Alvarado-Huayhuaz")
st.write("""
Esta página detalla los temas desarrollados en el ciclo verano de 6 semanas que abarca conceptos fundamentales en Física, Química y Matemáticas.
""")

# Contenido de las semanas
temario = {
    "Semana 1": {
        "Física": "Introducción a las magnitudes físicas y vectoriales, unidades SI y conversión de unidades.",
        "Química": "Estructura del átomo, configuración electrónica. Impresión 3D de moléculas.",
        "Matemáticas": "Planteamiento de ecuaciones y programación con calculadora CASIO."
    },
    "Semana 2": {
        "Física": "Cinemática: movimiento rectilíneo uniforme y uniformemente acelerado.",
        "Química": "Tabla periódica: grupos y periodos, propiedades periódicas.",
        "Matemáticas": "Introducción a la resolución de problemas usando Python."
    },
    "Semana 3": {
        "Física": "Dinámica: leyes de Newton.",
        "Química": "Enlaces químicos: iónicos y covalentes.",
        "Matemáticas": "Álgebra básica: ecuaciones lineales y sistemas de ecuaciones."
    },
    "Semana 4": {
        "Física": "Trabajo, energía y potencia. Concepto de energía cinética y potencial.",
        "Química": "Reacciones químicas: balanceo y tipos de reacciones.",
        "Matemáticas": "Geometría: áreas, perímetros y volúmenes de figuras comunes."
    },
    "Semana 5": {
        "Física": "Conservación de la energía y cantidad de movimiento.",
        "Química": "Soluciones: concentración, molaridad, preparación de soluciones.",
        "Matemáticas": "Funciones: conceptos básicos y representación gráfica."
    },
    "Semana 6": {
        "Física": "Gravitación y Leyes de Kepler.",
        "Química": "Ácidos y bases: pH, pOH y neutralización.",
        "Matemáticas": "Estadística descriptiva: media, mediana y moda."
    }
}

# Menú desplegable en la barra lateral
semana_seleccionada = st.sidebar.selectbox(
    "Selecciona la semana:",
    list(temario.keys())
)

# Mostrar contenido de la semana seleccionada
st.subheader(semana_seleccionada)
for materia, contenido in temario[semana_seleccionada].items():
    st.markdown(f"**{materia}:** {contenido}")

st.info("Esta página se irá actualizando luego de cada clase.")
