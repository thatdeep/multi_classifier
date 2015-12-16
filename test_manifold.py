"""
Copyright (c) 2015-2016 Constantine Belev



Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:



The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.



THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import numpy as np

from matplotlib import pyplot as plt

from numpy.linalg import norm

from riemannian_optimization.gd.gradient import approximate
from riemannian_optimization.utils.test_utils import generate_sigma_set

np.set_printoptions(linewidth=450, suppress=True)


if __name__ == "__main__":
    """
    m, n = 10, 5
    M = 50
    percent = .8
    a = np.random.random((m, n))
    """
    m, n = (10, 10)
    M = 50
    percent = 0.8
    a = 10*np.arange(m)[:, None] + np.arange(n)
    #sigma_set = (np.random.choice(m, M, replace=True), np.random.choice(n, M, replace=True))

    sigma_set = generate_sigma_set((m, n), percent)
    print(sigma_set[0].size)
    r = 2
    x, it, err = approximate(a, sigma_set, r)
    print('norm of x - a: {}'.format(norm(x.full_matrix() - a)))

    print('full matrix x:')
    print(x.full_matrix())

    print('-'*80)

    print('full matrix a: ')
    print(a)

    print('-'*80)

    print('delta x and a')
    print(x.full_matrix() - a)

    plt.plot(np.arange(len(err))[100:], err[100:])
    plt.show()