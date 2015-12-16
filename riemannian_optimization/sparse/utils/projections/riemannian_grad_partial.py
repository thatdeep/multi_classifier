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

from ..loss_functions import delta_on_sigma_set
from riemannian_optimization.lowrank_matrix import ManifoldElement


def riemannian_grad_partial(x, a, sigma_set, grad=None):
    """
    Riemannian gradient as a parts from which one can restore it

    If grad is not given,
    compute projection of Euclidean gradient of function
    $\dfrac{1}{2}| P_{\Sigma}(X - A)|_F^2$ at tangent space to manifold at x.

    Projection at x has the form
    RiemannianGrad f(x) = UMV^* + U_p V^* + U V_p^*,
    where M, U_p and V_p^* are returned by function

    Parameters
    ----------
    x : ManifoldElement, shape (M, N)
        Rank-r manifold element in which we compute gradient
    a : sparse matrix, shape (M, N)
        Matrix that we need to approximate -- it has nonzero entries only
        on sigma_set
    sigma_set : array_like
        set of indices in which matrix a can be evaluated
    grad : sparse matrix, shape (M, N), optional
        gradient given for being projected

    Returns
    -------
    out : tuple of ManifoldElements
        matrices M, U_p and V_p^* as partial riemannian gradient
    """
    grad = ManifoldElement(delta_on_sigma_set(x, a, sigma_set)) if grad is None else grad
    left_projected = grad.rdot(x.u.T).rdot(x.u)
    right_projected = grad.dot(x.v.T).dot(x.v)
    return left_projected + right_projected + left_projected.dot(x.v.T).dot(x.v)