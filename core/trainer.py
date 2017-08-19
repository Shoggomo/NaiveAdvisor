from nltk.classify import naivebayes
from data_processing_helper import *
from review_reader import *

class Trainer(object):
    '''
    Static class providing all necessary functions to train a classifier.
    '''

    # static variables:
    lowest_valid_rating = 1 # range in which a rating is considered as valid
    highest_valid_rating = 5
    valid_rating_properties_count = 7 # a valid rating has exactly 7 properties

    all_valid_ratings_count = 0 # valid and invalid ratings used for all classifier trainings
    all_invalid_ratings_count = 0

    @staticmethod
    def extract_features(single_rating):
        '''
        Extracts features from a single rating.
        Returns the features if all 6 ratings are valid or None if they aren't.
        '''

        # checking vadility of rating
        try:
            if len(single_rating) is not Trainer.valid_rating_properties_count: # raiting needs to have exactly 7 properties
                raise KeyError('Expected 7 properties.')

            it = DataProcessingHelper.iter_sorted(single_rating)

            for i in it: # filtering out invalid ratings, most of them have a rating of -1
                if int(float(i[1])) < Trainer.lowest_valid_rating or int(float(i[1])) > Trainer.highest_valid_rating: 
                    raise KeyError('Rating out of boundary')
               
            # creating the feature dictionary, if the rating does not contain this properties a KeyError is being raised
            # and this rating is ignored.    
            features = ({ 
                'Cleanliness':   int(single_rating['Cleanliness']),
                'Location':      int(single_rating['Location']),
                'Rooms':         int(single_rating['Rooms']),
                'Service':       int(single_rating['Service']), 
                'Sleep Quality': int(single_rating['Sleep Quality']),
                'Value':         int(single_rating['Value'])
                }, str(single_rating['Overall']))

            return features
        except KeyError: # this rating is invalid, return None instead of the features dictionary
            return None
       

    @staticmethod
    def create_feature_list(reviews):
        '''
        Creates and returns a feature list based on a list of reviews.
        '''
        feature_list = [] # all valid features 
        valid = 0 # valid reviews in this file
        invalid = 0 # invalid reviews in this file

        for i in range(len(reviews)): # iterating all reviews 
            features = Trainer.extract_features(reviews[i]['Ratings']) # extracting features of this single rating
            if features is not None: # check if the rating is valid 
                feature_list.append(features) # rating is valid, adding it to the feature_list
                valid += 1 # incrementing valid counter
            else: # rating is invalid
                invalid += 1 # incrementing invalid counter
        
        Trainer.all_valid_ratings_count += valid # updating valid ratings count shared by all function calls
        Trainer.all_invalid_ratings_count += invalid # updating invalid ratings count shared by all function calls

        print("Valid: {0} Invalid: {1}".format(valid, invalid)) 
        return (feature_list, (valid, invalid)) # returning tupel where index 0 contains the feature list and index
                                                # 1 a tupel containing the count of valid, invalid ratings

    @staticmethod
    def train_classifier(callback):
        '''
        Trains a classifier using the review_reader to extract data from the json files.
        After the training the classifier is being saved and the callback function is being invoked.
        '''
        review_reader = ReviewReader()
        next_reviews = review_reader.take_next()

        all_features = [] # *all* features extracted by *all* files

        this_valid_features = 0 # valid/invalid feature count used for *this* training
        this_invalid_features = 0
    
        while next_reviews != -1: # while there is a next .json file containing reviews
            try:
                feature_data = Trainer.create_feature_list(next_reviews) # creating a featurelist from json object
                features = feature_data[0] # features are at index 0 
                all_features.extend(features) # adding features extracted from the last .json file

                this_valid_features += feature_data[1][0] # counting valid features (ratings) used by the classifier
                this_invalid_features += feature_data[1][1] # counting invalid features (ratings) ignored by the classifier
            except Exception as ex: # general exception because unexpected
                print("Exception with message: {0}".format(ex.message)) # unexpected exception ocurred, printing it
            finally:
                  next_reviews = review_reader.take_next() # file has been processed, using next file

        classifier = naivebayes.NaiveBayesClassifier.train(all_features) # training classifier with all_featuers
        classifier.show_most_informative_features(5) # printing most informative features in console
        callback(classifier, (this_valid_features, this_invalid_features)) # returning a tupel, index 0 is the classifier and index 1
                                                                           # is a tupel containing the count of valid features used
                                                                           # by the classifier and invalid features which have been ignored.
         
