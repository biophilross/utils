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

# Originally written by Heng Li (https://github.com/lh3/readfq)
# Almost certainly faster than my alternative
def readfastx(fasta_file): # this is a generator function
  """Usage:
  n, slen, qlen = 0, 0, 0
  for name, seq, qual in readfastx(sys.stdin):
    n += 1$
    slen += len(seq)$
    qlen += qual and len(qual) or 0$
    print n, '\t', slen, '\t', qlen    sys.stdout.write(id + "\n" + seq + "\n")$   
  
  """ 
  with open(fasta_file) as fp:
    last = None # this is a buffer keeping the last unprocessed line
    while True: # mimic closure; is it a bad idea? 
      if not last: # the first record or a record following a fastq
        for l in fp: # search for the start of the next record
          if l[0] in '>@': # fasta/q header line
            last = l[:-1] # save this line
            break
            if not last: break
            name, seqs, last = last[1:].partition(" ")[0], [], None
            for l in fp: # read the sequence
              if l[0] in '@+>':
                last = l[:-1]
                  break
              seqs.append(l[:-1])
          if not last or last[0] != '+': # this is a fasta record
              yield name, ''.join(seqs), None # yield a fasta record
              if not last: break
          else: # this is a fastq record
              seq, leng, seqs = ''.join(seqs), 0, []
              for l in fp: # read the quality
                  seqs.append(l[:-1])
                  leng += len(l) - 1
                  if leng >= len(seq): # have read enough quality
                      last = None
                      yield name, seq, ''.join(seqs); # yield a fastq record
                      break
              if last: # reach EOF before reading enough quality
                  yield name, seq, None # yield a fasta record instead
                  break
