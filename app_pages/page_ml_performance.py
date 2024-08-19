import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation

def page_ml_performance_metrics():
    st.write("## Mildew Detector; ML Performance Metrics")
    
    st.write("---")

    st.info(
        f"This page is dedicated to providing insights into the performance of the machine learning model used for detecting powdery mildew in cherry leaves. "
        f"Here, you can explore the model's evaluation metrics, including accuracy, losses, and other key performance indicators. "
        f"The goal is to give the client a clear understanding of how the model performs, ensuring transparency and confidence in its predictions."
        )

    st.success(
        f"The main objective of this page is an extention of **Business Requiremnet 02**;\n"
        f"* **The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.**\n"
        f"* This page is dedicated to demonstrating the performance level of the predictive model."
        )
    st.write("---")
    
    version = 'v2'

    st.write("### Train, Validation and Test Set: Labels Frequencies")

    labels_distribution = plt.imread(f"outputs/{version}/labels_distribution.png")
    st.image(labels_distribution, caption='Labels Distribution on Train, Validation and Test Sets')
    st.write("---")


    st.write("### Model History")
    col1, col2 = st.beta_columns(2)
    with col1: 
        model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
        st.image(model_acc, caption='Model Training Accuracy')
    with col2:
        model_loss = plt.imread(f"outputs/{version}/model_training_losses.png")
        st.image(model_loss, caption='Model Training Losses')
    st.write("---")

    st.write("### Generalised Performance on Test Set")
    st.dataframe(pd.DataFrame(load_test_evaluation(version), index=['Loss', 'Accuracy']))

    st.success(
        f"The machine learning model has achieved an overall accuracy rate of **100%** "
    )

    st.write("---")
    
    st.warning(
        f"For further information about the project and the performance of the predictive model, please navigate to the [README file](https://github.com/GabrielH-02/Mildew-Detection-CL)."
        )