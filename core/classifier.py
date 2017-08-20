'''
    Providing an interface for handling iteraction
    with the classifier.
'''

import pickle
from data_processing_helper import *

class Classifier(object):  
    '''
    Static helper class providing static methods to interact with classifier object.
    Supports saving and loading a classifier from a file.
    Provides a static method to classify features and to extract the most useful features.
    '''
    # I/O
    @staticmethod
    def save_classifier(classifier):
        '''Saves classifier to file'''
        try:
            f = open('my_classifier.pickle', 'wb') 
            pickle.dump(classifier, f, -1)
        except IOError as error:
            print(
                "Could not save classifier. Do you have permission to write in this directory? Error: " + error.strerror)
        finally:
            print("Saved classifier.")
            if f is not None and not f.closed:
                f.close()
    
    @staticmethod
    def load_classifier():
        '''Loads classifier from file'''
        classifier = -1
        f = None 
        try:
            f = open('my_classifier.pickle', 'rb')
            classifier = pickle.load(f)
        except IOError as error:
            print(
                "No saved classifier has been found. Training is needed. Error: " + error.strerror)
        finally:
            if f is not None and not f.closed:
                f.close()
    
        return classifier

    @staticmethod 
    def save_statistics(statistics):
        '''
        Writes the valid/invalid ratings in a file
        '''
        DataProcessingHelper.write_json('statistic', 
            {
                'valid': statistics[0],
                'invalid': statistics[1],
                'accuracy': statistics[2]
            })
    
    @staticmethod
    def read_statistics():
        '''
        Reads the valid/invalid ratings from the file.
        '''
        statistic_json = -1
        try:
            statistic_json = DataProcessingHelper.read_json('statistic')
        except IOError:
            pass # nothing to do here
        
        return statistic_json
    
    # Information about classifier
    @staticmethod
    def most_useful_features(classifier, n=10):
        '''Returns the most useful n features of the given classifier'''
        return classifier.most_informative_features(n)

    @staticmethod
    def classify(classifier, features): 
        '''
        Uses the classifier to classify the features and returns the label as result.
        Catch ValueErrors when you use this.
        '''
        if len(features) is not 6:
            raise ValueError("You need to specify exactly 6 features!")

        it = DataProcessingHelper.iter_sorted(features)

        for i in it:
            if int(float(i[1])) < 1 or int(float(i[1])) > 5:
                raise ValueError('Rating out of boundary')

        required_featues = DataProcessingHelper.required_features()

        try:
            for i in range(len(required_featues)):
                features[required_featues[i]]
        except KeyError as error:
            raise ValueError('Wrong feature name(s) Message: ' + error.message)

        return classifier.classify(features)
    
    
# only a module for project
if __name__ == '__main__':
    print('This file is only providing an interface,\
           and is not executable as a standalone.')
    exit(1)
