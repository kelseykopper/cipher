# @author Kelsey Kopper
import sys

def read_map(map_name, mode): 
  """ Reads cipher map from the given text file. """
  cipher_map = dict()
  map = open(map_name, "r", encoding="utf-8")
  if mode == "-en": 
    for line in map: 
      # split each line into a list of 2 items (key and value)
      words = line.split()
      # insert into the map. assumes no duplicates
      cipher_map[words[0]] = words[1]
  else: 
    for line in map:
      words = line.split()
      cipher_map[words[1]] = words[0]

  map.close()
  return cipher_map

def gen_cipher(start, end, rot):
  """ Generate a cipher map. """
  cipher_map = dict()

  # TODO: generate a substitution cipher

  return cipher_map

def code_file(src_name, dst_name, map, mode): 
  """ Encodes/decodes source file to destination file using the cipher map.
      Note: map must be constructed such that keys are found in the source file
       and values are the "result" of encryption/decryption.
  """
  src = open(src_name, "r", encoding="utf-8")
  dst = open(dst_name, "w", encoding="utf-8")

  for line in src: 
    for letter in line: 
        val = map.get(letter)
        if (val != None):
          dst.write(val)
        else: 
          dst.write(letter)

  src.close()
  dst.close()

if __name__ == '__main__':
  if len(sys.argv) < 5: 
     print(f"Usage: {sys.argv[0]} src.txt dst.txt <mode> -rot x")

     print("Cipher may be specified by indicating the number of rotations. For Caesar cipher, use -rot 3")

     print("\nModes are as follows:")
     print("\t-en -> encode source file to destination")
     print("\t-de -> decode source file to destination")

     print("\nOptionally, you may choose to provide your own map using the following syntax:")
     print(f"Usage: {sys.argv[0]} src.txt dst.txt <mode> map.txt\n")
     sys.exit()

  src_name = sys.argv[1]
  dst_name = sys.argv[2]
  mode = sys.argv[3]

  # error checking
  if mode != "-en" and mode != "-de":
    print("Unknown mode.")

    print("\nModes are as follows:")
    print("\t-en -> encode source file to destination")
    print("\t-de -> decode source file to destination")
    sys.exit()

  # obtaining cipher map
  if len(sys.argv) == 6: 
    # need to generate a cipher map, rotation has been provided
    rot = sys.argv[5]
    cipher_map = gen_cipher('A', 'Z', rot)
    
  elif len(sys.argv) == 5: 
    # map file was provided, read file
    map_name = sys.argv[4]
    cipher_map = read_map(map_name, mode)

  code_file(src_name, dst_name, cipher_map, mode)

