'''
    Providing an interface for handling iteraction
    with the classifier.
'''

import pickle

# I/O


def save_classifier(classifier):
    '''Saves classifier to file'''
    f = open('my_classifier.pickle', 'wb') # TODO: Error handling
    pickle.dump(classifier, f, -1)
    f.close()


def load_classifier():
    '''Loads classifier from file'''
    classifier = -1
    f = None 
    try:
        f = open('my_classifier.pickle', 'rb')
        classifier = pickle.load(f)
    except IOError as error:
        print(
            "No saved classifier has been found. Training is needed. Error: " + error.strerror)
    finally:
        if f is not None and not f.closed:
            f.close()

    return classifier

# Information about classifier


def most_useful_features(classifier, n=1):
    '''Returns the most useful n features of the given classifier'''
    return classifier.show_most_informative_features(n)


# only a module for project
if __name__ == '__main__':
    print('This file is only providing an interface,\
           and is not executable as a standalone.')
    exit(1)
