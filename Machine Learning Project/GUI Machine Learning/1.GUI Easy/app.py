import streamlit as st
import joblib

def main():
    
    # st.markdown(unsafe_allow_html=True)


    model = joblib.load('model_joblib_test')
    p1=st.slider("Enter Your Age",18,100)
    
    s1=st.selectbox("Sex",("Male","Female"))
    
    if s1=="Male":
        p2=1
    else:
        p2=0
    
    p3=st.number_input("Enter Your BMI Value")
    
    p4=st.slider("Number of your children",0,4)
    s2=st.selectbox("Smoker",("Yes","No"))
    
    if s2=="Yes":
        p5=1
    else:
        p5=0
    
    p6=st.slider("Enter Your Region [1-4]",1,4)
    
    if st.button('Predict'):
        prediction = model.predict([[p1,p2,p3,p4,p5,p6]])
        
        
        st.success("Insurance Amount is {}".format(round(prediction[0],2)))
         
    
if __name__== '__main__':
    main()
