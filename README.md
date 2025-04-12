### Linear Regression Project - Estimating Price Based on mileage

#### Project Overview
This project implements a linear regression model to estimate the price of a vehicle based on its mileage (in kilometers). The model uses a dataset that contains the mileage and corresponding price of vehicles. The goal of the project is to:

1. Train a linear regression model to predict the price of a vehicle based on its mileage.
2. Calculate and display the accuracy of the model using the **Mean Absolute Error (MAE)**.
3. Compute the **R² score** to evaluate the model's performance.
4. Visualize the dataset along with the fitted regression line.

#### Key Features
- **Normalization of Data**: The data is normalized before training to improve the efficiency of the model.
- **Gradient Descent**: The model uses gradient descent to iteratively adjust the parameters (`theta0` and `theta1`) to minimize the error.
- **Visualization**: The model plots the actual data points along with the regression line to visually show the fit.
- **Accuracy Calculation**: The Mean Absolute Error (MAE) and R² score are used to evaluate the performance of the model.

#### Instructions

1. **Data Input**: 
   - The script reads the dataset from a CSV file (`data.csv`), where the first column contains the mileage (in kilometers), and the second column contains the price (in currency units).
   - The data is expected to be in the following format:
     ```
     Mileage,Price
     15000,20000
     30000,18000
     45000,16000
     ```
  
2. **Running the Model**:
   - To run the model, execute `linear_regression.py` and follow the prompts. The model will train using gradient descent and visualize the results.
   
   ```
   python linear_regression.py
   ```

3. **Results**:
   - After training the model, the script will print the values of `theta0` and `theta1`, along with the MAE (Mean Absolute Error).
   - It will also plot the dataset and the regression line for visualization.

     ![Screenshot from 2025-04-12 20-17-40](https://github.com/user-attachments/assets/642aa022-315d-44e1-bf2e-0b6ac3a0b2e2)


4. **Accuracy Calculation**:
   - To calculate the R² score, run the accuracy script (`Accuracy.py`). This will read the saved `theta0` and `theta1` from `values.psv` and compute the R² score for the model.
   
   ```
   python Accuracy.py
   ```

5. **Estimating Price**:
   - The model will provide an estimation for each price based on the trained parameters (`theta0` and `theta1`).

#### Example Output:
After running the model, you can expect output like:

```
Enter the mileage of the car: 240000
Value of theta0=8267.107639370304 and theta1=-0.01923808255621025
the prediction of this 240000.0 is 3649.967825879844

```
