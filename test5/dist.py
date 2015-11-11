#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('distributions.pdf')

files = [ ( 'mirflickr.dist', 'MIRFLICKR-25000', 0.499702, 0.500298),
         ( 'catagories.dist', '256 Categories', 0.499690, 0.500310),
         ( '102flowers.dist', '102 Flowers', 0.499485, 0.500515)]

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

for plot in files:
    with open(plot[0]) as f:
        data = f.read()

    data = data.split('\n')

    x = [int(row.split(' ')[0]) for row in data]
    y = [float(row.split(' ')[1]) for row in data]
    
    c = ['g' if float(row.split(' ')[1]) > plot[2] and float(row.split(' ')[1]) < plot[3] else 'r' for row in data]

    fig = plt.figure(figsize=(5,2))

    ax1 = fig.add_subplot(111)

    ax1.set_title("Distribution of codes for " + plot[1])    
    ax1.set_xlabel('bit \#')
    ax1.set_ylabel('Proportion set to 1')
    ax1.set_yticks([0.5], minor=True)
    ax1.yaxis.grid(True, which='minor')
    
    ax1.bar(x,y, width=1, color=c, edgecolor="none")
    ax1.xaxis.set_ticks([0,64,128,192,255])
    ax1.set_xlim(-5,260)
    
    plt.tight_layout()
    
    pp = PdfPages(plot[0].split('.')[0] + '.pdf')
    pp.savefig()
    pp.close()