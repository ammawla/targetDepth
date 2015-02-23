#!/usr/bin/python
#targetDepth.py
#Copyright Alex Mawla 2015. All Rights Reserved.

####################################################
#targetDepth	1.0.0				   #	
#Copyright Alex Mawla 2015. All Rights Reserved.   #
#Requirements: Samtools. Binary must be located in #
#/usr/bin or specified in shell environment path.  #
########################Input####################### 					   	
#      Indexed Coverage file (BAM format)[required]#
#      Partition file (CSV format): Four columns:  #
#      Partition Name, Chromosome, Start Position, #
#      Stop Position.[required] 		   #
#      Reference genome (bed format)[required]     #
#      Output directory[optional]		   #	
####################################################



import re
import os
import sys
import string
import csv
from optparse import OptionParser
import warnings
import string
import argparse
import subprocess

__author__ = "Alex Mawla"
__copyright__ = "Copyright Alex Mawla 2015. All Rights Reserved."
__credits__= []
__licence__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Alex Mawla"
__email__ = "ammawla@ucdavis.edu"

def main():
	usage = "usage: %prog [options] -b <in.bam> [required] -p <partitions.csv> [required] -r <genome.bed> [required] -o <output_dir>\n\nRequires Samtools to be in environment shell path."
	parser = OptionParser(usage, version='\n' + "%prog " + __version__ + '\n' + __copyright__ + '\n')
	parser.add_option("-b", "--input-bam", action="store", type="string", dest="input_bam", help="Alignment file in BAM format [Required]")
	parser.add_option("-o", "--output-dir", action="store", type="string", dest="output_dir", help="Output directory.") 
	parser.add_option("-p", "--partion-file", action="store", type="string", dest="partition_file", help="Partition file in csv format with four columns: Partition Name, Chromosome, Start Position, Stop Position. [Required]")
	parser.add_option("-r", "--reference-bed", action="store", type="string", dest="ref_bed", help="Reference genome in bed format. [Required]")
	
	(options, args)=parser.parse_args()
	
	if not (options.input_bam and options.partition_file and options.ref_bed):
		parser.print_help()
		sys.exit(0)

	if not os.path.exists(options.input_bam):
		print >>sys.stderr, "Cannot find input BAM file"
		print >>sys.stderr, options.input_bam + " does not exist"
		sys.exit(0)
	 
	if not (str.lower(os.path.splitext(options.input_bam)[1][1:])=='bam'):
		print >>sys.stderr, "Wrong alignment file type"
		print >>sys.stderr, options.input_bam + " is not a .bam file"
		sys.exit(0)

        if not os.path.exists(options.partition_file):
                print >>sys.stderr, "Cannot find input partition csv file"
                print >>sys.stderr, options.partition_file + " does not exist"
                sys.exit(0)

        if not (str.lower(os.path.splitext(options.partition_file)[1][1:])=='csv'):
                print >>sys.stderr, "Wrong partition file type"
                print >>sys.stderr, options.partition_file + " is not a .csv file"
                sys.exit(0)

	if not os.path.exists(options.output_dir):
		print >>sys.stderr, "Cannot find output directory folder"
                print >>sys.stderr, options.output_dir + " does not exist"
                sys.exit(0)

        if not os.path.exists(options.ref_bed):
                print >>sys.stderr, "Cannot find reference genome bed file"
                print >>sys.stderr, options.ref_bed + " does not exist"
                sys.exit(0)

        if not (str.lower(os.path.splitext(options.ref_bed)[1][1:])=='bed'):
                print >>sys.stderr, "Wrong reference genome file type"
                print >>sys.stderr, options.ref_bed + " is not a .bed file"
                sys.exit(0)
	
	f = open(options.partition_file)
	csv_f = csv.reader(f)
	f.next()
	for row in csv_f:
		partition = row[0]
		chrom = row[1]
		start = row[2]
		stop = row[3]  
		region = chrom + ":" + start + "-" + stop
		dest = options.output_dir + "/" +  partition + ".depth"
		cmd = "samtools depth -r " + region + " " +  options.input_bam + " > " + dest
		os.system(cmd)
  
if __name__ == '__main__':
  main()







