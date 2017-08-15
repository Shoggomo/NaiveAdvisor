import classifier
import review_reader
import trainer
import os


class SuperVisor(object):
    def __init__(self):
        self.classifier = classifier.load_classifier()
        if(self.classifier == -1):
            self.review_reader = review_reader.ReviewReader()
            self.trainer = trainer.Trainer(self.review_reader, 10)
            self.trainer.train_classifier()
            pass 


super_visor = SuperVisor()