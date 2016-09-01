import re
from sys import argv

def main():
    try:
        file = open(argv[1], "r")
        sequence = file.read()
        exons = []
        genes_id = []
        transcripts_id = []
        exons = re.findall("exon.\d+.\d+", sequence)
        genes_id = re.findall("gene_id..[A-Z0-9.]+..", sequence)
        transcripts_id = re.findall("transcript_id..[A-Z0-9.]+..", sequence)

        print(exons)
        print(genes_id)
        print(transcripts_id)
    except IOError:
        print("The file " + argv[1] + " cannot be opened")
    except IndexError:
        print("Argument file was not specified. Please, type the file name eg: python extractor.py file.gtf")

main()
