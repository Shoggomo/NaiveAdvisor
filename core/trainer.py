from nltk.classify import naivebayes
from data_processing_helper import *

# TODO: Consider making Trainer a static class
# or restructure the class making it more accessible for others
class Trainer(object):

    # static variables:
    lowest_valid_rating = 1 # range in which a rating is considered as valid
    highest_valid_rating = 5
    valid_rating_properties_count = 7 # a valid rating has exactly 7 properties

    all_valid_ratings_count = 0
    all_invalid_ratings_count = 0

    @staticmethod
    def extract_features(single_rating):
        '''
        Extracts features from a single rating.
        Returns the features if all 6 ratings are valid or None if they aren't.
        '''
        try:
            if len(single_rating) is not Trainer.valid_rating_properties_count:
                raise KeyError('Expected 7 properties.')

            it = DataProcessingHelper.iter_sorted(single_rating)

            for i in it:
                if int(float(i[1])) < Trainer.lowest_valid_rating or int(float(i[1])) > Trainer.highest_valid_rating:
                    raise KeyError('Rating out of boundary')
               
                
            features = ({
                # TODO: Data with ratings of -1 are invalid
                'Cleanliness':   int(single_rating['Cleanliness']),
                'Location':      int(single_rating['Location']),
                'Rooms':         int(single_rating['Rooms']),
                'Service':       int(single_rating['Service']), 
                'Sleep Quality': int(single_rating['Sleep Quality']),
                'Value':         int(single_rating['Value'])
                }, str(single_rating['Overall']))

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
        
        Trainer.all_valid_ratings_count += valid
        Trainer.all_invalid_ratings_count += invalid

        print("Valid: {0} Invalid: {1}".format(valid, invalid))
        return feature_list

    def train_classifier(self, callback):
        '''
        Trains a classifier using the review_reader to extract data from the json files.
        After the training the classifier is being saved and the callback function is being invoked.
        '''
        next_reviews = self.review_reader.take_next()
    
        while next_reviews != -1:
            try:
                features = Trainer.create_feature_list(next_reviews)
                self.all_features.extend(features)
            except Exception as ex:
                print("Exception with message: {0}".format(ex.message))
            finally:
                  next_reviews = self.review_reader.take_next()
        self.classifier = naivebayes.NaiveBayesClassifier.train(self.all_features)
        self.classifier.show_most_informative_features(5)
        callback(self.classifier)
         

    def __init__(self, review_reader, document_count, classifier=None):    
        self.review_reader = review_reader
        self.classifier = classifier
        self.all_features = []

