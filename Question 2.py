import numpy as np

w = np.random.rand(1, 3) * 10
w_1 = np.round(w[0][0], 1)
w_2 = np.round(w[0][1], 1)
theta = np.round(w[0][2], 1)

#inputs
x = [[0,0], [0, 1], [1, 0], [1, 1]]
x_array = np.asarray(x)

#expected out puts AND/OR/NOR/XOR
#out = np.array([0, 0, 0, 1])
out = x_array[:, 1] * x_array[:, 0]
def step (net):
    if net >= 0:
        return 1
    else:
        return 0

#the error vector
error = np.array([0, 0, 0, 0])
for i in range(len(x)):
    f_net = step(np.dot(np.asarray([w_1, w_2]), x[i]) + theta)
    error[i] = out[i] - f_net
E = np.sum(error)


max_it = 1000
t = 1
learning_rate = 0.1
vals = [[w_1, w_2, theta]]
while t < max_it and E != 0:
    for i in range(len(x)):
        f_net = step(np.dot(np.asarray([w_1, w_2]), x[i]) + theta)
        error[i] = out[i] - f_net
        w_1 = w_1 + learning_rate * error[i] * x[i][0]
        w_2 = w_2 + learning_rate * error[i] * x[i][1]
        theta = theta + learning_rate * error[i]
    vals.append([w_1, w_2, theta])
    E = np.sum(error)
   # print(t, 'sum of errors', E)
    t = t+1

print("w_1", w_1)
print("w_2", w_2)
test_LogicGate_00 = step(np.dot(np.asarray([w_1, w_2]), np.array([0, 0]) + theta))
test_LogicGate_01 = step(np.dot(np.asarray([w_1, w_2]), np.array([0, 1]) + theta))
test_LogicGate_10 = step(np.dot(np.asarray([w_1, w_2]), np.array([1, 0]) + theta))
test_LogicGate_11 = step(np.dot(np.asarray([w_1, w_2]), np.array([1, 1]) + theta))
print("LogicGate [0, 0]", test_LogicGate_00)
print("LogicGate [0, 1]", test_LogicGate_01)
print("LogicGate [1, 0]", test_LogicGate_10)
print("LogicGate [1, 1]", test_LogicGate_11)