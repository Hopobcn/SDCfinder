import numpy as np
import cupy
import time

interval_sleep = 5


def analize(x):
    print("the following elements are nonzero")
    idx_nonzero = cupy.nonzero(x)
    nonzero = x[idx_nonzero]
    nonzero_cpu = cupy.asnumpy(nonzero)
    bits = np.unpackbits(nonzero_cpu)
    print(idx_nonzero)
    print(bits)


def main():
    size = 100500
    x = cupy.zeros(size, dtype=cupy.uint8)
    while True:
        time.sleep(interval_sleep)
        checksum = x.sum()
        print(checksum)
        x[1] = 7
        if checksum != 0:
            print("detected curruption", checksum)
            analize(x)

if __name__ == "__main__":
    main()
