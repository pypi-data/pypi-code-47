""" Implements various models.

:author: Michel Bierlaire
:date: Fri Mar 29 17:13:14 2019
"""

import numpy as np
import biogeme.exceptions as excep

#from biogeme.expressions import Plus, Minus, Times, Divide, Power, bioMin, bioMax, And, Or, Equal, NotEqual, LessOrEqual, GreaterOrEqual, Less, Greater, UnaryMinus, MonteCarlo, bioNormalPdf, bioNormalCdf, PanelLikelihoodTrajectory, exp, log, Derive, Integrate, bioDraws, Numeric, Variable, DefineVariable, RandomVariable, Beta, bioLogLogit, bioLogLogitFullChoiceSet, bioMultSum, Elem, bioLinearUtility

from biogeme.expressions import _bioLogLogit, _bioLogLogitFullChoiceSet, exp, log, Elem, bioMin, bioMax, Numeric, Beta, bioMultSum, Variable

def loglogit(V,av,i):
    """The logarithm of the logit model 

    The model is defined as 
    
    .. math:: \\frac{a_i e^{V_i}}{\\sum_{i=1}^J a_j e^{V_j}}

    :param V: dict of objects representing the utility functions of
              each alternative, indexed by numerical ids.

    :type V: dict(int:biogeme.expressions.Expression)

    :param av: dict of objects representing the availability of each
               alternative (:math:`a_i` in the above formula), indexed
               by numerical ids. Must be consistent with V, or
               None. In this case, all alternatives are supposed to be
               always available.

    :type av: dict(int:biogeme.expressions.Expression)

    :param i: id of the alternative for which the probability must be
              calculated.
    :type i: int

    :return: choice probability of alternative number i.
    :rtype: biogeme.expressions.Expression
    """

    if av is None:
        return _bioLogLogitFullChoiceSet(V,av=None,choice=i)
    else:
        return _bioLogLogit(V,av,i)

def logit(V,av,i):
    """The logit model 

    The model is defined as 
    
    .. math:: \\frac{a_i e^{V_i}}{\\sum_{i=1}^J a_j e^{V_j}}

    :param V: dict of objects representing the utility functions of
              each alternative, indexed by numerical ids.

    :type V: dict(int:biogeme.expressions.Expression)

    :param av: dict of objects representing the availability of each
               alternative (:math:`a_i` in the above formula), indexed
               by numerical ids. Must be consistent with V, or
               None. In this case, all alternatives are supposed to be
               always available.

    :type av: dict(int:biogeme.expressions.Expression)

    :param i: id of the alternative for which the probability must be
              calculated.
    :type i: int

    :return: choice probability of alternative number i.
    :rtype: biogeme.expressions.Expression

    """
    if av is None:
        return exp(_bioLogLogitFullChoiceSet(V,av=None,choice=i))
    else:
        return exp(_bioLogLogit(V,av,i))


def boxcox(x,l):
    """Box-Cox transform 

    .. math:: B(x,\\ell) = \\frac{x^{\\ell}-1}{\\ell}. 

    It has the property that 

    .. math:: \\lim_{\\ell \\to 0} B(x,\\ell)=\\log(x).

    :param x: a variable to transform.
    :type x: biogeme.expressions.Expression
    :param l: parameter of the transformation.
    :type l: biogeme.expressions.Expression
    
    :return: the Box-Cox transform
    :rtype: biogeme.expressions.Expression
    """
    if type(l) is float or type(l) is int:
        if l < 0:
            raise excep.biogemeError(f"The parameter of a Box-Cox transform must be non negative, and not {l}.")
        if l < np.sqrt(np.finfo(np.float64).eps):
            if type(x) is float or type(x) is int:
                return np.log(x)
            else:
                return log(x)
        else:
            return (x**l-1.0)/l
    else:
        return Elem({0:(x**l-1.0)/l,1:log(x)},l < Numeric(np.sqrt(np.finfo(np.float64).eps)))
                

def piecewise(variable,thresholds):
    raise excep.biogemeError("The function 'piecewise' is obsolete and has been replaced by 'piecewiseVariables'. Its use has changed. Please refer to the documentation.")

def piecewiseVariables(variable,thresholds):
    """Generate the variables to include in a piecewise linear specification.

    If there are K thresholds, K-1 variables are generated. The first
    and last thresholds can be defined as None, corresponding to
    :math:`-\\infty` and :math:`+\infty`,respectively. If :math:`t` is
    the variable of interest, for each interval :math:`[a:a+b[`, we
    define a variable defined as:

    .. math:: x_{Ti} =\\left\\{  \\begin{array}{ll} 0 & \\text{if } t < a \\\\ t-a & \\text{if } a \\leq t < a+b \\\\ b  & \\text{otherwise}  \\end{array}\\right. \\;\\;\\;x_{Ti} = \\max(0,\\min(t-a,b)) 

    :param variable: variable for which we need the piecewise linear
       transform. The expression itself or the name of the variable can be given.
    :type variable: biogeme.expressions.Expression or str

    :param thresholds: list of thresholds
    :type thresholds: list(float)

    :return: list of variables to for the piecewise linear specification.
    :rtype: list(biogeme.expressions.Expression)

    .. seealso:: piecewiseFormula
    """
    I = len(thresholds)
    if all(t is None for t in thresholds):
        raise excep.biogemeError('All thresholds for the piecewise linear specification are set to None.')
    if None in thresholds[1:-1]:
        raise excep.biogemeError('For piecewise linear specification, only the first and the last thresholds can be None')

    # If the name of the variable is given, we transform it into an expression.
    if isinstance(variable,str):
        variable = Variable(variable)

    # First variable
    if thresholds[0] is None:
        results = [bioMin(variable,thresholds[1])]
    else:
        b = thresholds[1]-thresholds[0]
        results = [bioMax(Numeric(0),bioMin(variable - thresholds[0],b))]
    
    for i in range(1,I-2):
        b = thresholds[i+1]-thresholds[i]
        results += [bioMax(Numeric(0),bioMin(variable - thresholds[i],b))]

    # Last variable
    if thresholds[-1] is None:
        results += [bioMax(0,variable - thresholds[-2])]
    else:
        b = thresholds[-1]-thresholds[-2]
        results += [bioMax(Numeric(0),bioMin(variable - thresholds[-2],b))]
    return results

def piecewiseFormula(variable,thresholds,initialBetas = None):
    """Generate the formula for a piecewise linear specification.

    If there are K thresholds, K-1 variables are generated. The first
    and last thresholds can be defined as None, corresponding to
    :math:`-\\infty` and :math:`+\infty`,respectively. If :math:`t` is
    the variable of interest, for each interval :math:`[a:a+b[`, we
    define a variable defined as:
  
    .. math:: x_{Ti} =\\left\\{  \\begin{array}{ll} 0 & \\text{if } t < a \\\\ t-a & \\text{if } a \\leq t < a+b \\\\ b  & \\text{otherwise}  \\end{array}\\right. \\;\\;\\;x_{Ti} = \\max(0,\\min(t-a,b)) 

    New variables and new parameters are automatically created.

    :param variable: variable for which we need the piecewise linear
       transform.  
    :type string: name of the variable.

    :param thresholds: list of thresholds
    :type thresholds: list(float)

    :param initialBetas: list of values to initialize the beta
                         parameters.  The number of entries should be
                         the number of thresholds, plus one. If None,
                         the value of zero is used. Default: none.
    :type initialBetas: list(float)

    :return: expression of  the piecewise linear specification.
    :rtype: biogeme.expressions.Expression

    """

    I = len(thresholds)
    if all(t is None for t in thresholds):
        raise excep.biogemeError('All thresholds for the piecewise linear specification are set to None.')
    if None in thresholds[1:-1]:
        raise excep.biogemeError('For piecewise linear specification, only the first and the last thresholds can be None')
    if initialBetas is not None:
        if len(initialBetas) != I-1:
            raise excep.biogemeError(f'As there are {I} thresholds, a total of {I-1} values are needed to initialize the parameters. But {len(initialBetas)} are provided')
        
    vars = piecewiseVariables(Variable(f'{variable}'),thresholds)
    terms = []

    # First term
    betaValues = [0 if initialBetas is None else initialBetas[i] for i in range(I-1)]
    if thresholds[0] is None:
        beta = Beta(f'beta_{variable}_lessthan_{thresholds[1]}',betaValues[0],None,None,0)
    else:
        beta = Beta(f'beta_{variable}_{thresholds[0]}_{thresholds[1]}',betaValues[0],None,None,0)

    terms = [beta * vars[0]]

    # All terms, except the last
    for i in range(1,I-2):
        beta = Beta(f'beta_{variable}_{thresholds[i]}_{thresholds[i+1]}',betaValues[i],None,None,0)
        
        terms += [beta * vars[i]]

    # Last term
    if thresholds[-1] is None:
        beta = Beta(f'beta_{variable}_{thresholds[-2]}_more',betaValues[-2],None,None,0)
    else:
        beta = Beta(f'beta_{variable}_{thresholds[-2]}_{thresholds[-1]}',betaValues[-2],None,None,0)
    terms += [beta * vars[-1]]
    return bioMultSum(terms)

def piecewiseFunction(x,thresholds,betas):
    """Plot a piecewise linear specification.

    If there are K thresholds, K-1 variables are generated. The first
    and last thresholds can be defined as None, corresponding to
    :math:`-\\infty` and :math:`+\infty`,respectively. If :math:`t` is
    the variable of interest, for each interval :math:`[a:a+b[`, we
    define a variable defined as:
  
    .. math:: x_{Ti} =\\left\\{  \\begin{array}{ll} 0 & \\text{if } t < a \\\\ t-a & \\text{if } a \\leq t < a+b \\\\ b  & \\text{otherwise}  \\end{array}\\right. \\;\\;\\;x_{Ti} = \\max(0,\\min(t-a,b)) 

    :param x: value at which the piecewise specification must be avaluated
    :type x: float

    :param thresholds: list of thresholds
    :type thresholds: list(float)

    :param betas: list of the beta parameters.  The number of entries
                         should be the number of thresholds, plus
                         one.
    :type betas: list(float)

    :return: value of the numpy function
    :rtype: float
    """
    I = len(thresholds)
    if all(t is None for t in thresholds):
        raise excep.biogemeError('All thresholds for the piecewise linear specification are set to None.')
    if None in thresholds[1:-1]:
        raise excep.biogemeError('For piecewise linear specification, only the first and the last thresholds can be None')
    if len(betas) != I-1:
        raise excep.biogemeError(f'As there are {I} thresholds, a total of {I-1} values are needed to initialize the parameters. But {len(betas)} are provided')

    # If the first threshold is not -infinity, we need to check if
    # x is beyond it.
    if thresholds[0] is not None:
        if x < thresholds[0]:
            return 0
    rest = x
    total = 0
    for i in range(len(betas)):
        if thresholds[i+1] is None:
            total += betas[i] * rest
            return total
        elif x < thresholds[i+1]:
            total += betas[i] * rest
            return total
        else:
            total += betas[i] * (thresholds[i+1] - (0 if thresholds[i] is None else thresholds[i]))
            rest = x - thresholds[i+1]
    return total
    
    
def logmev(V,logGi,av,choice) :
    """ Log of the choice probability for a MEV model.
    
    :param V: dict of objects representing the utility functions of
              each alternative, indexed by numerical ids.

    :type V: dict(int:biogeme.expressions.Expression)

    :param logGi: a dictionary mapping each alternative id with the function

    .. math:: \\ln \\frac{\\partial G}{\\partial y_i}(e^{V_1},\\ldots,e^{V_J})
        
    where :math:`G` is the MEV generating function. If an alternative :math:`i` is not available, then :math:`G_i = 0`.

    :type logGi: dict(int:biogeme.expressions.Expression)

    :param av: dict of objects representing the availability of each
               alternative (:math:`a_i` in the above formula), indexed
               by numerical ids. Must be consistent with V, or
               None. In this case, all alternatives are supposed to be
               always available.

    :type av: dict(int:biogeme.expressions.Expression)

    :param choice: id of the alternative for which the probability must be
              calculated.
    :type choice: biogeme.expressions.Expression

    :return: log of the choice probability of the MEV model, given by
    
    .. math:: V_i + \\ln G_i(e^{V_1},\\ldots,e^{V_J}) - \\ln\\left(\\sum_j e^{V_j + \\ln G_j(e^{V_1},\\ldots,e^{V_J})}\\right)

    """
    H = {i:v + logGi[i] for i,v in V.items()}
    if av is None:
        logP = _bioLogLogitFullChoiceSet(H,av=None,choice=choice)
    else:
        logP = _bioLogLogit(H,av,choice)
    return logP

def mev(V,logGi,av,choice) :
    """ Choice probability for a MEV model.

    :param V: dict of objects representing the utility functions of
              each alternative, indexed by numerical ids.

    :type V: dict(int:biogeme.expressions.Expression)


    :param logGi: a dictionary mapping each alternative id with the function

    .. math:: \\ln \\frac{\\partial G}{\\partial y_i}(e^{V_1},\\ldots,e^{V_J})
        
    where :math:`G` is the MEV generating function. If an alternative :math:`i` is not available, then :math:`G_i = 0`.

    :param av: dict of objects representing the availability of each
               alternative (:math:`a_i` in the above formula), indexed
               by numerical ids. Must be consistent with V, or
               None. In this case, all alternatives are supposed to be
               always available.

    :type av: dict(int:biogeme.expressions.Expression)

    :param choice: id of the alternative for which the probability must be
              calculated.
    :type choice: biogeme.expressions.Expression

    :return: Choice probability of the MEV model, given by

    .. math:: \\frac{e^{V_i + \\ln G_i(e^{V_1},\\ldots,e^{V_J})}}{\\sum_j e^{V_j + \\ln G_j(e^{V_1},\\ldots,e^{V_J})}}

    """
    return exp(logmev(V,logGi,av,choice))

def logmev_endogenousSampling(V,logGi,av,correction,choice) :
    """Log of choice probability for a MEV model, including the correction for endogenous sampling as proposed by `Bierlaire, Bolduc and McFadden (2008)`_.

    .. _`Bierlaire, Bolduc and McFadden (2008)`: http://dx.doi.org/10.1016/j.trb.2007.09.003

    :param V: dict of objects representing the utility functions of
              each alternative, indexed by numerical ids.


    :param logGi: a dictionary mapping each alternative id with the function

    .. math:: \\ln \\frac{\\partial G}{\\partial y_i}(e^{V_1},\\ldots,e^{V_J})
        
    where :math:`G` is the MEV generating function. If an alternative :math:`i` is not available, then :math:`G_i = 0`.

    :type logGi: dict(int:biogeme.expressions.Expression)

    :param av: dict of objects representing the availability of each
               alternative (:math:`a_i` in the above formula), indexed
               by numerical ids. Must be consistent with V, or
               None. In this case, all alternatives are supposed to be
               always available.

    :type av: dict(int:biogeme.expressions.Expression)

    
    :param correction: a dict of expressions for the correstion terms
                       of each alternative.
    :type correction: dict(int:biogeme.expressions.Expression)

    :param choice: id of the alternative for which the probability must be
              calculated.
    :type choice: biogeme.expressions.Expression

    :return: log of the choice probability of the MEV model, given by

    .. math:: V_i + \\ln G_i(e^{V_1},\\ldots,e^{V_J}) + \\omega_i - \\ln\\left(\\sum_j e^{V_j + \\ln G_j(e^{V_1},\\ldots,e^{V_J})+ \\omega_j}\\right)

    where :math:`\\omega_i` is the correction term for alternative :math:`i`.
    """
    H = {i: v + logGi[i] + correction[i] for i,v in V.items()}
    logP = _bioLogLogit(H,av,choice)
    return logP



def mev_endogenousSampling(V,logGi,av,correction,choice) :
    """Choice probability for a MEV model, including the correction for endogenous sampling as proposed by `Bierlaire, Bolduc and McFadden (2008)`_.

    .. _`Bierlaire, Bolduc and McFadden (2008)`: http://dx.doi.org/10.1016/j.trb.2007.09.003

    :param V: dict of objects representing the utility functions of
              each alternative, indexed by numerical ids.


    :param logGi: a dictionary mapping each alternative id with the function

    .. math:: \\ln \\frac{\\partial G}{\\partial y_i}(e^{V_1},\\ldots,e^{V_J})
        
    where :math:`G` is the MEV generating function. If an alternative :math:`i` is not available, then :math:`G_i = 0`.

    :type logGi: dict(int:biogeme.expressions.Expression)

    :param av: dict of objects representing the availability of each
               alternative (:math:`a_i` in the above formula), indexed
               by numerical ids. Must be consistent with V, or
               None. In this case, all alternatives are supposed to be
               always available.

    :type av: dict(int:biogeme.expressions.Expression)

    
    :param correction: a dict of expressions for the correstion terms
                       of each alternative.
    :type correction: dict(int:biogeme.expressions.Expression)

    :param choice: id of the alternative for which the probability must be
              calculated.
    :type choice: biogeme.expressions.Expression

    :return: log of the choice probability of the MEV model, given by

    .. math:: V_i + \\ln G_i(e^{V_1},\\ldots,e^{V_J}) + \\omega_i - \\ln\\left(\\sum_j e^{V_j + \\ln G_j(e^{V_1},\\ldots,e^{V_J})+ \\omega_j}\\right)

    where :math:`\\omega_i` is the correction term for alternative :math:`i`.
    """
    return exp(logmev_endogenousSampling(V,logGi,av,correction,choice))


def getMevForNested(V,availability,nests) :
    """ Implements the MEV generating function for the nested logit model

    :param V: dict of objects representing the utility functions of
              each alternative, indexed by numerical ids.
    :type V: dict(int:biogeme.expressions.Expression)

    :param availability: dict of objects representing the availability of each
               alternative, indexed
               by numerical ids. Must be consistent with V, or
               None. In this case, all alternatives are supposed to be
               always available.

    :type availability: dict(int:biogeme.expressions.Expression)

    :param nests: A tuple containing as many items as nests. Each item is also a tuple containing two items

          - an object of type biogeme.expressions.Expression  representing the nest parameter,
          - a list containing the list of identifiers of the alternatives belonging to the nest.

      Example::

          nesta = MUA , [1,2,3]
          nestb = MUB , [4,5,6]
          nests = nesta, nestb


    
    :type nests: tuple

    :return: a dictionary mapping each alternative id with the function

    .. math:: \\ln \\frac{\\partial G}{\\partial y_i}(e^{V_1},\\ldots,e^{V_J}) = e^{(\\mu_m-1)V_i} \\left(\\sum_{i=1}^{J_m} e^{\\mu_m V_i}\\right)^{\\frac{1}{\\mu_m}-1}
    
    where :math:`m` is the (only) nest containing alternative :math:`i`, and :math:`G` is the MEV generating function.

    :rtype: dict(int:biogeme.expressions.Expression)

    """

    
    
    #y = {i:exp(v) for i,v in V.items()}
    logGi = {}
    for m in nests:
        if availability is None:
            sumdict = [exp(m[0] * V[i]) for i in m[1]]
        else:
            sumdict = [Elem({0:0.0,1: exp(m[0] * V[i])},availability[i]!=Numeric(0)) for i in m[1]]
        sum = bioMultSum(sumdict)
        for i in m[1]:
            logGi[i] = (m[0]-1.0) * V[i] + (1.0/m[0] - 1.0) * log(sum) 
    return logGi

def getMevForNestedMu(V,availability,nests,mu) :
    """Implements the MEV generating function for the nested logit model,
including the scale parameter

    :param V: dict of objects representing the utility functions of
              each alternative, indexed by numerical ids.
    :type V: dict(int:biogeme.expressions.Expression)

    :param availability: dict of objects representing the availability of each
               alternative, indexed
               by numerical ids. Must be consistent with V, or
               None. In this case, all alternatives are supposed to be
               always available.

    :type availability: dict(int:biogeme.expressions.Expression)

    :param nests: A tuple containing as many items as nests. Each item is also a tuple containing two items

          - an object of type biogeme.expressions.Expression  representing the nest parameter,
          - a list containing the list of identifiers of the alternatives belonging to the nest.

      Example::

          nesta = MUA , [1,2,3]
          nestb = MUB , [4,5,6]
          nests = nesta, nestb

    :type nests: tuple

    :param mu: scale parameter
    :type mu: biogeme.expressions.Expression

    :return: a dictionary mapping each alternative id with the function

    .. math:: \\frac{\\partial G}{\\partial y_i}(e^{V_1},\\ldots,e^{V_J}) = \\mu e^{(\\mu_m-1)V_i} \\left(\\sum_{i=1}^{J_m} e^{\\mu_m V_i}\\right)^{\\frac{\\mu}{\\mu_m}-1}
    
    where :math:`m` is the (only) nest containing alternative :math:`i`, and :math:`G` is the MEV generating function.

    :rtype: dict(int:biogeme.expressions.Expression)

    """

    #y = {i:exp(v) for i,v in V.items()}
    logGi = {}
    for m in nests:
        if availability is None:
            sumdict = [exp(m[0] * V[i]) for i in m[1]]
        else:
            sumdict = [Elem({0:0.0,1: exp(m[0] * V[i])},availability[i]!=0) for i in m[1]]
        sum = bioMultSum(sumdict)
        for i in m[1]:
            logGi[i] = log(mu) + (m[0]-1.0) * V[i] + (mu/m[0] - 1.0) * log(sum) 
    return logGi




def nested(V,availability,nests,choice) :
    """Implements the nested logit model as a MEV model. 
    
    :param V: dict of objects representing the utility functions of
              each alternative, indexed by numerical ids.
    :type V: dict(int:biogeme.expressions.Expression)

    :param availability: dict of objects representing the availability
                         of each alternative, indexed by numerical
                         ids. Must be consistent with V, or None. In
                         this case, all alternatives are supposed to
                         be always available.

    :type availability: dict(int:biogeme.expressions.Expression)

    :param nests: A tuple containing as many items as nests. Each item is also a tuple containing two items
                  - an object of type biogeme.expressions.Expression  representing the nest parameter,
                  - a list containing the list of identifiers of the alternatives belonging to the nest.

      Example::

          nesta = MUA , [1,2,3]
          nestb = MUB , [4,5,6]
          nests = nesta, nestb
    
    :type nests: tuple

    :param choice: id of the alternative for which the probability must be
              calculated.
    :type choice: biogeme.expressions.Expression

    :return: choice probability for the nested logit model,
             based on the derivatives of the MEV generating function produced
             by the function getMevForNested

    """

    ok, message = checkValidityNestedLogit(V,nests)
    if not ok:
        raise excep.biogemeError(message)
        
    logGi = getMevForNested(V,availability,nests)
    P = mev(V,logGi,availability,choice) 
    return P

def lognested(V,availability,nests,choice) :
    """Implements the log of a nested logit model as a MEV model. 
    
    :param V: dict of objects representing the utility functions of
              each alternative, indexed by numerical ids.

    :type V: dict(int:biogeme.expressions.Expression)

    :param availability: dict of objects representing the availability of each
               alternative (:math:`a_i` in the above formula), indexed
               by numerical ids. Must be consistent with V, or
               None. In this case, all alternatives are supposed to be
               always available.

    :type availability: dict(int:biogeme.expressions.Expression)

    :param nests: A tuple containing as many items as nests. Each item is also a tuple containing two items

          - an object of type biogeme.expressions.Expression  representing the nest parameter,
          - a list containing the list of identifiers of the alternatives belonging to the nest.

      Example::

          nesta = MUA , [1,2,3]
          nestb = MUB , [4,5,6]
          nests = nesta, nestb
    
    :type nests: tuple

    :param choice: id of the alternative for which the probability must be
              calculated.
    :type choice: biogeme.expressions.Expression

    :return: log of choice probability for the nested logit model,
             based on the derivatives of the MEV generating function produced
             by the function getMevForNested

    """
    ok, message = checkValidityNestedLogit(V,nests)
    if not ok:
        raise excep.biogemeError(message)
    logGi = getMevForNested(V,availability,nests)
    logP = logmev(V,logGi,availability,choice) 
    return logP

def nestedMevMu(V,availability,nests,choice,mu) :
    """Implements the nested logit model as a MEV model, where mu is also
    a parameter, if the user wants to test different normalization
    schemes.
 
    :param V: dict of objects representing the utility functions of
              each alternative, indexed by numerical ids.

    :type V: dict(int:biogeme.expressions.Expression)

    :param availability: dict of objects representing the availability of each
               alternative (:math:`a_i` in the above formula), indexed
               by numerical ids. Must be consistent with V, or
               None. In this case, all alternatives are supposed to be
               always available.

    :type availability: dict(int:biogeme.expressions.Expression)

    :param nests: A tuple containing as many items as nests. Each item is also a tuple containing two items

          - an object of type biogeme.expressions.Expression  representing the nest parameter,
          - a list containing the list of identifiers of the alternatives belonging to the nest.

      Example::

          nesta = MUA , [1,2,3]
          nestb = MUB , [4,5,6]
          nests = nesta, nestb
    
    :type nests: tuple

    :param choice: id of the alternative for which the probability must be
              calculated.
    :type choice: biogeme.expressions.Expression

    :param mu: expression producing the value of the top-level scale parameter.
    :type mu:  biogeme.expressions.Expression

    :return: the nested logit choice probability based on the following derivatives of the MEV generating function: 

    .. math:: \\frac{\\partial G}{\\partial y_i}(e^{V_1},\\ldots,e^{V_J}) = \\mu e^{(\\mu_m-1)V_i} \\left(\\sum_{i=1}^{J_m} e^{\\mu_m V_i}\\right)^{\\frac{\\mu}{\\mu_m}-1}

    Where :math:`m` is the (only) nest containing alternative :math:`i`, and
    :math:`G` is the MEV generating function.

    :rtype: biogeme.expressions.Expression

    """
    return exp(lognestedMevMu(V,availability,nests,choice,mu))

def lognestedMevMu(V,availability,nests,choice,mu) :
    """ Implements the log of the nested logit model as a MEV model, where mu is also a parameter, if the user wants to test different normalization schemes.


    :param V: dict of objects representing the utility functions of
              each alternative, indexed by numerical ids.

    :type V: dict(int:biogeme.expressions.Expression)

    :param availability: dict of objects representing the availability of each
               alternative (:math:`a_i` in the above formula), indexed
               by numerical ids. Must be consistent with V, or
               None. In this case, all alternatives are supposed to be
               always available.

    :type availability: dict(int:biogeme.expressions.Expression)

    :param nests: A tuple containing as many items as nests. Each item is also a tuple containing two items

          - an object of type biogeme.expressions.Expression  representing the nest parameter,
          - a list containing the list of identifiers of the alternatives belonging to the nest.

      Example::

          nesta = MUA , [1,2,3]
          nestb = MUB , [4,5,6]
          nests = nesta, nestb
    
    :type nests: tuple

    :param choice: id of the alternative for which the probability must be
              calculated.
    :type choice: biogeme.expressions.Expression

    :param mu: expression producing the value of the top-level scale parameter.
    :type mu:  biogeme.expressions.Expression

    :return: the log of the nested logit choice probability based on the following derivatives of the MEV generating function: 

    .. math:: \\frac{\\partial G}{\\partial y_i}(e^{V_1},\\ldots,e^{V_J}) = \\mu e^{(\\mu_m-1)V_i} \\left(\\sum_{i=1}^{J_m} e^{\\mu_m V_i}\\right)^{\\frac{\\mu}{\\mu_m}-1}

    where :math:`m` is the (only) nest containing alternative :math:`i`, and
    :math:`G` is the MEV generating function.

    :rtype: biogeme.expressions.Expression
    """
    
    y = {i:exp(v) for i,v in V.items()}
    logGi = getMevForNestedMu(V,availability,nests,mu)
    logP = logmev(V,logGi,availability,choice) 
    return logP

def cnl_avail(V,availability,nests,choice):
    """ Same as cnl. Maintained for backward compatibility

    :param V: dict of objects representing the utility functions of
              each alternative, indexed by numerical ids.
    :type V: dict(int:biogeme.expressions.Expression)

    :param availability: dict of objects representing the availability of each
               alternative, indexed
               by numerical ids. Must be consistent with V, or
               None. In this case, all alternatives are supposed to be
               always available.

    :type availability: dict(int:biogeme.expressions.Expression)

    :param nests: a tuple containing as many items as nests. Each item is also a tuple containing two items

          - an object of type biogeme.expressions.Expression  representing the nest parameter,
          - a dictionary mapping the alternative ids with the cross-nested parameters for the corresponding nest. 

        Example::

            alphaA = {1: alpha1a,2: alpha2a, 3: alpha3a, 4: alpha4a,5: alpha5a, 6: alpha6a}
            alphaB = {1: alpha1b,2: alpha2b, 3: alpha3b, 4: alpha4b,5: alpha5b, 6: alpha6b}
            nesta = MUA , alphaA
            nestb = MUB , alphaB
            nests = nesta, nestb

    :type nests: tuple

    :param choice: id of the alternative for which the probability must be
              calculated.
    :type choice: biogeme.expressions.Expression

    :return: choice probability for the cross-nested logit model.
    :rtype: biogeme.expressions.Expression
    """
    return cnl(V,availability,nests,choice)

def cnl(V,availability,nests,choice):
    """ Implements the cross-nested logit model as a MEV model. 

    :param V: dict of objects representing the utility functions of
              each alternative, indexed by numerical ids.
    :type V: dict(int:biogeme.expressions.Expression)

    :param availability: dict of objects representing the availability of each
               alternative, indexed
               by numerical ids. Must be consistent with V, or
               None. In this case, all alternatives are supposed to be
               always available.

    :type available: dict(int:biogeme.expressions.Expression)

    :param nests: a tuple containing as many items as nests. Each item is also a tuple containing two items

          - an object of type biogeme.expressions.Expression  representing the nest parameter,
          - a dictionary mapping the alternative ids with the cross-nested parameters for the corresponding nest. 

        Example::

            alphaA = {1: alpha1a,2: alpha2a, 3: alpha3a, 4: alpha4a,5: alpha5a, 6: alpha6a}
            alphaB = {1: alpha1b,2: alpha2b, 3: alpha3b, 4: alpha4b,5: alpha5b, 6: alpha6b}
            nesta = MUA , alphaA
            nestb = MUB , alphaB
            nests = nesta, nestb

    :type nests: tuple

    :param choice: id of the alternative for which the probability must be
              calculated.
    :type choice: biogeme.expressions.Expression

    :return: choice probability for the cross-nested logit model.
    :rtype: biogeme.expressions.Expression
    

    """
    return exp(logcnl(V,availability,nests,choice))

def logcnl_avail(V,availability,nests,choice) :
    """ Same as logcnl. Maintained for backward compatibility

    :param V: dict of objects representing the utility functions of
              each alternative, indexed by numerical ids.
    :type V: dict(int:biogeme.expressions.Expression)

    :param availability: dict of objects representing the availability of each
               alternative, indexed
               by numerical ids. Must be consistent with V, or
               None. In this case, all alternatives are supposed to be
               always available.

    :type availability: dict(int:biogeme.expressions.Expression)

    :param nests: a tuple containing as many items as nests. Each item is also a tuple containing two items

          - an object of type biogeme.expressions.Expression  representing the nest parameter,
          - a dictionary mapping the alternative ids with the cross-nested parameters for the corresponding nest. 

        Example::

            alphaA = {1: alpha1a,2: alpha2a, 3: alpha3a, 4: alpha4a,5: alpha5a, 6: alpha6a}
            alphaB = {1: alpha1b,2: alpha2b, 3: alpha3b, 4: alpha4b,5: alpha5b, 6: alpha6b}
            nesta = MUA , alphaA
            nestb = MUB , alphaB
            nests = nesta, nestb

    :type nests: tuple

    :param choice: id of the alternative for which the probability must be
              calculated.
    :type choice: biogeme.expressions.Expression

    :return: log of choice probability for the cross-nested logit model.
    :rtype: biogeme.expressions.Expression
    """
    return logcnl(V,availability,nests,choice)

def getMevForCrossNested(V,availability,nests) :
    """ Implements the MEV generating function for the cross-nested logit model as a MEV model. 
    
    :param V: dict of objects representing the utility functions of
              each alternative, indexed by numerical ids.
    :type V: dict(int:biogeme.expressions.Expression)

    :param availability: dict of objects representing the availability of each
               alternative, indexed
               by numerical ids. Must be consistent with V, or
               None. In this case, all alternatives are supposed to be
               always available.

    :type availability: dict(int:biogeme.expressions.Expression)

    :param nests: a tuple containing as many items as nests. Each item is also a tuple containing two items

          - an object of type biogeme.expressions.Expression  representing the nest parameter,
          - a dictionary mapping the alternative ids with the cross-nested parameters for the corresponding nest. 

        Example::

            alphaA = {1: alpha1a,2: alpha2a, 3: alpha3a, 4: alpha4a,5: alpha5a, 6: alpha6a}
            alphaB = {1: alpha1b,2: alpha2b, 3: alpha3b, 4: alpha4b,5: alpha5b, 6: alpha6b}
            nesta = MUA , alphaA
            nestb = MUB , alphaB
            nests = nesta, nestb

    :type nests: tuple

    :param choice: id of the alternative for which the probability must be
              calculated.
    :type choice: biogeme.expressions.Expression

    :return: log of the choice probability for the cross-nested logit model.
    :rtype: biogeme.expressions.Expression

    """
    Gi_terms = {}
    logGi = {}
    for i in V:
        Gi_terms[i] = list()
    biosum = {}
    for m in nests:
        if availability is None:
            biosum = bioMultSum([a**(m[0]) * exp(m[0] * (V[i])) for i,a in m[1].items()])
        else:
            biosum = bioMultSum([availability[i] * a**(m[0]) * exp(m[0] * (V[i])) for i,a in m[1].items()])
        for i,a in m[1].items():
            Gi_terms[i] += [a**(m[0])* exp((m[0]-1) * (V[i])) * biosum **((1.0/m[0])-1.0)]  
    for k in V:
        logGi[k] = log(bioMultSum(Gi_terms[k]))
    return logGi

def logcnl(V,availability,nests,choice) :
    """ Implements the log of the cross-nested logit model as a MEV model. 
    
    :param V: dict of objects representing the utility functions of
              each alternative, indexed by numerical ids.
    :type V: dict(int:biogeme.expressions.Expression)

    :param availability: dict of objects representing the availability of each
               alternative, indexed
               by numerical ids. Must be consistent with V, or
               None. In this case, all alternatives are supposed to be
               always available.

    :type availability: dict(int:biogeme.expressions.Expression)

    :param nests: a tuple containing as many items as nests. Each item is also a tuple containing two items

          - an object of type biogeme.expressions.Expression  representing the nest parameter,
          - a dictionary mapping the alternative ids with the cross-nested parameters for the corresponding nest. 

        Example::

            alphaA = {1: alpha1a,2: alpha2a, 3: alpha3a, 4: alpha4a,5: alpha5a, 6: alpha6a}
            alphaB = {1: alpha1b,2: alpha2b, 3: alpha3b, 4: alpha4b,5: alpha5b, 6: alpha6b}
            nesta = MUA , alphaA
            nestb = MUB , alphaB
            nests = nesta, nestb

    :type nests: tuple

    :param choice: id of the alternative for which the probability must be
              calculated.
    :type choice: biogeme.expressions.Expression

    :return: log of the choice probability for the cross-nested logit model.
    :rtype: biogeme.expressions.Expression

    """
    logGi = getMevForCrossNested(V,availability,nests)        
    logP = logmev(V,logGi,availability,choice) 
    return logP


def cnlmu(V,availability,nests,choice,mu) :
    """ Implements the cross-nested logit model as a MEV model with the homogeneity parameters is explicitly involved

    :param V: dict of objects representing the utility functions of
              each alternative, indexed by numerical ids.
    :type V: dict(int:biogeme.expressions.Expression)

    :param availability: dict of objects representing the availability of each
               alternative, indexed
               by numerical ids. Must be consistent with V, or
               None. In this case, all alternatives are supposed to be
               always available.

    :type availability: dict(int:biogeme.expressions.Expression)

    :param nests: a tuple containing as many items as nests. Each item is also a tuple containing two items

          - an object of type biogeme.expressions.Expression  representing the nest parameter,
          - a dictionary mapping the alternative ids with the cross-nested parameters for the corresponding nest. 

        Example::

            alphaA = {1: alpha1a,2: alpha2a, 3: alpha3a, 4: alpha4a,5: alpha5a, 6: alpha6a}
            alphaB = {1: alpha1b,2: alpha2b, 3: alpha3b, 4: alpha4b,5: alpha5b, 6: alpha6b}
            nesta = MUA , alphaA
            nestb = MUB , alphaB
            nests = nesta, nestb

    :type nests: tuple

    :param choice: id of the alternative for which the probability must be
              calculated.
    :type choice: biogeme.expressions.Expression

    :param mu: Homogeneity parameter :math:`\\mu`.
    :type mu: biogeme.expressions.Expression
    
    :return: choice probability for the cross-nested logit model.
    :rtype: biogeme.expressions.Expression
    """
    return exp(logcnlmu(V,availability,nests,choice,mu))

def getMevForCrossNestedMu(V,availability,nests,mu) :
    """ Implements the MEV generating function for the cross-nested logit model as a MEV model with the homogeneity parameters is explicitly involved.


    :param V: dict of objects representing the utility functions of
              each alternative, indexed by numerical ids.
    :type V: dict(int:biogeme.expressions.Expression)

    :param availability: dict of objects representing the availability of each
               alternative, indexed
               by numerical ids. Must be consistent with V, or
               None. In this case, all alternatives are supposed to be
               always available.

    :type availability: dict(int:biogeme.expressions.Expression)

    :param nests: a tuple containing as many items as nests. Each item is also a tuple containing two items

          - an object of type biogeme.expressions.Expression  representing the nest parameter,
          - a dictionary mapping the alternative ids with the cross-nested parameters for the corresponding nest. 

        Example::

            alphaA = {1: alpha1a,2: alpha2a, 3: alpha3a, 4: alpha4a,5: alpha5a, 6: alpha6a}
            alphaB = {1: alpha1b,2: alpha2b, 3: alpha3b, 4: alpha4b,5: alpha5b, 6: alpha6b}
            nesta = MUA , alphaA
            nestb = MUB , alphaB
            nests = nesta, nestb

    :type nests: tuple

    :param choice: id of the alternative for which the probability must be
              calculated.
    :type choice: biogeme.expressions.Expression

    :param mu: Homogeneity parameter :math:`\\mu`.
    :type mu: biogeme.expressions.Expression
    
    :return: log of the choice probability for the cross-nested logit model.
    :rtype: biogeme.expressions.Expression

    """
    Gi_terms = {}
    logGi = {}
    for i in V:
        Gi_terms[i] = list()
    biosum = {}
    for m in nests:
        if availability is None:
            biosum = bioMultSum([a**(m[0]/mu) * exp(m[0] * (V[i])) for i,a in m[1].items()])
        else:
            biosum = bioMultSum([availability[i] * a**(m[0]/mu) * exp(m[0] * (V[i])) for i,a in m[1].items()])
        for i,a in m[1].items():
            Gi_terms[i] += [a**(m[0]/mu)* exp((m[0]-1) * (V[i])) * biosum **((mu/m[0])-1.0)]  
    for k in V:
        logGi[k] = log(mu * bioMultSum(Gi_terms[k]))
    return logGi

def logcnlmu(V,availability,nests,choice,mu):
    """ Implements the log of the cross-nested logit model as a MEV model with the homogeneity parameters is explicitly involved.


    :param V: dict of objects representing the utility functions of
              each alternative, indexed by numerical ids.
    :type V: dict(int:biogeme.expressions.Expression)

    :param availability: dict of objects representing the availability of each
               alternative, indexed
               by numerical ids. Must be consistent with V, or
               None. In this case, all alternatives are supposed to be
               always available.

    :type availability: dict(int:biogeme.expressions.Expression)

    :param nests: a tuple containing as many items as nests. Each item is also a tuple containing two items

          - an object of type biogeme.expressions.Expression  representing the nest parameter,
          - a dictionary mapping the alternative ids with the cross-nested parameters for the corresponding nest. 

        Example::

            alphaA = {1: alpha1a,2: alpha2a, 3: alpha3a, 4: alpha4a,5: alpha5a, 6: alpha6a}
            alphaB = {1: alpha1b,2: alpha2b, 3: alpha3b, 4: alpha4b,5: alpha5b, 6: alpha6b}
            nesta = MUA , alphaA
            nestb = MUB , alphaB
            nests = nesta, nestb

    :type nests: tuple

    :param choice: id of the alternative for which the probability must be
              calculated.
    :type choice: biogeme.expressions.Expression

    :param mu: Homogeneity parameter :math:`\\mu`.
    :type mu: biogeme.expressions.Expression
    
    :return: log of the choice probability for the cross-nested logit model.
    :rtype: biogeme.expressions.Expression

    """
    logGi = getMevForCrossNestedMu(V,availability,nests,mu)
    logP = logmev(V,logGi,availability,choice) 
    return logP

def checkValidityNestedLogit(V,nests):
    """Verifies if the nested logit model is indeed based on a partition
       of the choice set.

    :param V: dict of objects representing the utility functions of
              each alternative, indexed by numerical ids.
    :type V: dict(int:biogeme.expressions.Expression)
    :param nests: A tuple containing as many items as nests. Each item is also a tuple containing two items

          - an object of type biogeme.expressions.Expression  representing the nest parameter,
          - a list containing the list of identifiers of the alternatives belonging to the nest.

      Example::

          nesta = MUA , [1,2,3]
          nestb = MUB , [4,5,6]
          nests = nesta, nestb

    :type nests: tuple


    :return: a tuple ok,message, where the message explains the
             problem is the nested structure is not OK.
    :rtype: tuple(bool, str)
    """

    ok = True
    message = 'The nested logit model is based on a partition. '
    
    fullChoiceSet = set([i for i,v in V.items()])
    unionOfNests = set.union(*[set(n[1]) for n in nests])
    if fullChoiceSet != unionOfNests:
        ok = False
        d1 = fullChoiceSet.difference(unionOfNests)
        d2 = unionOfNests.difference(fullChoiceSet)
        if d1:
            message += f'Alternatives in the choice set, but not in any nest: {d1}\n'
        if d2:
            message += f'Alternatives in a nest, but not in the choice set: {d2}\n'
    
    # Consider all pairs of nests and verify that the intersection is empty

    allPairs = [(n1, n2) for n1 in nests for n2 in nests if n1 != n2]
    for (n1,n2) in allPairs:
        inter = set(n1[1]).intersection(n2[1])
        if inter:
            ok = False
            message += f'Two nests contain the following alternative(s): {inter}\n'
    return ok, message

