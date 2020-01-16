import os
import sys

import pandas as pd
import numpy as np

import somutils

""" Som Pre Processer Model """
def execute(args):
    """
    
    '_output_dir_path_'
    '_som_input_path_'
    '_som_params_path_'
    '_columns_'
    '_rows_'
    '_iterations_'
    '_grid_type_'
    '_number_clusters_'

    return - dictionary with the following key, values
        'model_weights_path': path to saved .txt weights
        'som_figure': pyplot figure of trained SOM
    """
    workspace_dir = args['_output_dir_path_']
    if not os.path.isdir(workspace_dir):
        os.mkdir(workspace_dir)
    
    data_path = args['_som_input_path_']
    som_params_path = args['_som_params_path_']
    
    data_dataframe = pd.read_csv(data_path)
    data_dataframe.columns = data_dataframe.columns.str.lower()

    # List of columns to include as input into SOM
    selected_features = ["S", "VC", "VC_rat", "ER", "WtoD", "IR", "d50", 
                         "d84_d16", "nBars", "nFCs", "pArmor", "SSP", "SSP_bal"]
                         
    validation_class_feat = ["class"]
    
    selected_features_lower = [x.lower() for x in selected_features]
    
    #selected_features_sorted = selected_features_lower.sort()
    #tmp_df_cols = data_dataframe.columns
    #tmp_df_cols.sort()
    
    # The number of features for the SOM                     
    num_feats = len(selected_features_lower)  

    # Get only the data from the features of interest
    selected_data_feats_df = data_dataframe.loc[:, selected_features_lower]
    #print(selected_data_feats_df.head(n=50))
    # Handle NODATA / Missing data by removing (for now)
    selected_data_feats_df.dropna(how='any', inplace=True)
    #print(selected_data_feats_df.head(n=50))

    # NORMALIZE DATA by min, max normalization approach
    selected_feats_df_norm = somutils.normalize(selected_data_feats_df)

    # Display statistics on our normalized data
    print(selected_feats_df_norm.describe())

    # Initial learning rate for SOM. Will decay to 0.01 linearly
    init_learning_rate = 0.05

    # The number of rows for the grid and number of columns. This dictates 
    # how many nodes the SOM will consist of. Currently not calculated 
    # using PCA or other analyses methods.
    nrows = int(args['_rows_'])
    ncols = int(args['_columns_'])
    grid_type = args['_grid_type_']
    
    # Create the SOM grid (which initializes the SOM network)
    som_grid = somutils.create_grid(nrows, ncols, grid_type=grid_type)

    # Initial neighbourhood radius is defaulted to 2/3 of the longest distance
    # Should be set up similar to R package Kohonen
    # https://cran.r-project.org/web/packages/kohonen/kohonen.pdf
    # Radius will decay to 0.0 linearly
    init_radius = somutils.default_radius(som_grid)

    # Get the data as a matrix dropping the dataframe wrapper
    data = selected_feats_df_norm.as_matrix()

    # Number of iterations to run SOM
    niter = int(args['_iterations_'])
    # Number of clusters to cluster SOM
    nclusters = int(args['_number_clusters_'])

    # Run SOM
    som_weights, object_distances = somutils.run_som(data, som_grid, grid_type, niter, init_radius, init_learning_rate)
    # Save SOM model. This is done by saving the weights (numpy ndarray)
    som_model_weights_path = os.path.join(workspace_dir, 'som_model.txt')
    somutils.save_som_model(som_weights, som_model_weights_path, grid_type, cluster=nclusters)
    #np.save(som_model_weights_path, som_weights)

    # It's possible that some data samples were not selected for training, thus do
    # do not have a latest bmu
    object_distances = somutils.fill_bmu_distances(data, som_weights, object_distances)

    # Cluster SOM nodes
    clustering = somutils.cluster_som(som_weights, nclusters)

    # Let's save the clusters corresponding to the samples now
    results_path = os.path.join(workspace_dir, 'cluster_results.csv')
    somutils.save_cluster_results(selected_data_feats_df, results_path, clustering.labels_, (nrows, ncols), object_distances)
    # Display the SOM, coloring the nodes into different clusters from 
    # 'clustering' above
    # Optional: pass in original dataframe to plot 
    # the IDs onto their respective nodes
    som_figure_path = os.path.join(workspace_dir, 'som_figure.jpg')
    plt = somutils.basic_som_figure(data, som_weights, som_grid, clustering.labels_,
                                grid_type, som_figure_path, dframe=data_dataframe, class_name='class')
                                
    return {'model_weights_path':som_model_weights_path, 'som_figure':plt.gcf()}