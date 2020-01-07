"""
Clustering functions written specifically for the project.

"""
import numpy as np
from pprint import pprint

def distance(x, y):
    return np.linalg.norm(x - y)

def bruno(array, threshold=0.5):
    labeled_array = np.zeros(array.shape[0])
    clusters = [[array[0]]]
    centroids =[[array[0]]]
    c_history = [centroids[:]]
    for i, e in enumerate(array[1:], 1):
        new_centroids = [np.mean(c + [e], axis=0) for c in clusters]
        # for c in clusters:
        #     print(f"Tipos: c es {type(c)}, e es {type(e)}, [e] es {type([e])}")
        #     print(c+e)
        # pprint(new_centroids)
        distances = [distance(c, e) for c in new_centroids]
        index = np.argmin(distances)
        dist = distances[index]
        if dist <= threshold:
            clusters[index].append(e)
            centroids[index] = new_centroids[index]
            labeled_array[i] = index
        else:
            new_cluster = len(clusters)
            clusters.append([e])
            centroids.append([e])
            labeled_array[i] = new_cluster
        c_history.append(centroids[:])
    return labeled_array, centroids, c_history
