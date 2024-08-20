import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (
                                                    load_model_and_predict,
                                                    resize_input_image,
                                                    plot_predictions_probabilities
                                                    )

def page_mildew_detector_body():

    st.write("## Mildew Detector")
    
    st.write("---")

    st.info(
        f"This page provides an interactive interface for evaluating cherry leaf images. "
        f"You can upload your own cherry leaf images to test whether they are infected with powdery mildew or if they are healthy. "
        f"Use this tool to explore the model's predictions and assess the health of cherry leaves based on your uploaded images."
        )

    st.success(
        f"The main objective of this page is to answer **Business Requiremnet 02**;\n"
        f"* **The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.**\n"
        )
    st.write("---")

    st.warning(
        f"Download a selection of cherry leaf images, either infected with powdery mildew or healthy, for live prediction.\n"
        f"* You can download the images from [here](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves?select=cherry-leaves)."
        )

    st.write("---")

    st.error(f"Please upload a **PNG file** that is decent size for a clear reading")

    images_buffer = st.file_uploader(
        'Upload Cherry Leaf Images. You may select more than one.',
        type='png',
        accept_multiple_files=True
    )
   
    if images_buffer:
        df_report = pd.DataFrame([])
        for image in images_buffer:

            try:
                img_pil = Image.open(image)
                st.info(f"Cherry Leaf Image: **{image.name}**")
                img_array = np.array(img_pil)
                st.image(img_pil, caption=f"Image Size: {img_array.shape[1]}px width x {img_array.shape[0]}px height")

                version = 'v2'
                resized_img = resize_input_image(img=img_pil, version=version)
                pred_proba, pred_class = load_model_and_predict(resized_img, version=version)
                plot_predictions_probabilities(pred_proba, pred_class)

                df_report = df_report.append({"Name": image.name, 'Prediction': pred_class},
                                            ignore_index=True)
            
            except Exception as e:
                st.error(f"Error predicting this image '{image.name}': {e}")
        
        if not df_report.empty:
            st.success("Prediction Report")
            st.table(df_report)
            st.markdown(download_dataframe_as_csv(df_report), unsafe_allow_html=True)
