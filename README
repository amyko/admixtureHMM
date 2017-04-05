# admixtureHMM

Here's an example of how to run the HMM. 



COMMAND TO RUN HMM:
The following command will run the HMM on the input path given by absolute_input_path and store the result given by absolute_output_path.

python run_hmm.py -i absolute_input_path -o absolute_output_path



INPUT FILE FORMAT:
AN example input file is given in example_input.txt. The first row of the file is a header, and the subsequent rows are the data. Each row corresponds to a single SNP. The first column is the position in bp; the second column is the allele frequencies of the derived allele for Yoruba; the third column is the allele frequenceis for the derived allele in Neanderthals (or Denisovans); and the subsequent columns are the haplotypes for the individuals of interest:

pos	afr	nea	ind1_hap1	ind1_hap2	ind2_hap1	ind2_hap2
1	0.1	0.5	1		0		0		1
2	0.02	1.0	1		0		0		0
3	0	0.5	1		0		0		0



OUTPUT FILE FORMAT:
An example output file is given in example_output.txt. Each row is the start and end positions for the inferred tracts for a particular haplotype.  For example, if indiv1 had two tracts the output would look like:

ind1_hap1 start_1 end_1 start_2 end_2

If there was no tract, it would just contain the name of the haplotype:

ind1_hap1



OPTIONAL PARAMETERS:
There are other options you can adjust as well, including recombination rate, admixture time, admixture proportion, posterior probability threshold at which to call a tract, etc. The flags for these options are given below:

-t admixture time in generations (default=1900)
-m admixture proportion (default=.05)
-ht confidence level at which to call tracts (default=.9)
-r recombination rate in per bp per gen

You can read the comments in run_hmm.py to learn more about these.
