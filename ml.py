import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

X = None
y = None

@st.cache_data
def get_data(filename):
    heart_disease = pd.read_csv("./Data/heart-disease.csv")
    return heart_disease

with header:
    st.header("Welcome to my data science project", divider="rainbow")

with dataset:
    st.header("Heart Disease dataset", divider='blue')

    heart_disease = get_data("./Data/heart-disease.csv")
    st.write(heart_disease.head())

    X = heart_disease.drop('target', axis=1)
    y = heart_disease['target']

    st.subheader("Chol distribution on Heart Disease dataset")
    chol_dist = (heart_disease['chol'].value_counts()).head(50)
    st.bar_chart(chol_dist)

with features:
    st.header("These are the features of NYC data", divider="blue")

    st.write(X.dtypes)


with model_training:
    st.header("Training the model now!", divider="blue")
    st.text("Choose the hyperparameters of the model and see how the performance change!")

    sel_col, dis_col = st.columns(2)

    with sel_col:

        max_depth = st.slider("what should be the max_depth of the model", min_value=10, max_value=100, value=20)

        n_estimators = st.selectbox("How many trees should be there", options=[100,200,300,'No limit'])

        # input_features = sel_col.text_input("which feature(s) should be used as the input feature?", value='PULocationID')
        input_features = st.multiselect("which feature(s) should be used as the input feature?", options=list(X))

        if n_estimators == 'No limit':
            clf = RandomForestClassifier(max_depth=max_depth)
        else:
            clf = RandomForestClassifier(n_estimators=n_estimators,
                                        max_depth=max_depth)
        
        if input_features:
            X_selected = heart_disease[input_features]

            clf.fit(X_selected, y)

            y_preds = clf.predict(X_selected)

            with dis_col:
                st.subheader("Mean absolute error of the model is: ")
                st.write(mean_absolute_error(y, y_pred=y_preds))
                        
                st.subheader("Mean squared error of the model is:")
                st.write(mean_squared_error(y, y_pred=y_preds))

                st.subheader("R squared score of the model is:")
                st.write(r2_score(y_true=y, y_pred=y_preds))
