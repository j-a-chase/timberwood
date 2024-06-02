################################################################################
# Name: James A. Chase
# File: interpreter.py
# Date Created: 1 June 2024
# Description:
#
# Built-in Interpreter class used to evaluate results from a Logger class.
#
################################################################################

# imports
from asserts.asserts import notMain, assertExists, assertType

class Interpreter:
    def __init__(self) -> None:
        '''
        Constructor

        Parameters: None

        Returns: None
        '''
        self._log_data = None
        self._metrics = {
            'ACTION': 0,
            'WARNING': 0,
            'ERROR': 0,
            'CRITICAL': 0
        }

    def read_log(self, path: str = './', name: str = 'runtime.log') -> None:
        '''
        Reads in a TimberWood log file.

        Parameters:
            - path: a string containing the path to the TimberWood log file. \
                    Default is root project directory
            - name: a string containing the TimberWood log file name. Default \
                    is runtime.log
        
        Returns: None
        '''
        assertType(str, type(path))
        assertType(str, type(name))
        assertExists(path)

        with open(path+name) as log:
            self._log_data = [line for line in log.readlines()]

    def calculate_metrics(self, actions: bool = False, warnings: bool = True,
                          errors: bool = True, criticals: bool = True) -> None:
        '''
        Calculates log metrics based off of types of logs listed.

        Parameters:
            - actions: a boolean indicating if actions metrics should be \
                       tracked
            - warnings: a boolean indicating if warnings metrics should be \
                        tracked
            - errors: a boolean indicating if errors metrics should be tracked
            - criticals: a boolean indicating if critical failures should be \
                         tracked. RECOMMENDED TO NOT SET TO FALSE

        Returns: None
        '''
        assertType(bool, type(actions))
        assertType(bool, type(warnings))
        assertType(bool, type(errors))
        assertType(bool, type(criticals))

        for line in self._log_data:
            colon = line.index(':')
            metric = line[1:colon]
            if actions and metric == 'ACTION':
                self._metrics[metric] += 1
            elif warnings and metric == 'WARN':
                self._metrics[metric] += 1
            elif errors and metric == 'ERROR':
                self._metrics[metric] += 1
            elif criticals and metric == 'CRITICAL':
                self._metrics[metric] += 1
            else:
                print(f'Error calculating metric {metric}...')
                self.metrics = {}
                return
    
    def print_summary(self, writeout: bool = False) -> None:
        '''
        Prints log summary, with optional parameter to write it to a file
        instead.

        Parameters:
            - writeout: a boolean indicating if output should be written to a \
                        file or not

        Returns: None
        '''
        self._metrics = {k: v for k, v in self._metrics.items() if v > 0}
        summary = []
        summary.append('Log Metrics Summary:')
        summary.append('='*125)
        for k, v in self._metrics.items():
            summary.append(f'{k} -> {v}')
        summary.append('-'*125)
        if 'WARN' in self._metrics:
            summary.append(f'Software completed with {self._metrics['WARN']} warnings.')
            summary.append('-'*125)
        if 'ERROR' in self._metrics:
            summary.append(f'Software had {self._metrics['ERROR']} errors.')
            summary.append('-'*125)
        if 'CRITICAL' in self._metrics:
            summary.append(f'Software suffered from {self._metrics['CRITICAL']} critical failures')
        summary.append('='*125)        

if __name__ == '__main__':
    notMain('This is a class file. Import its contents into another file.')
