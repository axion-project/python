import numpy as np

# Sigmoid activation function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Input dataset
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

# Output dataset
y = np.array([[0],
              [1],
              [1],
              [0]])

# Initialize weights and biases with random values
np.random.seed(42)
input_neurons = 2
hidden_neurons = 2
output_neurons = 1

# Weights and biases for the hidden layer
W1 = np.random.rand(input_neurons, hidden_neurons)
b1 = np.random.rand(1, hidden_neurons)

# Weights and biases for the output layer
W2 = np.random.rand(hidden_neurons, output_neurons)
b2 = np.random.rand(1, output_neurons)

# Learning rate
learning_rate = 0.1

# Number of iterations
epochs = 10000

# Training the neural network
for epoch in range(epochs):
    # Forward propagation
    # Input to hidden layer
    hidden_input = np.dot(X, W1) + b1
    hidden_output = sigmoid(hidden_input)
    
    # Hidden layer to output layer
    output_input = np.dot(hidden_output, W2) + b2
    predicted_output = sigmoid(output_input)
    
    # Calculate error
    error = y - predicted_output
    
    # Backpropagation
    # Output layer error
    d_predicted_output = error * sigmoid_derivative(predicted_output)
    
    # Hidden layer error
    error_hidden_layer = d_predicted_output.dot(W2.T)
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_output)
    
    # Update weights and biases
    W2 += hidden_output.T.dot(d_predicted_output) * learning_rate
    b2 += np.sum(d_predicted_output, axis=0, keepdims=True) * learning_rate
    W1 += X.T.dot(d_hidden_layer) * learning_rate
    b1 += np.sum(d_hidden_layer, axis=0, keepdims=True) * learning_rate

# Display the final output
print("Predicted Output after training:")
print(predicted_output)

# Test the neural network with new data
new_data = np.array([[0, 0],
                     [0, 1],
                     [1, 0],
                     [1, 1]])

hidden_input = np.dot(new_data, W1) + b1
hidden_output = sigmoid(hidden_input)
output_input = np.dot(hidden_output, W2) + b2
predicted_output = sigmoid(output_input)

print("Predicted Output for new data:")
print(predicted_output)
