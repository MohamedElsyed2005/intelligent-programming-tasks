import numpy as np
import matplotlib.pyplot as plt

class Perceptron:
    def __init__(self, input_size, learning_rate=0.1, epochs=10):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = np.zeros(input_size) 

    def activation(self, x):
        return np.where(x >= 0, 1, 0) 

    def forward(self, X):
        return self.activation(np.dot(X, self.weights))

    def train(self, X, y):
        for _ in range(self.epochs):
            for xi, target in zip(X, y):
                prediction = self.forward(xi)
                error = target - prediction
                self.weights += self.learning_rate * error * xi 

    def __call__(self, inputs):
        return self.forward(inputs)


X = np.array([
    [1.0627, 1.1438, 1], [0.4268, 1.5955, 1], [1.5946, 0.9812, 1],
    [1.1636, 1.0873, 1], [0.9066, 1.3629, 1], [0.7058, 2.0916, 1],
    [0.9318, 1.0570, 1], [1.5334, 1.0296, 1], [0.9522, 0.5838, 1],
    [1.1472, 0.3319, 1], [3.3572, 2.8118, 1], [2.6541, 2.4290, 1],
    [3.6270, 1.2031, 1], [2.2795, 2.2856, 1], [2.8001, 2.3450, 1],
    [3.4078, 2.3560, 1], [3.6451, 2.3343, 1], [3.5954, 1.3988, 1],
    [2.9901, 1.9216, 1], [2.1980, 2.1287, 1]
])
y = np.array([1] * 10 + [0] * 10) 

perceptron = Perceptron(input_size=3, learning_rate=0.1, epochs=10)
perceptron.train(X, y)

apples = X[:10, :2]
oranges = X[10:, :2]
plt.scatter(apples[:, 0], apples[:, 1], color='red', label='Apples')
plt.scatter(oranges[:, 0], oranges[:, 1], color='orange', label='Oranges')

x_values = np.linspace(min(X[:, 0]), max(X[:, 0]), 100)
y_values = -(perceptron.weights[0] * x_values + perceptron.weights[2]) / perceptron.weights[1]
plt.plot(x_values, y_values, label='Decision Boundary', color='blue')

plt.legend()
plt.title("Perceptron Decision Boundary")
plt.show()

for input_ in X:
    output = perceptron(input_)
    print(f"Input: {input_[:2]} => Output: {output}")
