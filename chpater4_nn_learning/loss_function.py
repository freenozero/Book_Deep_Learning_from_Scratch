import numpy as np

def sum_squares_error(y, t):
    return 0.5 * np.sum((y-t) ** 2)

def cross_entropy_error(y, t):
    delta = 1e-7 # 함수에 0을 입력하면 -inf가 되어 더이상 진행하지 않게됨을 방지
    return -np.sum(t * np.log(y + delta))

def mini_cross_entropy_error(y, t):
    '''
    배치용 교차 엔트로피 오차, 정답레이블: 원-핫 인코딩
    '''
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
    
    batch_size = y.shape[0]
    return -np.sum(t*np.log(y + 1e-7)) / batch_size

def mini2_cross_entropy_error(y, t):
    '''
    배치용 교차 엔트로피 오차, 정답레이블: 숫자 레이블
    '''
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
    
    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7))/ batch_size