import re
from sys import argv

def main():

        #fasta file
        file_fasta = open(argv[1], "r")

        with open(argv[1], 'r') as f:
            content = f.readlines()[1:]
        fasta_content = "".join(content).replace("\n","")

        #gtf file
        file_gtf = open(argv[2], "r")
        gtf = file_gtf.readlines()

        #organism_informatiom
        organism = argv[3]

        for line in gtf:
            # [ start inclusive : end exclusive ]
            print '> Organism: ' + organism + ' | Gene Id: ' + line.split()[6] + ' | Transcript_Id' +  line.split()[8] + ' | ' \
                                            + line.split()[0] + ' | ' + line.split()[1] + ' | ' + line.split()[2] + ' | Start: ' + line.split()[3] + ' | End: ' + line.split()[4]
            print fasta_content [ int(line.split()[3]) : int(line.split()[4]) ] + '\n'


main()
