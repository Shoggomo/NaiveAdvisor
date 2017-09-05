# Matthias Herrmann

import heapq
import json

class DataProcessingHelper(object):
    '''
    Static helper class providing methods which are used by other modules in the project "core".
    '''
    @staticmethod
    def iter_sorted(dictionary):
        '''
        Can be used with for in loop to iterate all values in a dictionary.
        '''
        # https://stackoverflow.com/a/15940903/5111904
        keys = list(dictionary)
        heapq.heapify(keys) # Transforms to heap in O(N) time
        while keys:
            k = heapq.heappop(keys) # takes O(log n) time
            yield (k, dictionary[k])

    @staticmethod   
    def read_json(path):
        '''
        Loads content from a file into memory as json object.
        '''
        with open(path,'r') as json_file:
            data = json.load(json_file)
        return data

    @staticmethod
    def write_json(path, data):
        '''
        Writes data as json to the specified path.
        '''
        with open(path, 'w') as outfile:
            json.dump(data, outfile, indent=4)

    @staticmethod
    def required_features():
        '''Returns a list of features which are required by the classifier to classify.'''
        return  ['Cleanliness', 'Location', 'Rooms', 'Service','Sleep Quality','Value']
    