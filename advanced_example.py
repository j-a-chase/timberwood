#
# Example Python program using TimberWood package for crash logging
#

from timberwood.logger import Logger

from os import mkdir
from os.path import exists
from signal import signal, SIGINT, SIGTERM
import sys

if not exists('./logs'):
    mkdir('./logs')

LOG = Logger('./logs', project_name='Example Project 2')

def shutdown_handler(signum=None, frame=None, exc_type=None, exc_value=None,
                     exc_traceback=None):
    # the critical method is used when uncaught exceptions cause the program to
    # crash
    # this method should be reserved for these special situations!
    if exc_type is not None:
        LOG.critical(f'Uncaught exception: {exc_type, exc_value, exc_traceback}')
    LOG.flush()
    print("FATAL ERROR! CHECK LOG!")
    sys.exit(1)

def main() -> None:
    '''
    Main function

    Parameters: None

    Returns: None
    '''
    if not LOG.create():
        print('Aborting...')
        return
    
    LOG.action('Showing example of failing program.')
    
    # you can use the warning method to log messages for when potentially
    # expected or abnormal behavior occur!
    LOG.warning("Approaching buggy section!")

    # the error method can be used to log errors before terminating the program
    # should only be used when code that will break the program is reached
    LOG.error('This code is going to break me!')
    
    # With proper setup, you can even have the logger flush its contents on
    # application failure.
    # for example, this uncaught parsing error will break the program!
    # With proper setup, the Logger will instead print the error to the log
    # instead of the console!
    val = int('Hello world!')

    # due to the exception, this line will never be run!
    LOG.action('Example shown.')

if __name__ == '__main__':
    # register signal handlers
    signal(SIGINT, shutdown_handler)
    signal(SIGTERM, shutdown_handler)

    # set function to handle crashes
    sys.excepthook = shutdown_handler

    try:
        main()
    except Exception as e:
        shutdown_handler(exc_type=type(e),
                         exc_value=e.args[0],
                         exc_traceback=e.__traceback__)
