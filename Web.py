from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
#imagenes_animadas: https://lottiefiles.com/search?q=office%20work&category=animations
#---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_2pezcshb.json")
img_contact_form = Image.open("Image/MTC.png")
img_lottie_animation = Image.open("Image/MTC2.jpg")
#--- HEADER SECTION -----
with st.container():
    st.subheader ("Hi,I am Ricardo")
    st.title("A Data analyst from Germany")
    st.write("I am passionate homologation")
    st.write("[Learn More >](https://pythonandvba.com)")

# ----- WHAT I DO --------
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header ("What I do")
        st.write("##")
        st.write(
            """
            On my youtube channel
            p
            d
            s
            """
            )
        st.write("[channel>](https://www.youtube.com/results?search_query=formulario+python+web+a+ms+word)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")


#----- PROJECT ------
with st.container():
    st.write("---")
    st.header("Homologación")
    st.write("##")
    image_c, text_c=st.columns((1, 2))
    with image_c:
        st.image(img_contact_form)
    with text_c:
        st.subheader("Homologacion de Oficio")
        st.write(
            """
            para esta caso de los equipos no requieren de homoogacion
            """
            )
        st.markdown("[mas informacion ...](http://localhost:8501/)")
with st.container():
    image_c, text_c=st.columns((1, 2))
    with image_c:
        st.image(img_lottie_animation)
    with text_c:
        st.subheader("Homologacion de Oficio")
        st.write(
            """
            para esta caso de los equipos no requieren de homoogacion
            """
            )
        st.markdown("[mas informacion ...](http://localhost:8501/)")

#----- Contact ------
with st.container():
    st.write("---")
    st.header("contactame...")
    st.write("##")


    contact_form = """
    <form action="https://formsubmit.co/barriosmunozrn1a@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Nombre" required>
     <input type="email" name="email" placeholder="correo" required>
     <textarea name="mensaje"  placeholder="Escribe tu mensaje" required><\textarea>
     <button type="submit">Send</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
