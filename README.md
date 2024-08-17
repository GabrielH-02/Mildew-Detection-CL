# **Mildrew Detection:** Cherry Leaves

## 1.0 - Dataset Content

- The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). This dataset was provided by Code Institute. 
- The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

## 2.0 - Business Requirements

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

- 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
- 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

## 3.0 - Hypothesis and Validation

### 3.1 - Hypothesis

We suspect that cherry leaves infected with powdery mildew have distinct visual characteristics, such as a white powdery appearance, that differentiate them from healthy leaves.

### 3.2 - How to Validate?

- By applying a study showing how to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.
- As well as the capability to predict if a cherry leaf is healthy or contains powdery mildew.

An Image Montage indicates that infected leaves typically display a white, powdery surface. Studies involving Average Image, Variability Image, and Difference between Averages analyses
are expected to reveal distinguishing patterns that differentiate healthy leaves from those affected by powdery mildew.

## 4.0 - The rationale to map the business requirements to the Data Visualisations and ML tasks

### 4.1 - Business Requirements Rationales 

**Business Requirement 1:** The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.

This requirement is focused on visual analysis, involving the creation of various data visualisations. Tasks include data collection, image analysis, and generating visual representations to help the client observe differences between healthy and infected leaves. Therefore this requirement can be labelled as **Data Visualization**.

**Business Requirement 2:** The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

This requirement targets predictive modelling, which involves machine learning. Tasks related to this include developing and training a classification model, optimising it for accuracy, and validating its performance to ensure accurate predictions as per the client's needs. Therefore this requirement can be labelled as **Classification**.

### 4.2 - Epics and Tasks

As a collective of these two objectives, the project can be broken down into five different epics, which are listed below with an addition of tasks which need to be done for each epic.

#### 4.2.1 - Information Gathering and Data Collection

This epic focuses on understanding the client's needs and gathering the necessary data, including all cherry leaf images. It is primarily aimed at addressing **Data Visualization**.

- **Task 1:** Collect cherry leaf images from the appropriate dataset on Kaggle.

#### 4.2.2 - Data Visualization, Cleaning, and Preparation

This epic deals with processing the gathered data to ensure it is properly prepared for effective modelling. It is also focused on **Data Visualization**.

- **Task 2:** Analyze the data to ensure each image is the same size. Split the dataset into training, testing, and validation sets.
- **Task 3:** Create visual data representations for the client, including average images, variability images, and image montages (for both healthy and infected leaves). Completing this task will satisfy **Business Requirement 1**.

#### 4.2.3 - Model Training, Optimization, and Validation

This epic is concerned with the model, ensuring it meets the necessary standards and can classify whether a leaf image is infected with powdery mildew. It is focused on the **Classification** objective.

- **Task 4:** Develop and train a classification neural network on the provided dataset. Optimise the model to achieve a minimum accuracy of at least 97%.
- **Task 5:** Validate the model and analyse its performance, ensuring it meets the client's goals and requirements.

#### 4.2.4 - Dashboard Planning, Design, and Development

This epic addresses how the observations and predictive interface will be presented to the client, with a focus on both **Data Visualization** and **Classification**. It leans more towards Data Visualization but also includes the creation of an interface for leaf health prediction.

- **Task 6:** Design and develop a dashboard using Streamlit, meeting the client's requirements. The dashboard should include a project summary, hypothesis, machine learning performance metrics, leaf observations, and an interactive predictive interface for testing. It should fulfil both business requirements and be sufficiently interactive.

#### 4.2.5 - Dashboard Deployment and Release

This epic focuses on the deployment and execution of the project, ensuring that the client can access the information securely, according to the NDA. It addresses both **Data Visualization** and **Classification**.

- **Task 7:** Deploy the dashboard to an appropriate hosting platform (such as Heroku) so that the client can access the project. Ensure that access to the dashboard is restricted to the client, in compliance with the NDA.


## 5.0 - ML Business Case

### 5.1 - Business Objectives

Farmy & Foods aims to enhance the quality assurance process of their cherry plantations by addressing the challenge of powdery mildew found on the cherry leaves, which affects their crops. As established, there are two business requirements; however, here are the key business objectives for this machine learning (ML) project:

1. **Automate Mildew Detection**: Reduce dependency on manual labour for inspecting cherry leaves by implementing an automated solution that uses machine learning to detect powdery mildew.

2. **Improve Crop Quality**: Ensure that only healthy, mildew-free cherries reach the market, thereby maintaining the brand's reputation for quality and reducing the risk of customer dissatisfaction.

3. **Optimise Operational Efficiency**: Streamline the inspection process across multiple farms, saving time and resources while improving scalability.

### 5.2 - Business Benefits

Based on meeting the Business Objectives, the successful implementation of this ML project is expected to deliver the following business benefits:

1. **Increased Productivity**: Automating the inspection process will allow Farmy & Foods to monitor more trees in less time, freeing up employees to focus on other critical tasks.

2. **Cost Reduction**: By reducing the need for extensive manual inspections and minimising crop loss due to undetected mildew, the company will achieve significant cost savings.

3. **Enhanced Decision-Making**: The data-driven approach will provide actionable insights, allowing Farmy & Foods to make informed decisions about crop management and mildew prevention.

4. **Market Differentiation**: Ensuring that only the highest-quality produce reaches the market will strengthen the company’s position as a premium brand, enhancing customer trust and loyalty.

### 5.3 - Business Risks and Mitigation

#### Risk 1: Model Accuracy and Reliability
- **Risk**: The ML model may not achieve the desired level of accuracy (97%), leading to incorrect classifications of cherry leaves and potential crop losses.

- **Mitigation**: To mitigate this risk, rigorous model validation and tuning will be undertaken, including cross-validation and testing on unseen data. The model will only be deployed once it consistently meets or exceeds the 97% accuracy threshold.

#### Risk 2: Resistance to Technological Change
- **Risk**: Employees may resist adopting the new technology due to unfamiliarity with machine learning and fear of job displacement.

- **Mitigation**: Comprehensive training programmes and workshops will be provided to ensure employees are comfortable using the new system. Emphasising the role of technology in augmenting rather than replacing human labour will help ease the transition.

#### Risk 3: Data Privacy and Security
- **Risk**: The data provided by the client is under an NDA (Non-Disclosure Agreement), which imposes strict limitations on data sharing and usage.

- **Mitigation**: Access to the data will be restricted to authorised personnel only. All project participants will be briefed on the NDA terms, and data handling protocols will be established to ensure compliance with the agreement.

#### Risk 4: Model Deployment and Integration
- **Risk**: The model’s large size, due to high-resolution images, may complicate deployment and integration into existing systems.

- **Mitigation**: Image resolution will be adjusted to balance model performance and size. Additionally, Git LFS (Large File Storage) will be used for managing large files, ensuring smooth integration and deployment.

### 5.4 - Conclusion

The proposed ML solution for detecting powdery mildew in cherry leaves represents a strategic investment in Farmy & Foods’ operational efficiency and product quality. By achieving automation in mildew detection, the company stands to gain significant competitive advantages, including cost savings, improved productivity, and enhanced market reputation. Careful consideration of risks and their mitigation will ensure the project’s success, delivering long-term value to the business.


## 6.0 - Dashboard Design 

### 6.1 - Page 1: Project Summary

This page is divided into four sections that collectively provide a comprehensive introduction to the project, giving the user an overview and insight into the project's objectives and requirements. The sections are as follows:

- **General Information**
    - Powdery mildew is a fungal disease affecting the cherry plantations at Farmy & Foods, posing a threat to the quality of their produce.
    - The current process involves manually inspecting each cherry tree by visually examining leaf samples. An employee spends around 30 minutes per tree for inspection and an additional minute if treatment is needed.
    - Due to the extensive number of cherry trees across multiple farms, this manual inspection process is not scalable.
    - The IT team suggests implementing a machine learning system using a neural network model to accurately classify images of cherry leaves as either healthy or infected with powdery mildew.

- **Additional Information**
    - This section provides a brief explanation of where to find more detailed information about the project.
    - [Click here to view the README file](https://github.com/GabrielH-02/Mildew-Detection-CL).

- **Project Dataset**
    - The dataset consists of over 4,000 images from the client's crop fields, depicting both healthy cherry leaves and those affected by powdery mildew.  
    - It can be accessed on [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves).

- **Business Requirements**
    - The project has **two business requirements**:
        1. The client wants to understand how to visually differentiate a healthy cherry leaf from one infected with powdery mildew.
        2. The client is interested in predicting whether a cherry tree is healthy or infected with powdery mildew.

### 6.2 - Page 2: Leaf Observations

This page consists of three sections that provide insights into the visualization and analysis aspects of the project. Its main purpose is to visually demonstrate the differences between a healthy leaf and one infected with powdery mildew, addressing **Business Requirement 1**. The sections are:

- **Business Requirement**
    - The client seeks to study how to visually differentiate a healthy cherry leaf from one infected with powdery mildew.

- **Checkbox 01**
    - Visuals comparing healthy and infected cherry leaves, highlighting the visual differences between them.

- **Checkbox 02**
    - An image montage displaying both healthy cherry leaves and mildew-infected cherry leaves.

### 6.3 - Page 3: Mildew Detector

This page contains three sections that together provide user interaction and a predictive interface to assess the health status of cherry leaves. The primary purpose of this page is to determine whether a cherry leaf is healthy or infected with powdery mildew, thereby addressing **Business Requirement 2**. The sections are:

- **Business Requirement**
    - The client is interested in predicting whether a cherry leaf is healthy or infected with powdery mildew.

- **Dataset Download**
    - A link to download a set of mildew-infected cherry leaf images and healthy cherry leaf images for live prediction.

- **Predictive Interface**
    - A file uploader widget allowing users to upload multiple cherry leaf images.
    - Upon uploading, the image will be displayed along with a prediction statement indicating whether the leaf is infected with powdery mildew or healthy, along with the associated probability.
    - A table showing the image name and prediction results.
    - A download button to export the results table.

### 6.4 - Page 4: Hypothesis and Validation

This page consists of two sections that present the project’s hypothesis and validate the project's findings. Additionally, it provides statements to simplify observations. The sections are:

- **Hypothesis**
    - We suspect that cherry leaves infected with powdery mildew have distinct visual characteristics, such as a white powdery appearance, that differentiate them from healthy leaves.
    - An image montage suggests that infected leaves typically show a white, powdery surface. Studies involving average image analysis, variability analysis, and differences between averages are expected to reveal patterns that distinguish healthy leaves from those affected by powdery mildew.

- **Validation**
    - This section clearly explains how the project was validated in alignment with the client's requirements and guidelines.

### 6.5 - Page 5: ML Performance Metrics

This page is divided into two sections that provide informative and insightful perspectives on the machine learning model’s performance. The sections are:

- **Metrics of Model Training and Evaluation**
    - Details of the performance metrics used during the model's training and evaluation phases.

- **Visuals of Model Performance and Accuracy**
    - Graphical representations of the model's performance and accuracy, providing a visual understanding of the results.



## 7.0 - Unfixed Bugs

<!-- - You will need to mention unfixed bugs and why they were unfixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable for consideration, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed. -->

## 8.0 - Deployment

### Heroku

- The App live link is: ``
- Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large, then add large files not required for the app to the .slugignore file.

## 9.0 - Main Data Analysis and Machine Learning Libraries

- **Numpy**: This library is essential for numerical computing in Python. In the mildew detection project, NumPy is used to handle arrays, perform mathematical operations on image data, and manage the underlying data structures that support the machine learning models used to classify cherry leaves.

- **Pandas**: Pandas is crucial for data manipulation and analysis. In this project, Pandas is employed to organise, clean, and preprocess the cherry leaf dataset, which includes images labeled as healthy or infected with powdery mildew. This ensures the data is in the right format before being fed into the machine learning models.

- **Matplotlib & Seaborn**: These libraries are used for creating visualisations to better understand the dataset and the model's performance. In the context of mildew detection, Matplotlib and Seaborn are used to generate visual comparisons between healthy and mildew-infected cherry leaves, as well as to plot model accuracy, loss curves, and other key metrics that inform the effectiveness of the detection system.

- **Scikit-learn**: Scikit-learn plays a key role in the machine learning pipeline for this project. It is used to split the cherry leaf dataset into training and testing sets, evaluate model performance, and apply cross-validation techniques to ensure the model reliably distinguishes between healthy and infected leaves.

- **TensorFlow & Keras**: TensorFlow, with its Keras API, is used to build and train the neural network that powers the mildew detection system. In this project, TensorFlow and Keras enable the development of a deep learning model that can accurately classify images of cherry leaves as either healthy or infected with powdery mildew, meeting the project's objective of automating the detection process.

## 10.0 - Credits

<!-- - In this section, you need to reference where you got your content, media and from where you got extra help. It is common practice to use code from other repositories and tutorials. However, it is necessary to be very specific about these sources to avoid plagiarism.
- You can break the credits section up into Content and Media, depending on what you have included in your project. -->

### 10.1 - Content

<!-- - The text for the Home page was taken from Wikipedia Article A.
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https-//www.youtube.com/).
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/). -->

### 10.2 - Acknowledgements (optional)

<!-- - Thank the people who provided support throughout this project. -->
