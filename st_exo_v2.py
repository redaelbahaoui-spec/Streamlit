import streamlit as st
import pandas as pd
import pickle
st.title("MSDE7 - Streamlit Exercise")
st.image("https://www.ehtp.ac.ma/wp-content/uploads/2022/03/logo2@2x-600x139.png", caption="EHTP", width=400)
#st.selectbox('How would you like to use the prediction model ? ', ['','Input Parametres directly', 'Load a file of data']) 


choice = st.selectbox(
    'How would you like to use the prediction model ? ',
    ['', 'Input Parametres directly', 'Load a file of data']
)
if choice == 'Input Parametres directly':
    st.sidebar.title("Input Parametres")

    st.sidebar.subheader("Parametres")
    lenght = st.sidebar.slider('Sepal Length', 4.00, 8.00)
    width = st.sidebar.slider('Sepal Width', 2.00, 5.00)
    petal_length = st.sidebar.slider('Petal Length', 1.00, 7.00)
    petal_width = st.sidebar.slider('Petal Width', 0.10, 3.00)
    st.subheader("User Input Parametres :")
    df = pd.DataFrame([{
    "sepal_length": lenght,
    "sepal_width": width,
    "petal_length": petal_length,
    "petal_width": petal_width
}])
    
    st.write(df)
    st.subheader("Class labels and their corresponding index numbers :")
    df_p = pd.DataFrame(["Setosa", "Versicolor", "Virginica"], index=["0", "1", "2"], columns=["0"])
    st.write(df_p)
    model = pickle.load(open(r"C:\Users\Reda\Desktop\10_Labs_deploiement\Streamlit\app solution\modeliris6.pkl", "rb"))
    pred = model.predict(df)
    st.subheader("Predicted :")  
    st.write(pred)
elif choice == 'Load a file of data':
    st.subheader("Load a File of Data")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file,header=None)
        st.write(df)


