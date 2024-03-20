import numpy as np

# from sklearn import preprocessing as pre

inputs = [
    [1, 1, 25.5, 1, 0],
    [3, 0, 35, 0, 0],
    [2, 1, 19, 3, 2],
    [1, 0, 29.5, 1, 2],
]
# layer 1
# 4x5 inputs, 8 neurons 5x8 weights + 8 bioses output: 4x8
# layer 2
# 4x8 inputs 8 neruons 8x8 weights + 8 bioses output 4x8
# layer 3
# 4x8 inputs 5 neurons 8x5 weights + 5 bioses output 4x5
# last layer
# 4x5 inputs 1 neuron 5x1 weights + 1 bios output 4X1


class dense:
    """This class creates layers for neural networks"""

    def __init__(self, input_n, neurons):
        self.bios = np.zeros(neurons)
        self.weights = np.random.rand(input_n, neurons)

    def forward(self, inputs):
        """This is a function that is used to propagate forword in the network."""
        self.output = np.dot(np.array(inputs), self.weights) + self.bios
        return self.output

    # activation functions: Sigmoid, relu, sofmax


class Activations:
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def relu(self, x):
        return np.maximum(0, x)

    def sofmax(self, x):
        exp = np.exp(x - np.max(x, axis=1, keepdims=True))
        pr = exp / np.sum(exp, axis=1, keepdims=True)
        return pr

    def b_step(self, x):
        return x * (1 / x)


# layers
layer1 = dense(5, 8)
layer2 = dense(8, 8)
layer3 = dense(8, 5)
layer4 = dense(5, 1)
func = Activations()
# propagations
ans = layer1.forward(inputs)
ne1 = func.sofmax(ans)

ans2 = layer2.forward(ne1)
ne2 = func.sofmax(ans2)

ans3 = layer3.forward(ne2)
ne3 = func.sofmax(ans3)

ans4 = layer4.forward(ne3)
ne4 = func.b_step(ans4)
print(ans4)

print(func.b_step(np.array([0, 4, -6, 8])))

import tensorflow as tf

print(tf)