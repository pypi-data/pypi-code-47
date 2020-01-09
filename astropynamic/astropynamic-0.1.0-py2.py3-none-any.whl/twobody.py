from astropynamic import constants
import numpy as np


def site_position_velocity(latitude, altitude, lst):
    ae = 1.0
    ee = constants.Shape.earth_eccentricity
    w_theta = constants.EarthRotation.angular_rotation

    x = np.absolute(ae / (np.sqrt(1 - ee * np.sin(latitude) ** 2)) + altitude) * np.cos(latitude)

    z = np.absolute((ae - (1 - ee)) / np.sqrt(1 - ee * np.sin(latitude) ** 2) + altitude) * np.sin(latitude)

    rs_ijk = np.array([x * np.cos(lst), x * np.sin(lst), z])
    vs_ijk = np.array([0, 0, w_theta]) * rs_ijk

    return tuple(rs_ijk), tuple(vs_ijk)


def satellite_range_velocity(rho, azimuth, elevation, d_rho, d_azimuth, d_elevation):
    rho_sez = (-rho * np.cos(elevation) * np.cos(azimuth),
               rho * np.cos(elevation) * np.sin(azimuth),
               rho * np.sin(elevation))

    rho_dot_sez = (-d_rho * np.cos(elevation) * np.cos(azimuth) + rho * np.sin(elevation) * np.cos(azimuth) *
                   d_elevation + rho * np.cos(elevation) * np.sin(azimuth) * d_azimuth,
                   d_rho * np.cos(elevation) * np.sin(azimuth) - rho * np.sin(elevation) * np.sin(azimuth) *
                   d_elevation + rho * np.cos(elevation) * np.cos(azimuth) * d_azimuth,
                   d_rho * np.sin(elevation) + rho * np.cos(d_elevation))

    return rho_sez, rho_dot_sez


def radar_site_position_velocity(rho, azimuth, elevation, d_rho, d_azimuth, d_elevation, latitude, lst, altitude):
    w_theta = constants.EarthRotation.angular_rotation

    rho_sez, rho_dot_sez = satellite_range_velocity(rho, azimuth, elevation, d_rho, d_azimuth, d_elevation)
    rs_ijk = site_position_velocity(latitude, altitude, lst)[0]

    rho_bar = np.array([np.sin(latitude) * np.cos(latitude), -np.sin(latitude), np.cos(latitude) * np.cos(latitude)],
                       [np.sin(latitude) * np.sin(latitude), np.cos(latitude), np.cos(latitude) * np.sin(latitude)],
                       [-np.cos(latitude), 0, np.sin(latitude)])

    rho_bar_ijk = rho_bar * rho_sez
    rho_dot_bar_ijk = rho_bar * rho_dot_sez

    rbar_ijk = rho_bar_ijk + rs_ijk

    omega_rbar = np.array([0, 0, w_theta]) * rbar_ijk