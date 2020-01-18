#!python

"""
Program: simpleSynapse
Author: Andrew Blair and Robert Hu
Description: A simple Synapse organization and maintenance python client script.
"""

import os
import shutil
import hashlib
import synapseclient
import synapseutils
from synapseclient import Project, Folder, File, Link

class simpleSynapse:
    """
    A simple class used to organize and sync a Synapse project. 
    
    Attributes
    ----------
    login : str
        Synapse username
    password : str
        Synapse password
    project : str
        Synapse project name
    
    Methods
    -------
        
    sync_synapse_to_local()
        Sync Synapse to local
        
    sync_local_to_synapse()
        Syn local to synapse
        
    References
    -------
    https://python-docs.synapse.org/
    """
    
    def __init__(self, login, password, project):
        
        self.syn = synapseclient.Synapse()
        self.syn.login(login, password, forced=True)

        self.project = Project(project)
        self.project = self.syn.store(self.project)
    
    def syn_client(self):
        '''
        Construct a Python client object for the Synapse repository service
        
        :param: None
        return: Synapse client constructor
        '''
        return self.syn
    
    def syn_project(self):
        '''
        Construct a Python client for the Synapse project
        
        :param: None
        return: Synapse project constructor
        '''
        return self.project
    
    def check_subdirs(self, synapse_folder_dict, paths, subdirs):
        '''
        Check if subdirectories are on Synapse, if not sync the folder
        
        :param synapse_folder_dict: list, a list of strings that are subdirectories
        :param paths: str,
        :param subdirs: list,
        return synapse_folder_dict: dict,
        '''
        for dirs in subdirs:
            if dirs == '.ipynb_checkpoints':
                shutil.rmtree(paths + '/' + dirs)
            else:
                dir_entityID = self.syn.findEntityId(dirs, parent=synapse_folder_dict[paths.split('/')[-1]])
                if dir_entityID is not None:
                    synapse_folder_dict[dirs] = dir_entityID
                else:
                    folder = Folder(dirs, parent=synapse_folder_dict[paths.split('/')[-1]])
                    folder = self.syn.store(folder)
                    synapse_folder_dict[folder.name] = folder.id
        return synapse_folder_dict
    
    def check_files(self, synapse_folder_dict, files):
        '''
        Check if the md5 has changed on Synapse, if not  
        
        :param synapse_folder_dict:
        :param files:
        return: None
        '''
        for data in files:
            if data == 'SYNAPSE_METADATA_MANIFEST.tsv':
                os.unlink(paths + '/' + data)
            else:
                file_entityID = self.syn.findEntityId(data, parent=synapse_folder_dict[paths.split('/')[-1]])
                if file_entityID is not None:
                    file_entity = self.syn.get(file_entityID, downloadFile=False)
                    local_md5 = synapseclient.utils.md5_for_file(paths + '/' + data).hexdigest()
                    if file_entity.md5 != local_md5:
                        self.file_store(paths + '/' + data, synapse_folder_dict[paths.split('/')[-1]])
                else:
                    self.file_store(paths + '/' + data, synapse_folder_dict[paths.split('/')[-1]])
                    
    def file_store(self, file_path, parent_entityID):
        '''
        Create a new Entity or updates an existing Entity, uploading any files in the process to Synapse project
        
        :param file_path: str, path to the file that will be uploaded to Synapse
        :param parent_entityID: str, An id or an object of a Synapse entity that is the parent of the file being uploaded
        return: None
        '''
        file = File(file_path, parent=parent_entityID)
        file = self.syn.store(file)
        
    def sync_local_to_synapse(self):
        '''
        Synac local to Synapse, only if the md5 is not the same
        
        :param: None
        return: None
        '''
        synapse_folder_dict = {self.project.name :self.project.id}
        for paths, subdirs, files in os.walk(self.project.name):
            if subdirs:
                synapse_folder_dict = self.check_subdirs(synapse_folder_dict, paths, subdirs)
            if files:
                self.check_files(synapse_folder_dict, paths, files)
    
    def sync_synapse_to_local(self):
        '''
        Sync Synapse to local, without overwriting local entities
        
        :param: None
        return: None
        '''
        if not os.path.exists(self.project['name']): 
            os.makedirs(self.project['name'])
        synapseutils.sync.syncFromSynapse(self.syn, self.project['id'], path=self.project['name'], ifcollision="keep.local")