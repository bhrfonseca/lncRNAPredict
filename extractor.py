import re
from sys import argv

class LengthError(Exception):
    def __str__(self):
        return repr("An error ocurred at the extraction. Take a look the *.gtf file and compare it with each regular expression attribute")

def main():
    try:
        file = open(argv[1], "r")
        
        sequence = file.read()

        # We can improve this feature 
        chromosomes = re.findall("^[\w\d\s]+[A-Z]", sequence, re.MULTILINE)
        exons = re.findall("exon[\s]+[\d]+[\s]+[\d]+", sequence, re.MULTILINE)
        genes = re.findall("gene_id[\s\d\.\"\w]+", sequence, re.MULTILINE)
        transcripts = re.findall("transcript_id[\s\d\w\.\"]+", sequence, re.MULTILINE)

        # The four list must be the same size
        if (len(chromosomes)*4 != (len(exons) + len(genes) + len(transcripts) + len(chromosomes))):
            raise LengthError

        # How all lists have the same size, I can use a length of one of them
        for x in range(len(exons)):
            print(chromosomes[x]+" "+exons[x]+" "+genes[x]+" "+transcripts[x])

    except IOError:
        print("The file " + argv[1] + " cannot be opened")
    except IndexError:
        print("Argument file was not specified. Please, type the file name eg: python extractor.py file.gtf")
    except LengthError as e:
        print(e)
        
main()
