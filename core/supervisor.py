from classifier import *
from trainer import *


class SuperVisor(object):
    '''
    This is the main module of the core folder. It uses the other modules to train a classifier or 
    to read it from a file. 
    This class is the only module in the core folder which should be used by other modules (not in this folder).
    Use this module to interact with the classifier.
    '''
    def on_trained_classifier(self, trained_classifier, statistics):
        '''
        Callback method, called when classifier has been trained.
        '''
        Classifier.save_classifier(trained_classifier)
        Classifier.save_statistics(statistics) # saving statistics
        self.statistics = Classifier.read_statistics() # reading saved statistics
        self.loaded_callback(self)

    def classify(self, features):
        '''
        Takes features and uses the classifier of this class to return a label.
        '''
        return Classifier.classify(self.classifier, features)

    def get_statistics(self):
        '''
        Returns count of valid ratings and invalid (ignored) ratings as a tupel.
        '''
        return self.statistics

    def get_classifier(self):
        '''
        Returns the classifier of this class.
        '''
        return self.classifier

    def get_most_useful_features(self, n=10):
        '''
        Returns the most useful features of this classifier.
        '''
        return Classifier.most_useful_features(self.classifier, n)

    def __init__(self, loaded_callback, force_training=False, max_files=-1):
        self.max_files = max_files
        self.loaded_callback = loaded_callback
        self.classifier = Classifier.load_classifier()
        self.statistics = Classifier.read_statistics()

        if force_training or (self.classifier is -1) or (self.statistics is -1):
            Trainer.train_classifier(self.on_trained_classifier, max_files)
        else:
            self.loaded_callback(self)
