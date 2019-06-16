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
# Created by sameh at 2019-06-15
# -----------------------------------------------------------------------------------------


import random
from collections import Iterable


class InputParam:
    """ An input parameter for a fitness function
    """
    def __init__(self, name, param_value=None):
        """ Initialise a new input parameter

        Parameters
        ----------
        name : str
            parameter name
        param_value : object
            parameter value
        """
        self.name = name
        self.val_type = None
        self._val = param_value

    def current_value(self):
        """ Get current value

        Returns
        -------
        object
            current object value
        """
        return self._val


class EvoParam(InputParam):
    """ A class for the evolutionary learning input parameter
    """

    def __init__(self, name, value_range=None, seed=1234):
        """ Initialise a new instance of `Parameter` class

        Parameters
        ----------
        name : str
            name of the parameter
        value_range : list
            the range of possible values for the parameter
        seed : int
            random seed
        """
        super().__init__(name=name)
        self._value_range = value_range
        self.seed = seed
        self.rs = random.Random()
        self.rs.seed(seed)

    def get_rand_value(self):
        """ Get random parameter value

        Returns
        -------
        object
            random value from the parameter's range possible values
        """
        self._val = self.rs.choice(self._value_range)
        return self._val

    def get_value_range(self):
        """ Get parameter value range

        Returns
        -------
        Iterable
            parameter value range
        """
        return self._value_range

    def set_value_range(self, value_range):
        """ Get parameter value range

        value_range : Iterable
            parameter value range
        """
        if isinstance(value_range, Iterable):
            self._value_range = value_range


class EvoFlagParam(EvoParam):
    """ A class for a flag evolutionary learning input parameter
    """

    def __init__(self, name, seed=1234):
        """ Initialise a new instance of `EvoFlagParam` class

        Parameters
        ----------
        name : str
            name of the parameter
        """
        super().__init__(name=name, value_range=[0, 1], seed=seed)
        self.type = None


class EvoIntParam(EvoParam):
    """A class for an integer evolutionary learning input parameter
    """

    def __init__(self, name, min_val=-100, max_val=100, seed=1234):
        """ Initialise a new instance of `EvoIntParam` class

        Parameters
        ----------
        name : str
            name of the parameter
        min_val : int
            minimum value for the parameter
        max_val : int
            maximum value for the parameter
        """
        self._min_val = min_val
        self._max_val = max_val
        val_range = list(range(min_val, max_val+1))
        super().__init__(name=name, value_range=val_range, seed=seed)
        self.type = int

    def set_max_value(self, max_value):
        """ Set parameter range max value

        Parameters
        ----------
        max_value : int
        """
        self._max_val = max_value

    def get_max_value(self):
        """ Get parameter range max value

        Returns
        -------
        int
            parameter max value
        """
        return self._max_val

    def set_min_value(self, min_value):
        """ Set parameter range max value

        Parameters
        ----------
        min_value : int
        """
        self._min_val = min_value

    def get_min_value(self):
        """ Get parameter range min value

        Returns
        -------
        int
            parameter min value
        """
        return self._min_val


class EvoFloatParam(EvoIntParam):
    """A class for a float evolutionary learning input parameter
    """

    def __init__(self, name, min_val=-100, max_val=100, step=0.1, seed=1234):
        """ Initialise a new instance of `EvoFloatParam` class

        Parameters
        ----------
        name : str
            name of the parameter
        min_val : float
            minimum value for the parameter
        max_val : float
            maximum value for the parameter
        step : float
            the possible parameter value step from the min to max
        """
        super().__init__(name=name, min_val=0, max_val=1, seed=seed)
        self._min_val = min_val
        self._max_val = max_val
        self._step = step
        val_range = [v for v in range(int(min_val*step), int((max_val+step)*step))]
        self._value_range = val_range
        self.type = float

    def set_step_value(self, step):
        """ Set parameter range step value

        Parameters
        ----------
        step : float
            the new step value
        """
        self._step = step

    def get_step_value(self):
        """ Get parameter range step value

        Returns
        -------
        int
            parameter step value
        """
        return self._step


class EvoCategoricalParam(EvoParam):
    """ A class for a Categorical evolutionary learning input parameter
    """

    def __init__(self, name, categories, seed=1234):
        """ Initialise a new instance of `EvoCategoricalParam` class

        Parameters
        ----------
        name : str
            name of the parameter
        categories : list
            the list of possible values for the parameter
        """
        super().__init__(name=name, value_range=categories, seed=seed)
        self.type = None
