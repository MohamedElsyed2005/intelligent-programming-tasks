import numpy as np
import matplotlib.pyplot as plt

class Perceptron:
    def __init__(self, input_size, learning_rate=0.1, epochs=10):
        # Initialize weights and bias
        self.weights = np.zeros(input_size)
        self.bias = 0
        self.learning_rate = learning_rate
        self.epochs = epochs
    
    def activation(self, x):
        # Step function: returns 1 if x >= 0, else 0
        return 1 if x >= 0 else 0
    
    def predict(self, X):
        # Calculate weighted sum and apply activation
        weighted_sum = np.dot(X, self.weights) + self.bias
        return self.activation(weighted_sum)
    
    def train(self, X, y):
        # Training loop
        for _ in range(self.epochs):
            for i in range(len(X)):
                # Make prediction
                prediction = self.predict(X[i])
                # Update weights and bias if prediction is wrong
                error = y[i] - prediction
                self.weights += self.learning_rate * error * X[i]
                self.bias += self.learning_rate * error

# Prepare the data from Lab 2
# Apples (label = 1)
apples_x1 = np.array([1.0627, 0.4268, 1.5946, 1.1636, 0.9066, 
                      0.7058, 0.9318, 1.5334, 0.9522, 1.1472])
apples_x2 = np.array([1.1438, 1.5955, 0.9812, 1.0873, 1.3629, 
                      2.0916, 1.0570, 1.0296, 0.5838, 0.3319])

# Oranges (label = 0)
oranges_x1 = np.array([3.3572, 2.6541, 3.6270, 2.2795, 2.8001, 
                       3.4078, 3.6451, 3.5954, 2.9901, 2.1980])
oranges_x2 = np.array([2.8118, 2.4290, 1.2031, 2.2856, 2.3450, 
                       2.3560, 2.3343, 1.3988, 1.9216, 2.1287])

# Combine features
X = np.vstack((
    np.column_stack((apples_x1, apples_x2)),
    np.column_stack((oranges_x1, oranges_x2))
))

# Create labels (1 for apples, 0 for oranges)
y = np.array([1] * 10 + [0] * 10)

# Train the perceptron
perceptron = Perceptron(input_size=2, learning_rate=0.1, epochs=100)
perceptron.train(X, y)

# Test the perceptron
print("Testing the trained perceptron:")
for i in range(len(X)):
    prediction = perceptron.predict(X[i])
    print(f"Sample {i}: Predicted: {prediction}, Actual: {y[i]}")

# Plotting
plt.scatter(apples_x1, apples_x2, color='red', label='Apples')
plt.scatter(oranges_x1, oranges_x2, color='orange', label='Oranges')

# Calculate the decision boundary
x1 = np.array([0, 4])  # Range covering the data points
x2 = -(perceptron.weights[0] * x1 + perceptron.bias) / perceptron.weights[1]

plt.plot(x1, x2, 'b-', label='Decision Boundary')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.title('Perceptron Classification: Apples vs Oranges')
plt.grid(True)
plt.show()

# Print the learned parameters
print(f"\nLearned weights: {perceptron.weights}")
print(f"Learned bias: {perceptron.bias}")