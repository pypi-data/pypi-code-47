from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.dummy import DummyRegressor
from sklearn.pipeline import Pipeline

from jcopml.tuning.skopt import BayesSearchCV
from jcopml.automl._automl_params import autoreg_params, autoclf_params, _reg_algo, _clf_algo


class AutoRegressor:
    def __init__(self, preprocessor, random_state=42):
        """
        Quick way to create a regression benchmark.


        == Example usage ==
        automl = AutoRegressor(preprocessor)
        model = automl.fit(X, y)


        == Arguments ==
        preprocessor: sklearn ColumnTranformer
            preprocessor pipeline using scikit-learn and jcopml

        random_state: int or None
            random state for parameter search
        """
        self.preprocessor = preprocessor
        self.random_state = random_state

    def fit(self, X, y, test_size=0.2, algo="all", search_mode="random", poly=False, cv=3, n_trial=50):
        f"""
        == Arguments ==
        X: numpy or pandas DataFrame
            input features
        y: numpy or pandas DataFrame
            target
        test_size: float
            test split ratio used in sklearn train_test_split
        algo: list or str
            list of algo to use. Input "all" to use all available algorithms.
            Available algorithms: {_reg_algo}
        search_mode: {"random", "bayes"}
            Perform parameter search.
            - random: RandomizedSearchCV
            - bayes: BayesSearchCV
        poly: bool
            Set poly=True to consider polynomial features in parameter search
        cv: int or sklearn Split object
            cross validation fold. See: RandomizedSearchCV or BayesSearchCV
        n_trial: int
            number of search trial / iteration

        == Return ==
        scikit-learn model (SearchCV object)
        """
        if poly and ("numeric__poly__degree" not in self.preprocessor.get_params()):
            raise Exception("Polynomial features are not set in the numerical pipeline")

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=self.random_state)

        pipeline = Pipeline([
            ("prep", self.preprocessor),
            ('algo', DummyRegressor())
        ])

        cv_algo = RandomizedSearchCV if search_mode == "random" else BayesSearchCV
        model = cv_algo(pipeline, autoreg_params(algo, search_mode, poly), cv=cv, n_iter=n_trial, n_jobs=-1, verbose=1,
                        random_state=self.random_state)
        model.fit(X_train, y_train)

        _report(model, X_train, y_train, X_test, y_test)
        return model


class AutoClassifier:
    def __init__(self, preprocessor, random_state=42):
        """
        Quick way to create a classification benchmark.


        == Example usage ==
        automl = AutoClassifier(preprocessor)
        model = automl.fit(X, y)


        == Arguments ==
        preprocessor: sklearn ColumnTranformer
            preprocessor pipeline using scikit-learn and jcopml

        random_state: int or None
            random state for parameter search
        """
        self.preprocessor = preprocessor
        self.random_state = random_state

    def fit(self, X, y, test_size=0.2, algo="all", search_mode="random", poly=False, cv=3, n_trial=50):
        f"""
        == Arguments ==
        X: numpy or pandas DataFrame
            input features
        y: numpy or pandas DataFrame
            target
        test_size: float
            test split ratio used in sklearn train_test_split
        algo: list or str
            list of algo to use. Input "all" to use all available algorithms.
            Available algorithms: {_clf_algo}
        search_mode: {"random", "bayes"}
            Perform parameter search.
            - random: RandomizedSearchCV
            - bayes: BayesSearchCV
        poly: bool
            Set poly=True to consider polynomial features in parameter search
        cv: int or sklearn Split object
            cross validation fold. See: RandomizedSearchCV or BayesSearchCV
        n_trial: int
            number of search trial / iteration

        == Return ==
        scikit-learn model (SearchCV object)
        """
        if poly and ("numeric__poly__degree" not in self.preprocessor.get_params()):
            raise Exception("Polynomial features are not set in the numerical pipeline")
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, stratify=y,
                                                            random_state=self.random_state)

        pipeline = Pipeline([
            ("prep", self.preprocessor),
            ('algo', DummyRegressor())
        ])

        cv_algo = RandomizedSearchCV if search_mode == "random" else BayesSearchCV
        model = cv_algo(pipeline, autoclf_params(algo, search_mode, poly), cv=cv, n_iter=n_trial, n_jobs=-1, verbose=1,
                        random_state=self.random_state)
        model.fit(X_train, y_train)

        _report(model, X_train, y_train, X_test, y_test)
        return model


def _report(model, X_train, y_train, X_test, y_test):
    print("================== Best Model ==================")

    for k, v in model.best_params_.items():
        if k != "algo":
            print(f"{k:25} | {v}")
        else:
            print(f"{k:25} | {v.__class__.__name__}")
    print("================================================")
    print()
    print("==================== Score =====================")
    print(f"Train: {model.score(X_train, y_train)}")
    print(f"Valid: {model.best_score_}")
    print(f"Test : {model.score(X_test, y_test)}")
    print("================================================")
