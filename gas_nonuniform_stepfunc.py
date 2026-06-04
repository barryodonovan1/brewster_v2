#!/usr/bin/env python

""" Module of bits for non-uniform, step-function gas profile to emulate gas sequestration due to cloud formation"""
import numpy as np

def non_uniform_gas(press, logPt, logf_deep, logf_upper):
    """
    Construct a vertically varying gas volume mixing ratio profile
    as a step function.
    Parameters
    ----------
    press : ndarray
        Pressure grid (must be positive, increasing).
    logPt : float
        log10 of the transition pressure Pt (same units as `press`).
    logf_deep : float
        log10 of the gas volume mixing ratio below Pt (high pressure / deep atmosphere).
    logf_upper : float
        log10 of the gas volume mixing ratio above Pt (low pressure / upper atmosphere).
    Returns
    -------
    gas_f : ndarray
        log10 of the gas volume mixing ratio profile on the `press` grid.
    Notes
    -----
    The profile is defined as:
        log10(f(P)) = logf_upper    for P < Pt  (upper atmosphere)
        log10(f(P)) = logf_deep     for P >= Pt (deep atmosphere)
    """
    gas_f = np.zeros_like(press)

    Pt = 10.**logPt

    for i in range(0, press.size):
        if (press[i] < Pt):
            gas_f[i] = float(logf_upper)
        else:
            gas_f[i] = float(logf_deep)

    return gas_f
