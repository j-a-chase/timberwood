#
# Example python program using timberwood package
#

from timberwood.logger import Logger

from os import mkdir
from os.path import exists

if not exists('./logs'):
    mkdir('./logs')

LOG = Logger('./logs', 'runtime.log', 'Example Project 1')

def function1() -> None:
    print('I\'m function 1!')

def main() -> None:
    '''
    Main function

    Parameters: None

    Returns: None
    '''
    # the 'create' method creates the initial log and header
    if not LOG.create():
        print('Error creating log! Aborting program...')

    # You can use the 'action' method to log actions your program is taking
    # with custom messages to display in the log
    LOG.action('Running function1...')
    function1()
    LOG.action('Run of function1 complete.')

    # Logs are stored in a list in the class, which are written to a file all at
    # once upon completion. Calling the 'flush' method is what writes them to
    # the specified file in the specified directory
    LOG.flush()

if __name__ == '__main__':
    main()
