from classifier import *
import review_reader
import trainer
import os


class SuperVisor(object):
    '''
    This is the main module of the core folder. It uses the other modules to train a classifier or 
    to read it from a file. 
    This class is the only module in the core folder which should be used by other modules (not in this folder).
    Use this module to interact with the classifier.
    '''
    def on_trained_classifier(self, trained_classifier):
        '''
        Callback method, called when classifier has been trained.
        '''
        Classifier.save_classifier(trained_classifier)

    def classify(self, features):
        '''
        Takes features and uses the classifier of this class to return a label.
        '''
        return Classifier.classify(self.classifier, features)

    def __init__(self):
        self.classifier = Classifier.load_classifier()
        if(self.classifier == -1):
            self.review_reader = review_reader.ReviewReader()
            self.trainer = trainer.Trainer(self.review_reader, 10)
            self.trainer.train_classifier(self.on_trained_classifier)
            pass 



super_visor = SuperVisor()