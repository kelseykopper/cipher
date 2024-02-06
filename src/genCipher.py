""" Generate random substitution ciphers. have multiple files for possible symbols? 
  or use ascii """
import random
import json
import os

# range of values for cipher values
MAP_RANGE = (33, 1423)

# range of values for inputs (i.e., inputs are assumed to use ASCII only; ignore formatting, whitespace)
INPUT_RANGE = (33, 126) 

class CipherMap:
  """ Handle cipher map operations. Create/read maps and handle encoding/decoding 
      files. """
  def __init__(self, file_name):
    self.cipher_map = []
    self.file_name = file_name

  def get_char(self):
    """ Get a random Unicode character. """
    char = random.randint(MAP_RANGE[0], MAP_RANGE[1])
    return chr(char)

  def create_cipher(self, file_name):
    """ Generate a random substitution cipher. Return the cipher list object
        and store in file_name as json """

    kv_pairs = []
    used = []

    for i in range(INPUT_RANGE[0], INPUT_RANGE[1]):

      # get a random character, make sure it doesn't already exist in the cipher map
      val = ""
      while val in used:
        val = self.get_char()
      
      # append this pair to our list of key value pairs
      key = chr(i)
      kv_pairs.append([key, val])
      used.append(val)
    
    # write all key value pairs to json file for later use
    with open(file_name, 'w') as f:
      json.dump(kv_pairs, f)

    self.cipher_map = kv_pairs
  
  def read_map(self, map_name): 
    """ Reads cipher map from the given json file. """
    with open(map_name, "r") as f: 
      kv_pairs = json.load(f)

    self.cipher_map = kv_pairs

  def code_file(self, mode): 
    """ Encodes/decodes source file to destination file using the cipher map.
    """

    # error handling
    if self.cipher_map == []:
      print("Error: no cipher map provided. Terminating...\n")
      return

    # read from source file, create a temp file to write the encoded/decoded file to
    with open(self.file_name, 'r') as file, open("temp.txt", "w") as temp:
      for line in file:
        for char_key in line: 
          # find char_key in cipher_map, replace
          break 
      
      # we only want to modify the input file, so overrwrite input file w/ temp, delete temp
      file = temp
      try:
        os.remove("temp.txt")
      except OSError as e:
        print(f'Error deleting file: {e}')



# def gen_alphabet(alphabet, rot, map, mode):
#   """ Helper function to create a cipher structure for the given rotation. """

#   # get the last letter in keys alphabet before cipher values should wrap around
#   # to the start of the alphabet
#   last_letter = chr(ord(alphabet[-1]) - rot + 1)

#   for letter in alphabet:
#     if letter == last_letter:
#       # wrap back to start of alphabet
#       value = alphabet[0]
#     elif letter > last_letter: 
#       i = alphabet.index(value) # get the index of "value" from last iteration
#       value = alphabet[i + 1]  # increments value alphabetically
#     else: 
#       # convert letter to ASCII, add rotation, then convert back to char
#       value = chr(ord(letter) + rot)

#     if mode == "-en":
#       map[letter] = value
#     elif mode == "-de":
#       map[value] = letter

# def gen_cipher(rot, mode):
#   """ Generate a cipher map. """
#   cipher_map = dict()
#   lowercase_alphabet = list(string.ascii_lowercase)
#   uppercase_alphabet = list(string.ascii_uppercase)

#   gen_alphabet(lowercase_alphabet, rot, cipher_map, mode)
#   gen_alphabet(uppercase_alphabet, rot, cipher_map, mode)

#   return cipher_map

