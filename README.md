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
- [License](#license)

## Introduction

VibeCaster is a Sentiment Analysis tool designed to interpret and classify emotions conveyed in product reviews. Built using machine learning and natural language processing techniques, VibeCaster aims to help businesses and individuals understand customer sentiments at scale.

## Features

- **Sentiment Classification**: Classify reviews into Positive, Neutral, or Negative categories.
- **High Accuracy**: Utilizes a machine learning model trained on a large dataset for high accuracy.
- **User-Friendly Web Interface**: Navigate easily through a futuristic web interface.

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
- `data/Industrial_and_Scientific_5.json.gz`: Dataset used for model training.

## Usage

### Data Preprocessing and Model Training

1. Open the `Model_Training.ipynb` notebook and run all the cells to preprocess the data and train the model.

### Web Interface

1. Start the Flask server:
    ```bash
    python app.py
    ```

2. Navigate to `http://localhost:8000` in your web browser.

## Contributing

Feel free to submit pull requests or issues to improve the project.

## License

This project is open-source and available under the [MIT License](LICENSE).
