import numpy as np

class Neuron:
    def __init__(self, n_input):
        self.weigth = np.random.rand(n_input)
        self.bias = np.random.rand()
        self.output = 0
        self.inputs = None
        self.dweit = np.zeros_like(self.weigth)
        self.dbias = 0

    def activate(self, x):
        return 1 / (1 + np.exp(-x))
    
    def derivate_activate(self, x):
        return self.activate(x) * (1 - self.activate(x))
    
    def forward(self, inputs):
        self.inputs = inputs
        weighted_sum = np.dot(self.weigth, inputs) + self.bias
        self.output = self.activate(weighted_sum)
       
        return self.output
    
    def backward(self, d_output, learning_rate):
        d_activation = d_output * self.derivate_activate(self.output)
        self.dweit = d_activation * self.inputs
        self.dbias = d_activation
        d_input = np.dot(d_activation, self.weigth)
        self.weigth -= self.dweit * learning_rate
        self.bias -= self.dbias * learning_rate
        
        return d_input

if __name__ == "__main__":
    neuron = Neuron(3)
    inputs = np.array([1, 2, 3])
    output = neuron.forward(inputs)
    print("Neuron output:", output)
