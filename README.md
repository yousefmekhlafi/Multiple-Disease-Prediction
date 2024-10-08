# End-to-End Multiple Machine Learning Algorithm Application for Predicting 3 Diseases

 PROJECT STATUS: Malfunctioning. app.py is being debugged, you can still check the code and run the pipeline from main.py 
 
 GUIDED: Yes  

# DISCLAIMERS
Coded along Sidhardhan YT channel 
1. Diabetes link: https://www.youtube.com/watch?v=xUE7SjVx9bQ&list=PLfFghEzKVmjuhQwKhYXvdU94GSU-6Jcjr&index=4&pp=iAQB
2. Heart Disease link: https://www.youtube.com/watch?v=qmqCYC-MBQo&list=PLfFghEzKVmjuhQwKhYXvdU94GSU-6Jcjr&index=5&pp=iAQB
3. Parkinson's link: https://www.youtube.com/watch?v=HbyN_ey-JVc&list=PLfFghEzKVmjuhQwKhYXvdU94GSU-6Jcjr&index=6&pp=iAQB
4. Streamlit deployment link: https://www.youtube.com/watch?v=8Q_QQVQ1HZA&list=PLfFghEzKVmjuhQwKhYXvdU94GSU-6Jcjr&index=1&pp=iAQB


# Project Scopes and Goals: 

Scope of simple deployment Guided with Siddhardhan's YT channel: 

1. Learn ML classification on different datasets with jupyter notebook experiments conducted separately
2. Saved models are used to deploy said experiments in a Streamlit app locally


Personal effort scope: 

1. Leveraging ChatGPT to learn how to convert the jupyter notebook ML experiments and streamlit app into an end-to-end modular coding, pipeline-oriented application
2. Get an idea on how multiple algorithms work in an end-to-end production grade workflow
3. Reverse engineer the entire project's methods to develop other multiple-algorithm applications in the future 
4. Breaking experiments down to ingestion, validation, transformation (missing and is probably cause of the bug), model training and model evaluation pipelines
5. Learning how to create a multiple algorithm prediction pipeline
6. Learning how to create a streamlit application for all 3 algorithms that can be dockerized and deployed locally and on cloud services 


# How to run on your local machine: 

1. Clone my repository (on your local machine)

"git clone https://github.com/yousefmekhlafi/Multiple-Disease-Prediction"

2. Create a virtual environment on vscode "multipledisease" and activate it

"conda create -n multipledisease python=3.12.4 -y"
"conda activate multipledisease"

3. install requirements
"pip install -r requirements.txt"

4. Run the app on terminal
"streamlit run app.py"

CTRL + click LMB the link provided on terminal and run predictions  


# Project workflow

1. Step 1: Create template for automated creation of directories and files
2. Step 2: Create requirements.txt and setup.py
3. Step 3: Create logging, exception handling and utils modules 
4. Step 4: Conduct experiments in jupyter notebooks separately (already done)
5. Step 5: For each step in pipeline; update: config.yaml, params.yaml, entity, configuration manager, components, pipelines, main, app
6. Step 6: Run, test, and debug the app 


# Jupyter Notebook ML Experiment Methodology (Per ML algorithm)

1. Import dependencies
2. Load the data
3. Check for missing values
4. Perform simple EDA for checking feature types
5. Transform data and encode when/if necessary
6. Split the data into training and testing datasets
7. Train the model
8. Test the model on random samples
9. Save the model
