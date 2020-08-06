import numpy as np
import random

## a simple neural network project couretisey of Michel Nielsen
## http://neuralnetworksanddeeplearning.com/

class Network (object):
    
    ## Creates a network from a list of neurons called sizes. Creating a network like this: net = Network([1,2,3]) creates a network with one neuron in the first layer , two in the second and so on
    
    ## Python syntax here, learn why __init__ is used here
    def __init__(self,size):
        self.num_layers = len(size)
        self.size = size
        
        ## Don't really understand this python syntax or what it does
        ## but i think it fills a list called bias with random numbers based on the input vector size
        self.bias = [np.random.randn(y,1) for y in size[1:]]
        
        ## Same as above but two dimensional array? Learn this syntax
        self.weight = [np.random.randn(y,x) for x,y in zip(size[:-1],size[1:])]
                
    def feedforward(self,a):
        # Returns the network output for the input a
        # but what does "network output" mean in this context? Is it the output in the final layer or from the first layer? Learn what this does better
        for b, w in zip(self.bias,self.weight):
            a = sigmoid(np.dot(w,a)+b)
        return a
        
        def SGD(self,trainingData,epochs,miniBatchSize,eta,
        testData=none):
            ## This is the "training" part of the network, using gradient descent. Still don't know the mathematics behind it fully but basically finds the best way to reduce the cost function yada yada ...
            
            
            if testData: nTest = len(testData)
            n = len(trainingData)
            for j in xrange(epochs):
                random.shuffle(trainingData)
                miniBatches = [trainingData[k:k+miniBatchSize] for k in xrange(0,n,miniBatchSize,eta)]
                for miniBatch in miniBatches:
                    self.updateMiniBatch(miniBatch,eta)
                if testData:
                    ## Don't understand this, learn what it does and why
                    print("Epoch")
                    
                else:
                    print("Epoch complete")
                    
        def updateMiniBatch(self,miniBatch,eta):
            ## Updates networks wieghts and biases with backpropogation
            
            ## TODO: continue here

