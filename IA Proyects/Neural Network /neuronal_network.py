import numpy as np
from .layer import Layer

class NeuralNetwork:
    
    def __init__(self):
        self.layers = []
        self.loss_list = []

    def add_layer(self, num_neurons, input_size):
        if not self.layers:
            self.layers.append(Layer(num_neurons, input_size))
        else:
            previous_layer_size = len(self.layers[-1].neurons)
            self.layers.append(Layer(num_neurons, previous_layer_size))

    def forward(self, inputs):
        for layer in self.layers:
            inputs = layer.forward(inputs)
        return inputs
    
    def backward(self, d_output, learning_rate):
        for layer in reversed(self.layers):
            d_output = layer.backward(d_output, learning_rate)


    def train(self, X, y, epochs = 1000,learning_rate = 0.1):
        for epoch in range(epochs):
            loss = 0
            for i in range(len(X)):
                output = self.forward(X[i])
                loss += np.mean((output - y[i]) ** 2)
                loss_gradient = 2 * (output - y[i]) 
                self.backward(loss_gradient, learning_rate)
            
            loss /= len(X)
            self.loss_list.append(loss)
            if epoch % 100 == 0:
                print(f"Epoch {epoch}, Loss: {loss:.4f}")

    def predict(self, X):
        predictions = []
        for i in range(len(X)):
            predictions.append(self.forward(X[i]))
        return np.array(predictions)

if __name__ == "__main__":
    nn = NeuralNetwork()
    nn.add_layer(4, 2)
    nn.add_layer(3, 4)
    nn.add_layer(1, 3)

    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [1], [1], [0]])

    nn.train(X, y, epochs=1000, learning_rate=0.1)

    predictions = nn.predict(X)
    print("Predictions:")
    print(predictions)
