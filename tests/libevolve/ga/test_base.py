# -*- coding: utf-8 -*-

import pytest
from libevolve.ga import GeneticAlgorithm


def test_ga_constructor():
    """
    test the constructor function of the genetic algorithms module
    """
    ga = GeneticAlgorithm()
    ga = GeneticAlgorithm(population_size=10, nb_generations=15, mutation_size=1, mutation_probability=0.9)

    assert ga.population_size == 10, "Population size not assigned properly"
    assert ga.nb_generations == 15, "Population size not assigned properly"
    assert ga.mutation_size == 1, "Population size not assigned properly"
    assert ga.mutation_probability == 0.9, "Population size not assigned properly"


def test_ga_evolve_exceptions():
    """

    """


