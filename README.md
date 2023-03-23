# Boston_House_price

This project uses linear regression to predict the median value of owner-occupied homes in Boston. The dataset used for this project contains information about various factors that affect the value of a home such as crime rate, tax rate, average number of rooms, and more.


The dataset was first subjected to exploratory data analysis (EDA) to identify patterns, correlations, and outliers. The data was then preprocessed by scaling numerical features.

Linear Regression algorithm was used to train the model on the preprocessed data. The model achieved an r2 score of 0.763 and an adj_r2 score of 0.741 on the dataset.

A Flask application was created using the trained model, allowing the user to input values for the various features and receive a predicted median value for their house.

To run this code, you will need to have Python and the following libraries installed:

pandas

numpy

scikit-learn

Flask


1. Clone this repo and open folder with IDE(VS-Code)
2. Setup Environment with python version 3.70

    ```
     conda create -n env python=3.7 y
    
3. Install requirements.txt file 

    ```
      pip install -r requirements.txt
    
  
 4. Run the following command on python terminal:
       ```
          python app.py    
          
      ´``
5.Render HTML in local browser 
