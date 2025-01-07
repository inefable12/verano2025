import streamlit as st
import pandas as pd

##############
st.sidebar.image("imagenes/img1.PNG",
                 caption="CICLO VERANO: BONIFATTI 2025")

#############################Pagina 1############################## 
def Home():
  st.header('CICLO VERANO "BONIFATTI 2025" 🍫', divider='rainbow')
  st.info("Profesor Jesús Alvarado-Huayhuaz")
  st.sidebar.markdown("# Nivel Secundaria")
  st.sidebar.markdown("Desde el 7 de enero hasta 15 de febrero")
  st.sidebar.markdown("Esta página detalla los temas desarrollados en el ciclo verano de 6 semanas que abarca conceptos fundamentales en Física, Química y Matemáticas.")
  
def pagina1():
  st.title("Conceptos Básicos: Física, Química y Matemáticas")
  st.info('Semana 1: 7, 9 y 11 de enero del 2025') 
  st.write(pd.DataFrame({'Curso': ['Física',
                                  'Química',
                                  'Matemáticas'],
                         'Tema': ["Introducción a las magnitudes físicas y vectoriales, unidades SI y conversión de unidades.",
                                   "Estructura del átomo, configuración electrónica. Impresión 3D de moléculas",
                                   "Planteamiento de ecuaciones y programación con calculadora CASIO."]}))
#st.header("Introducción")

def pagina2():
  st.title("Temas introductorios de Física, Química y Matemáticas")
  st.info('Semana 2: 14, 16 y 18 de enero del 2025') 
  st.write(pd.DataFrame({'Curso': ['Física',
                                  'Química',
                                  'Matemáticas'],
                         'Tema': ["Cinemática: movimiento rectilíneo uniforme y uniformemente acelerado.",
                                   "Tabla periódica: grupos y periodos, propiedades periódicas.",
                                   "Introducción a la resolución de problemas usando Python."]}))

def pagina3():
  st.title("Temas introductorios de Física, Química y Matemáticas")
  st.info('Semana 3: 21, 23 y 25 de enero del 2025') 
  st.write(pd.DataFrame({'Curso': ['Física',
                                  'Química',
                                  'Matemáticas'],
                         'Tema': ["Dinámica: leyes de Newton.",
                                   "Enlaces químicos: iónicos y covalentes.",
                                   "Álgebra básica: ecuaciones lineales y sistemas de ecuaciones"]}))

def pagina4():
  st.title("Temas introductorios de Física, Química y Matemáticas")
  st.info('Semana 4: 28 y 30 de enero; 1 de febrero del 2025') 
  st.write(pd.DataFrame({'Curso': ['Física',
                                  'Química',
                                  'Matemáticas'],
                         'Tema': ["Trabajo, energía y potencia. Concepto de energía cinética y potencial.",
                                   "Reacciones químicas: balanceo y tipos de reacciones.",
                                   "Geometría: áreas, perímetros y volúmenes de figuras comunes."]}))

def pagina5():
  st.title("Temas introductorios de Física, Química y Matemáticas")
  st.info('Semana 5: 4, 6 y 8 de febrero del 2025') 
  st.write(pd.DataFrame({'Curso': ['Física',
                                  'Química',
                                  'Matemáticas'],
                         'Tema': ["Conservación de la energía y cantidad de movimiento.",
                                   "Soluciones: concentración, molaridad, preparación de soluciones.",
                                   "Funciones: conceptos básicos y representación gráfica."]}))

def pagina6():
  st.title("Temas introductorios de Física, Química y Matemáticas")
  st.info('Semana 6: 11, 13 y 15 de febrero del 2025') 
  st.write(pd.DataFrame({'Curso': ['Física',
                                  'Química',
                                  'Matemáticas'],
                         'Tema': ["Gravitación y Leyes de Kepler",
                                   "Ácidos y bases: pH, pOH y neutralización.",
                                   "Estadística descriptiva: media, mediana y moda."]}))

################################################################### 
##########################Configuracion############################    
###################################################################    

page_names_to_funcs = {
  "Inicio": Home,
  "Semana 1": pagina1,
  "Semana 2": pagina2,
  "Semana 3": pagina3,
  "Semana 4": pagina4,
  "Semana 5": pagina5,
  "Semana 6": pagina6,
}

selected_page = st.sidebar.selectbox("Selecciona la semana:", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()

st.info("Esta página se irá actualizando luego de cada clase.")
