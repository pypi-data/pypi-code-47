from sklearn import cluster
import json
import pandas as pd
import matplotlib.image
import numpy as np
img = matplotlib.image
import os


class Marscoordfinder:
    '''
    Description: This class contains functions that will allow the user to produce a pandas DataFrame of equidistant
                    latitude and longitude points within a given region.
                    Furthermore, the points will be constrained to land mass as this is the most common need
    Key Functions:
        - getNPointsInRegion - This function allows you to specify number of coordinates you'd like as well as
                                North, South, East and West boundaries
        - pointsInRegion - This function allows you to specify number of coordinates you'd like as well as provide
                            the filepath to a JSON file containing the boundary coordinates of a given region

    Notes:
        To create the JSON file mentioned above, instructions are in the README file of this package
    '''

    def __init__(self, world_landmap='water_8k.png'):
        self.world_land_map = img.imread(os.path.dirname(__file__) + '/' + world_landmap)

    def isLand(self, xcoord, ycoord):
        '''
        :function: classify a given coordinate as being land or not
        :param xcoord: longitude of specific point
        :param ycoord: latitude of specific point
        :return: 1 or 0 depending if the point is on land or not
        '''
        im = self.world_land_map
        xcoord = xcoord + 180
        ycoord = ycoord + 90
        x_pixel = int((xcoord / 360) * im.shape[1]) - 1
        y_pixel = int(((180 - ycoord) / 180) * im.shape[0]) - 1
        is_land = im[y_pixel, x_pixel]
        return int(is_land) != 1

    def getPointsBetween(self, n, s, e, w, fidelity):
        '''
        :function:  function to return a matrix of points in the specified bounded region as well as whether they are
                    on land or not
        :param n: Northern Latitude
        :param s: Southern Latitude
        :param e: Eastern Longitude
        :param w: Western Longitude
        :param fidelity: granularity of the coordinate grid returned (smaller means more points)
        :return: matrix of coordinates and indicator as to being in land or not
        '''

        longitude_list = []
        latitude_list = []

        long = w
        while long <= e:
            longitude_list.append(long)
            long += fidelity

        lat = n
        while lat >= s:
            latitude_list.append(lat)
            lat -= fidelity

        coord_matrix = []
        for lon in longitude_list:
            for lat in latitude_list:
                is_land = self.isLand(lon, lat)
                coord_matrix.append([lon, lat, is_land])

        return np.matrix(coord_matrix)

    def getNPointsInRegion(self, NPoints, n=89, s=-60, e=180, w=-180, fidelity=1):
        '''

        :param NPoints: Number of coordinates you want to find
        :param n: Northern Latitude
        :param s: Southern Latitude
        :param e: Eastern Longitude
        :param w: Western Longitude
        :param fidelity: granularity of the coordinate grid returned (smaller means more points)
        :return: Pandas DataFrame of the points found to be land,
                Pandas DataFrame the equidistant coordinates within this region
        '''
        globe_m = self.getPointsBetween(n, s, e, w, fidelity)
        land = np.squeeze(np.asarray(globe_m[:, 2] == 1))
        land_m = globe_m[land]

        myCL = cluster.k_means(land_m, NPoints)
        centroids = myCL[0]

        return pd.DataFrame(land_m).iloc[:,0:2], pd.DataFrame(centroids).iloc[:,0:2]

    def pointsInRegion(self, NPoints, filepath=None):
        '''

        :param NPoints: Number of coordinates you want to find
        :param filepath: filepath of corresponding JSON file which bounds a given region
        :return: Pandas DataFrame of the points found to be land,
                Pandas DataFrame the equidistant coordinates within this region
        '''

        filename = filepath
        with open(filename, 'r') as f:
            json_file = json.load(f)

        coordinates = json_file['features'][0]['geometry']['coordinates'][0]
        coordinates_pd = pd.DataFrame(coordinates)
        min_long = min(coordinates_pd.iloc[:, 0])
        min_lat = min(coordinates_pd.iloc[:, 1])
        max_long = max(coordinates_pd.iloc[:, 0])
        max_lat = max(coordinates_pd.iloc[:, 1])

        globe_m = self.getPointsBetween(n=max_lat, s=min_lat, e=max_long, w=min_long, fidelity=0.08)
        land = np.squeeze(np.asarray(globe_m[:, 2] == 1))
        land_m = globe_m[land]
        long, lat = land_m[:, 0], land_m[:, 1]

        columns = ['Long', 'Lat', 'intersections', 'in/out']
        index = range(0, len(land_m))

        intersections = pd.DataFrame(index=index, columns=columns)

        for j in range(len(land_m)):

            intersections.iloc[j, 0] = long[j]
            intersections.iloc[j, 1] = lat[j]

            inter = 0
            for i, points in enumerate(coordinates):
                start_x = coordinates[i][0]
                start_y = coordinates[i][1]
                if i < len(coordinates) - 1:
                    next_x = coordinates[i + 1][0]
                    next_y = coordinates[i + 1][1]
                else:
                    next_x = coordinates[0][0]
                    next_y = coordinates[0][1]

                centroid_x = long[j]
                centroid_y = lat[j]

                if start_y < centroid_y and next_y < centroid_y:
                    continue
                elif start_y > centroid_y and next_y > centroid_y:
                    continue
                elif start_x < centroid_x and next_x < centroid_x:
                    continue
                else:
                    inter += 1

            intersections.iloc[j, 2] = inter

        for k in range(len(intersections)):
            if intersections.iloc[k, 2] % 2 == 0:
                intersections.iloc[k, 3] = 0
            else:
                intersections.iloc[k, 3] = 1

        is_in = intersections['in/out'] == 1

        centroids_in = land_m[is_in]

        cl = cluster.k_means(centroids_in, NPoints)
        centroids_new = pd.DataFrame(cl[0]).iloc[:, 0:2]

        return pd.DataFrame(land_m).iloc[:, 0:2], (centroids_new)

    def createJson(self, centroids, filepath):
        centroids_in_df = centroids
        centroids_in_df['location'] = ''
        centroids_in_df.columns = ['longitude', 'latitude', 'location']

        for l in range(len(centroids_in_df)):
            centroids_in_df.iloc[l, 2] = 'Location {}'.format(l)

        # centroids_in_df = centroids_in_df.drop('in', 1)
        centroids_in_df = centroids_in_df[['location', 'longitude', 'latitude']]
        centroids_in_df['longitude'] = centroids_in_df['longitude'].apply(str)
        centroids_in_df['latitude'] = centroids_in_df['latitude'].apply(str)
        df_transpose = centroids_in_df.transpose()
        df_transpose.to_json(r'{}'.format(filepath))
        return True
