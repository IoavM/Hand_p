import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image, ImageOps

# App Setup
st.set_page_config(page_title='Reconocimiento de Dígitos', layout='wide')

st.title('Reconocimiento de Dígitos')

st.subheader("Dibuja el dígito para predecir el número")

# Add canvas component
# Specify canvas parameters in the application
drawing_mode = "freedraw"
stroke_width = st.slider('Selecciona el ancho de línea', 1, 30, 15)
stroke_color = '#FFFFFF'  # Drawing color white
bg_color = '#b227aa'      # Background color black

with st.sidebar:
    st.subheader('TABLERO')
    stroke_width = st.slider('Selecciona el ancho de línea', 1, 30, 15)
# Create a canvas component
canvas_result = st_canvas(
    fill_color="rgba(178, 39, 170 )",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=200,
    width=750,
    key="canvas",
    drawing_mode=drawing_mode
)

# Ensure the user has drawn something
# Add "Predict Now" button (currently not functional)
if st.button("Predecir Ahora"):
    st.write("Funcionalidad de predicción pendiente")

# Add sidebar information

    
