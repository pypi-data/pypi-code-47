from sklearn.datasets import make_circles

def load_circles():
    return make_circles(200, random_state=1, noise=0.05)

