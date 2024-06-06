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

from os.path import exists

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
            'WARN': 0,
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

        with open(f'{path}/{name}') as log:
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
            # skip lines that don't contain metrics
            if line[0] != '[': continue
            
            # summarize metrics
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
    
    def print_summary(self, writeout: str|None = None) -> None:
        '''
        Prints log summary, with optional parameter to write it to output.log
        in a given directory instead.

        Parameters:
            - writeout: a string containing a path to write the result to if \
                        desired.

        Returns: None
        '''
        self._metrics = {k: v for k, v in self._metrics.items() if v > 0}
        summary = []
        summary.append('Log Metrics Summary:\n')
        summary.append('='*125)
        summary.append('\n')
        for k, v in self._metrics.items():
            summary.append(f'{k} -> {v}')
            summary.append('\n')
        summary.append('-'*125)
        summary.append('\n')
        if 'WARN' in self._metrics:
            summary.append(f'Software completed with {self._metrics['WARN']} warnings.\n')
            summary.append('-'*125)
            summary.append('\n')
        if 'ERROR' in self._metrics:
            summary.append(f'Software had {self._metrics['ERROR']} errors.\n')
            summary.append('-'*125)
            summary.append('\n')
        if 'CRITICAL' in self._metrics:
            summary.append(f'Software suffered from {self._metrics['CRITICAL']} critical failures.\n')
        summary.append('='*125)
        summary.append('\n')

        if writeout is not None and exists(writeout):
            with open(f'{writeout}/outfile.log', 'w') as out:
                out.writelines(summary)
        else:
            for line in summary:
                print(line, end='')

if __name__ == '__main__':
    notMain('This is a class file. Import its contents into another file.')
