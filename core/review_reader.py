'''
Handles interaction with test data.
'''
import os
from data_processing_helper import *

class ReviewReader(object):
    '''
    ReviewReader provides an interface for reading one
    tripadvisor json file at a time.
    '''

    def take_next(self):
        '''
        Takes the next file in the directory and returns it as json object.
        '''
        if self.last + 1 < len(self.filenames): 
            json_object = DataProcessingHelper.read_json(os.path.join(self.directory_path, self.filenames[self.last + 1])) 
            self.last = self.last + 1
            return json_object['Reviews']
        else:
            return -1 # No file left

    @staticmethod
    def get_file_list(directory_path):
        '''
        Returns a list of all files in one directory
        '''
        return [name for name in os.listdir(directory_path)]

    def __init__(self, directory_path=os.path.dirname(os.getcwd())+'/json'):
        self.last = -1
        self.directory_path = directory_path
        self.filenames = ReviewReader.get_file_list(self.directory_path)

