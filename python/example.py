#!/usr/bin/python3
"""
QuanCulator
===========
example for QuanCulator
-----------------------
        _                 _
       (_)               | |
 _ __   _  __  __   ___  | |
| '__| | | \ \/ /  / _ \ | |
| |    | |  >  <  |  __/ | |
|_|    |_| /_/\_\  \___| |_|
"""
__author__    = ['Axel Ország-Krisz Dr.', 'Richárd Ádám Vécsey Dr.']
__copyright__ = "Copyright 2021, QuanCulator Project"
__credits__   = ['Axel Ország-Krisz Dr.', 'Richárd Ádám Vécsey Dr.']
__license__   = 'Copyrighted'
__version__   = '0.1'
__status__    = 'Final'

import quanculator

EXAMPLE_LINK = 'http://www.quantum.com'

# creating webobject
webobject = quanculator.WebObject(EXAMPLE_LINK)

# creating QuantumObject
quantums = quanculator.QuantumObject(webobject.webcontent)

# getting results
print('   Number of Total Quantum(s): {:>4d}'.format(quantums.totalquantums))
print('Number of Explicit Quantum(s): {:>4d}'.format(quantums.explicitquantums))
print('  Number of Hidden Quantum(s): {:>4d}'.format(quantums.hiddenquantums))
print('  Number of Broken Quantum(s): {:>4d}'.format(quantums.brokenquantums))
print('   Number of Quantum Spill(s): {:>4d}'.format(quantums.quantumspills))
