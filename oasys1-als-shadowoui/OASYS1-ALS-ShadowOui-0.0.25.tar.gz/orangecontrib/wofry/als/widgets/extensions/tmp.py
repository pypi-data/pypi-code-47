import numpy


def calculate_wavefront1D(wavelength=1e-10,
                          undulator_length=1.0, undulator_distance=10.0,
                          x_min=-0.1, x_max=0.1, number_of_points=101,
                          wavefront_position=0, add_random_phase=0):
    from wofry.propagator.wavefront1D.generic_wavefront import GenericWavefront1D

    sigma_r = 2.740 / 4 / numpy.pi * numpy.sqrt(wavelength * undulator_length)
    sigma_r_prime = 0.69 * numpy.sqrt(wavelength / undulator_length)

    wavefront1D = GenericWavefront1D.initialize_wavefront_from_range(x_min=x_min, x_max=x_max,
                                                                     number_of_points=number_of_points)
    wavefront1D.set_wavelength(wavelength)

    if wavefront_position == 0:  # Gaussian source
        wavefront1D.set_gaussian(sigma_x=sigma_r, amplitude=1.0, shift=0.0)
    elif wavefront_position == 1:  # Spherical source, Gaussian intensity
        wavefront1D.set_spherical_wave(radius=undulator_distance, center=0.0, complex_amplitude=complex(1, 0))
        # weight with Gaussian
        X = wavefront1D.get_abscissas()
        A = wavefront1D.get_complex_amplitude()
        sigma = undulator_distance * sigma_r_prime
        sigma_amplitude = sigma * numpy.sqrt(2)
        Gx = numpy.exp(-X * X / 2 / sigma_amplitude ** 2)
        wavefront1D.set_complex_amplitude(A * Gx)

    if add_random_phase:
        wavefront1D.add_phase_shifts(2 * numpy.pi * numpy.random.random(wavefront1D.size()))

    return wavefront1D


output_wavefront = calculate_wavefront1D(wavelength=1e-10,
                                         1 = 1,
                                             undulator_length = 3.98,
                                                                undulator_distance = 13.73,
                                                                                     x_min = -0.00147,
                                                                                             x_max = 0.00147,
                                                                                                     number_of_points = 1000,
                                                                                                                        add_random_phase = 0)
from srxraylib.plot.gol import plot

plot(output_wavefront.get_abscissas(), output_wavefront.get_intensity())
