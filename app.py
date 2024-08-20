import streamlit as st

from app_pages.multipage import MultiPage
from app_pages.page_project_summary import page_project_summary_body
from app_pages.page_leaf_observations import page_leaf_observations_body
from app_pages.page_mildew_detector import page_mildew_detector_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_ml_performance import page_ml_performance_metrics


app = MultiPage(app_name="Cherry Leaf : Mildew Detector")  

app.add_page("Project Summary", page_project_summary_body)
app.add_page("Cherry Leaf Observations", page_leaf_observations_body)
app.add_page("Mildew Detection", page_mildew_detector_body)
app.add_page("Project Hypothesis and Validation", page_project_hypothesis_body)
app.add_page("ML Performance Metrics", page_ml_performance_metrics)

app.run()