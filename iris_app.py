import pickle
import streamlit as st
from sklearn.tree import DecisionTreeClassifier
with open('iris_classifier.pickle','rb') as f:
    clf = pickle.load(f)


def main():
    st.title('Iris-Species-classifier')
    sl = st.number_input("SepalLenght")
    sw = st.number_input("SepalWidth")
    pl = st.number_input("PetalLength")
    pw = st.number_input("PetalWidth")
    if st.button("Predict"):
        result = clf.predict([[sl,sw,pl,pw]])
        if(result==0):
            st.success("Setosa")
        elif(result==1):
            st.success("Versicolor")
        else:
            st.success("Virginca")
if __name__=='__main__':
    main()