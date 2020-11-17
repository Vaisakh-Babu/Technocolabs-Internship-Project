import streamlit as st
import pickle
import numpy as np
model = pickle.load(open('model.pkl','rb'))


def predict_rf(LIMIT_BAL,EDUCATION,MARRIAGE,AGE, PAY_1, BILL_AMT1, BILL_AMT2, BILL_AMT3, BILL_AMT4, BILL_AMT5, BILL_AMT6, PAY_AMT1, PAY_AMT2, PAY_AMT3, PAY_AMT4, PAY_AMT5, PAY_AMT6):
    input=np.array([[LIMIT_BAL,EDUCATION,MARRIAGE,AGE, PAY_1, BILL_AMT1, BILL_AMT2, BILL_AMT3, BILL_AMT4, BILL_AMT5, BILL_AMT6, PAY_AMT1, PAY_AMT2, PAY_AMT3, PAY_AMT4, PAY_AMT5, PAY_AMT6]])
    pred=model.predict(input)
    return (pred)
def main():
    st.title("Credit Card Default Prediction")
    html_temp = """
    <div>
        <h2>Parameters</h2>
    </div>
    """
        
    st.markdown(html_temp,unsafe_allow_html=True)
    
    LIMIT_BAL  = st.text_input("LIMIT_BAL","Type Here")
    EDUCATION  = st.text_input("EDUCATION","Type Here")
    MARRIAGE   = st.text_input("MARRIAGE","Type Here")
    AGE        = st.text_input("AGE","Type Here")
    PAY_1      = st.text_input("PAY_1","Type Here")
    BILL_AMT1  = st.text_input("BILL_AMT1","Type Here")
    BILL_AMT2  = st.text_input("BILL_AMT2","Type Here")
    BILL_AMT3  = st.text_input("BILL_AMT3","Type Here")
    BILL_AMT4  = st.text_input("BILL_AMT4","Type Here")
    BILL_AMT5  = st.text_input("BILL_AMT5","Type Here")
    BILL_AMT6  = st.text_input("BILL_AMT6","Type Here")
    PAY_AMT1   = st.text_input("PAY_AMT1","Type Here")
    PAY_AMT2   = st.text_input("PAY_AMT2","Type Here")
    PAY_AMT3   = st.text_input("PAY_AMT3","Type Here")
    PAY_AMT4   = st.text_input("PAY_AMT4","Type Here")
    PAY_AMT5   = st.text_input("PAY_AMT5","Type Here")
    PAY_AMT6   = st.text_input("PAY_AMT6","Type Here")
    
    pos = """
    <div style="background-color:#F4D03F" ;padding:10px>
        <h2>Default</h2>
    </div>
    """
    
    neg = """
    <div style="background-color:#F08080" ;padding:10px>
        <h2>Not Default</h2>
    </div>
    """
    
    if st.button("Predict"):
        output = predict_rf(LIMIT_BAL,EDUCATION,MARRIAGE,AGE, PAY_1, BILL_AMT1, BILL_AMT2, BILL_AMT3, BILL_AMT4, BILL_AMT5, BILL_AMT6, PAY_AMT1, PAY_AMT2, PAY_AMT3, PAY_AMT4, PAY_AMT5, PAY_AMT6)
        st.success('_-_-_')
        if output == 1:
            st.markdown(pos,unsafe_allow_html=True)
        else:
            st.markdown(neg,unsafe_allow_html=True)
if __name__=='__main__':
    main()
