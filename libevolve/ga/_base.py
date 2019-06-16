# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------------------
# author     = "Sameh K. Mohamed"
# copyright  = "Copyright 2019, The Project"
# credits    = ["Sameh K. Mohamed"]
# license    = "MIT"
# version    = "0.0.0"
# maintainer = "Sameh K. Mohamed"
# email      = "sameh.kamaleldin@gmail.com"
# status     = "Development"
# -----------------------------------------------------------------------------------------
# Created by sameh at 2019-06-16
# -----------------------------------------------------------------------------------------

from collections import Iterable
from deap import base, algorithms, creator, tools


class GeneticAlgorithm:
    """ A class for a generic genetic algorithm
    """
    def __init__(self, parameters, fitness_function, objective_weights):
        """ Initialise a new instance of the `GeneticAlgorithm` class

        Parameters
        ----------
        parameters : Iterable
            the set of evolutionary learning parameters
        fitness_function : function
            the fitness function. Expects named parameters that are equal or subset of the input parameters with the
            same names as specified in the input parameters. Must return an iterable.
        objective_weights : Iterable
            the assigned weights to the fitness function output objective values. Positive values denote maximisation
            objective while negative values represent minimisation objective of the corresponding objective output.
        """
        self.parameters = parameters
        self.fitness_function = fitness_function
        self.objective_weights = objective_weights
