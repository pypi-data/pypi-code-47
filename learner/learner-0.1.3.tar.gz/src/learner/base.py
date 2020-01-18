"""Define the learners"""


class BaseLearner:
    """The base Class of all the learners"""
    def __init__(self):
        self._demory = dict()
        self._models = dict()
        self._current_data = None
        self._current_model = None

    @property
    def n_data(self):
        return len(self._demory)

    @property
    def n_model(self):
        return len(self._models)

    @property
    def demory(self):
        """Memory of all the data that have been added"""
        return self._demory

    @property
    def models(self):
        """List of all the models that have been added"""
        return self._models

    @property
    def current_data(self):
        return self._current_data

    @current_data.setter
    def current_data(self, name):
        if name in self.demory:
            self._current_data = self.demory[name]
        else:
            raise NameError(f"{name} is not in the demory of this learner.")

    def add_data(self, data, name=None):
        self._current_data = data
        if not name:
            name = f"data_{self.n_data}"
        self._demory[name] = data

    @property
    def current_model(self):
        return self._current_model

    @current_model.setter
    def current_model(self, name):
        if name in self.models:
            self._current_model = self.models[name]
        else:
            raise NameError(f"{name} is not a known model for this learner.")

    def add_model(self, model, name=None):
        self._current_model = model
        if not name:
            name = f"model_{self.n_data}"
        self._models[name] = model

    def fit(self):
        pass

    def partial_fit(self):
        pass

    def validate(self):
        pass

    def predict(self):
        pass


class Learner(BaseLearner):
    """A typical Leaner with reasonable default settings"""
    def __init__(self):
        super().__init__()
        pass
