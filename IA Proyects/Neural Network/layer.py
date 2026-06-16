import numpy as np
from .neuron import Neuron

class Layer:

    def __init__(self, num_neurons, input_size):
        self.neurons = [Neuron(input_size) for _ in range(num_neurons)]
        self.output = np.zeros(num_neurons)

    def forward(self, inputs):
        return np.array([neuron.forward(inputs) for neuron in self.neurons])
    
    def backward(self, d_output, learning_rate):
        d_input = np.zeros(len(self.neurons[0].inputs))
        for i, neuron in enumerate(self.neurons):
            d_input += neuron.backward(d_output[i], learning_rate)
        return d_input
    

if __name__ == "__main__":
    layer = Layer(3, 4)
    inputs = np.array([1, 8,5, 6])

    layer_output = layer.forward(inputs)
    print("Layer output:", layer_output)