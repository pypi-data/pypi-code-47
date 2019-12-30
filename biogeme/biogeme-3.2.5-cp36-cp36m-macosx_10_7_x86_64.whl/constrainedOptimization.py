"""
Working file for constrained optimization. Will be transferred to optimization.py when fimished and tested.

:author: Michel Bierlaire
:date: Mon Dec 23 16:36:03 2019

"""



import numpy as np
import biogeme.exceptions as excep
import scipy.optimize as sc
import scipy.linalg as la
import inspect as ip
import biogeme.messaging as msg

def project(x,bounds):
    """Project a point onto the feasible domain defined by the bounds.

    :param x: point to project
    :type x: numpy.array

    :param bounds: list of tuples (ell,u) containing the lower and upper bounds
          for each free parameter
    :type bounds: list(tuple)

    :return: projected point
    :rtype: numpy.array
    """

    if len(x) != len(bounds):
        raise excep.biogemeError(f"Incompatible size: {len(x)} and {len(bounds)}")

    y = np.asarray([np.minimum(bounds[i][1],np.maximum(bounds[i][0],x[i])) for i in range(len(x))])
    return y

def feasible(x, bounds):
    """ Check if point verifies the bound constraints

    :param x: point to project
    :type x: numpy.array

    :param bounds: list of tuples (ell,u) containing the lower and upper bounds
          for each variable
    :type bounds: list(tuple)

    :return: True if x is feasible, False otherwise.
    :rtype: bool
    """
    if len(x) != len(bounds):
        raise excep.biogemeError(f"Incompatible size: {len(x)} and {len(bounds)}")
    for i in range(len(x)):
        if x[i] < bounds[i][0]:
            return False
        if x[i] > bounds[i][1]:
            return False
    return True

def breakPoints(x, d, radius, bounds):
    """ Projects the direction d, starting from x, on the intersection of
the bound constraints, and the trust region of given radius.

    :param x: current point
    :type x: numpy.array

    :param d: search direction
    :type d: numpy.array

    :param radius: radius of the trust region
    :type radius: float

    :param bounds: list of tuples (ell,u) containing the lower and upper bounds
          for each free parameter
    :type bounds: list(tuple)

    :return: list of tuple (index, value), where index is the index of the variable, and value the value of the corresponding breakpoint.
    :rtype: list(tuple(int,float))

    """
    n = len(x)
    if len(d) != n:
        raise excep.biogemeError(f"Incompatible size: {n} and {len(d)}")
    if len(bounds) != n:
        raise excep.biogemeError(f"Incompatible size: {n} and {len(bounds)}")

    breakPoints = [np.minimum(bounds[i][1]-x[i],radius)/d[i] if d[i] > np.finfo(float).eps else np.maximum(bounds[i][0]-x[i],-radius)/d[i] if d[i] < -np.finfo(float).eps else 0 for i in range(n)]

    if any(b < 0 for b in breakPoints):
        raise excep.biogemeError("Infeasible point")

    return sorted(enumerate(breakPoints), key=lambda x:x[1])

def generalizedCauchyPoint(xk,gk,H,bounds,radius):
    """ Implementation of Step 2 of the Specific Algorithm by `Conn et al. (1988)`_. 

    .. _`Conn et al. (1988)`: https://www.ams.org/journals/mcom/1988-50-182/S0025-5718-1988-0929544-3/S0025-5718-1988-0929544-3.pdf

    :param xk: current point
    :type xk: numpy.array. Dimension n.

    :param gk: vector g involved in the quadratic model definition.
    :type gk: numpy.array. Dimension n.
    
    :param H: matrix H involved in the quadratic model definition.
    :type H: numpy.array. Dimension n x n.

    :param bounds: list of tuples (ell,u) containing the lower and upper bounds
          for each free parameter
    :type bounds: list(tuple)

    :param radius: radius of the trust region
    :type radius: float

    :return: generalized Cauchy point based on inexact line search.
    :rtype: numpy.array. Dimension n.

    """

    x = xk
    g = gk - H @ xk
    d = -gk
    
    bp = breakPoints(xk,d,radius,bounds)

    currentBreakPoint = 0
    while currentBreakPoint < len(bp) and bp[currentBreakPoint][1] == 0.0:
        d[bp[currentBreakPoint][0]] == 0.0
        currentBreakPoint += 1

    fprime = np.inner(gk,d)

    if fprime >= 0:
        return x

    fsecond = np.inner(d, H @ d)

    #for b in range(currentBreakPoint,len(bp)):
        
    
    tmin = 0
    tmax = np.finfo(np.float).max
    t = radius / np.inner(g,g)
    mx = model(x)
    logger.debug(f'x={x}')
    logger.debug(f'g={g}')
    while tmax - tmin > np.finfo(np.float).eps:
        logger.debug(f't={t}')
        logger.debug(f'x - t * g = {x - t * g}')
        p = project(x - t * g,bounds)
        logger.debug(f'p={p}')
        s = p - x
        logger.debug(f's={s}')
        gs = np.inner(g,s)
        logger.debug(f'g^Ts = {gs}')
        snorm = la.norm(s)
        logger.debug(f'snorm={snorm}')
        m = model(p)

        logger.debug(f'{m} <= {mx} + {klbs} * {gs} = {mx + klbs * gs}')
        logger.debug(f'')
        if snorm > radius or m > mx + kubs * gs:
            logger.debug(f'tmax={t}')
            tmax = t
        elif snorm < kfrd * radius and m < mx + klbs * gs:
            logger.debug(f'tmin={t}')
            tmin = t
        else:
            return p

        if tmax == np.finfo(np.float).max:
            t = 2 * t
        else:
            t = 0.5 * (tmin + tmax)
    
    logger.warning(f'Inexact line search is not converging')
    return x

