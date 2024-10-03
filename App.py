import tensorflow as tf
from PIL import Image, ImageOps
from streamlit_drawable_canvas import st_canvas

# App


# Streamlit 
st.set_page_config(page_title='Reconocimiento de Dígitos', layout='wide')
st.title('Reconocimiento de Dígitos' )
st.subheader("Dibuja el digito para prdecir el número")

# Add canvas component
# Specify canvas parameters in application
drawing_mode = "freedraw"
stroke_width = st.slider('Selecciona el ancho de línea', 1, 30, 15)
stroke_color = '#FFFFFF' # Set background color to white
bg_color = '#000000'

# Create a canvas component
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=200,
    width=200,
    key="canvas",
)

# Add "Predict Now" button

# Add sidebar
st.sidebar.title("Acerca de:")
st.sidebar.text("En esta aplicación se evalua ")
st.sidebar.text("la capacidad de un RNA de reconocer") 
st.sidebar.text("digitos escritos a mano.")
st.sidebar.text("Basado en desarrollo de Vinay Uniyal")
#st.sidebar.text("GitHub Repository")
#st.sidebar.write("[GitHub Repo Link](https://github.com/Vinay2022/Handwritten-Digit-Recognition)")
