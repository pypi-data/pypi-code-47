import re
import glob
import operator
import collections
import numpy as np
import pandas as pd
import networkx as nx
from RISparser import readris
import matplotlib.pyplot as plt
from itertools import combinations
from rake_nltk import Rake, Metric
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
        self.columns = ['title', 'abstract']

        self.regex = re.compile('[@_!#$%^&*()’<>?±+•°/|`\'\"^-©}{~:;]')
        self.raked_keywords = []
        self.real_keywords = []
        self.all_keywords = []
        self.terms = []

        self.centrality = ""
        self.dfm_dataframe = pd.DataFrame()

        self.network_graph = nx.Graph()
        self.bad_chars = ['•', '°', ';', ':', '!', '?', "*", '[', ']', '}', '{', '@', '~', '_', '#', '$', '%', '^', '&',
                          '(', ')', '<', '>', '/', '|', '±', '+', '©', '`', '’', "'"]

    def remove_punctuations(self, raw_string):
        """
        This method removes all symbols and numbers from a string

        :param raw_string: string with characters and numbers
        :return: cleaned string
        """

        text = str(raw_string)
        text = text.translate({ord(c): '' for c in "1234567890"})

        return text.translate({ord(c): '' for c in self.bad_chars})

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
        jstor_li = []

        # import all files in the directory, automatically detect on file name extension [supports WOS and Scopus]

        all_files = glob.glob(path + "*")
        for filename in all_files:
            if filename.endswith('.txt'):
                df = pd.read_csv(filename, index_col=False, delimiter="\t", quotechar=None, quoting=3, encoding='utf-8')
                wos_li.append(df)
            elif filename.endswith('.csv'):
                df = pd.read_csv(filename)
                scopus_li.append(df)
            elif filename.endswith('.ris'):
                with open(filename, 'r', encoding='utf-8') as f:
                    lines = f.readlines()

                with open(filename, "w", encoding='utf-8') as f:
                    strings = ("Provider", "Database", "Content")
                    for line in lines:
                        if not any(s in line for s in strings):
                            f.write(line)

                with open(filename, 'r', encoding='utf-8') as bibliography_file:
                    entries = list(readris(bibliography_file))
                    for entry in entries:
                        jstor_li.append(entry)


        if len(wos_li) != 0:  # check to see if any web of science results was imported

            # concatenate files from same database into DataFrame
            wos_dataset = pd.concat(wos_li, axis=0, ignore_index=True)

            # merge article titles and abstract to form text from which keywords will be extracted
            text = list(wos_dataset[['AB', 'TI']].apply(lambda x: '{}{}'.format(x[0], x[1]), axis=1))
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

        if len(scopus_li) != 0:  # check to see if any scopus results was imported

            # concatenate files from same database into DataFrame
            scopus_dataset = pd.concat(scopus_li, axis=0, ignore_index=True)

            text = list(scopus_dataset[['Abstract', 'Title']].apply(lambda x: '{}{}'.format(x[0], x[1]), axis=1))
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

        if len(jstor_li) != 0:  # check to see if any jstor results was imported
            # concatenate files from same database into DataFrame
            jstor_dataset = pd.DataFrame(jstor_li)

            i = 0
            for a, b in zip(jstor_dataset.abstract, jstor_dataset.authors):
                jstor_dataset.at[i, 'abstract'] = str(a).translate({ord(c): '' for c in self.bad_chars})
                jstor_dataset.at[i, 'authors'] = str(b).translate({ord(c): '' for c in self.bad_chars})
                i = i + 1

            text = list(jstor_dataset[['abstract', 'title']].apply(lambda x: '{}{}'.format(x[0], x[1]), axis=1))
            jstor_text = [self.remove_punctuations(t) for t in text]

            self.search_results['id'] = self.search_results['id'] + list(jstor_dataset['issn'])
            self.search_results['text'] = self.search_results['text'] + jstor_text
            self.search_results['title'] = self.search_results['title'] + list(jstor_dataset['title'])
            self.search_results['abstract'] = self.search_results['abstract'] + list(jstor_dataset['abstract'])
            self.search_results['keywords'] = self.search_results['keywords'] + (['NaN'] * len(jstor_dataset.index))
            self.search_results['type'] = self.search_results['type'] + list(jstor_dataset['type_of_reference'])
            self.search_results['authors'] = self.search_results['authors'] + list(jstor_dataset['type_of_reference'])
            self.search_results['affiliation'] = self.search_results['affiliation'] + (
                    ['NaN'] * len(jstor_dataset.index))
            self.search_results['source'] = self.search_results['source'] + list(jstor_dataset['name_of_database'])
            self.search_results['year'] = self.search_results['year'] + list(jstor_dataset['year'])
            self.search_results['volume'] = self.search_results['volume'] + list(jstor_dataset['volume'])
            self.search_results['issue'] = self.search_results['issue'] + list(jstor_dataset['number'])
            self.search_results['startpage'] = self.search_results['startpage'] + list(jstor_dataset['start_page'])
            self.search_results['endpage'] = self.search_results['endpage'] + list(jstor_dataset['end_page'])
            self.search_results['doi'] = self.search_results['doi'] + list(jstor_dataset['doi'])
            self.search_results['language'] = self.search_results['language'] + (['English'] * len(jstor_dataset.index))
            self.search_results['database'] = self.search_results['database'] + list(jstor_dataset['name_of_database'])

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
        r = Rake(language='english', punctuations='!"#$%&\'()*+,-),./“:;≥≤<=|‘>©?@[\\]^_`{|}~',
                 ranking_metric=Metric.WORD_DEGREE)

        # Extraction using the text column the text.
        texts = list(DataFrame['text'])

        r.extract_keywords_from_sentences(texts)
        raked_keywords = r.get_ranked_phrases()  # raked keywords

        # Extract author keywords from naive search results and remove blank values
        author_keywords = list(DataFrame['keywords'])
        real_keywords = [x.lower() for x in author_keywords if
                         str(x) != 'nan']  # removing nan values from list of author keywords

        # merge all keywords and split into list
        real_keywords = "".join(real_keywords)
        real_keywords = real_keywords.split(";")

        # merge raked keywords with author keywords
        keywords = raked_keywords + real_keywords

        # loop through all keywords, remove every keyword with a digit in it and create new cleaned list
        digits_cleaned_all_keywords = [x for x in keywords if (any(char.isdigit() for char in x) == False)]

        regex = re.compile('[@_!#$%^&""*..,≈·ακ⩽(∼苔草沼泽的no排放量天)<>?•η°/|}{~:]')

        # loop through all keywords, remove every keyword with a symbol in it using regex and create new cleaned list
        all_keywords = [x.strip() for x in digits_cleaned_all_keywords if (regex.search(x) is None)]

        # Convert keyword list to set and then back to list to deduplicate keyword list
        all_keywords = list(set(all_keywords))
        all_keywords.sort(reverse=False)

        return all_keywords

    def create_dtm(self, doc, min_len=2, max_len=3, **kwargs):
        """
        This method creates a Document-Term Matrix


        :param min_len: minimum keyword length
        :param max_len: maximum keyword length
        :param doc: a list of article title, abstract or any article property
        :param keywords: a list of keywords to use for the Document-Term Matrix
        :param dfm_type: whether the dtm should be created based on document tokens or a restricted list of keywords
                options: token or keywords
        :return: a multidimensional array of a Document-Term Matrix and a list of terms(columns)
        """

        keywords = kwargs.get('keywords', None)
        dfm_type = kwargs.get('dfm_type', None)

        doc = list(doc)
        cleaned_list = [str(x) for x in doc if str(x) != 'nan']
        doc_set = cleaned_list

        vec = CountVectorizer(ngram_range=(min_len, max_len), lowercase=True)

        if dfm_type:
            if dfm_type.lower() == "token":
                tf = vec.fit_transform(doc_set)
            elif dfm_type.lower() == "keywords":
                if keywords:
                    vec.fit(keywords)
                    tf = vec.transform(doc_set)
                else:
                    tf = vec.fit_transform(doc_set)
        else:
            if keywords:
                vec.fit(keywords)
                tf = vec.transform(doc_set)
            else:
                tf = vec.fit_transform(doc_set)

        self.terms = vec.get_feature_names()
        self.terms.sort(reverse=False)

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

        #         keywords.sort()
        nodes = [i for i in range(len(keywords))]
        edges = []

        for row in A:
            # loop through all rows(article) in multidimensional array and the index of each column(keyword) with
            # a value of 1 and store the column indices in a list
            x = [i for i, e in enumerate(list(row)) if e >= 1]
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
            nx.draw_networkx(H, with_label=True)
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
                        degree, closeness, betweenness or eigenvalue
        :return: a dictionary containing nodes with their importance
        """
        if method.lower() == "degree":
            self.centrality = dict(g.degree())
        elif method.lower() == "closeness":
            self.centrality = nx.closeness_centrality(g)
        elif method.lower() == "betweenness":
            self.centrality = nx.betweenness_centrality(g)
        elif method.lower() == "eigenvalue":
            self.centrality = nx.eigenvector_centrality(g)

        self.centrality = sorted(self.centrality.items(), key=operator.itemgetter(1),
                                 reverse=False)  # returns a list of tuples

        return dict(self.centrality)

    def plot_degree_distribution(self, g, save_plot=False, save_directory=None):
        """
        This method plots a distribution of the graph degree

        :param g: graph whose degree distribution is to be plotted
        :param save_plot: if save_plot=True saves the plot to a .png
        :param save_directory: the path to a directory where search results will be saved if save_plot is set to TRUE
        :return:
        """

        importance_data = self.make_importance(g, "degree")

        fig, ax = plt.subplots(figsize=(12, 12), dpi=80)
        plt.plot(importance_data["rank"], importance_data["importance"], 'o')
        plt.title("Ranked Node Strengths")
        plt.ylabel("Node Strength")
        plt.xlabel("Rank")
        plt.show()

        if save_plot:
            if save_directory is not None:
                fig.savefig(r"{}".format(save_directory + "degree_distribution.png"))
            else:
                fig.savefig("ranked_node_strength.png")

    def plot_degree_histogram(self, g, save_plot=False, save_directory=None):
        """
        This method plots a histogram of the graph degree

        :param g: graph whose degree distribution is to be plotted
        :param save_plot: if save_plot=True saves the plot to a .png
        :param save_directory: the path to a directory where search results will be saved if save_plot is set to TRUE
        :return:
        """
        degree_sequence = sorted([d for n, d in g.degree()], reverse=False)  # degree sequence

        degreeCount = collections.Counter(degree_sequence)
        deg, cnt = zip(*degreeCount.items())

        fig, ax = plt.subplots(figsize=(12, 12), dpi=80)
        plt.bar(deg, cnt, width=0.7, color='b')

        plt.title("Degree Histogram")
        plt.ylabel("Count")
        plt.xlabel("Degree")
        ax.set_xticks([d + 0.4 for d in deg])
        ax.set_xticklabels(deg)
        plt.figure()
        plt.show()

        if save_plot:
            if save_directory is not None:
                fig.savefig(r"{}".format(save_directory + "degree_distribution.png"))
            else:
                fig.savefig("degree_distribution.png")

    def find_knots(self, x, y, degrees, knot_num=1):
        """
        This method find the knots of a two sets of values

        :param x: x values
        :param y: y values
        :param degrees: degrees of the spline
        :param knot_num: number of knots of the spline
        :return: t = knots, c = spline coefficients, k = B-spline order
        """
        spl = interpolate.splrep(x, y, k=degrees, s=knot_num)
        return spl

    def fit_spline(self, t, c, k):
        """
        This methods fits t = knots, c = spline coefficients, k = B-spline order to a B-spline

        :param t: knots
        :param c: spline coefficients
        :param k: B-spline order
        :return: fitted B-spline
        """
        return interpolate.BSpline(t, c, k)

    def make_importance(self, g, importance_method):
        """
        This methods creates a dataframe made up of node names with their importance and their rank (index) from a graph

        :param g: graph
        :param importance_method: method to use to check node importance
        :return: a data frame of rank, node importance and node name
        """

        centrality = self.get_centrality(g, importance_method)
        rank = [i + 1 for i in range(len(centrality))]

        centrality = {k: v for k, v in centrality.items() if not str(k).isdigit()}

        importance = list(centrality.values())
        node_names = list(centrality.keys())
        lis = [list(a) for a in zip(rank, importance, node_names)]
        importance_data = pd.DataFrame(lis, columns=['rank', 'importance', 'nodenames'])

        return importance_data

    def find_cutoff(self, g, method, importance_method, degrees=2, knot_num=1, percent=0.2, diagnostics=False):
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
            spl = self.find_knots(list(importance_data["rank"]), importance_data["importance"], degrees,
                                  knot_num)
            knots, c, k = spl
            cut_points = list(set([int(x) for x in np.floor(knots)]))
            cutoff_df = importance_data[importance_data['rank'].isin(cut_points)]
            cut_strengths = list(set(list(cutoff_df.importance)))
            cut_strength = sorted(cut_strengths)[int(len(sorted(cut_strengths)) * (1.0 - percent))]

            if diagnostics is True:
                y2 = interpolate.splev(importance_data["rank"], spl)
                plt.figure(figsize=(12, 12), dpi=80)
                plt.plot(importance_data["rank"], importance_data["importance"], 'o', importance_data["rank"], y2)
                [plt.axvline(_x, linewidth=1, color='r') for _x in cut_points]
                plt.show()

        elif method.lower() == "cumulative":
            cumulative_sum_asc = list(np.cumsum(sorted(importance_data["importance"], reverse=False)))

            cumulative_strength = np.amax(np.cumsum(sorted(importance_data["importance"])))
            cumulative_cut_point = [i for i in cumulative_sum_asc if i >= cumulative_strength * (1.0 - percent)][0]

            cumulative_cut_point_index = cumulative_sum_asc.index(cumulative_cut_point)
            cut_strength = list(sorted(importance_data["importance"], reverse=False))[cumulative_cut_point_index]

            if diagnostics is True:
                plt.figure(figsize=(6, 6), dpi=80)
                plt.plot(cumulative_sum_asc, 'o')
                plt.title("Cumulative sum of ranked node importance")
                plt.ylabel("Cumulative node importance")
                plt.xlabel("Index")
                plt.axvline(cumulative_cut_point_index, linewidth=1, color='r')
                plt.show()

        return cut_strength

    def get_keywords(self, g, importance_method, cutoff_strength, save_keywords=True, save_directory=None,
                     draw_reduced_graph=False):
        """

        :param g: graph
        :param importance_method: method to use to check node importance
        :param cutoff_strength:  where to cut off of the graph
        :param save_keywords: if save_keywords=True saves the keywords to a .csv
        :param save_directory: path to a directory where suggested keywords will be saved if save_dataset is set to TRUE
        :param draw_reduced_graph: RUE, draws reduced graph
        :return: suggested keywords for final review
        """

        importance_data = self.make_importance(g, importance_method)
        keywords = list(importance_data.loc[importance_data['importance'] >= cutoff_strength, "nodenames"])
        reduced_graph = g.subgraph(keywords)

        if draw_reduced_graph is True:
            nx.draw_networkx(reduced_graph, with_label=True, pos=nx.spring_layout(reduced_graph))

        keywords = [self.remove_punctuations(x) for x in keywords]
        # check if keyword isn't an empty string
        suggested_keywords = [i for i in keywords if i]
        df = pd.DataFrame(suggested_keywords, columns=["keywords"])

        if save_keywords:
            if save_directory is not None:
                df.to_csv(r"{}".format(save_directory + 'relevant_keywords.csv'), index=False)
            else:
                df.to_csv('relevant_keywords.csv', index=False)

        return suggested_keywords