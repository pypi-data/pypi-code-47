import numpy as np

penalty_12 = ["l1", "l2"]
penalty_12none = ["l1", "l2", None]
penalty_12e = ["l1", "l2", "elasticnet"]
penalty_all = ["l1", "l2", None, "elasticnet"]
max_iter = [100, 300, 1000]
max_iter_inf = [100, 300, 500, 1000, np.inf]
max_iter_inf2 = [100, 300, 500, 1000, -1]
tol = [1e-4, 1e-3, 1e-2]
warm_start = [True, False]
alpha = [1e-5, 1e-4, 1e-3, 1e-2, 0.1, 1, 3, 10]
alpha_small = [1e-5, 1e-3, 0.1, 1]
n_iter = [5, 10, 20]
eta0 = [1e-4, 1e-3, 1e-2, 0.1]
C = [1e-2, 0.1, 1, 5, 10]
C_small = [0.1, 1, 5]
epsilon = [1e-3, 1e-2, 0.1, 0]
normalize = [True, False]
kernel = ["linear", "poly", "rbf", "sigmoid"]
degree = [1, 2, 3, 4, 5]
gamma = list(np.logspace(-9, 3, 6)) + ["auto"]
gamma_small = list(np.logspace(-6, 3, 3)) + ["auto"]
coef0 = [0, 0.1, 0.3, 0.5, 0.7, 1]
coef0_small = [0, 0.4, 0.7, 1]
shrinking = [True, False]
nu = [1e-4, 1e-2, 0.1, 0.3, 0.5, 0.75, 0.9]
nu_small = [1e-2, 0.1, 0.5, 0.9]
n_neighbors = [5, 7, 10, 15, 20]
neighbor_algo = ["ball_tree", "kd_tree", "brute"]
neighbor_leaf_size = [1, 2, 5, 10, 20, 30, 50, 100]
neighbor_metric = ["cityblock", "euclidean", "l1", "l2", "manhattan"]
neighbor_radius = [1e-2, 0.1, 1, 5, 10]
learning_rate = ["constant", "invscaling", "adaptive"]
learning_rate_small = ["invscaling", "adaptive"]
n_estimators = [2, 3, 5, 10, 25, 50, 100]
n_estimators_small = [2, 10, 25, 100]
max_features = [3, 5, 10, 25, 50, "auto", "log2", None]
max_features_small = [3, 5, 10, "auto", "log2", None]
max_depth = [None, 3, 5, 7, 10]
max_depth_small = [None, 5, 10]
min_samples_split = [2, 5, 10, 0.1]
min_impurity_split = [1e-7, 1e-6, 1e-5, 1e-4, 1e-3]
tree_learning_rate = [0.8, 1]
min_samples_leaf = [2]

logreg_gridsearch = {
    "penalty": penalty_12,
    "max_iter": max_iter,
    "tol": tol,
    "warm_start": warm_start,
    "C": C,
    "solver": ["liblinear"],
}
