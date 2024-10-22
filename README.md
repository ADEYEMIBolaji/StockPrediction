# Stock Market Price Prediction Using Machine Learning

## Project Overview

This project aims to build a robust framework for stock market price prediction using multiple machine learning and deep learning techniques. The models used in this project include:

- **ARIMA** (AutoRegressive Integrated Moving Average)
- **Auto ARIMA** (Automatic ARIMA)
- **Random Forest**
- **Support Vector Machine (SVM)**
- **Long Short-Term Memory (LSTM)**

The project involves training these models on stock price data sourced from Yahoo Finance, followed by feature engineering and hyperparameter tuning to enhance prediction accuracy. The ultimate goal is to compare the performance of these models and draw insights from their behavior on different stock datasets, including Apple, Google, Amazon, Microsoft, and Tesla.

## Features

- **Stock Data Collection**: The data is collected from Yahoo Finance for multiple companies.
- **Time Series Analysis**: ARIMA and Auto ARIMA models are applied for forecasting based on historical time series data.
- **Machine Learning Models**: Random Forest and SVM models are trained for regression-based stock price predictions.
- **Deep Learning**: LSTM networks are implemented to capture long-term dependencies in stock price movements.
- **Feature Engineering**: Feature selection and extraction methods like `RoC`, `RSI`, `MACD`, etc., are used to enrich model training.
- **Model Evaluation**: Evaluation metrics include RMSE, MAE, and R², which help compare the effectiveness of each model.
  
## Project Structure

- **data/**: Contains the raw and processed stock data used for model training and evaluation.
- **notebooks/**: Jupyter notebooks with detailed steps of data preprocessing, model training, and analysis.
- **src/**: Source code for the machine learning models, including feature engineering, ARIMA, Random Forest, SVM, and LSTM implementations.
- **results/**: The results folder containing evaluation metrics, prediction vs actual graphs, and comparative analysis of all models.
- **README.md**: This documentation file explaining the project details.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/stock-price-prediction.git
   cd stock-price-prediction
   ```

2. **Create a virtual environment** (Optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Download the stock data**: Run the script to fetch historical stock data from Yahoo Finance.
   
2. **Run the models**: Train the machine learning and deep learning models by running the following command:
   
   ```bash
   python src/main.py
   ```

3. **Evaluate the models**: Model performance will be evaluated, and the results will be saved in the `results/` folder.

4. **Jupyter Notebooks**: You can also explore and modify the code through Jupyter notebooks provided in the `notebooks/` directory.


## Future Work

- **Model Optimization**: Additional tuning of hyperparameters and integration of advanced techniques such as hybrid models.
- **Data Expansion**: Using additional datasets and testing the models on various market conditions.
- **Model Generalization**: Extending the models to work with different financial instruments such as commodities or forex markets.
  
## Contributing

Feel free to fork the repository and submit pull requests if you would like to contribute to the project. You can also open an issue if you find any bugs or have suggestions for improvements.

## License
