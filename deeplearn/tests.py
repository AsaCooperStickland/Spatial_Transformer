from __future__ import print_function

__docformat__ = 'restructedtext en'

import six.moves.cPickle as pickle
import gzip
import os
import sys
import timeit

import numpy

#import theano
#import theano.tensor as T
print('working')
data_dir, data_file = os.path.split('data/mnist.pkl.gz')
print(data_dir)
print(data_file)
print(os.path.isfile('data/mnist.pkl.gz'))
