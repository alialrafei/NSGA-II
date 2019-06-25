# -*- coding: utf-8 -*-

from abc import abstractmethod
from .util import GeneticHistory


class GeneticAlgorithm:
    """ A class for a generic genetic algorithm
    """
    def __init__(self,
                 population_size=50,
                 nb_generations=20,
                 mutation_size=1,
                 mutation_probability=0.3,
                 crossover_probability=0.5):
        """ Initialise a new instance of the `GeneticAlgorithm` class

        Parameters
        ----------
        population_size : int
            the population size
        nb_generations : int
            the number of generations
        mutation_size : int
            the number of genes to be mutated
        mutation_probability : float
            the probability of mutation for the chosen genes
        crossover_probability : float
            probability of crossover

        Examples
        ----------
        >>> from libevolve.ga import GeneticAlgorithm
        >>> ga = GeneticAlgorithm(population_size=10, nb_generations=15, mutation_size=1, mutation_probability=0.9)
        """

        self.population_size = population_size
        self.nb_generations = nb_generations
        self.mutation_size = mutation_size
        self.mutation_probability = mutation_probability
        self.crossover_probability = crossover_probability

        self.parameters = None
        self.fitness_function = None
        self.objective_weights = None
        self.history = GeneticHistory()

    def _mutate(self, individual):
        """ Mutate a single individual

        Parameters
        ----------
        individual : list
            the individual list of `EvoParam`

        Returns
        -------
        list
            the mutated individual list of `EvoParam`
        """

    def evolve(self, parameters, fitness_function, objective_weights):
        """ Perform evolution on the specified parameters and objective function

        parameters : Iterable
            the set of evolutionary learning parameters
        fitness_function : function
            the fitness function. Expects named parameters that are equal or subset of the input parameters with the
            same names as specified in the input parameters. Must return an iterable.
        objective_weights : Iterable
            the assigned weights to the fitness function output objective values. Positive values denote maximisation
            objective while negative values represent minimisation objective of the corresponding objective output.

        Returns
        -------
        list
            set of best parameter values
        list
            set of fitness function scores for the best parameters
        GeneticHistory
            history of the genetic evolution

        Examples
        ----------
        >>> from libevolve.ga import GeneticAlgorithm
        >>> from libevolve.common import *
        >>> ga = GeneticAlgorithm(population_size=10, nb_generations=15, mutation_size=1, mutation_probability=0.9)
        >>> best_solution, best_score, history = ga.evolve()
        """
        best_solution, score = None, 0.0

        return best_solution, score
