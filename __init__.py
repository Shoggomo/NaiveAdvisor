import rest_api
import sys
from core import supervisor
import time

def supervisor_ready(supervisor):
    rest_api.run(supervisor)

def print_proper_usage():
    print('Invalid argument(s), usage: "python __init__.py --ft" where "--ft" is optional.')
    print('Ignoring invalid argument(s) => continue without forcing training.')

def main():
    '''
    Entry point of application. Checking arguments and launching classifier and webserver.
    '''
    # validating arguments
    should_train = False
    if len(sys.argv) is 2:
        # checking arguments for --ft flag
        if sys.argv[1] == '--ft':
            should_train = True
            print('***User wishes to train classifier***')
        else:
            print_proper_usage()

    # no second argument, default behaviour
    if len(sys.argv) is 1:
        print('***No arguments have been passed***')
        print('***Only training classifier if necessary***')

    # invalid argument count
    if len(sys.argv) > 2:
        print_proper_usage()

    time.sleep(2)

    supervisor.SuperVisor(supervisor_ready, force_training=should_train)

if __name__ == "__main__":
    main()
