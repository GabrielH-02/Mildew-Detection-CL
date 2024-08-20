import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread

import itertools
import random


def page_leaf_observations_body():
    
    st.write("## Cherry Leaf Observations")
    st.write("---")
    
    st.info(
        f"This page allows you to delve into the dataset of Cherry Leaf images, " 
        f"where you can visually explore and analyze the differences between "
        f"**Healthy** Leaf images and those which have been infected by **Powdery Mildew.**"
        )
    
    st.success(
        f"The main objective of this page is to answer **Business Requiremnet 01**;\n"
        f"* **The client is interested in conducting a study to visually "
        f"differentiate a cherry leaf that is healthy from one that contains powdery mildew.**\n"
        )
    st.write("---")
    
    version = 'v1'

    # Checkbox 01 - Difference between Average and Variability Image
    if st.checkbox("Compare the average and variability of leaf images"):
      
      avg_powdery_mildew = plt.imread(f"outputs/{version}/avg_var_powdery_mildew.png")
      avg_healthy = plt.imread(f"outputs/{version}/avg_var_healthy.png")
      
      st.warning(
        f"* We observed that the average and variability images did not reveal clear patterns. "
        f"However, there is a slight difference in the colour pigmentation of the average images between the two labels."
        )

      st.image(avg_powdery_mildew , caption='Powdery-Mildew Leaf - Average and Variability')
      st.image(avg_healthy, caption='Healthy Leaf - Average and Variability')
      
      st.write("---")

    # Checkbox 02 - Differences between average Powdery-Mildew and average Healthy Images
    if st.checkbox("Examine the differences between the average images of Powdery Mildew and Healthy Leaves"):
          
          diff_avgs = plt.imread(f"outputs/{version}/avg_diff.png")

          st.warning(
            f"* While there are slight differences between the average images, "
            f"the study did not reveal clear patterns."
            )
          
          st.image(diff_avgs, caption='Difference between average images')
          
          st.write("---")

    # Checkbox 03 - Image Montage
    if st.checkbox("Display Image Montage of Healthy and Powdery Mildew Cherry Leaves"): 
      
      st.warning("Choose a label (Healthy or Powdery-Mildew) and click 'Create Leaf Montage' to generate a visual comparison.")
      
      data_dir = 'inputs/cherry_leaves_dataset/cherry-leaves'
      labels = os.listdir(data_dir+ '/validation')
      label_to_display = st.selectbox(label="Select label", options=labels, index=0)

      if st.button("Create Leaf Montage"):
            try:
                image_montage(dir_path=data_dir + '/validation',
                              label_to_display=label_to_display,
                              nrows=8, ncols=3, figsize=(10, 25))
            except Exception as e:
                st.error(f"Error: {e}")
      
      st.write("---")



def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15,10)):
  sns.set_style("white")
  labels = os.listdir(dir_path)

  if label_to_display in labels:

    images_list = os.listdir(dir_path+'/'+ label_to_display)
    
    if nrows * ncols < len(images_list):
      img_idx = random.sample(images_list, nrows * ncols)
    else:
        st.warning(
            f"Reduce the number of rows or columns to create your montage. \n"
            f"There are {len(images_list)} images in your subset, but you've requested a montage with {nrows * ncols} spaces."
            )
        return
    
    list_rows= range(0,nrows)
    list_cols= range(0,ncols)
    plot_idx = list(itertools.product(list_rows,list_cols))

    fig, axes = plt.subplots(nrows=nrows,ncols=ncols, figsize=figsize)
    for x in range(0,nrows*ncols):
      img = imread(dir_path + '/' + label_to_display + '/' + img_idx[x])
      axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
      axes[plot_idx[x][0], plot_idx[x][1]]
      axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
      axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
    plt.tight_layout()
    
    st.pyplot(fig=fig)

  else:
    print("The label you selected doesn't exist.")
    print(f"The existing options are: {labels}")
      