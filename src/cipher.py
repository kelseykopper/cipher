""" Generate random substitution ciphers. have multiple files for possible symbols? 
  or use ascii """
import random
import json
import os

# range of values for cipher values
MAP_RANGE = (127, 1423)
# range of values for inputs (i.e., inputs are assumed to use ASCII only; ignore formatting, whitespace)
INPUT_RANGE = (33, 126) 

class CipherMap:
  """ Handle cipher map operations. Create/read maps and handle encoding/decoding 
      files. """
  def __init__(self, name):
    """
    Initialize cipher map.

    Args:
      name (string): Name of cipher library. Will be used to either locate a 
      pre-existing library, or store a new library.

    """
    # create 2 dicts (one for encryption lookup, the other for decryption lookup)
    self.encrypt = dict()
    self.decrypt = dict() 

    self.name = name

    # create file path & names for encryption, decryption json files
    # TODO: make this not broken
    self.cipher_path = "lib/" + self.name + "/"
    self.encrypt_name = self.cipher_path + self.name + "_encrypt"
    self.decrypt_name = self.cipher_path + self.name + "_decrypt"

  def create_cipher(self):
    """ Generate a random substitution cipher. Return the cipher list object
        and store in files.
    """

    def get_char():
      """ Helper function to get a random Unicode character. """
      char = random.randint(MAP_RANGE[0], MAP_RANGE[1])
      return chr(char)

    # creating cipher lib + error handling if lib already exists
    if not os.path.exists(self.cipher_path):
      os.makedirs(self.cipher_path)
    else:
      print("Error: cipher library already exists. Terminating...\n")

    used = []

    for i in range(INPUT_RANGE[0], INPUT_RANGE[1]):
      # get a random character, make sure it doesn't already exist in the cipher map
      val = ""
      while val in used:
        val = get_char()
      
      # add this key/val pair to both encrypt & decrypt dicts
      key = chr(i)
      self.encrypt[key] = val 
      self.decrypt[val] = key
      used.append(val)
    
    # write all key value pairs to json files for later use
    with open(self.encrypt_name, 'w') as encrypt_file, open(self.decrypt_name, 'w') as decrypt_file:
      json.dump(self.encrypt, encrypt_file)
      json.dump(self.decrypt, decrypt_file)
  
  def read_map(self): 
    """ Reads cipher map from files.
    """
    # load both encrypt/decrypt dicts from json file
    with open(self.encrypt_name, "r") as encrypt_file, open(self.decrypt_name, "r") as decrypt_file:
      # TODO: add error handling if files aren't found
      self.encrypt = json.load(encrypt_file)
      self.decrypt = json.load(decrypt_file)

  def code_file(self, file_name, mode): 
    """ Encodes/decodes source file to destination file using the cipher map.

        Args:
          file_name (string): Path to the file to encrypt/decrypt.
          mode (string): Determines whether to encrypt or decrypt the file.
            Options: "encrypt" or "decrypt".
    """

    # error handling
    if self.encrypt == {} or self.decrypt == {}:
      print("Error: cipher maps are emtpy. Terminating...\n")
      return

    # read from source file, create a temp file to write the encoded/decoded file to
    with open(file_name, 'r') as file, open("temp.txt", "w") as temp:
      if mode == "encrypt":
        for line in file:
          for char_key in line: 
            val = self.encrypt.get(char_key)
            if val != None:
              temp.write(val)
            else:
              temp.write(char_key)

      elif mode == "decrypt":
        for line in file:
          for char_val in line: 
            key = self.decrypt.get(char_val)
            if key != None:
              temp.write(key)
            else:
              temp.write(char_val)

    # now write to our source file, read from temp file to overwrite original contents of source
    with open(file_name, 'w') as file, open("temp.txt", "r") as temp:
      # NOTE: this approach stores all data as a single string. 
      # not great for large files (>4096 bytes, maybe use a different approach?)
      data = temp.read()
      file.write(data)
      
    # we only want to modify the input file, so delete temp
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

