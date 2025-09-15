# Topic: Neural Networks Fundamentals

## Date
2025-01-15

## Source
- **Type**: Course
- **Title**: Deep Learning Specialization
- **Author/Instructor**: Andrew Ng
- **Link**: https://www.coursera.org/specializations/deep-learning

## Key Concepts

### Main Idea
Neural networks are computational models inspired by biological neural networks that can learn complex patterns in data through interconnected layers of artificial neurons.

### Technical Details
- **Definition**: A network of interconnected nodes (neurons) that process information through weighted connections
- **How it works**: Input → Hidden Layers → Output, with weights adjusted through backpropagation
- **Use cases**: Image recognition, natural language processing, regression, classification
- **Advantages**: Can learn non-linear relationships, automatic feature extraction
- **Limitations**: Requires large datasets, computationally expensive, "black box" nature

## Code Examples
```python
import tensorflow as tf
from tensorflow import keras

# Simple neural network for binary classification
model = keras.Sequential([
    keras.layers.Dense(64, activation='relu', input_shape=(784,)),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)
```

## Visual Notes
- Forward propagation: Input → Weighted sum → Activation function → Output
- Backpropagation: Calculate gradients and update weights
- Architecture diagram: Input layer → Hidden layers → Output layer

## Connections
- **Related to**: Linear regression, logistic regression, perceptrons
- **Prerequisites**: Linear algebra, calculus, basic statistics
- **Next steps**: Convolutional Neural Networks (CNNs), Recurrent Neural Networks (RNNs)
- **Applications**: Computer vision, NLP, recommendation systems

## Questions & Clarifications
- [x] How does backpropagation actually work mathematically?
- [ ] What's the difference between different activation functions?
- [ ] How to choose the right architecture for a problem?

## Practice Ideas
- [ ] Build a simple neural network from scratch using NumPy
- [ ] Implement different activation functions
- [ ] Create a neural network for MNIST digit classification

## Personal Notes
The concept of automatic feature extraction is fascinating - the network learns representations that humans might not think of. The universal approximation theorem is mind-blowing: any continuous function can be approximated by a neural network with enough hidden units.

---
**Difficulty**: Intermediate  
**Confidence Level**: 4 (Can implement basic networks, need more practice with advanced architectures)  
**Review Date**: 2025-02-15
