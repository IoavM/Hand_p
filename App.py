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
bg_color = '#000000'      # Background color black

# Create a canvas component
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=200,
    width=200,
    key="canvas",
    drawing_mode=drawing_mode
)

# Ensure the user has drawn something
if canvas_result.image_data is not None:
    st.image(canvas_result.image_data)  # Show the image as preview (if needed)
    # Here, you can process the image further if needed using PIL

# Add "Predict Now" button (currently not functional)
if st.button("Predecir Ahora"):
    st.write("Funcionalidad de predicción pendiente")

# Add sidebar information
st.sidebar.title("Acerca de:")
st.sidebar.text("En esta aplicación se evalúa")
st.sidebar.text("la capacidad de una RNA de reconocer")
st.sidebar.text("dígitos escritos a mano.")
st.sidebar.text("Basado en el desarrollo de Vinay Uniyal.")
