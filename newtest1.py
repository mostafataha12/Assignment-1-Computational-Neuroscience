import numpy as np

weights = {
    'w1': np.random.uniform(-0.5, 0.5),
    'w2': np.random.uniform(-0.5, 0.5),
    'w3': np.random.uniform(-0.5, 0.5),
    'w4': np.random.uniform(-0.5, 0.5),
    'w5': np.random.uniform(-0.5, 0.5),
    'w6': np.random.uniform(-0.5, 0.5),
    'w7': np.random.uniform(-0.5, 0.5),
    'w8': np.random.uniform(-0.5, 0.5)
}

b1, b2 = 0.5, 0.7

inputs = {
    'h1': 0.75336507,
    'h2': 0.593269992,
    'o1': 0.596884378,
    'o2': 0.772928465
}


def tanh(x):
    return np.tanh(x)

h1_output = tanh(inputs['h1'] * weights['w1'] + inputs['h2'] * weights['w2'] + b1)
h2_output = tanh(inputs['h1'] * weights['w3'] + inputs['h2'] * weights['w4'] + b1)

o1_output = tanh(h1_output * weights['w5'] + h2_output * weights['w6'] + b2)
o2_output = tanh(h1_output * weights['w7'] + h2_output * weights['w8'] + b2)


print("Output of the network:")
print(f"o1: {o1_output}")
print(f"o2: {o2_output}")
