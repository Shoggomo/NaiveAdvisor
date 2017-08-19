from classifier import *
import review_reader
import trainer
import os


class SuperVisor(object):
    
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