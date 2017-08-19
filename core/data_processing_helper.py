import heapq


# https://stackoverflow.com/a/15940903/5111904

class DataProcessingHelper(object):
    '''
    Static helper class providing methods which are used by other modules in the project "core".
    '''
    @staticmethod
    def iter_sorted(dictionary):
        '''
        Can be used with for in loop to iterate all values in a dictionary.
        '''
        keys = list(dictionary)
        heapq.heapify(keys) # Transforms to heap in O(N) time
        while keys:
            k = heapq.heappop(keys) # takes O(log n) time
            yield (k, dictionary[k])


    @staticmethod
    def required_features():
        '''Returns a list of features which are required by the classifier to classify.'''
        return  ['Cleanliness', 'Location', 'Rooms', 'Service','Sleep Quality','Value']
    