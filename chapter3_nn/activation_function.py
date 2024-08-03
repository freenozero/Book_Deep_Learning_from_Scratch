import numpy as np

def step_function(x):
    if x > 0:
        return 1
    else:
        return 0
    
def diff_step_function(x):
    '''
    step_function 함수와 달리 넘파이 배열을 인수로 넣을 수 있음
    '''
    y = x > 0
    return y.astype(np.int)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)