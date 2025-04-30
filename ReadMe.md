


# Hotel Price Prediction

This repository contains a project for predicting hotel prices using machine learning models. The project utilizes an online dataset and predicts hotel prices based on selected features.

## Features

- **Dataset**: The dataset is sourced online and includes various features such as location, rating, amenities, and more.
- **Prediction Model**: The model uses machine learning algorithms, specifically the RandomForest Regressor, to predict hotel prices based on the provided features.
- **Key Features Used**:
    - Location
    - Star Rating
    - Number of Reviews
    - Amenities
    - Seasonal Trends

## Installation

1. Clone the repository:
     ```bash
     git clone https://github.com/your-username/hotel-price-prediction.git
     ```
2. Navigate to the project directory:
     ```bash
     cd hotel-price-prediction
     ```
3. Install the required dependencies:
     ```bash
     pip install -r requirements.txt
     ```

## Usage

1. Prepare the dataset:
     - Download the dataset from the provided source.
     - Place it in the `data/` directory.

2. Train the model:
     ```bash
     run the modeelling.pynb file to create.pkl files
     ```

3. Make predictions:
     ```bash
     run app.py and check predictions on localhost
     ```

## Project Structure

```
Hotel_Price_Management/
├── data/               # Dataset files
├── models/             # Saved models
├── notebooks/          # Jupyter notebooks for exploration
├── requirements.txt    # Python dependencies
└── ReadMe.md           # Project documentation
app.py
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.



## Acknowledgments

- Dataset source: [https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand/data](#)
- Inspiration: Machine learning applications in the hospitality industry.
- Tools: Python, Scikit-learn, Pandas, NumPy, Matplotlib.
- Model: RandomForest Regressor.


