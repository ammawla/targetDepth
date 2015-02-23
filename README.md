targetDepth Version 1.0.0

Copyright Alex Mawla 2015. All Rights Reserved.

Takes in an indexed coverage file with a partition csv file identifying regions of interest, and outputs depth of coverage files for each partition of interest. 

Requirements: Samtools (http://samtools.sourceforge.net).
    Samtools binary must be located in /usr/bin or specified in the terminal shell environment path.

Input:

  1) Indexed Coverage file (BAM format) [required]
  
  2) Partition file (CSV format) [required] 	
        Four columns:  
            Partition Name, Chromosome, Start Position, Stop Position
  
  3) Reference genome (bed format) [required]     
  
  4) Output directory [optional]		   


