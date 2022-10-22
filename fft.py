import numpy as np 




#FFT calculation for an array x with N elements, where N is a power of 2.
def fft(x, N):
    X = np.empty(int(N),dtype = np.complex)
    if N == 1:
        X[0] = x[0]
    else:
        E = fft(x[::2], N/2) #even index terms
        O = fft(x[1::2], N/2) #odd index terms
        for k in range(int(N/2)):
            e = E[k]
            o = np.exp(-1j*2*np.pi*k/N)*O[k]
            X[k] = e + o 
            X[k + int(N/2)] = e - o
    return X
            
def main():
    size = 128 #Must be a power of 2
    x =  np.random.random_sample((size,)) 
    X = fft(x,size)



if __name__=="__main__":
    main()