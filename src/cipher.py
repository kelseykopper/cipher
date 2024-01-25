# @author Kelsey Kopper
import sys
import string

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
  elif mode == "-de": 
    for line in map:
      words = line.split()
      cipher_map[words[1]] = words[0]

  map.close()
  return cipher_map

def gen_alphabet(alphabet, rot, map, mode):
  """ Helper function to create a cipher structure for the given rotation. """

  # get the last letter in keys alphabet before cipher values should wrap around
  # to the start of the alphabet
  last_letter = chr(ord(alphabet[-1]) - rot + 1)

  for letter in alphabet:
    if letter == last_letter:
      # wrap back to start of alphabet
      value = alphabet[0]
    elif letter > last_letter: 
      i = alphabet.index(value) # get the index of "value" from last iteration
      value = alphabet[i + 1]  # increments value alphabetically
    else: 
      # convert letter to ASCII, add rotation, then convert back to char
      value = chr(ord(letter) + rot)

    if mode == "-en":
      map[letter] = value
    elif mode == "-de":
      map[value] = letter

def gen_cipher(rot, mode):
  """ Generate a cipher map. """
  cipher_map = dict()
  lowercase_alphabet = list(string.ascii_lowercase)
  uppercase_alphabet = list(string.ascii_uppercase)

  gen_alphabet(lowercase_alphabet, rot, cipher_map, mode)
  gen_alphabet(uppercase_alphabet, rot, cipher_map, mode)

  return cipher_map

def code_file(src_name, dst_name, map): 
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
  # testing mode
  if len(sys.argv) == 2 and sys.argv[1] == "-test":
    print("Testing functions ---------------------------------------------")
    gen_cipher(3)
    sys.exit()

  if len(sys.argv) < 5: 
     print(f"Usage: python3 {sys.argv[0]} src.txt dst.txt <mode> -rot x")

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

  # error handling
  if mode != "-en" and mode != "-de":
    print("Unknown mode.")

    print("\nModes are as follows:")
    print("\t-en -> encode source file to destination")
    print("\t-de -> decode source file to destination")
    sys.exit()

  # obtaining cipher map
  if len(sys.argv) == 6: 
    # need to generate a cipher map, rotation has been provided
    rot = int(sys.argv[5])
    cipher_map = gen_cipher(rot, mode)
    
  elif len(sys.argv) == 5: 
    # map file was provided, read file
    map_name = sys.argv[4]
    cipher_map = read_map(map_name, mode)

  code_file(src_name, dst_name, cipher_map)

