import streamlit as st

def page_project_hypothesis_body():
    st.write("## Project Hypothesis and Validation")

    st.write("### Hypothesis")
    st.info(
        f"* We hypothesize that cherry leaves infected with powdery mildew exhibit distinct visual characteristics, such as a white powdery appearance, that set them apart from healthy leaves. "
        f"The project is based on the assumption that these visual differences can be effectively captured and analyzed to differentiate between healthy and infected leaves.\n"
        f"* The analysis includes an Image Montage, which suggests that infected leaves generally display a white, powdery surface. Studies involving Average Image, Variability Image, and Difference between Averages analyses "
        f"are expected to uncover patterns that clearly distinguish healthy leaves from those affected by powdery mildew."
    )

    st.write("### Validation")
    st.success(
        f"* The validation process involves comparing the visual characteristics of healthy and infected cherry leaves to verify the hypothesis. "
        f"This includes using image analysis techniques to confirm the presence of the distinct white powdery surface on infected leaves.\n"
        f"* Furthermore, the machine learning model's performance is assessed to ensure it accurately predicts whether a cherry leaf is healthy or infected with powdery mildew. The model's accuracy, based on test set evaluations, "
        f"provides a quantitative measure of its effectiveness in differentiating between healthy and infected leaves. This process ensures that the project meets its objectives and the client's requirements for reliable mildew detection."
    )
