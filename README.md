# VibeCaster: Casting the Vibe of Reviews

<!-- ![VibeCaster Logo](/assets/logo.png)-->  <!-- Uncomment this line and add a logo image here -->

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [File Structure](#file-structure)
- [Usage](#usage)
- [Contributing](#contributing)

## Introduction

VibeCaster is a Sentiment Analysis tool designed to interpret and classify emotions conveyed in product reviews. Built using machine learning and natural language processing techniques, this project serves me to learn more about training models in the context of Natural Language Processing.

## Features

- **Sentiment Classification**: Classify reviews into Positive, Neutral, or Negative categories.
- **High Accuracy**: Utilizes logistic regression trained on a large dataset(ca. 500 000 Entries) .
- **User-Friendly Web Interface**: Navigate easily through a futuristic web interface. Just paste in your review and get the sentiment analysis displayed on the screen.

## Prerequisites

- Python 3.x
- pip

## Installation

1. **Clone the Repository**:
    ```bash
    git clone <repository_url>
    ```

2. **Navigate to the Project Directory**:
    ```bash
    cd VibeCaster
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## File Structure

- `Model_Training.ipynb`: Jupyter Notebook containing all the data preprocessing and model training steps.
- `app.py`: Flask application for the web interface.
- `data/`: Datasets that can be  used for model training.

## Usage

### Data Preprocessing and Model Training
(Optional)
1. Open the `Model_Training.ipynb` notebook and run all the cells to preprocess the data and train the model.

### Web Interface

1. Start the Flask server:
    ```bash
    python app.py
    ```

2. Navigate to `http://localhost:8000` in your web browser.

## Contributing

Feel free to submit pull requests or issues to improve the project.
