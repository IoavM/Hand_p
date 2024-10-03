import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from streamlit_drawable_canvas import st_canvas

def predictDigit(image):
    model = tf.keras.models.load_model("model/handwritten.h5")
    image = ImageOps.grayscale(image)
    img = image.resize((28,28))
    img = np.array(img, dtype='float32')
    img = img/255
    plt.imshow(img)
    plt.show()
    img = img.reshape((1,28,28,1))
    pred= model.predict(img)
    result = np.argmax(pred[0])
    return result
# App Setup
st.set_page_config(page_title='Reconocimiento de Dígitos', layout='wide')

st.title('Reconocimiento de Dígitos')

st.subheader("Dibuja el dígito para predecir el número")

# Add canvas component
# Specify canvas parameters in the application
drawing_mode = "freedraw"
bg_color = '#b227aa'      # Background color black

with st.sidebar:
    st.subheader('TABLERO')
    stroke_width = st.slider('Selecciona el ancho de línea', 1, 30, 15)
    st.subheader('Color')
    stroke_color = st.color_picker("Selecciona un color", "#000000")
    st.write("Color: ", stroke_color)
    
    
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
if st.button('Predecir'):
    if canvas_result.image_data is not None:
        input_numpy_array = np.array(canvas_result.image_data)
        input_image = Image.fromarray(input_numpy_array.astype('uint8'),'RGBA')
        input_image.save('prediction/img.png')
        img = Image.open("prediction/img.png")
        res = predictDigit(img)
        st.header('El Digito es : ' + str(res))
    else:
        st.header('Por favor dibuja en el canvas el digito.')

resp = st.checkbox('¿ Acertó el número ?')
if resp:
    st.text('Excelente')

# Add sidebar information

    
