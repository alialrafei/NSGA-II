# -*- coding: utf-8 -*-

from abc import abstractmethod
from random import Random
from .util import GeneticHistory, normalise
from ..common import *


class GeneticAlgorithm:
    """ A class for a generic genetic algorithm
    """
    def __init__(self,
                 population_size=50,
                 nb_generations=20,
                 mutation_size=1,
                 mutation_probability=0.3,
                 crossover_probability=0.5,
                 selection_size=20,
                 seed=1234,
                 verbose=0):
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
        selection_size : int
            the size of natural selection group
        seed : int
            random seed
        verbose : int
            verbosity level

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

        self.verbose = verbose
        self.seed = seed
        self.rs = Random(seed)
        self.parameters = None
        self.fitness_function = None
        self.objective_weights = None
        self.history = GeneticHistory()

    @abstractmethod
    def _crossover(self, parent1, parent2):
        """ Crossover between two parents individuals

        Parameters
        ----------
        parent1 : Individual
            first parent individual
        parent2 : Individual
            second parent individual

        Returns
        -------
        Individual
            first child individual
        Individual
            second child individual
        """
        pass

    @abstractmethod
    def natural_selection(self, population, fitness_scores, *args, **kwargs):
        """ Perform genetic natural selection

        population : list
            list of individuals
        fitness_fitness_scores : list
            list of fitness scores lists
        args : list
            other un named arguments
        kwargs : dict
            other named arguments

        Returns
        -------
        list
            list of chosen individuals
        """
        pass

    def evolve(self, parameters, fitness_function, objective_weights, *args, **kwargs):
        """ Perform evolution on the specified parameters and objective function

        parameters : list
            the set of evolutionary learning parameters
        fitness_function : function
            the fitness function. Expects named parameters that are equal or subset of the input parameters with the
            same names as specified in the input parameters. Must return an iterable.
        objective_weights : list
            the assigned weights to the fitness function output objective values. Positive values denote maximisation
            objective while negative values represent minimisation objective of the corresponding objective output.
        args : list
            other un named arguments
        kwargs : dict
            other named arguments

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
        best_solution, best_score = None, 0.0

        nb_params = len(parameters)
        nb_objectives = len(objective_weights)
        param_names = [p.name for p in parameters]
        population = []

        # generate initial population
        for _ in range(self.population_size):
            ind = Individual(parameters, seed=self.rs.randint(0, 9999999999))
            population.append(ind)

        current_generation = population
        current_generation_fitness = [[] for _ in range(nb_objectives)]

        for generation_idx in range(self.nb_generations):
            for ind in current_generation:
                ind_fitness = fitness_function(**ind.key_params)
                for idx, fitness_value in enumerate(ind_fitness):
                    current_generation_fitness[idx].append(fitness_value)

                # selection

                # crossover

                # mutations

        return best_solution, best_score, self.history
