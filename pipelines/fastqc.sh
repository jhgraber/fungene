#fastqc -o fastqc-v0.11.8/bam --noextract -t 1 -f bam samtools/samtools-1.9/axolotl-transcriptome.14-09157-3A_AAACAT_L001.bam 
fastqc -o fastqc-v0.11.8/fastq --noextract -t 2 -f fastq 14-09157-3A_AAACAT_L001_R1_001.fastq 14-09157-3A_AAACAT_L001_R2_001.fastq 
