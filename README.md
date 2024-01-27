# Adam Optimizer in Deep Learning

This project demonstrates the implementation of the Adam optimizer, a popular optimization algorithm used in training deep learning models. It is written in Python and utilizes NumPy for numerical operations, along with Matplotlib for visualizing the training performance.

## Project Structure

- `/notebook`: Contains Jupyter notebooks for an interactive walkthrough.
  - `adamoptimizer.ipynb`: The Jupyter notebook illustrating the Adam optimizer process.
- `/source`: Contains the source Python script.
  - `adam.py`: The Python script implementing the Adam optimizer in a neural network.
- `/myenv`: Suggested directory for setting up a virtual Python environment.
- `.gitignore`: Specifies files and directories to be ignored by version control.
- `LICENSE`: The license document for the project.
- `README.md`: The file providing documentation and instructions.
- `requirements.txt`: A list of necessary Python dependencies.

## Installation

To run the neural network with the Adam optimizer, you need to have Python installed along with the necessary libraries. Install the dependencies with:

pip install -r requirements.txt


This will install NumPy and Matplotlib, which are required for the project.

## Usage

To execute the neural network training with the Adam optimizer:

1. Navigate to the `/source` directory.
2. Run the `adam.py` script with the following command:


python adam.py


Alternatively, you can open the `adamoptimizer.ipynb` notebook within the `/notebook` directory if you prefer working in a Jupyter notebook environment.

## Neural Network Overview

The neural network uses a single hidden layer and is trained on a simple dataset to perform binary classification. The Adam optimizer is used to update the network's weights, aiming to minimize the error between the predicted and actual outputs.

The key steps in the script include:

- Importing the required libraries.
- Creating the input (`X`) and output (`y`) datasets.
- Defining the sigmoid activation function.
- Specifying the model's hyperparameters, including the learning rate and the number of neurons.
- Initializing the model's weights.
- Iterating over a set number of epochs to train the model using the Adam optimizer.
- Visualizing the reduction in error over each epoch.

## Visualization

The script plots the error at the end of each epoch, providing a visual representation of the learning process. The error is expected to decrease as the number of epochs increases, indicating that the model is learning from the data.

## Requirements

The `requirements.txt` file includes:

numpy
matplotlib


Ensure these libraries are installed before running the script.

## Contributions

Contributions to this project are welcome. Please feel free to fork the repository, make your improvements, and submit a pull request.

## License

This project is released under the MIT License. See the `LICENSE` file for more details.
