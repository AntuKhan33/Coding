import streamlit as st

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

import scikitplot as skplt
from joblib import dump, load
import matplotlib.pyplot as plt

categories = ['alt.atheism', 'comp.graphics', 'rec.autos', 'sci.electronics', 'talk.politics.guns',]


@st.experimental_memo
def load_and_vectorize_dataset():
    ## Load Dataset
    news_groups = datasets.fetch_20newsgroups(categories=categories)
    X_train, X_test, Y_train, Y_test = train_test_split(news_groups.data, news_groups.target, train_size=0.8, random_state=123)

    ## Vectorize Data
    vectorizer = CountVectorizer(max_features=50_000)
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)
    
    return X_train_vec, X_test_vec, Y_train, Y_test
X_train_vec, X_test_vec, Y_train, Y_test = load_and_vectorize_dataset()

def train_model(n_estimators, max_depth, max_features, bootstrap):
    rf_classif = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, max_features=max_features, bootstrap=bootstrap)
    rf_classif.fit(X_train_vec, Y_train)
    return rf_classif


#Dashboard
st.title("Random Forest  :tea: :coffee:")
st.markdown("Try different values of random forest classifier. Select widget values and submit model for training. Various ML metrics will be displayed after training.")

with st.form("train_model"):
    col1, col2,col3 = st.columns(3, gap="medium")

    with col1:
        n_estimators=st.slider("No of Estimators:",min_value=100,max_value=1000)
        max_depth=st.slider("Max Depth:",min_value=2,max_value=20)
        max_features=st.selectbox("Max  Features:",options=["sqrt",'log2',None])
        bootstrap = st.checkbox("Bootstrap")
        save_model = st.checkbox("Save Model")
        
        submitted=st.form_submit_button("Train")
        
    if submitted:
        rf_classif=train_model(n_estimators,max_depth,max_features,bootstrap)
        if save_model:
            dump(rf_classif,'rf_classif.dat')
            
        Y_test_preds=rf_classif.predict(X_test_vec)
        Y_train_preds=rf_classif.predict(X_train_vec)
        Y_test_probs=rf_classif.predict_proba(X_test_vec)
        
        
           
        with col2:
                 
            st.metric("Train Accuracy", value="{:.2f} %".format(100*accuracy_score(Y_train, Y_train_preds)))
                    
                
            st.metric("Test Accuracy", value="{:.2f} %".format(100*accuracy_score(Y_test, Y_test_preds)))
            st.markdown("### Confusion Matrix")
            conf_mat_fig = plt.figure(figsize=(6,6))
            ax1 = conf_mat_fig.add_subplot(111)
            skplt.metrics.plot_confusion_matrix(Y_test, Y_test_preds, ax=ax1)
            st.pyplot(conf_mat_fig, use_container_width=True)
            st.markdown("### Classification Report:")
        st.code("=="+classification_report(Y_test, Y_test_preds, target_names=categories))

        with col3:
            st.markdown("### ROC & Precision-Recall Curves") 
            roc_fig = plt.figure(figsize=(6,6))
            ax1 = roc_fig.add_subplot(111)
            skplt.metrics.plot_roc(Y_test, Y_test_probs, ax=ax1)
            st.pyplot(roc_fig, use_container_width=True)


            pr_fig = plt.figure(figsize=(6,6))
            ax1 = pr_fig.add_subplot(111)
            skplt.metrics.plot_precision_recall(Y_test, Y_test_probs, ax=ax1)
            st.pyplot(pr_fig, use_container_width=True)

        