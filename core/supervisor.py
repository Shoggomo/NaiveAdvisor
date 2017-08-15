import classifier
import review_reader
import os

class SuperVisor(object):
    
    def __init__(self):
        self.classifier = classifier.load_classifier()
        if(self.classifier == -1):
            self.review_reader = review_reader.ReviewReader()

super_visor = SuperVisor()