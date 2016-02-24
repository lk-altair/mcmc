# -*- coding: utf-8 -*-

from __future__ import division, print_function

import numpy as np
from cycler import cycler
from matplotlib import rcParams

__all__ = ["COLORS", "SQUARE_FIGSIZE", "setup"]

COLORS = dict(
    DATA="k",
    MODEL_1="#1f77b4",
    MODEL_2="#ff7f0e",
)

SQUARE_FIGSIZE = np.array((4, 4))


def setup():
    rcParams["font.size"] = 20
    rcParams["font.family"] = "serif"
    rcParams["font.serif"] = "Computer Sans"
    rcParams["text.usetex"] = True
    rcParams["figure.autolayout"] = True
    rcParams["axes.prop_cycle"] = cycler("color", (
        "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b",
        "#e377c2", "#7f7f7f", "#bcbd22", "#17becf",
    ))  # d3.js color cycle
