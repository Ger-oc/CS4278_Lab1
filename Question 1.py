import numpy as np

def unitStep(v):
    if v >= 0:
        return 1
    else:
        return 0

def perceptronModel(x, w, b):
    v = np.dot(w, x) + b
    y = unitStep(v)
    return y

# OR Logic function
# W1 = 1, w2 = 1, b =-.05
def lodgicFunction(x):
    w = np.array([1,1])
    b = -0.5
    return perceptronModel(x, w, b)

#testing percertrion Model
test1 = np.array([0, 1])
test2 = np.array([1, 1])
test3 = np.array([0, 0])
test4 = np.array([1, 0])

print("OR ({}, {}) = {}".format(0, 1, lodgicFunction(test1)))
print("OR ({}, {}) = {}".format(0, 1, lodgicFunction(test2)))
print("OR ({}, {}) = {}".format(0, 1, lodgicFunction(test3)))
print("OR ({}, {}) = {}".format(0, 1, lodgicFunction(test4)))