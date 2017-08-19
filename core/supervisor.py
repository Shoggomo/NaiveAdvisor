from classifier import *
from trainer import *



class SuperVisor(object):
    '''
    This is the main module of the core folder. It uses the other modules to train a classifier or 
    to read it from a file. 
    This class is the only module in the core folder which should be used by other modules (not in this folder).
    Use this module to interact with the classifier.
    '''
    def on_trained_classifier(self, trained_classifier, features_count):
        '''
        Callback method, called when classifier has been trained.
        '''
        Classifier.save_classifier(trained_classifier)
        print(features_count)

    def classify(self, features):
        '''
        Takes features and uses the classifier of this class to return a label.
        '''
        return Classifier.classify(self.classifier, features)

    def __init__(self, loaded_callback, force_training=False):
        self.classifier = Classifier.load_classifier()

        if force_training or self.classifier is -1:
            Trainer.train_classifier(self.on_trained_classifier)
        


super_visor = SuperVisor(None)