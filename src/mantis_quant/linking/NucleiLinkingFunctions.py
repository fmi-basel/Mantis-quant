# Copyright (C) 2023 Friedrich Miescher Institute for Biomedical Research

##############################################################################
#                                                                            #
# Author: Nicole Repina              <nicole.repina@fmi.ch>                  #
#                                                                            #
##############################################################################

from copy import deepcopy

import numpy as np


def calculate_quantiles(pc, q=0.5, column=-1):
    """
    Calculate mean and standard deviation of nuclear volumes in organoid
    Helper function used during affine linking
    q is quantile in range [0,1] to calclulate
    """
    quantile = np.quantile(pc[:, column].transpose(), q)
    iqr = np.quantile(pc[:, column].transpose(), 0.75) - np.quantile(
        pc[:, column].transpose(), 0.25
    )
    return quantile, iqr


def remove_labels(seg_img, labels_to_remove, datatype):
    """
    Remove labels from segmentation image.
    labels_to_remove is list of labels, and each value should match data format of
    """
    seg_img_relabeled = deepcopy(seg_img)

    for lab in labels_to_remove:
        lab = lab.astype(datatype)
        seg_img_relabeled[seg_img_relabeled == lab] = 0

    return seg_img_relabeled