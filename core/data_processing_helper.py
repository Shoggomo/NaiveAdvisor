import heapq


# https://stackoverflow.com/a/15940903/5111904

class DataProcessingHelper(object):

    @staticmethod
    def iter_sorted(dictionary):
        '''
        Can be used with for in loop to get all values in a dictionary.
        '''
        keys = list(dictionary)
        heapq.heapify(keys) # Transforms to heap in O(N) time
        while keys:
            k = heapq.heappop(keys) # takes O(log n) time
            yield (k, dictionary[k])


    @staticmethod
    def required_features():
        return  ['Cleanliness', 'Location', 'Rooms', 'Service','Sleep Quality','Value']
    