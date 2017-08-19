from classifier import *
from trainer import *


class SuperVisor(object):
    '''
    This is the main module of the core folder. It uses the other modules to train a classifier or 
    to read it from a file. 
    This class is the only module in the core folder which should be used by other modules (not in this folder).
    Use this module to interact with the classifier.
    '''
    def on_trained_classifier(self, trained_classifier, valid_invalid_statistic):
        '''
        Callback method, called when classifier has been trained.
        '''
        Classifier.save_classifier(trained_classifier)
        Classifier.save_valid_ratings_statistic(valid_invalid_statistic)
        self.valid_invalid_statistic = valid_invalid_statistic
        self.loaded_callback()

    def classify(self, features):
        '''
        Takes features and uses the classifier of this class to return a label.
        '''
        return Classifier.classify(self.classifier, features)

    # TODO: Documentation + classifier accuracy

    def get_valid_invalid_statistic(self):
        return self.valid_invalid_statistic

    def get_classifier(self):
        return self.classifier

    def get_most_useful_features(self, n=10):
        return Classifier.most_useful_features(self.classifier, n)

    def __init__(self, loaded_callback, force_training=False):
        self.loaded_callback = loaded_callback
        self.classifier = Classifier.load_classifier()
        self.valid_invalid_statistic = Classifier.read_valid_ratings_statistic()

        if force_training or (self.classifier is -1) or (self.valid_invalid_statistic is -1):
            Trainer.train_classifier(self.on_trained_classifier)
        else:
            self.loaded_callback()
        

def done():
    pass 

super_visor = SuperVisor(done)
pass 
