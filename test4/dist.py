#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('distributions.pdf')

#files = [ ( 'mirflickr.dist', 'MIRFLICKR-25000', 0.499702, 0.500298),
         #( 'catagories.dist', '256 Categories', 0.499690, 0.500310),
         #( '102flowers.dist', '102 Flowers', 0.499485, 0.500515)]

files = ['k1000_102flowers.radii',
         'k1000_catagories.radii',
         'k1000_mirflickr.radii',
         'k10_102flowers.radii',
         'k10_catagories.radii',
         'k10_mirflickr.radii']


for plot in files:
    with open(plot) as f:
        data = f.read()

    data = data.split('\n')

    
    sumv = 0.0
    maxv = 0.0
    
    for row in data:
        if len(row)== 0:
            continue
        val =  float(row.split(' ')[1])
        sumv += val
        maxv = max(maxv, val)
    print plot
    print "    sum:" , sumv
    print "    max:", maxv
    
    
