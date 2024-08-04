import streamlit as st

def page_project_summary_body():
    st.write("### Project Summary")

    st.info(
        f"**General Information**\n"
        
        f"* Powdery mildew is a fungal disease affecting the cherry plantations at Farmy & Foods, "
        f"posing a threat to the quality of their produce.\n"
        f"* The current process involves manually inspecting each cherry tree by visually examining leaf samples. "
        f"An employee spends around 30 minutes per tree for inspection and an additional minute if treatment is needed.\n"
        f"* Due to the extensive number of cherry trees across multiple farms, this manual inspection process is not scalable.\n\n"
        
        f"* Thus the IT team suggests implementing a machine learning system using a neural network model to accurately classify " 
        f"images of cherry leaves as either healthy or infected with powdery mildew.\n\n"
    )
    
    st.write(
        f"* For additional information about the project, please visit and **read** the "
        f"[Project README file](https://github.com/GabrielH-02/Mildew-Detection-CL)."
    )

    st.warning(
        f"* The dataset comprises images of cherry leaves collected from Farmy & Foods' crops. "
        f"It can be accessed on [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves)."
    )

    st.success(
        f"The project has **2 business requirements**:\n"
        f"* 1 - The client is interested in conducting a study to visually "
        f"differentiate a cherry leaf that is healthy from one that contains powdery mildew.\n"
        f"* 2 - The client is interested in predicting if a cherry tree is healthy or contains powdery mildew."
    )

