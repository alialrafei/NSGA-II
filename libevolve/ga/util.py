# -*- coding: utf-8 -*-


def normalise(data):
    """

    Parameters
    ----------
    data : list
        list of values

    Returns
    -------
    list
    normalised list of values
    """
    return [float(x)/sum(data) for x in data]


class GeneticHistory:
    """ History of a genetic optimisation procedure

    """
    def __init__(self):
        self.run_log = []
        self.nb_generations = 0
        self.hall_of_fame = []
