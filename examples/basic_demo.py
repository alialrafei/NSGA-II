from string import ascii_lowercase
from libevolve.common import *
from libevolve.ga import GeneticAlgorithm


def objective_fn(a, b, c):
    c = ord(c)
    return -(a+b-c)**2 + a + b, -(a-c)**2


def main():

    a = EvoIntParam(name="a", min_val=0, max_val=10)
    b = EvoFloatParam(name="b", min_val=10, max_val=20, step=0.5)
    c = EvoCategoricalParam(name="c", categories=list(ascii_lowercase.lower()))

    ga = GeneticAlgorithm()
    best_score, best_params, history = ga.evolve(parameters=[a, b, c],
                                                 fitness_function=objective_fn,
                                                 objective_weights=[-1, 1])


if __name__ == '__main__':
    main()
