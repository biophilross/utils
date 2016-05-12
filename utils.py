import os,sys

def read_fasta(fasta_file):
    """Read in a fasta file
    
    Input: fasta file path
    Output: NA
    Return: dictionary indexable by headers in your fasta file that return the respective sequences
    """
  seqs = dict()
  with open(fasta_file) as f:
    header = f.readline()
    # check to make sure FASTA file is properly formatted
    if(header[0] != ">"):
      sys.stderr.write("FASTA file does not start with properly formatted header. Aborting.")
      sys.exit(0)
    header = header.rstrip(os.linesep)
    id = header.split("|")[0]
    id = id.replace(">", "")
    id = id.replace(" ", "_")
    sequences = []
    for line in f:
      line = line.rstrip("\n")
      if(line[0] == ">"):
        seqs[id] = "".join(sequences)
        header = line
        header = header.replace(">", "")
        header = header.replace(" ", "")
        id = header.split("|")[0]
        sequences = []
      else:
        line = line.rstrip(os.linesep)
        sequences.append(line)

  seqs[id] = "".join(sequences)
  return(seqs)
  

def print_fasta(fasta_dict, width=60):
  """Print fasta dictionary to stdout
  
  Input: fasta file dictinoary
  Output: fasta file printed to stdout
  Return: NA
  """
  d = fasta_dict
  
  for key in d.keys():
    id = ">" + key
    seq = "\n".join(textwrap.wrap(d[key], width))
    sys.stdout.write(id + "\n" + seq + "\n")
