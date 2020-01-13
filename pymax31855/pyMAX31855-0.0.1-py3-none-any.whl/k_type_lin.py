##file: k_type_lin.py
#author: Menschel (C) 2019
#purpose: separate k_type linerization from max 31855
 
# we need math in order to linearize the k-type thermocouple by NIST data
import math

# extract of https://srdata.nist.gov/its90/download/type_k.tab
# 
# ************************************
# * This section contains coefficients for type K thermocouples for
# * the two subranges of temperature listed below.  The coefficients 
# * are in units of °C and mV and are listed in the order of constant 
# * term up to the highest order.  The equation below 0 °C is of the form 
# * E = sum(i=0 to n) c_i t^i.
# *
# * The equation above 0 °C is of the form 
# * E = sum(i=0 to n) c_i t^i + a0 exp(a1 (t - a2)^2).
# *
# *     Temperature Range (°C)
# *        -270.000 to 0.000 
# *         0.000 to 1372.000
# ************************************
# name: reference function on ITS-90
# type: K
# temperature units: °C
# emf units: mV
# range: -270.000, 0.000, 10
#   0.000000000000E+00
#   0.394501280250E-01
#   0.236223735980E-04
#  -0.328589067840E-06
#  -0.499048287770E-08
#  -0.675090591730E-10
#  -0.574103274280E-12
#  -0.310888728940E-14
#  -0.104516093650E-16
#  -0.198892668780E-19
#  -0.163226974860E-22
# range: 0.000, 1372.000, 9
#  -0.176004136860E-01
#   0.389212049750E-01
#   0.185587700320E-04
#  -0.994575928740E-07
#   0.318409457190E-09
#  -0.560728448890E-12
#   0.560750590590E-15
#  -0.320207200030E-18
#   0.971511471520E-22
#  -0.121047212750E-25
# exponential:
#  a0 =  0.118597600000E+00
#  a1 = -0.118343200000E-03
#  a2 =  0.126968600000E+03
t2v_coeff_m270_0 = [
                    0.000000000000E+00,
                    0.394501280250E-01,
                    0.236223735980E-04,
                    -0.328589067840E-06,
                    -0.499048287770E-08,
                    -0.675090591730E-10,
                    -0.574103274280E-12,
                    -0.310888728940E-14,
                    -0.104516093650E-16,
                    -0.198892668780E-19,
                    -0.163226974860E-22,
                    ]
t2v_coeff_0_1372 = [
                    -0.176004136860E-01,
                    0.389212049750E-01,
                    0.185587700320E-04,
                    -0.994575928740E-07,
                    0.318409457190E-09,
                    -0.560728448890E-12,
                    0.560750590590E-15,
                    -0.320207200030E-18,
                    0.971511471520E-22,
                    -0.121047212750E-25,                  
                   ]

t2v_exp = [0.118597600000E+00,
           -0.118343200000E-03,
           0.126968600000E+03,
           ]

def temp2voltage(t_degC):
    """return the linearized temperature for a voltage produced by a K-Type thermocouple according to NIST
       @param t_degC: temperature in deg C
       @return: voltage in millivolt
    """
    if t_degC < 0:
        coeffs = t2v_coeff_m270_0
        exp_offset = 0
    else:
        coeffs = t2v_coeff_0_1372
        exp_offset = t2v_exp[0] * math.exp( t2v_exp[1] * math.pow( t_degC - t2v_exp[2] ,2) )
    
    u_mv = sum(coeffs[i]*math.pow(t_degC,i) for i in range(len(coeffs))) + exp_offset
    
    return u_mv


# extract of https://srdata.nist.gov/its90/download/type_k.tab
# 
# ************************************
# * This section contains coefficients of approximate inverse 
# * functions for type K thermocouples for the subranges of 
# * temperature and voltage listed below. The range of errors of 
# * the approximate inverse function for each subrange is also given. 
# * The coefficients are in units of °C and mV and are listed in 
# * the order of constant term up to the highest order.
# * The equation is of the form t_90 = d_0 + d_1*E + d_2*E^2 + ... 
# *     + d_n*E^n,
# * where E is in mV and t_90 is in °C.
# *
# *    Temperature        Voltage            Error 
# *      range              range            range
# *      (°C)               (mV)             (° C)
# *    -200. to 0.      -5.891 to 0.000    -0.02 to 0.04
# *     0. to 500.      0.000 to 20.644    -0.05 to 0.04
# *     500. to 1372.   20.644 to 54.886   -0.05 to 0.06
# ********************************************************
# Inverse coefficients for type K:
#  
# Temperature  -200.             0.           500.
#   Range:        0.           500.          1372.
#  
#   Voltage   -5.891          0.000         20.644
#   Range:     0.000         20.644         54.886
#  
#          0.0000000E+00  0.000000E+00 -1.318058E+02
#          2.5173462E+01  2.508355E+01  4.830222E+01
#         -1.1662878E+00  7.860106E-02 -1.646031E+00
#         -1.0833638E+00 -2.503131E-01  5.464731E-02
#         -8.9773540E-01  8.315270E-02 -9.650715E-04
#         -3.7342377E-01 -1.228034E-02  8.802193E-06
#         -8.6632643E-02  9.804036E-04 -3.110810E-08
#         -1.0450598E-02 -4.413030E-05  0.000000E+00
#         -5.1920577E-04  1.057734E-06  0.000000E+00
#          0.0000000E+00 -1.052755E-08  0.000000E+00
#  
#   Error      -0.02          -0.05          -0.05
#   Range:      0.04           0.04           0.06
#      

m2t_coeff_m5891_0 = [
                    0.0000000E+00,
                    2.5173462E+01,
                    -1.1662878E+00,
                    -1.0833638E+00,
                    -8.9773540E-01,
                    -3.7342377E-01,
                    -8.6632643E-02,
                    -1.0450598E-02,
                    -5.1920577E-04,
                    #0.0000000E+00, no need to calculate this zero value
                    ]

m2t_coeff_0_20644 = [
                     0.000000E+00,
                     2.508355E+01,
                     7.860106E-02,
                     -2.503131E-01,
                     8.315270E-02,
                     -1.228034E-02,
                     9.804036E-04,
                     -4.413030E-05,
                     1.057734E-06,
                     -1.052755E-08,
                     ]

m2t_coeff_20644_54886 = [
                         -1.318058E+02,
                         4.830222E+01,
                         -1.646031E+00,
                         5.464731E-02,
                         -9.650715E-04,
                         8.802193E-06,
                         -3.110810E-08,
                         #0.000000E+00, no need to calculate this zero value
                         #0.000000E+00,
                         #0.000000E+00,
                         ]

def voltage2temp(u_mv):
    """return the voltage for a temperature of a K-Type thermocouple according to NIST
       @param u_mv: millivolt
       @return: temperature in deg C
    """
    if u_mv < -5.891:
        coeffs = m2t_coeff_m5891_0
    elif u_mv < 20.644:
        coeffs = m2t_coeff_0_20644
    elif u_mv < 54.886:
        coeffs = m2t_coeff_20644_54886
    else:
        raise ValueError("Out of Range")
    t_degC = sum(coeffs[i]*math.pow(u_mv,i) for i in range(len(coeffs)))
    return t_degC