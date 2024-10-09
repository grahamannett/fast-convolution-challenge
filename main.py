"""
8/18/24
Matic Take-Home Challenge

Graham Annett

Convolution Challenege
----------------------

This problem is premised by how to compute the convolution for a given matrix M and Kernel K.
While this functionality is built into libraries like numpy and scipy, this challenge is premised with the kernel K being a 1D kernel with the following values [-1, 0, 1].
This is an important kernel in relation to signal and edge detection and while can be computed with just out of the box functions, the challenge is to optimize the computation.

Since there is no mention of padding or stride, we assume that we are to compute the convolution in the same manner as 'valid' mode in numpy, e.g. only for complete overlap.
If this were not the case, we would need to adjust our implementation to account for the padding and stride, but would remain the fastest unless the kernel changed in some manner.

The specs emphasize generalization is not the point of this and that the kernel does not change.
From this we can understand that the point of this is to optimize around the fact that this kernel can be computed in a more efficient manner than the general convolution operation.
The way that we can do this is by taking the difference for the matrix M with offsets of 2 and -2 as the kernel is [1, 0, -1].

I compared it to the following implementations to confirm that is it quicker than the general approach (if our assumptions change, this may not be the case and other methods may actually be quicker):

Benchmark Results (with 10_000x10_000 matrix):
- numpy
    - convolve - 0.59954214 seconds
        - np.apply_along_axis(lambda a: np.convolve(a, k, mode=mode), axis=0, arr=m)
    - correlate - 0.58970404 seconds
        - np.apply_along_axis(lambda a: np.correlate(a, k, mode=mode), axis=0, arr=m)
- scipy
    - correlate2d - 1.18232965 seconds
        - sp.signal.correlate2d(m, k[:, None], mode=mode)
    - convolve - 5.38580179 seconds
        - sp.signal.convolve(m, k[:, None], mode=mode)
    - fftconvolve - 2.46590471 seconds
        - sp.signal.fftconvolve(m, k[:, None], mode=mode)


Assumptions:
    - Kernel is fixed and does not change (this question is premised on understanding the convolution operation in relation to the kernel, rather than blindly applying functions)
    - Convolution only for complete overlap (e.g. np 'valid' mode), otherwise would have mentioned padding or stride in description/info.
        - Likely also given `Gracefully handle border conditions as per your preferences` in the description, meaning we assume a stride of 1 and only complete overlap.
    - While the input is unsigned, the output should be signed.  This means that while the max value of the output is 255, the min value may be <0 and requires a signed output
        - If this is not true, all values below 0 should be set to 0.  If we should handle overflows some other way, this should be specified.
"""

import sys
import time

import numpy as np

# Assuming basetype is uint8 as unsigned char is specified.
np_dtype = np.uint8
# not needed unless for benchmarking against numpy/scipy
kernel = [-1, 0, 1]
mode = "valid"


def fast_conv(m):
    """
    Computes the 1D-convolution of the matrix M for the kernel K = [-1, 0, 1]

    It is necessary to cast to int as the input specifies unsigned char meaning the original values will be between 0 and 255.
    Since the  will be akin to:
        -1 * ((m[2:, :] - m[:-2, :]))
    Can further optimize it by casting to int16 and flipping the order
    """
    return m[:-2, :].astype(np.int16, copy=False) - m[2:, :].astype(
        np.int16, copy=False
    )


def timeit(func: callable, fargs: tuple):
    """
    Measures the computation time of a function and optionally prints the result.
    """

    t0 = time.time()
    out = func(*fargs)
    t_done = time.time() - t0

    print(f"Computation time for {func.__name__}: {t_done:.8f} seconds")
    return out


def main():
    # Read the 'rows' and 'cols' from command line arguments
    if len(sys.argv) != 3:
        print("Usage:\n\tpython script.py (rows:int) (cols:int)")
        sys.exit(1)

    rows, cols = int(sys.argv[1]), int(sys.argv[2])

    # allow for random values between the min and max of the np_dtype
    dtype_range = np.iinfo(np_dtype).min, np.iinfo(np_dtype).max

    # value not necessary but for consistency or benchmarking against `np.convolve(a, k, mode="valid")`
    K = np.array(kernel)
    # Create an unsigned char matrix M of size [rows x cols]
    M = np.random.randint(*dtype_range, size=(rows, cols), dtype=np_dtype)

    Dx = timeit(fast_conv, (M.T,)).T
    Dy = timeit(fast_conv, (M,))

    min_max_Dx = Dx.min(), Dx.max()
    min_max_Dy = Dy.min(), Dy.max()

    print(f"Dx min: {min_max_Dx[0]}, Dx max: {min_max_Dx[1]}")
    print(f"Dy min: {min_max_Dy[0]}, Dy max: {min_max_Dy[1]}")


if __name__ == "__main__":
    main()
