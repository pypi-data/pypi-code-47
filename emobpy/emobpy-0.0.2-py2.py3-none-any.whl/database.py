import time
# import networkx as nx
import pickle
import os
import uuid


class DataBase(object):
    """docstring for DataBase."""

    def __init__(self, folder):
        super(DataBase, self).__init__()

        self.name = ''
        self.folder = folder
        self.oldpath = []
        self.db = {}
        # self.treelistnames = []

    def loadfiles(self, loaddir=''):
        if loaddir:
            self.repo = loaddir
        else:
            self.repo = self.folder
        os.makedirs(self.repo, exist_ok=True)
        self.currentpath = [f for f in os.listdir(self.repo) if os.path.isfile(os.path.join(self.repo, f))]
        self.path_list = list(set(self.currentpath) - set(self.oldpath))
        if self.path_list:
            self.oldpath = self.currentpath

        for f in self.path_list:
            self.fpath = os.path.join(self.repo, f)
            if f.split('.')[-1] == 'pickle':
                self.pickle_off = open(self.fpath, "rb")
                self.obj = pickle.load(self.pickle_off)
                self.pickle_off.close()
                self.db[self.obj['name']] = self.obj
                del self.pickle_off

    def update(self):
        self.loadfiles()

    def getdb(self):
        self.update()
        return self.db

    # def createtree(self):
    #     self.update()
    #     self.tree = []
    #     for l in self.db.keys():
    #         self.cond = l
    #         self.inputs = [self.cond]
    #         while 'input' in self.db[self.cond].keys():
    #             self.inputs.append(self.db[self.cond]['input'])
    #             self.cond = self.db[self.cond]['input']
    #         self.tree.append(self.inputs[::-1])
    #     self.edge = []
    #     for row in self.tree:
    #         self.p = 'Profiles'
    #         for u in row:
    #             self.edge.append(tuple([self.p, u]))
    #             self.p = u
    #     self.edges = list(set(self.edge))
    #     self.nodes = list(set([j for i in self.edge for j in i]))
    #     self.G = nx.DiGraph()
    #     self.G.add_edges_from(self.edge)
    #     treefilename = 'tree_' + time.strftime("%Y%m%d_%H%M%S") + '.dot'
    #     self.treelistnames.append(treefilename)
    #     nx.drawing.nx_agraph.write_dot(self.G, treefilename)
    #     try:
    #         import matplotlib.pyplot as plt
    #         self.pos = nx.drawing.nx_agraph.graphviz_layout(self.G, prog='dot')
    #         nx.draw(self.G, self.pos, with_labels=False, arrows=True)
    #         plt.show()
    #         print('Load the file {} in "https://www.yworks.com/yed-live/"'.format(treefilename))
    #     except ImportError:
    #         print('Graph file has been created: "{}"; but for a preview "matplotlib" is required. Load the file in "https://www.yworks.com/yed-live/"'.format(treefilename))
    #     del self.G

    def remove(self, name):
        self.acum = []
        self.db.pop(name, None)
        if os.path.isfile(os.path.join(self.folder, name+'.pickle')):
            os.remove(os.path.join(self.folder, name+'.pickle'))
            self.acum.append(name + '.pickle')
        self.update()
        print('Files deleted:', len(self.acum))
        print(self.acum)
        del self.acum


class DataManager:
    ''' docstring DataManager '''

    def __init__(self):
        super(DataManager, self).__init__()

    def savedb(self, object, dbdir='db_files'):
        object.update()
        if not object.name:
            nnn = 'db_' + time.strftime("%Y%m%d_%H%M%S") + '_' + uuid.uuid4().hex[:5]  # + time.strftime("%Y%m%d_%H%M%S")
            object.name = nnn[:]
        os.makedirs(dbdir, exist_ok=True)
        with open(os.path.join(dbdir, object.name + '.pickle'), 'wb') as datei:
            pickle.dump(object, datei)
        print(datei)
        print('=== Database saved ===')

    def loaddb(self, dbfilepath, profilesdir):
        with open(dbfilepath, 'rb') as datei:
            obj = pickle.load(datei)
        obj.folder = profilesdir
        obj.update()
        return obj
