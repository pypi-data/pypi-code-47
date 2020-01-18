from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier
from sklearn.svm import SVR, SVC
from xgboost import XGBRegressor, XGBClassifier
from sklearn.linear_model import ElasticNet, LogisticRegression
from jcopml.tuning import random_search_params as rsp, bayes_search_params as bsp

_reg_algo = ["rf", "knn", "svm", "xgb", "enet"]
_clf_algo = ["rf", "knn", "svm", "xgb", "logreg"]


def _reg_map(algo, search_mode):
    f = rsp if search_mode == "random" else bsp

    _map = {
        "rf": (RandomForestRegressor(n_jobs=-1, random_state=42), f.rf_params, f.rf_poly_params),
        "knn": (KNeighborsRegressor(), f.knn_params, f.knn_poly_params),
        "svm": (SVR(max_iter=500), f.svm_params, f.svm_poly_params),
        "xgb": (XGBRegressor(n_jobs=-1, random_state=42), f.xgb_params, f.xgb_poly_params),
        "enet": (ElasticNet(), f.enet_params, f.enet_poly_params)
    }
    return _map[algo]


def _clf_map(algo, search_mode):
    f = rsp if search_mode == "random" else bsp

    _map = {
        "rf": (RandomForestClassifier(n_jobs=-1, random_state=42), f.rf_params, f.rf_poly_params),
        "knn": (KNeighborsClassifier(), f.knn_params, f.knn_poly_params),
        "svm": (SVC(max_iter=500), f.svm_params, f.svm_poly_params),
        "xgb": (XGBClassifier(n_jobs=-1, random_state=42), f.xgb_params, f.xgb_poly_params),
        "logreg": (LogisticRegression(), f.logreg_params, f.logreg_poly_params)
    }
    return _map[algo]


def autoreg_params(algo, search_mode, poly):
    if algo == "all":
        algo = _reg_algo

    params = []
    for a in algo:
        if a in _reg_algo:
            algo, param, poly_param = _reg_map(a, search_mode)
            p = poly_param if poly else param
            p["algo"] = [algo]
            params.append(p)
        else:
            print(f"Available algorithms {tuple(_reg_algo)}. {a} is not available.")
    return params


def autoclf_params(algo, search_mode, poly):
    if algo == "all":
        algo = _clf_algo

    params = []
    for a in algo:
        if a in _clf_algo:
            algo, param, poly_param = _clf_map(a, search_mode)
            p = poly_param if poly else param
            p["algo"] = [algo]
            params.append(p)
        else:
            print(f"Available algorithms {tuple(_clf_algo)}. {a} is not available.")
    return params
