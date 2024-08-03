import numpy as np

def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1

def diff_AND(x1, x2):
    '''
    가중치와 편향을 도입한 AND 게이트
    '''
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5]) # AND와는 가중치(w, b)만 다름
    b = 0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5]) # AND와는 가중치(w, b)만 다름
    b = - 0.2
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def XOR(x1, x2):
    '''
    XOR 게이트는 비선형 영역이라 다층 퍼셉트론으로 구현
    (AND, NAND, OR 게이트는 단층 퍼셉트론으로 구현이 가능)
    단층 퍼셉트론은 직선형 영역만 표현 가능하고, 다층 퍼셉트론은 비선형 영역도 표현할 수 있다.
    '''
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = diff_AND(s1, s2)
    return y

print(XOR(0, 0))
print(XOR(1, 0))
print(XOR(0, 1))
print(XOR(1, 1))