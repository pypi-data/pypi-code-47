import re
import glob
import collections
import numpy as np
import pandas as pd
import networkx as nx
from rake_nltk import Rake
import matplotlib.pyplot as plt
from itertools import combinations
import scipy.interpolate as interpolate
from sklearn.feature_extraction.text import CountVectorizer


class Ananse(object):
    """
     A python package to partially automate search term selection and write search strategies for systematic reviews

    """

    def __init__(self):
        self.search_results = {'id': [], 'text': [], 'title': [], 'abstract': [], 'keywords': [], 'type': [],
                               'authors': [],
                               'affiliation': [], 'source': [], 'year': [], 'volume': [], 'issue': [], 'startpage': [],
                               'endpage': [], 'doi': [], 'language': [], 'database': []}

        self.wos_li = []
        self.scopus_li = []
        self.regex = re.compile('[@_!#$%^&*()<>?•°/|}{~:]')
        self.columns = ['title', 'abstract']
        self.raked_keywords = []
        self.real_keywords = []
        self.all_keywords = []
        self.terms = []
        self.centrality = ""
        self.dfm_dataframe = pd.DataFrame()
        # self.t, self.c, self.k, self.spline = None
        self.cut_strengths = []
        self.deg_seq = {}
        self.network_graph = nx.Graph()
        self.bad_chars = ['•', '°', ';', ':', '!', '?', "*", '[', ']', '}', '{', '@', '~', '_', '#', '$', '%', '^', '&',
                          '(', ')', '<', '>', '/', '|', '±', '+', '-', '©', '`', '’', "'"]

    def remove_punctuations(self, raw_string):
        """
        This method removes all symbols and numbers from a string

        :param raw_string: string with characters and numbers
        :return: cleaned string
        """

        raw_string = raw_string.translate({ord(c): '' for c in "1234567890"})

        return raw_string.translate({ord(c): '' for c in self.bad_chars})

    def import_naive_results(self, path, save_dataset=False, save_directory=None, clean_dataset=False):
        """
        This method imports the search results from a specified path

        :param clean_dataset: if TRUE, de-duplicates search results after importing
        :param save_dataset: if TRUE, saves the full search results to a .csv
        :param save_directory: the path to a directory where search results will be saved if save_dataset is set to TRUE
        :param path: path containing the naive search results files
        :return: a pandas data frame consisting of assembled search results
        """

        wos_li = []
        scopus_li = []

        # import all files in the directory, automatically detect on file name extension [supports WOS and Scopus]

        all_files = glob.glob(path + "*")
        for filename in all_files:
            if filename.endswith('.txt'):
                df = pd.read_csv(filename, index_col=False, delimiter="\t", quotechar=None, quoting=3)
                wos_li.append(df)
            elif filename.endswith('.csv'):
                df = pd.read_csv(filename)
                scopus_li.append(df)

        # check if anything was imported
        if len(wos_li) != 0:  # check to see if any web of science results was imported

            # concatenate files from same database into DataFrame
            wos_dataset = pd.concat(wos_li, axis=0, ignore_index=True)

            # merge article titles and abstract to form text from which keywords will be extracted
            text = list(wos_dataset[['TI', 'AB']].apply(lambda x: '{}{}'.format(x[0], x[1]), axis=1))
            wos_text = [self.remove_punctuations(t) for t in text]

            self.search_results['id'] = list(wos_dataset['UT'])
            self.search_results['text'] = wos_text
            self.search_results['title'] = list(wos_dataset['TI'])
            self.search_results['abstract'] = list(wos_dataset['AB'])
            self.search_results['keywords'] = list(wos_dataset['DE'])
            self.search_results['type'] = list(wos_dataset['DT'])
            self.search_results['authors'] = list(wos_dataset['AU'])
            self.search_results['affiliation'] = list(wos_dataset['C1'])
            self.search_results['source'] = list(wos_dataset['SO'])
            self.search_results['year'] = list(wos_dataset['PY'])
            self.search_results['volume'] = list(wos_dataset['VL'])
            self.search_results['issue'] = list(wos_dataset['IS'])
            self.search_results['startpage'] = list(wos_dataset['BP'])
            self.search_results['endpage'] = list(wos_dataset['EP'])
            self.search_results['doi'] = list(wos_dataset['DI'])
            self.search_results['language'] = list(wos_dataset['LA'])
            self.search_results['database'] = (['WOS'] * len(wos_dataset.index))
        elif len(scopus_li) != 0:  # check to see if any scopus results was imported

            # concatenate files from same database into DataFrame
            scopus_dataset = pd.concat(scopus_li, axis=0, ignore_index=True)

            text = list(scopus_dataset[['Title', 'Abstract']].apply(lambda x: '{}{}'.format(x[0], x[1]), axis=1))
            scopus_text = [self.remove_punctuations(t) for t in text]

            self.search_results['id'] = self.search_results['id'] + list(scopus_dataset['EID'])
            self.search_results['text'] = self.search_results['text'] + scopus_text
            self.search_results['title'] = self.search_results['title'] + list(scopus_dataset['Title'])
            self.search_results['abstract'] = self.search_results['abstract'] + list(scopus_dataset['Abstract'])
            self.search_results['keywords'] = self.search_results['keywords'] + list(scopus_dataset['Author Keywords'])
            self.search_results['type'] = self.search_results['type'] + list(scopus_dataset['Document Type'])
            self.search_results['authors'] = self.search_results['authors'] + list(scopus_dataset['Authors'])
            self.search_results['affiliation'] = self.search_results['affiliation'] + list(
                scopus_dataset['Affiliations'])
            self.search_results['source'] = self.search_results['source'] + list(scopus_dataset['Source'])
            self.search_results['year'] = self.search_results['year'] + list(scopus_dataset['Year'])
            self.search_results['volume'] = self.search_results['volume'] + list(scopus_dataset['Volume'])
            self.search_results['issue'] = self.search_results['issue'] + list(scopus_dataset['Issue'])
            self.search_results['startpage'] = self.search_results['startpage'] + list(scopus_dataset['Page start'])
            self.search_results['endpage'] = self.search_results['endpage'] + list(scopus_dataset['Page end'])
            self.search_results['doi'] = self.search_results['doi'] + list(scopus_dataset['DOI'])
            self.search_results['language'] = self.search_results['language'] + (
                    ['English'] * len(scopus_dataset.index))
            self.search_results['database'] = self.search_results['database'] + list(scopus_dataset['Source'])

        # merge all search database results into a dataframe

        data_frame = pd.DataFrame.from_dict(self.search_results)

        if save_dataset is True:
            if save_directory is not None:
                data_frame.to_csv(r"{}".format(save_directory + 'imported_results.csv'), index=False)
            else:
                data_frame.to_csv('data/IMPORTED/imported_results.csv', index=False)

        if clean_dataset is True:
            data_frame = self.deduplicate_dataframe(data_frame, self.columns)

        return data_frame

    def deduplicate_dataframe(self, DataFrame, columns):
        """
        this method duplicated a DataFrame based on certain columns
        it considers on the first occurrence of a row as unique and deletes(inplace=True) other duplicates

        :param DataFrame: a pandas DataFrame to be deduplicated
        :param columns: a list of fields to check for duplicate values and deduplicated the dataframe
        :return: DataFrame with removed duplicate rows depending on Arguments passed.
        """
        if columns:
            for column in columns:
                DataFrame.drop_duplicates(subset=column, keep='first', inplace=True)
        else:
            for column in self.columns:
                DataFrame.drop_duplicates(subset=column, keep='first', inplace=True)

        return DataFrame

    def extract_terms(self, DataFrame, min_len=2, max_len=4):
        """
        This method uses the RAKE Algorithm to extract keywords from the text column of the DataFrame of naive search
        results.


        :param DataFrame:
        :param min_len: minimum keyword length
        :param max_len: maximum keyword length
        :return: a list consisting of  a combination of extracted keywords and author keyword
        """
        r = Rake(language='english', min_length=min_len, max_length=max_len,
                 punctuations='!"#$%&\'()*+,-),./“:;≥•°≤<=|±+‘>©?@[\\]^_`{|}~')

        # Extraction using the text column the text.
        texts = list(DataFrame['text'])

        r.extract_keywords_from_sentences(texts)
        self.raked_keywords = r.get_ranked_phrases()  # raked keywords

        # Extract author keywords from naive search results and remove blank values
        author_keywords = list(DataFrame['keywords'])
        self.real_keywords = [x.lower() for x in author_keywords if
                              str(x) != 'nan']  # removing nan values from list of author keywords

        # merge all keywords and split into list
        self.real_keywords = "".join(self.real_keywords)
        self.real_keywords = self.real_keywords.split(";")

        # merge raked keywords with author keywords
        keywords = self.raked_keywords + self.real_keywords

        # loop through all keywords, remove every keyword with a digit in it and create new cleaned list
        digits_cleaned_all_keywords = [x for x in keywords if (any(char.isdigit() for char in x) == False)]

        regex = re.compile('[@_!#$%^&*()<>?•°/|}{~:]')

        # loop through all keywords, remove every keyword with a symbol in it using regex and create new cleaned list
        all_keywords = [x for x in digits_cleaned_all_keywords if (regex.search(x) is None)]

        # Convert keyword list to set and then back to list to deduplicate keyword list
        all_keywords = list(set(all_keywords))

        return self.all_keywords

    def create_dtm(self, doc, keywords, min_len=2, max_len=3, dfm_type=""):
        """
        This method creates a Document-Term Matrix


        :param min_len: minimum keyword length
        :param max_len: maximum keyword length
        :param doc: a list of article title, abstract or any article property
        :param keywords: a list of keywords to use for the Document-Term Matrix
        :param dfm_type: whether the dfm should be created based on document tokens or a restricted list of keywords
                [token, keywords]
        :return: a multidimensional array of a Document-Term Matrix and a list of terms(columns)
        """

        doc = list(doc)
        cleaned_list = [str(x) for x in doc if str(x) != 'nan']
        doc_set = cleaned_list

        vec = CountVectorizer(ngram_range=(min_len, max_len))

        if dfm_type.lower() == "token":
            tf = vec.fit_transform(doc_set)
        elif dfm_type == "" or dfm_type.lower() == "keywords":
            if keywords:
                vec.fit(keywords)
                tf = vec.transform(doc_set)
            else:
                tf = vec.fit_transform(doc_set)

        self.terms = vec.get_feature_names()

        return tf.toarray(), self.terms

    def dtm_to_dataframe(self, dtm, keywords, doc):
        """
        This method created a data frame of a Document-Term Matrix

        :param dtm:  a multidimensional array of a Document-Term Matrix
        :param keywords: a list of keywords to use for the Document-Term Matrix
        :param doc: a list of article title, abstract or any article property
        :return: a data frame of a Document-Term Matrix
        """
        doc = list(doc)
        self.dfm_dataframe = pd.DataFrame(data=dtm, columns=keywords, index=doc)
        return self.dfm_dataframe

    def create_network(self, im, keywords, draw_graph=False, save_network=False, save_directory=None):
        """
        This method creates a graph when given a Document-Term Matrix in the form of an incidence matrix

        :param im: the incidence matrix
        :param keywords: keywords for labelling
        :param draw_graph: if TRUE, graph is drawn
        :param save_network: if TRUE, saves the graph to a .png
        :param save_directory: the path to a directory where search results will be saved if save_dataset is set to TRUE
        :return: a networkx graph
        """

        A = im

        keywords.sort()
        nodes = [i for i in range(len(keywords))]
        edges = []

        for row in A:
            # loop through all rows(article) in multidimensional array and the index of each column(keyword) with
            # a value of 1 and store the column indices in a list
            x = [i for i, e in enumerate(list(row)) if e == 1]
            # make a combination of this column indices to show how their connection (edge)
            perm = combinations(x, 2)
            for i in list(perm):
                # store every single combination made
                edges.append(list(i))

        self.network_graph.add_nodes_from(nodes)
        self.network_graph.add_edges_from(edges)
        num_of_nodes = self.network_graph.number_of_nodes()

        old_labels = [i for i in range(num_of_nodes)]
        new_labels = keywords
        mapping = dict(zip(old_labels, new_labels))

        H = nx.relabel_nodes(self.network_graph, mapping)

        if draw_graph:
            plt.figure(figsize=(12, 12))
            nx.draw_networkx(H, with_label=True, pos=nx.spring_layout(H))
            if save_network:
                if save_directory is not None:
                    plt.savefig(r"{}".format(save_directory + "simple_path.png.png"))
                else:
                    plt.savefig("degree_distribution .png")

        return H

    def get_centrality(self, g, method):
        """
        This method evaluate the node importance of a graph

        :param g: a graph from which you find its node importance
        :param method: the method for finding the node importance
        :return: a dictionary containing nodes with their importance
        """
        if method.lower() == "degree":
            self.centrality = nx.degree_centrality(g)
        elif method.lower() == "closeness":
            self.centrality = nx.closeness_centrality(g)
        elif method.lower() == "betweenness":
            self.centrality = nx.betweenness_centrality(g)

        return self.centrality

    def plot_degree_distribution(self, g, save_plot=False, save_directory=None):
        """
        This method plots a distribution of the graph degree

        :param g: graph whose degree distribution is to be plotted
        :param save_plot: if save_plot=True saves the plot to a .png
        :param save_directory: the path to a directory where search results will be saved if save_plot is set to TRUE
        :return:
        """
        for n in g.nodes():
            deg = g.degree(n)
            if deg not in self.deg_seq:
                self.deg_seq[deg] = 0
            self.deg_seq[deg] += 1

        items = sorted(self.deg_seq.items())
        fig = plt.figure(figsize=(12, 12), dpi=80)
        ax = fig.add_subplot(111)
        ax.plot([k for (k, v) in items], [v for (k, v) in items])
        plt.title("Network Distribution")
        plt.show()

        if save_plot:
            if save_directory is not None:
                fig.savefig(r"{}".format(save_directory + "degree_distribution.png"))
            else:
                fig.savefig("degree_distribution.png")

    def plot_degree_histogram(self, g, save_plot=False, save_directory=None):
        """
        This method plots a histogram of the graph degree

        :param g: graph whose degree distribution is to be plotted
        :param save_plot: if save_plot=True saves the plot to a .png
        :param save_directory: the path to a directory where search results will be saved if save_plot is set to TRUE
        :return:
        """
        degree_sequence = sorted([d for n, d in g.degree()], reverse=True)  # degree sequence

        degreeCount = collections.Counter(degree_sequence)
        deg, cnt = zip(*degreeCount.items())

        fig, ax = plt.subplots(figsize=(12, 12), dpi=80)
        plt.bar(deg, cnt, width=0.80, color='b')

        plt.title("Degree Histogram")
        plt.ylabel("Count")
        plt.xlabel("Degree")
        ax.set_xticks([d + 0.4 for d in deg])
        ax.set_xticklabels(deg)

        if save_plot:
            if save_directory is not None:
                fig.savefig(r"{}".format(save_directory + "degree_distribution.png"))
            else:
                fig.savefig("degree_distribution.png")

    def plot_rank_degree_distribution(self, g, save_plot=False, save_directory=None):
        """
        This methods plots a rank degree distribution of the graph

        :param g: graph whose degree distribution is to be plotted
        :param save_plot: if save_plot=True saves the plot to a .png
        :param save_directory: the path to a directory where search results will be saved if save_plot is set to TRUE
        :return:
        """
        degree_sequence = sorted([d for n, d in g.degree()], reverse=True)
        d_max = max(degree_sequence)

        fig = plt.figure(figsize=(12, 12), dpi=80)
        fig.add_subplot(111)
        plt.loglog(degree_sequence, 'b-', marker='o')
        plt.title("Degree rank plot")
        plt.ylabel("degree")
        plt.xlabel("rank")

        if save_plot:
            if save_directory is not None:
                fig.savefig(r"{}".format(save_directory + "degree_distribution.png"))
            else:
                fig.savefig("rank_degree_distribution.png")

    def find_knots(self, x, y, degrees, knot_num=1):
        """
        This method find the knots of a two sets of values

        :param x: x values
        :param y: y values
        :param degrees: degrees of the spline
        :param knot_num: number of knots of the spline
        :return: t = knots, c = spline coefficients, k = B-spline order
        """
        t, c, k = interpolate.splrep(x, y, k=degrees, s=knot_num)
        return t, c, k

    def fit_spline(self, t, c, k):
        """
        This methods fits t = knots, c = spline coefficients, k = B-spline order to a B-spline

        :param t: knots
        :param c: spline coefficients
        :param k: B-spline order
        :return: fitted B-spline
        """
        self.spline = interpolate.BSpline(t, c, k, extrapolate=False)
        return self.spline

    def make_importance(self, g, importance_method):
        """
        This methods creates a dataframe made up of node names with their importance and their rank (index) from a graph

        :param g: graph
        :param importance_method: method to use to check node importance
        :return: a data frame of rank, node importance and node name
        """
        centrality = self.get_centrality(g, importance_method)
        rank = [i + 1 for i in range(len(centrality))]
        importance = list(centrality.values())
        node_names = list(centrality.keys())
        lis = [list(a) for a in zip(rank, importance, node_names)]
        importance_data = pd.DataFrame(lis, columns=['rank', 'importance', 'nodenames'])

        return importance_data

    def find_cutoff(self, g, method, importance_method, degrees=2, knot_num=1, percent=0.8):
        """
        This method finds the cutoff for a graph network using either cumulative or spline method of cutting of
        the degree distribution

        :param g: graph
        :param method: method of finding cutoff
        :param importance_method: method to use to check node importance
        :param degrees: spline degree
        :param knot_num: spline number of knots
        :param percent: cutoff percentage for cumulative method
        :return: cutoff strengths
        """

        importance_data = self.make_importance(g, importance_method)
        if method.lower() == "spline":
            knots, c, k = self.find_knots(list(importance_data["rank"]), importance_data["importance"], degrees,
                                          knot_num)
            cut_points = [np.floor(x) for x in list(knots)]
            self.cut_strengths = list(list(importance_data.importance)[int(i - 1)] for i in cut_points)
        elif method.lower() == "cumulative":
            cumulative_sum = np.cumsum(sorted(importance_data["importance"]))
            cum_str = np.amax(cumulative_sum)
            cut_point = [i for i in cumulative_sum if i >= (cum_str * percent)][0]
            self.cut_strengths = list(sorted(importance_data["importance"]))[int(cut_point)]

        return self.cut_strengths

    def reduce_graph(self, g, importance_method, cutoff_strengths, draw_reduced_graph=False):
        """
        This methods generated a graph consisting of only important nodes

        :param g: graph
        :param draw_reduced_graph: RUE, draws reduced graph
        :param importance_method: method to use to check node importance
        :param cutoff_strengths: cut off of the graph
        :return: a list of important nodes and a reduced graph of only important nodes
        """
        importance_data = self.make_importance(g, importance_method)
        if isinstance(cutoff_strengths, list):
            cutoff_strengths = np.amax(cutoff_strengths)
        importance_nodes = list(importance_data.loc[importance_data['importance'] > cutoff_strengths, "nodenames"])
        reduced_graph = g.subgraph(importance_nodes)

        if draw_reduced_graph is True:
            nx.draw_networkx(reduced_graph, with_label=True, pos=nx.spring_layout(reduced_graph))

        return reduced_graph, importance_nodes

    def get_keywords(self, reduced_graph, save_keywords=True, save_directory=None):
        """

        :param reduced_graph: a reduced graph consisting of only important nodes(keywords)
        :param save_keywords: if save_keywords=True, saves the keywords to a .csv
        :param save_directory: path to a directory where suggested keywords will be saved if save_dataset is set to TRUE
        :return: suggested keywords for final review
        """
        keywords = [self.remove_punctuations(x) for x in reduced_graph.nodes()]
        suggested_keywords = [i for i in keywords if i]
        df = pd.DataFrame(suggested_keywords, columns=["keywords"])

        if save_keywords:
            if save_directory is not None:
                df.to_csv(r"{}".format(save_directory + 'relevant_keywords.csv'), index=False)
            else:
                df.to_csv('relevant_keywords.csv', index=False)

        return suggested_keywords
