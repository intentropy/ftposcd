#!/bin/bash
#
#  This software requires python >= 3.6

python3 setup.py clean && python3 setup.py bdist && sudo python3 setup.py install
python3 setup.py clean
rm -fr build dist
