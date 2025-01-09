import streamlit as st
import pandas as pd
from PIL import Image

##############
st.sidebar.image("imagenes/img1.PNG",
                 caption="Dicta: Dr. Jesús Alvarado-Huayhuaz")

#############################Pagina 1############################## 
def Home():
  st.header('CICLO VERANO "BONIFATTI 2025" 🍫', divider='rainbow')
  #st.info("Profesor Jesús Alvarado-Huayhuaz")
  image = Image.open("imagenes/Reforzamiento_2025.png")
  st.image(image, caption='CICLO VERANO "BONIFATTI 2025"')
  st.sidebar.markdown("# Nivel Secundaria")
  st.sidebar.markdown("Desde el 7 de enero hasta 15 de febrero")
  st.sidebar.markdown("Esta página detalla los temas desarrollados en el ciclo verano de 6 semanas que abarca conceptos fundamentales en Física, Química y Matemáticas.")
  
def pagina1():
  st.title("Conceptos Básicos")
  st.info('Semana 1: 7, 9 y 11 de enero del 2025') 
  st.write(pd.DataFrame({'Curso': ['Física',
                                  'Química',
                                  'Matemáticas'],
                         'Tema': ["Introducción a las magnitudes físicas y vectoriales, unidades SI y conversión de unidades.",
                                   "Estructura del átomo, configuración electrónica. Impresión 3D de moléculas",
                                   "Planteamiento de ecuaciones y programación con calculadora CASIO."]},hide_index=True))

  st.subheader("Anotaciones del Jueves 9 de enero del 2025")
  st.write("Libros, diseño de moléculas e impresión 3D")
  st.write("Carpeta de libros compartidos: https://drive.google.com/drive/folders/12kibnRt1O8SzsfK12cnQFR7RkzO2Q4Ql?usp=sharing")
  
  st.subheader("Anotaciones del Martes 7 de enero del 2025")
  st.write("Manual de la Calculadora CASIO:")
  st.write("https://www.manual.pe/casio/cfx-9850gc-plus/manual?p=405#google_vignette")
  st.write("Descarga gratuita: https://drive.google.com/file/d/0By0zSAlbksYOZWstVkRLdE5ydjA/view?usp=sharing&resourcekey=0-0kNx0yr-VQp5OqLFf2BguQ")
  image1 =Image.open("imagenes/casio_imagen.PNG")
  st.image(image1, caption='Calculadora CASIO')

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

st.info("Nuestras redes.")
st.link_button("Tiktok", "https://www.tiktok.com/@inefable12x")
st.link_button("Youtube", "https://www.youtube.com/channel/UCm6lcnfmNS2stsUYVvrFOzg")
st.link_button("Facebook", "https://www.facebook.com/tallerespuquna")
st.link_button("Github", "https://github.com/inefable12")
