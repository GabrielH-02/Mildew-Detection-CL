import streamlit as st

def page_project_hypothesis_body():
    st.write("## Project Hypothesis and Validation")

    st.write(f"### Hypothesis")
    st.info(
        f"* We suspect that cherry leaves infected with powdery mildew have distinct visual characteristics, "
        f"such as a white powdery appearance, that differentiate them from healthy leaves.\n"
        f"* An Image Montage indicates that infected leaves typically display a white, powdery surface. "
        f"Studies involving Average Image, Variability Image, and Difference between Averages analyses "
        f"are expected to reveal distinguishing patterns that differentiate healthy leaves from those affected by powdery mildew."

    )

    st.write(f"### Validation")
    st.success(
        f"* The outcome of the project, and the validation of the whole project"
    )

    st.write(f"### Observations")
    st.success(
        f"* The findings of the project"
    )