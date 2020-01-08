import os
import numpy as np


def test_compilation():
    """
    Compile models and make sure they exist afterwards. Not more, not less
    :return:
    """
    import os
    from compile import compile_xmile
    src = "./test_models/test_trend.stmx"
    dest = "./test_models/test_trend.py"
    target = "py"

    compile_xmile(src, dest, target)
    assert os.path.isfile(dest)

    import os
    from compile import compile_xmile
    src = "./test_models/test_if.stmx"
    dest = "./test_models/test_if.py"
    target = "py"

    compile_xmile(src, dest, target)
    assert os.path.isfile(dest)

    import os
    from compile import compile_xmile
    src = "./test_models/test_step.stmx"
    dest = "./test_models/test_step.py"
    target = "py"

    compile_xmile(src, dest, target)
    assert os.path.isfile(dest)

    from compile import compile_xmile
    src = "./test_models/test_dt_fraction.stmx"
    dest = "./test_models/test_dt_fraction.py"
    target = "py"

    compile_xmile(src, dest, target)
    assert os.path.isfile(dest)

    from compile import compile_xmile
    src = "./test_models/test_dt_rational.stmx"
    dest = "./test_models/test_dt_rational.py"
    target = "py"

    compile_xmile(src, dest, target)
    assert os.path.isfile(dest)

    from compile import compile_xmile
    src = "./test_models/test_no_dimensions.stmx"
    dest = "./test_models/test_no_dimensions.py"
    target = "py"

    compile_xmile(src, dest, target)
    assert os.path.isfile(dest)

    from compile import compile_xmile
    src = "./test_models/test_time.stmx"
    dest = "./test_models/test_time.py"
    target = "py"

    compile_xmile(src, dest, target)
    assert os.path.isfile(dest)

    from compile import compile_xmile
    src = "./test_models/test_smooth.stmx"
    dest = "./test_models/test_smooth.py"
    target = "py"

    compile_xmile(src, dest, target)
    assert os.path.isfile(dest)

    from compile import compile_xmile
    src = "./test_models/test_abs.stmx"
    dest = "./test_models/test_abs.py"
    target = "py"

    compile_xmile(src, dest, target)
    assert os.path.isfile(dest)

    from compile import compile_xmile
    src = "./test_models/test_cos.stmx"
    dest = "./test_models/test_cos.py"
    target = "py"

    compile_xmile(src, dest, target)
    assert os.path.isfile(dest)

    import os
    from compile import compile_xmile
    src = "./test_models/test_tan.stmx"
    dest = "./test_models/test_tan.py"
    target = "py"

    compile_xmile(src, dest, target)
    assert os.path.isfile(dest)

    import os
    from compile import compile_xmile
    src = "./test_models/test_sim_builtins.stmx"
    dest = "./test_models/test_sim_builtins.py"
    target = "py"

    compile_xmile(src, dest, target)
    assert os.path.isfile(dest)

    src = "./test_models/test_random.stmx"
    dest = "./test_models/test_random.py"
    target = "py"

    compile_xmile(src, dest, target)
    assert os.path.isfile(dest)

    import os
    from compile import compile_xmile
    src = "./test_models/test_array.stmx"
    dest = "./test_models/test_array.py"
    target = "py"

    compile_xmile(src, dest, target)
    assert os.path.isfile(dest)

    import os
    from compile import compile_xmile
    src = "./test_models/test_delay.stmx"
    dest = "./test_models/test_delay.py"
    target = "py"

    compile_xmile(src, dest, target)
    assert os.path.isfile(dest)

    import os
    from compile import compile_xmile
    src = "./test_models/test_array_extended.stmx"
    dest = "./test_models/test_array_extended.py"
    target = "py"

    compile_xmile(src, dest, target)
    assert os.path.isfile(dest)

    import os
    from compile import compile_xmile
    src = "./test_models/test_array_2dimensional.stmx"
    dest = "./test_models/test_array_2dimensional.py"
    target = "py"

    compile_xmile(src, dest, target)
    assert os.path.isfile(dest)


def test_trend_model():
    """
    TREND
    :return:
    """
    test_data = {1.0: 0.693147, 1.1: 0.697040160401, 1.2: 0.700323219004, 1.3: 0.703089928837, 1.4: 0.705420181666,
                 1.5: 0.707381895491,
                 1.6: 0.709032694287,
                 1.7: 0.710421386843,
                 1.8: 0.711589257659,
                 1.9: 0.712571186098,
                 2.0: 0.713396611268,
                 2.1: 0.714090360164,
                 2.2: 0.71467335582,
                 2.3: 0.71516322101,
                 2.4: 0.715574791619,
                 2.5: 0.71592055229,
                 2.6: 0.716211005471,
                 2.7: 0.716454983599,
                 2.8: 0.716659912871,
                 2.9: 0.71683203587,
                 3.0: 0.71697659933,
                 3.1: 0.717098012368,
                 3.2: 0.717199979768,
                 3.3: 0.717285614178,
                 3.4: 0.717357530533,
                 3.5: 0.717417925486,
                 3.6: 0.717468644203,
                 3.7: 0.717511236531,
                 3.8: 0.717547004206,
                 3.9: 0.717577040536,
                 4.0: 0.717602263746,
                 4.1: 0.717623444997,
                 4.2: 0.717641231926,
                 4.3: 0.717656168424,
                 4.4: 0.717668711245,
                 4.5: 0.717679243966,
                 4.6: 0.717688088705,
                 4.7: 0.717695515965,
                 4.8: 0.717701752905,
                 4.9: 0.717706990285,
                 5.0: 0.717711388292,
                 5.1: 0.717715081448,
                 5.2: 0.717718182712,
                 5.3: 0.717720786944,
                 5.4: 0.717722973802,
                 5.5: 0.717724810175,
                 5.6: 0.717726352235,
                 5.7: 0.717727647151,
                 5.8: 0.717728734532,
                 5.9: 0.71772964764,
                 6.0: 0.717730414404,
                 6.1: 0.717731058279,
                 6.2: 0.71773159896,
                 6.3: 0.717732052986,
                 6.4: 0.717732434246,
                 6.5: 0.717732754401,
                 6.6: 0.717733023245,
                 6.7: 0.717733249002,
                 6.8: 0.717733438576,
                 6.9: 0.717733597767,
                 7.0: 0.717733731445,
                 7.1: 0.717733843698,
                 7.2: 0.71773393796,
                 7.3: 0.717734017115,
                 7.4: 0.717734083584,
                 7.5: 0.717734139399,
                 7.6: 0.717734186269,
                 7.7: 0.717734225628,
                 7.8: 0.717734258678,
                 7.9: 0.717734286431,
                 8.0: 0.717734309737,
                 8.1: 0.717734329307,
                 8.2: 0.71773434574,
                 8.3: 0.71773435954,
                 8.4: 0.717734371128,
                 8.5: 0.717734380859,
                 8.6: 0.71773438903,
                 8.7: 0.717734395892,
                 8.8: 0.717734401654,
                 8.9: 0.717734406492,
                 9.0: 0.717734410556,
                 9.1: 0.717734413967,
                 9.2: 0.717734416832,
                 9.3: 0.717734419238,
                 9.4: 0.717734421258,
                 9.5: 0.717734422955,
                 9.6: 0.71773442438,
                 9.7: 0.717734425576,
                 9.8: 0.71773442658,
                 9.9: 0.717734427424,
                 10: 0.717734428132}
    from test_models.test_trend import simulation_model
    sim = simulation_model()

    assert sim.dt == 0.1
    assert sim.starttime == 1
    assert sim.stoptime == 10

    for i in np.arange(sim.starttime, sim.stoptime, sim.dt):
        i = round(i, 1)
        assert round(sim.equation('trendOfInputFunction', i), 3) == round(test_data[i], 3)

    os.remove("test_models/test_trend.py")


def test_smooth():
    """
    SMTH1
    :return:
    """
    from test_models.test_smooth import simulation_model
    sim = simulation_model()
    assert sim.dt == 0.1
    assert sim.starttime == 1
    assert sim.stoptime == 10

    for i in np.arange(sim.starttime, sim.stoptime, sim.dt):
        assert sim.equation('exponentialAverage', i) == sim.equations['smooth'](i)

    os.remove("test_models/test_smooth.py")


def test_abs():
    """
    ABS(x)
    :return:
    """
    import numpy as np
    import os
    from test_models.test_abs import simulation_model
    sim = simulation_model()
    assert sim.dt == 0.25
    assert sim.starttime == 1
    assert sim.stoptime == 61

    assert sum([sim.equation("stock1", t) for t in np.arange(sim.starttime, sim.stoptime, sim.dt)]) == (
            sim.stoptime - 1) * (1 / sim.dt) * 100

    os.remove("test_models/test_abs.py")


def test_dt_fraction():
    """
    DT as fraction (1/4)
    :return:
    """
    from test_models.test_dt_fraction import simulation_model
    sim = simulation_model()
    assert sim.dt == 0.25
    assert sim.starttime == 1
    assert sim.stoptime == 61
    os.remove("test_models/test_dt_fraction.py")


def test_dt_rational():
    """
    DT rational
    :return:
    """
    from test_models.test_dt_rational import simulation_model
    sim = simulation_model()
    assert sim.dt == 0.25
    assert sim.starttime == 1
    assert sim.stoptime == 61
    os.remove("test_models/test_dt_rational.py")


def test_no_dimensions():
    """
    Simple model without dimensions.
    :return:
    """
    from test_models.test_no_dimensions import simulation_model
    sim = simulation_model()
    assert sim.dt == 0.25
    assert sim.starttime == 1
    assert sim.stoptime == 61
    os.remove("test_models/test_no_dimensions.py")


def test_time():
    """
    TIME
    :return:
    """
    from test_models.test_time import simulation_model
    sim = simulation_model()
    assert sim.dt == 0.25
    assert sim.starttime == 1
    assert sim.stoptime == 61
    os.remove("test_models/test_time.py")


def test_cos():
    """
    COS(X)
    :return:
    """
    import numpy as np
    import os
    from test_models.test_cos import simulation_model
    sim = simulation_model()
    assert sim.dt == 0.25
    assert sim.starttime == 1
    assert sim.stoptime == 61

    for t in np.arange(sim.starttime, sim.stoptime, sim.dt):
        assert sim.equation("stock1", t) == np.cos(1.0)
    os.remove("test_models/test_cos.py")


def test_tan():
    """
    TAN(x)
    :return:
    """
    import numpy as np
    import os
    from test_models.test_tan import simulation_model
    sim = simulation_model()
    assert sim.dt == 0.25
    assert sim.starttime == 1
    assert sim.stoptime == 61

    for t in np.arange(sim.starttime, sim.stoptime, sim.dt):
        assert sim.equation("stock1", t) == np.tan(1.0)
    os.remove("test_models/test_tan.py")


def test_sim_builtins():
    """
    DT, starttime, stoptime
    :return:
    """
    import numpy as np
    import os
    from test_models.test_sim_builtins import simulation_model
    sim = simulation_model()
    assert sim.dt == 0.25
    assert sim.starttime == 1
    assert sim.stoptime == 61

    for t in np.arange(sim.starttime, sim.stoptime, sim.dt):
        assert sim.equation("p", t) == np.pi
        assert sim.equation("start", t) == sim.starttime
        assert sim.equation("stop", t) == sim.stoptime
    os.remove("test_models/test_sim_builtins.py")


def test_random():
    '''
    Random and Random with seed
    :return:
    '''
    import numpy as np
    import os
    from test_models.test_random import simulation_model
    sim = simulation_model()
    assert sim.dt == 0.25
    assert sim.starttime == 1
    assert sim.stoptime == 61

    for t in np.arange(sim.starttime, sim.stoptime, sim.dt):
        val_btw_0_10 = sim.equation('rndBetween0And10', t)
        assert val_btw_0_10 < 10 and val_btw_0_10 > 0
        assert sim.equation("rnd", t) == 1
        assert sim.equation("rndSeed", t) == 1
    os.remove("test_models/test_random.py")


def test_step():
    import numpy as np
    import os
    from test_models.test_step import simulation_model
    sim = simulation_model()
    assert sim.dt == 0.25
    assert sim.starttime == 1
    assert sim.stoptime == 13

    for t in np.arange(sim.starttime, sim.stoptime, sim.dt):
        assert sim.equation("function", t) == 100.0 if t < 4.0 else sim.equation("function", t) == 150

    os.remove("test_models/test_step.py")


def test_delay():
    import numpy as np
    import os
    from test_models.test_delay import simulation_model
    sim = simulation_model()
    assert sim.dt == 0.25
    assert sim.starttime == 1
    assert sim.stoptime == 13

    for t in np.arange(sim.starttime, sim.stoptime, sim.dt):
        assert sim.equation("function", t) == 100.0 if t < 5.0 else sim.equation("function", t) == 150

    os.remove("test_models/test_delay.py")


def test_if():
    import numpy as np
    import os
    from test_models.test_if import simulation_model
    sim = simulation_model()
    assert sim.dt == 0.25
    assert sim.starttime == 1
    assert sim.stoptime == 13

    for t in np.arange(sim.starttime, sim.stoptime, sim.dt):
        assert sim.equation("function", t) == 100.0 if t < 4.0 else sim.equation("function", t) == 150

    os.remove("test_models/test_if.py")


def test_array():
    expected_result = {1.0: 0.0,
                       1.25: 0.25,
                       1.5: 0.5,
                       1.75: 0.75,
                       2.0: 1.0,
                       2.25: 1.25,
                       2.5: 1.5,
                       2.75: 1.75,
                       3.0: 2.0,
                       3.25: 2.25,
                       3.5: 2.5,
                       3.75: 2.75,
                       4.0: 3.0,
                       4.25: 3.25,
                       4.5: 3.5,
                       4.75: 3.75,
                       5.0: 4.0,
                       5.25: 4.25,
                       5.5: 4.5,
                       5.75: 4.75,
                       6.0: 5.0,
                       6.25: 5.25,
                       6.5: 5.5,
                       6.75: 5.75,
                       7.0: 6.0,
                       7.25: 6.25,
                       7.5: 6.5,
                       7.75: 6.75,
                       8.0: 7.0,
                       8.25: 7.25,
                       8.5: 7.5,
                       8.75: 7.75,
                       9.0: 8.0,
                       9.25: 8.25,
                       9.5: 8.5,
                       9.75: 8.75,
                       10.0: 9.0,
                       10.25: 9.25,
                       10.5: 9.5,
                       10.75: 9.75,
                       11.0: 10.0,
                       11.25: 10.25,
                       11.5: 10.5,
                       11.75: 10.75,
                       12.0: 11.0,
                       12.25: 11.25,
                       12.5: 11.5,
                       12.75: 11.75,
                       13.0: 12.0}
    import numpy as np
    result = {}
    from test_models.test_array import simulation_model
    mod = simulation_model()
    for t in np.arange(1, 13 + 0.25, 0.25):
        result[t] = mod.equations["stock[1]"](t)
        assert mod.equation("inflow[1]", t) == 1
        assert mod.equation("inflow[2]", t) == 2
        assert mod.equation("inflow[3]", t) == 3
        assert sum(mod.equation("inflow[*]", t)) == 6
        #assert mod.equation("inflow[1:3,2,1]", t) == 9

    assert result == expected_result
    os.remove("test_models/test_array.py")

def test_array_extended():
    from test_models.test_array_extended import simulation_model
    from numpy import arange

    sim = simulation_model()
    dt = sim.dt
    starttime = sim.starttime
    stoptime = sim.stoptime

    min_expected_results = [0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75, 4.0, 4.25, 4.5, 4.75, 5.0, 5.25, 5.5, 5.75, 6.0, 6.25, 6.5, 6.75, 7.0, 7.25, 7.5, 7.75, 8.0, 8.25, 8.5, 8.75, 9.0, 9.25, 9.5, 9.75, 10.0, 10.25, 10.5, 10.75, 11.0, 11.25, 11.5, 11.75, 12.0]
    max_expected_results = [0.0,  0.75,1.5,  2.25, 3.0,3.75, 4.5, 5.25, 6.0, 6.75, 7.5, 8.25, 9.0, 9.75, 10.5, 11.25, 12.0,12.75, 13.5,  14.25,  15.0, 15.75,  16.5, 17.25, 18.0, 18.75, 19.5,20.25, 21.0, 21.75,22.5, 23.25,24.0,24.75,25.5, 26.25,27.0, 27.75, 28.5,29.25,  30.0,30.75, 31.5, 32.25,33.0, 33.75, 34.5,35.25,36.0]
    mean_expected_results = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0, 14.5, 15.0, 15.5, 16.0, 16.5, 17.0, 17.5, 18.0, 18.5, 19.0, 19.5, 20.0, 20.5, 21.0, 21.5, 22.0, 22.5, 23.0, 23.5, 24.0]
    array_expected_results = {'germany': [0.0, 1.25, 2.5, 3.75, 5.0, 6.25, 7.5, 8.75, 10.0, 11.25, 12.5, 13.75, 15.0, 16.25, 17.5, 18.75, 20.0, 21.25, 22.5, 23.75, 25.0, 26.25, 27.5, 28.75, 30.0, 31.25, 32.5, 33.75, 35.0, 36.25, 37.5, 38.75, 40.0, 41.25, 42.5, 43.75, 45.0, 46.25, 47.5, 48.75, 50.0, 51.25, 52.5, 53.75, 55.0, 56.25, 57.5, 58.75, 60.0], 'england': [1.0, 3.5, 6.0, 8.5, 11.0, 13.5, 16.0, 18.5, 21.0, 23.5, 26.0, 28.5, 31.0, 33.5, 36.0, 38.5, 41.0, 43.5, 46.0, 48.5, 51.0, 53.5, 56.0, 58.5, 61.0, 63.5, 66.0, 68.5, 71.0, 73.5, 76.0, 78.5, 81.0, 83.5, 86.0, 88.5, 91.0, 93.5, 96.0, 98.5, 101.0, 103.5, 106.0, 108.5, 111.0, 113.5, 116.0, 118.5, 121.0], 'austria': [3.0, 6.75, 10.5, 14.25, 18.0, 21.75, 25.5, 29.25, 33.0, 36.75, 40.5, 44.25, 48.0, 51.75, 55.5, 59.25, 63.0, 66.75, 70.5, 74.25, 78.0, 81.75, 85.5, 89.25, 93.0, 96.75, 100.5, 104.25, 108.0, 111.75, 115.5, 119.25, 123.0, 126.75, 130.5, 134.25, 138.0, 141.75, 145.5, 149.25, 153.0, 156.75, 160.5, 164.25, 168.0, 171.75, 175.5, 179.25, 183.0], 'greece': [4.0, 9.0, 14.0, 19.0, 24.0, 29.0, 34.0, 39.0, 44.0, 49.0, 54.0, 59.0, 64.0, 69.0, 74.0, 79.0, 84.0, 89.0, 94.0, 99.0, 104.0, 109.0, 114.0, 119.0, 124.0, 129.0, 134.0, 139.0, 144.0, 149.0, 154.0, 159.0, 164.0, 169.0, 174.0, 179.0, 184.0, 189.0, 194.0, 199.0, 204.0, 209.0, 214.0, 219.0, 224.0, 229.0, 234.0, 239.0, 244.0]}
    stddev_expected_results = [0.0, 0.2041241452319315, 0.408248290463863, 0.6123724356957945, 0.816496580927726, 1.0206207261596576, 1.224744871391589, 1.4288690166235205, 1.632993161855452, 1.8371173070873836, 2.041241452319315, 2.2453655975512468, 2.449489742783178, 2.6536138880151094, 2.857738033247041, 3.0618621784789726, 3.265986323710904, 3.4701104689428357, 3.6742346141747673, 3.8783587594066984, 4.08248290463863, 4.286607049870562, 4.4907311951024935, 4.694855340334425, 4.898979485566356, 5.103103630798288, 5.307227776030219, 5.5113519212621505, 5.715476066494082, 5.919600211726014, 6.123724356957945, 6.327848502189877, 6.531972647421808, 6.73609679265374, 6.940220937885671, 7.144345083117603, 7.3484692283495345, 7.552593373581465, 7.756717518813397, 7.960841664045329, 8.16496580927726, 8.369089954509192, 8.573214099741124, 8.777338244973055, 8.981462390204987, 9.185586535436919, 9.38971068066885, 9.593834825900782, 9.797958971132712]
    sum_expected_results = [0.0, 1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 10.5, 12.0, 13.5, 15.0, 16.5, 18.0, 19.5, 21.0, 22.5, 24.0, 25.5, 27.0, 28.5, 30.0, 31.5, 33.0, 34.5, 36.0, 37.5, 39.0, 40.5, 42.0, 43.5, 45.0, 46.5, 48.0, 49.5, 51.0, 52.5, 54.0, 55.5, 57.0, 58.5, 60.0, 61.5, 63.0, 64.5, 66.0, 67.5, 69.0, 70.5, 72.0]
    prod_expected_results = [0.0, 0.09375, 0.75, 2.53125, 6.0, 11.71875, 20.25, 32.15625, 48.0, 68.34375, 93.75, 124.78125, 162.0, 205.96875, 257.25, 316.40625, 384.0, 460.59375, 546.75, 643.03125, 750.0, 868.21875, 998.25, 1140.65625, 1296.0, 1464.84375, 1647.75, 1845.28125, 2058.0, 2286.46875, 2531.25, 2792.90625, 3072.0, 3369.09375, 3684.75, 4019.53125, 4374.0, 4748.71875, 5144.25, 5561.15625, 6000.0, 6461.34375, 6945.75, 7453.78125, 7986.0, 8542.96875, 9125.25, 9733.40625, 10368.0]

    max_results = [sim.equation("maxconverter",t) for t in arange(starttime,stoptime+dt,dt)]
    min_results = [sim.equation("minconverter", t) for t in arange(starttime, stoptime + dt, dt)]
    mean_results = [sim.equation("meanconverter",t) for t in arange(starttime,stoptime+dt,dt)]
    stddev_results = [round(sim.equation("stddevconverter",t),3)for t in arange(starttime,stoptime+dt,dt)] # 3 digits accuracy required
    sum_results = [sim.equation("sumconverter",t) for t in arange(starttime,stoptime+dt,dt)]
    prod_results = [round(sim.equation("prodconverter",t),3) for t in arange(starttime,stoptime+dt,dt)] # 3 digits accuracy required



    array_results = {"germany": [], "england": [], "austria": [], "greece": []}
    for i in arange(starttime, stoptime + dt, dt):
        array_results["germany"] += [sim.equation("countryStock[germany]", i)]
        array_results["england"] += [sim.equation("countryStock[england]", i)]
        array_results["austria"] += [sim.equation("countryStock[austria]", i)]
        array_results["greece"] += [sim.equation("countryStock[greece]", i)]
        assert sim.equation("sizeconverter", i) == 4


    assert max_expected_results == max_results
    assert min_expected_results == min_results
    assert mean_expected_results == mean_results
    assert array_expected_results == array_results
    assert [round(x,3) for x in stddev_expected_results] == stddev_results
    assert sum_expected_results == sum_results
    assert [round(x,3) for x in prod_expected_results] == prod_results

    os.remove("test_models/test_array_extended.py")

def test_array_2dimensional():
    from test_models.test_array_2dimensional import simulation_model
    from numpy import arange

    sim = simulation_model()
    dt = sim.dt
    starttime = sim.starttime
    stoptime = sim.stoptime

    rankinv_expected_results = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    smallestinventory_expected_results = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 55.0, 60.0]
    largestinventory_expected_results = [0.0, 0.0, 0.0, 0.0, 0.0, 2.5, 5.0, 7.5, 10.0, 12.5, 15.0, 17.5, 20.0, 22.5, 25.0, 27.5, 30.0, 32.5, 35.0, 37.5, 40.0, 42.5, 45.0, 47.5, 50.0, 52.5, 60.0, 70.0, 80.0, 90.0, 100.0, 110.0, 120.0, 130.0, 140.0, 150.0, 160.0, 170.0, 180.0, 190.0, 200.0, 210.0, 220.0, 230.0, 240.0, 250.0, 260.0, 270.0, 280.0]
    totalinventory_expected_results = [0.0, 0.0, 0.0, 0.0, 0.0, 2.5, 5.0, 7.5, 10.0, 17.5, 25.0, 32.5, 40.0, 55.0, 70.0, 85.0, 100.0, 125.0, 150.0, 175.0, 200.0, 235.0, 270.0, 305.0, 340.0, 382.5, 425.0, 467.5, 510.0, 555.0, 600.0, 645.0, 690.0, 740.0, 790.0, 840.0, 890.0, 945.0, 1000.0, 1055.0, 1110.0, 1172.5, 1235.0, 1297.5, 1360.0, 1432.5, 1505.0, 1577.5, 1650.0]
    avginventory_expected_results = [0.0, 0.0, 0.0, 0.0, 0.0, 0.20833333333333334, 0.4166666666666667, 0.625, 0.8333333333333334, 1.4583333333333333, 2.0833333333333335, 2.7083333333333335, 3.3333333333333335, 4.583333333333333, 5.833333333333333, 7.083333333333333, 8.333333333333334, 10.416666666666666, 12.5, 14.583333333333334, 16.666666666666668, 19.583333333333332, 22.5, 25.416666666666668, 28.333333333333332, 31.875, 35.416666666666664, 38.958333333333336, 42.5, 46.25, 50.0, 53.75, 57.5, 61.666666666666664, 65.83333333333333, 70.0, 74.16666666666667, 78.75, 83.33333333333333, 87.91666666666667, 92.5, 97.70833333333333, 102.91666666666667, 108.125, 113.33333333333333, 119.375, 125.41666666666667, 131.45833333333334, 137.5]
    avginventory_results = [round(sim.equation('averageInventory', t),3) for t in arange(starttime, stoptime + dt, dt)]
    avginventoryusingsize_results = [round(sim.equation('averageInventoryUsingSize', t), 3) for t in arange(starttime, stoptime + dt, dt)]
    totalinventory_results = [round(sim.equation('totalInventory', t),3) for t in arange(starttime, stoptime + dt, dt)]
    largestinventory_results = [sim.equation('largestGermanInventory', t) for t in arange(starttime, stoptime + dt, dt)]
    smallestinventory_results = [sim.equation('smallestGermanInventory', t) for t in arange(starttime, stoptime + dt, dt)]
    rankinv_results = [sim.equation('rankinv', t) for t in arange(starttime, stoptime + dt, dt)]

    assert [round(x,3) for x in avginventory_expected_results] == avginventory_results == avginventoryusingsize_results
    assert totalinventory_results == totalinventory_expected_results
    assert largestinventory_expected_results == largestinventory_results
    assert smallestinventory_expected_results == smallestinventory_results
    assert rankinv_expected_results == rankinv_results

    for t in arange(sim.starttime, sim.stoptime + sim.dt, sim.dt):
        assert sim.memoize('productionDuration[1,germany]', t) == 1
        assert sim.memoize('productionDuration[1,england]', t) == 2
        assert sim.memoize('productionDuration[1,austria]', t) == 3
        assert sim.memoize('productionDuration[1,greece]', t) == 4
        assert sim.memoize('productionDuration[2,germany]', t) == 5
        assert sim.memoize('productionDuration[2,england]', t) == 6
        assert sim.memoize('productionDuration[2,austria]', t) == 8
        assert sim.memoize('productionDuration[2,greece]', t) == 7
        assert sim.memoize('productionDuration[3,germany]', t) == 9
        assert sim.memoize('productionDuration[3,england]', t) == 10
        assert sim.memoize('productionDuration[3,austria]', t) == 11
        assert sim.memoize('productionDuration[3,greece]', t) == 12

    os.remove("test_models/test_array_2dimensional.py")