import streamlit as st

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
  st.write(pd.DataFrame({'Tema': ['Física',
                                  'Química',
                                  'Matemáticas'],
                         'Fecha': ["Introducción a las magnitudes físicas y vectoriales, unidades SI y conversión de unidades.",
                                   "Estructura del átomo, configuración electrónica. Impresión 3D de moléculas",
                                   "Planteamiento de ecuaciones y programación con calculadora CASIO."]}))
#st.header("Introducción")

def pagina2():
 
    "Semana 2": {
        "Física": "Cinemática: movimiento rectilíneo uniforme y uniformemente acelerado.",
        "Química": "Tabla periódica: grupos y periodos, propiedades periódicas.",
        "Matemáticas": "Introducción a la resolución de problemas usando Python."
    }

def pagina3():
    "Semana 3": {
        "Física": "Dinámica: leyes de Newton.",
        "Química": "Enlaces químicos: iónicos y covalentes.",
        "Matemáticas": "Álgebra básica: ecuaciones lineales y sistemas de ecuaciones."
    }

def pagina4():
    "Semana 4": {
        "Física": "Trabajo, energía y potencia. Concepto de energía cinética y potencial.",
        "Química": "Reacciones químicas: balanceo y tipos de reacciones.",
        "Matemáticas": "Geometría: áreas, perímetros y volúmenes de figuras comunes."
    }

def pagina5():
    "Semana 5": {
        "Física": "Conservación de la energía y cantidad de movimiento.",
        "Química": "Soluciones: concentración, molaridad, preparación de soluciones.",
        "Matemáticas": "Funciones: conceptos básicos y representación gráfica."
    }

def pagina6():
    "Semana 6": {
        "Física": "Gravitación y Leyes de Kepler.",
        "Química": "Ácidos y bases: pH, pOH y neutralización.",
        "Matemáticas": "Estadística descriptiva: media, mediana y moda."
    }


################################################################### 
##########################Configuracion############################    
###################################################################    

page_names_to_funcs = {
  "Inicio": Home,
  "Semana 1": pagina1(),
  "Semana 2": pagina2(),
  "Semana 3": pagina3(),
  "Semana 4": pagina4(),
  "Semana 5": pagina5(),
  "Semana 6": pagina6(),
}

selected_page = st.sidebar.selectbox("Selecciona la semana:", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()

st.info("Esta página se irá actualizando luego de cada clase.")
