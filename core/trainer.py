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
                # TODO: Data with ratings of -1 are invalid
                'Cleanliness':   single_rating['Cleanliness'] if single_rating['Cleanliness'] > 0 else 1,
                'Location':      single_rating['Location'] if single_rating['Location'] > 0 else 1,
                'Rooms':         single_rating['Rooms'] if single_rating['Rooms'] > 0 else 1,
                'Service':       single_rating['Service'] if single_rating['Service'] > 0 else 1,
                'Sleep Quality': single_rating['Sleep Quality'] if single_rating['Sleep Quality'] > 0 else 1,
                'Value':         single_rating['Value'] if single_rating['Value'] > 0 else 1
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
        
        print("Valid: {0} Invalid: {1}".format(valid, invalid))
        return feature_list

    def train_classifier(self):
        next_reviews = self.review_reader.take_next()
    
        while next_reviews != -1:
            try:
                features = Trainer.create_feature_list(next_reviews)
                # TODO: Classify
                if self.classifier is None:
                    if len(features) > 1:
                        self.classifier = naivebayes.NaiveBayesClassifier.train(features)
                    else:
                        self.classifier.train(features)    
            except Exception as ex:
                print("Exception with message: {0}".format(ex.message))
                pass
            finally:
                  next_reviews = self.review_reader.take_next()
         

    def __init__(self, review_reader, document_count, classifier=None):    
        self.review_reader = review_reader
        self.classifier = classifier


