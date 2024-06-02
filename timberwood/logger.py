################################################################################
# Name: James A. Chase
# File: logger.py
# Date: 21 May 2024
# Description:
#
# Class file for Logger class. Used to create class logs to track failures and
# warnings in programs.
#
################################################################################

# imports
from .asserts.asserts import assertType, assertExists, notMain
from datetime import datetime

class Logger:
    def __init__(self, path: str = './', name: str = 'runtime.log', project_name: str = '') -> None:
        '''
        Constructor

        Parameters:
            - path: a string containing the directory to write the log file to
            - name: a string containing filename for the log file
            - project_name: a string containing the program the log is running \
                            for

        Returns: None
        '''
        assertType(str, type(path))
        assertType(str, type(name))
        assertType(str, type(project_name))

        assertExists(path)

        self._log = f'{path}/{name}'
        self._prog = project_name

        # will hold each logged line
        self._data = []

    def create(self) -> bool:
        '''
        Creates the log file.

        Parameters: None

        Returns:
            - a boolean indicating if creation was successful or not
        '''
        try:
            with open(self._log, 'w') as log:
                log.write(f'{self._prog} - Begin Log:\n')
                log.write('='*125)
                log.write('\n')
        except OSError:
            return False
        return True
    
    def flush(self) -> None:
        '''
        Flushes log data to file on error or completion.

        Parameters: None

        Returns: None
        '''
        try:
            with open(self._log, 'a') as log:
                for record in self._data:
                    log.write(record)
                    log.write('\n')
                log.write('='*125)
                log.write('\n')
        except OSError:
            print('Error flushing log!')

    def action(self, action: str) -> bool:
        '''
        Log an action taken by a program.

        Parameters:
            - action: a string containing the action that was taken

        Returns:
            - a boolean indicating if the log was successful
        '''
        if type(action) != str:
            return False
        
        self._data.append(f'[ACTION:{datetime.now()}] {action}')
        return True
    
    def warning(self, warning: str) -> bool:
        '''
        Log a warning given from a program.

        Parameters:
            - warning: a string containing the warning given

        Returns:
            - a boolean indicating if the log was successful
        '''
        if type(warning) != str:
            return False
        
        self._data.append(f'[WARN:{datetime.now()}] {warning}')
        return True
    
    def error(self, error: str, expected: str='', actual: str='') -> bool:
        '''
        Log an error from a program.

        Parameters:
            - error: a string containing the error thrown
            - expected: an optional parameter that allows the expected value \
                        of a parameter to be displayed
            - actual: an optional parameter that allows the actual value of a \
                      parameter to be displayed

        Returns:
            - a boolean indicating if the log was successful
        '''
        if type(error) != str or type(expected) != str or type(actual) != str:
            return False
        
        self._data.append(f'[ERROR:{datetime.now()}] {error}')
        if expected != '' and actual != '':
            self._data[-1] += f'Expected: {expected} - Actual: {actual}'
        return True
    
    def critical(self, message: str) -> None:
        '''
        Logs a critical error that results in program termination.

        Parameters:
            - message: a string containing the final error message

        Returns: None
        '''
        if type(message) != str:
            return False
        
        self._data.append(f'[CRITICAL:{datetime.now()}] {message}')
        return True

if __name__ == '__main__':
    notMain('This is a class file. Import its contents into another file.')
