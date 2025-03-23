# Algerian Forest Fire Prediction: FWI using Linear Regression

## Overview

This project aims to predict the **Fire Weather Index (FWI)** for **Algerian forest fires** using **linear regression** and its variants. The Fire Weather Index is a key metric used to assess the risk of wildfires based on weather conditions. By accurately predicting the FWI, this project helps improve wildfire prevention, early detection, and resource allocation.

### **Key Technologies Used:**
- Python
- **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
- **Machine Learning Models:** Linear Regression, Ridge Regression, Lasso Regression, ElasticNet Regression

---

## Table of Contents

1. [Project Description](#project-description)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Data](#data)
5. [Models](#models)
6. [Evaluation Metrics](#evaluation-metrics)
7. [Results](#results)
8. [Contributing](#contributing)
9. [License](#license)

---

## Project Description

The goal of this project is to create a machine learning model that predicts the **Fire Weather Index (FWI)** for forest fire risk in Algeria based on meteorological data. The model uses historical weather data (temperature, wind speed, humidity, and precipitation) along with the corresponding FWI to train and predict future fire risks.

**Approach:**
- The dataset is cleaned and preprocessed to handle missing values and normalize features.
- Multiple linear regression techniques, including **Ridge**, **Lasso**, and **ElasticNet**, are implemented to predict the FWI based on the features.
- The model is evaluated using metrics such as **Mean Squared Error (MSE)**, **Mean Absolute Error (MAE)**, and **R² (Coefficient of Determination)**.

---

## Installation

To set up and run this project, follow these steps:

1. Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/fwi-prediction.git
```

2. Navigate to the project directory:

```bash
cd fwi-prediction
```

3. Install the required dependencies using **pip**:

```bash
pip install -r requirements.txt
```

---

## Usage

To train the model and make predictions, you can run the following Python script:

```bash
python train_predict.py
```

This will:
1. Load and preprocess the weather dataset.
2. Train the **Linear Regression**, **Ridge Regression**, **Lasso Regression**, and **ElasticNet Regression** models.
3. Evaluate the models based on various performance metrics.
4. Display a comparison of the model results (MSE, MAE, R²) using **Matplotlib** or **Seaborn** visualizations.

### Example Command to Run:
```bash
python train_predict.py --data_path 'data/algerian_fwi_data.csv' --output_path 'results/output.csv'
```

---

## Data

The project requires a dataset with historical weather data and FWI values. You can obtain the dataset from any reliable source (e.g., meteorological data from Algeria).

### Expected Dataset Columns:
- **Temperature (°C)**
- **Wind Speed (km/h)**
- **Relative Humidity (%)**
- **Precipitation (mm)**
- **Fire Weather Index (FWI)** (target variable)

Make sure your dataset is formatted as a CSV file with these columns.

---

## Models

This project implements several variants of linear regression:

- **Linear Regression:** Basic model to predict FWI using a linear relationship between the features and the target.
- **Ridge Regression:** Linear regression with L2 regularization to prevent overfitting by penalizing large coefficients.
- **Lasso Regression:** Linear regression with L1 regularization that can perform feature selection.
- **ElasticNet Regression:** A combination of L1 and L2 regularization that balances the benefits of Ridge and Lasso.

Each model is trained on the same dataset and evaluated based on its performance metrics.

---

## Evaluation Metrics

To evaluate the performance of the models, the following metrics are used:

- **Mean Squared Error (MSE):** Measures the average squared difference between predicted and actual values.
- **Mean Absolute Error (MAE):** The average of the absolute errors between predicted and actual values.
- **R² (Coefficient of Determination):** A statistical measure that explains the proportion of variance in the dependent variable that is predictable from the independent variables.

---

## Results

The results of the model performance will be displayed in a comparison table and plotted in a graph using **Matplotlib** or **Seaborn**. The best-performing model will be selected based on the **lowest MSE**, **lowest MAE**, and **highest R² score**.

Sample results:

| Model               | MSE   | MAE   | R²    |
|---------------------|-------|-------|-------|
| Linear Regression    | 0.45  | 0.62  | 0.87  |
| Ridge Regression     | 0.42  | 0.58  | 0.89  |
| Lasso Regression     | 0.47  | 0.64  | 0.85  |
| ElasticNet Regression| 0.44  | 0.60  | 0.88  |

---

## Contributing

We welcome contributions to this project! To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push the changes to your forked repository (`git push origin feature-branch`).
5. Submit a pull request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to modify this `README.md` file as needed to suit your project’s details. Let me know if you'd like to add anything else!