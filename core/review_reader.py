'''
Handles interaction with test data.
'''
import os
import json 
import trainer

class ReviewReader(object):
    '''
    ReviewReader provides an interface for reading one
    tripadvisor json file at a time.
    '''

    def take_next(self):
        '''
        Takes the next file in the directory and returns it as json object.
        '''
        if self.last+1 <= self.filenames: 
            json_object = ReviewReader.read_json(os.path.join(self.directory_path, self.filenames[self.last + 1])) 
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

    @staticmethod   # TODO: Error handling
    def read_json(path):
        '''
        Loads content from a file into memory as json object.
        '''
        with open(path,'r') as json_file:
            data = json.load(json_file)
        return data

    def __init__(self, directory_path=os.path.dirname(os.getcwd())+'/json'):
        self.last = -1
        self.directory_path = directory_path
        self.filenames = ReviewReader.get_file_list(self.directory_path)
        self.test = self.take_next()
        trainer.Trainer.create_feature_list(self.test)

