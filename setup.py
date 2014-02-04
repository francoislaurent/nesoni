#!/usr/bin/env python

from os.path import join, dirname

from setuptools import setup

directory = dirname(__file__)

# Get version
with open(join(directory,'nesoni','__init__.py'),'rU') as f:
    exec f.readline()

with open(join(directory,'nesoni','nesoni-r','R','nesoni_version.R'),'wb') as f:
    print >> f, '#Autogenerated'
    print >> f, 'nesoni_version <- function() { \''+ VERSION + '\' }'

setup(
    name='nesoni',
    version=VERSION,
    description = 'Collection of tools for processing high-throughput sequencing data, with an emphasis on bacterial data.',
    author = 'Paul Harrison',
    author_email = 'paul.harrison@monash.edu',
    url = 'http://bioinformatics.net.au/software.nesoni.shtml',
    
    packages = [
        'nesoni', 
        'nesoni.third_party',
        'nesoni.third_party.vcf',
        'treemaker',
        ],
    
    package_data = {
        'nesoni' : [
            'nesoni-r/DESCRIPTION',
            'nesoni-r/R/*',
            'CHANGES',
            ],            
        },
    
    entry_points = {
        'console_scripts' : [
            'nesoni = nesoni:main',
            ]
        },
    
    classifiers = [
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        ],
    )

