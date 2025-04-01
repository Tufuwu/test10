import os
import random

import numpy as np
import tensorflow as tf


SEEDS = [
    541016860, 434342745, 1462316, 746159945, 433636464,
    530723967, 295017836, 302019026, 640140178, 957046961,
    475444362, 278306975, 83585224, 685067992, 400240993,
    239621435, 637466954, 573280196, 231193742, 149726676,
    173557752, 157690354, 847183411, 579721348, 922190945,
    205545199, 435523622, 27731640, 639969698, 494394683,
    509097569, 296723603, 397822181, 181062463, 651607747,
    259044820, 558942884, 6185167, 297465764, 848614446,
    58396361, 81275008, 171129753, 27911984, 739412663,
    976969665, 206198540, 585568140, 855303989, 655946607,
    78027203, 632573122, 580221649, 481977876, 714217144,
    250995193, 128923793, 950784322, 572672493, 46038406,
    246931758, 419410508, 786353275, 394197612, 690922961,
    192002917, 727569102, 474539245, 656187073, 412487813,
    833266582, 214460854, 964486850, 472001483, 118002895,
    187278713, 264115218, 503303705, 251222528, 342483875,
    519826287, 908523901, 893494846, 812561810, 547050153,
    97712332, 585164726, 251525466, 692143777, 549429461,
    654783681, 798090934, 787868382, 572836811, 169359452,
    581246016, 629679352, 107783031, 674411860, 123498125
]


def set_random_seed(seed: int):
    """
    Sets the Python, NumPy, and Tensorflow random seeds to the provided value.

    :param seed: the random seed value to use
    """
    os.environ['PYTHONHASHSEED'] = str(seed)
    random.seed(seed)
    np.random.seed(seed)
    tf.random.set_seed(seed)
