from nltk.classify import naivebayes

class Trainer(object):

    @staticmethod
    def extract_features(single_rating):
        '''
        Extracts features from a single rating.
        Returns the features if all 6 ratings are valid or None if they aren't.
        '''
        try:
            features = ({
                'Cleanliness':   single_rating['Cleanliness'],
                'Location':      single_rating['Location'],
                'Rooms':         single_rating['Rooms'],
                'Service':       single_rating['Service'],
                #'Sleep Quality': single_rating['Sleep Quality'],
                'Value':         single_rating['Value']
                }, single_rating['Overall'])

            return features
        except KeyError as error: # not all required ratings are there
            return None
       

    @staticmethod
    def create_feature_list(reviews):
        '''
        Creates and returns a feature list based on a list of reviews.
        '''
        feature_list = []
        valid = 0
        invalid = 0

        for i in range(len(reviews)):
            features = Trainer.extract_features(reviews[i]['Ratings'])
            if features is not None:
                feature_list.append(features)
                valid = valid + 1 
            else:
                invalid = invalid + 1
        return feature_list

    def train_classifier(self):
        next = self.review_reader.take_next()
    
        while next != -1:
            features = Trainer.create_feature_list(next)
            # TODO: Classify
            if self.classifier is None:
                if len(features) > 1:
                    self.classifier = naivebayes.NaiveBayesClassifier.train(features)
            else:
                self.classifier.train(features)
                    
            next = self.review_reader.take_next()

    def __init__(self, review_reader, document_count, classifier=None):    
        self.review_reader = review_reader
        self.classifier = classifier


