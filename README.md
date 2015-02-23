targetDepth Version 1.0.0
Copyright Alex Mawla 2015. All Rights Reserved.


Requirements: Samtools. Binary must be located in /usr/bin or specified in shell environment path.

Input:
  1) Indexed Coverage file (BAM format) [required]
  2) Partition file (CSV format) [required] 	
        Four columns:  
          Partition Name, Chromosome, Start Position, Stop Position
  3) Reference genome (bed format) [required]     
  4) Output directory [optional]		   


