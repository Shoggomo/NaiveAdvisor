'''
    Providing an interface for handling iteraction
    with the classifier.
'''

import pickle

class Classifier(object):  
    # I/O
    @staticmethod
    def save_classifier(classifier):
        '''Saves classifier to file'''
        try:
            f = open('my_classifier.pickle', 'wb') # TODO: Error handling
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
    
    # Information about classifier
    @staticmethod
    def most_useful_features(classifier, n=1):
        '''Returns the most useful n features of the given classifier'''
        return classifier.most_informative_features(n)

    @staticmethod
    def classify(classifier, features): # TODO: better exception handling
        '''Uses the classifier to classify the features and returns the label as result.'''
        if len(fea)
        try:
            label = classifier.classify(features)
            return label 
        except Exception as error:
            raise # throw exception anyway
    
    
# only a module for project
if __name__ == '__main__':
    print('This file is only providing an interface,\
           and is not executable as a standalone.')
    exit(1)
