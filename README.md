
![Screenshot 2025-02-23 194602](https://github.com/user-attachments/assets/cdfe9af4-dad8-4af3-a180-14616294aa9e)

🧠 Simple Neural Network with Tanh Activation

🚀 A lightweight, fully connected artificial neural network (ANN) implementation using NumPy!

This project demonstrates a simple 2-layer feedforward neural network that uses the tanh activation function to process inputs and generate outputs.

✨ Features:
Custom Forward Pass: Implements a basic neural network with one hidden layer.
Tanh Activation: Uses the hyperbolic tangent function for non-linearity.
Random Weight Initialization: Weights are initialized in the range [-0.5, 0.5] for experimentation.
Reproducible Results: Uses np.random.seed(42) to ensure consistency in weight initialization.

🔧 How It Works:
Inputs (i1, i2) are passed into the hidden layer.
The hidden layer neurons apply weighted sums and activate using the tanh function.
The output layer processes the hidden layer outputs and applies the tanh activation again.
The final outputs (o1, o2) are printed
