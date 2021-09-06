import numpy as np

def A(x):
    if x.size != 64:
        raise ValueError('Input must be a vector of 64 components.')
    Fx = np.fft.fft(x.ravel())
    Fx[16:49] = 0.0
    return np.real(np.fft.ifft(Fx))