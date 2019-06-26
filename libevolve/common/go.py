# -*- coding: utf-8 -*-

from random import Random
from libevolve.common import *


def validate_input_param(obj):
    """ Check if an object is an EvoParam

    Parameters
    ----------
    obj : object

    Returns
    -------
    bool
        flag that is true when the object is an EvoParam instance and False otherwise

    Examples
    ----------
    >>> from libevolve.common import *
    >>> from libevolve.common.go import validate_input_param
    >>> a = EvoIntParam(name="a")
    >>> validate_input_param(a)
    True
    """
    return isinstance(obj, EvoParam)


def check_list_has_duplicates(list_obj):
    """ Check if list has duplicates

    Parameters
    ----------
    list_obj : list
        list object

    Returns
    -------
    bool
        true if the list has duplicates and False otherwise

    Examples
    ----------
    >>> from libevolve.common.go import check_list_has_duplicates
    >>> check_list_has_duplicates([1,2,3,4,2])
    True
    """
    return len(list_obj) != len(set(list_obj))


class Individual(list):
    """
    A genetic algorithm individual (list of evolutionary parameters)
    """
    def __init__(self, parameters, seed=1234):
        """ initialise an instance of the class `Individual`

        Parameters
        ----------
        parameters : Iterable
            list of parameters
        seed : int
            random seed

        Examples
        ----------
        >>> from libevolve.common import Individual
        >>> ind = Individual([EvoIntParam(name="a"), EvoFloatParam(name="b")])
        """
        super().__init__()
        self._parameters = parameters
        self.rs = Random(seed)
        self.randomise()

    @property
    def key_params(self):
        """ Get individual's parameters dictionary

        Returns
        -------
        dict
            individual's parameters dictionary

        Examples
        ----------
        >>> from libevolve.common import *
        >>> from libevolve.common import Individual
        >>> ind = Individual([EvoIntParam(name="a"), EvoFloatParam(name="b")])
        >>> ind.key_params
        {'a': 12, 'b': -10}
        """
        return {p.name: p.current_value for p in self._parameters}

    @property
    def param_names(self):
        """ Get individual's parameters' names

        Returns
        -------
        list
            Parameters' names

        Examples
        ----------
        >>> from libevolve.common import *
        >>> from libevolve.common import Individual
        >>> ind = Individual([EvoIntParam(name="a"), EvoFloatParam(name="b")])
        >>> ind.param_names
        ['a', 'b']
        """
        return [p.name for p in self._parameters]

    @property
    def nb_params(self):
        """ Get the number of parameters

        Returns
        -------
        int
            number of parameters

        Examples
        ----------
        >>> from libevolve.common import *
        >>> from libevolve.common import Individual
        >>> ind = Individual([EvoIntParam(name="a"), EvoFloatParam(name="b")])
        >>> ind.nb_params
        2
        """
        return len(self._parameters)

    def randomise(self):
        """ Randomise the individual's parameters

        Examples
        ----------
        >>> from libevolve.common import *
        >>> from libevolve.common import Individual
        >>> ind = Individual([EvoIntParam(name="a"), EvoFloatParam(name="b")])
        >>> ind.randomise()

        """
        del self[:]
        for p in self._parameters:
            self.append(p.get_rand_value())

    def mutate(self, mutation_size=1, mutation_probability=0.5, mutation_type="default"):
        """ Mutate the individual

        Parameters
        ----------
        mutation_size : int
            the number of affected parameters in the mutation
        mutation_probability : float
            mutation probability
        mutation_type : str
            the mutation type

        Returns
        -------
        Individual
            mutated values

        Examples
        ----------
        >>> from libevolve.common import *
        >>> from libevolve.common import Individual
        >>> ind = Individual([EvoIntParam(name="a"), EvoFloatParam(name="b")])
        >>> ind.mutate()
        [-71, -10]
        """
        param_indices = list(range(self.nb_params))
        self.rs.shuffle(param_indices)
        selected_params_indices = param_indices[:mutation_size]
        for param_idx in selected_params_indices:
            if self.rs.random() < mutation_probability:
                self[param_idx] = self._parameters[param_idx].get_rand_value()
        return self
