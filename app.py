import streamlit as st

st.title("Temario de Conceptos Básicos: Física, Química y Matemáticas")

st.header("Introducción")
st.write("""
Esta página detalla los temas desarrollados en un curso de 6 semanas que abarca conceptos fundamentales en Física, Química y Matemáticas.
""")

# Contenido de las semanas
temario = {
    "Semana 1": {
        "Física": "Introducción a las magnitudes físicas, unidades SI, conversión de unidades.",
        "Química": "Estructura del átomo, configuración electrónica.",
        "Matemáticas": "Operaciones básicas, potencias y raíces, introducción a funciones."
    },
    "Semana 2": {
        "Física": "Cinemática: movimiento rectilíneo uniforme y uniformemente acelerado.",
        "Química": "Tabla periódica: grupos y periodos, propiedades periódicas.",
        "Matemáticas": "Álgebra básica: ecuaciones lineales y sistemas de ecuaciones."
    },
    "Semana 3": {
        "Física": "Dinámica: leyes de Newton, fuerza neta, fricción.",
        "Química": "Enlaces químicos: iónicos y covalentes.",
        "Matemáticas": "Geometría: áreas, perímetros y volúmenes de figuras comunes."
    },
    "Semana 4": {
        "Física": "Trabajo, energía y potencia. Concepto de energía cinética y potencial.",
        "Química": "Reacciones químicas: balanceo y tipos de reacciones.",
        "Matemáticas": "Trigonometría básica: seno, coseno y tangente."
    },
    "Semana 5": {
        "Física": "Conservación de la energía y cantidad de movimiento.",
        "Química": "Soluciones: concentración, molaridad, preparación de soluciones.",
        "Matemáticas": "Funciones: conceptos básicos y representación gráfica."
    },
    "Semana 6": {
        "Física": "Ondas y sonido: características y tipos de ondas.",
        "Química": "Ácidos y bases: pH, pOH y neutralización.",
        "Matemáticas": "Estadística descriptiva: media, mediana y moda."
    }
}

for semana, temas in temario.items():
    st.subheader(semana)
    for materia, contenido in temas.items():
        st.markdown(f"**{materia}:** {contenido}")

st.info("Esta página es una referencia para los estudiantes interesados en reforzar sus conocimientos básicos.")
