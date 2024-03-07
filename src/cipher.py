""" Classes and logic behind cipher library storage and cipher creation.

This file contains methods relating to the CipherMap class, which handles cipher
creation and file conversion.

This file is intended to be used in combination with main.py, which contains 
this program's front-end UI.

"""

import random
import json
import os

# range of values for cipher values
MAP_RANGE = (127, 1423)

# range of values for inputs (i.e., inputs are assumed to use ASCII only; ignore formatting, whitespace)
INPUT_RANGE = (33, 126) 

class CipherMap:
  """ @brief Handle cipher map operations. Create/read maps and handle 
      encoding/decoding files. 
  """
  def __init__(self):
    """
    @brief Initialize cipher map.
    """
    # create 2 dicts (one for encodeion lookup, the other for decodeion lookup)
    self.encode = dict()
    self.decode = dict() 

    self.name = ""
    self.name_is_set = False # bool to handle error checking

    # initialize file paths to none
    self.cipher_path = None
    self.encode_name = None 
    self.decode_name = None

  def __str__(self):
    if not self.name_is_set:
      return "Error: map has not been created or identified."
    else:
      return self.cipher_path
  
  def set_name(self, name):
    """ @brief set library name for this cipher map
        @param name Type string contains name of cipher library 
    """
    self.name = name 
    self.name_is_set = True

    # create file path & names for encoding, decoding json files
    self.cipher_path = os.path.join("./lib", self.name)
    self.encode_name = os.path.join(self.cipher_path, self.name + "_encode.json")
    self.decode_name = os.path.join(self.cipher_path, self.name + "_decode.json")
    print(self.cipher_path)
    
  def already_exists(self):
    """ @brief Check if cipher library already exists. 
        @return boolean indicating whether library was found
    """
    if os.path.exists(self.cipher_path) and self.name_is_set:
      print("DNE")
      return True
    else:
      return False

  def create_cipher(self):
    """ @brief Generate a random substitution cipher and store maps in json files.
        @return Cipher list object
    """

    def get_char():
      """ Helper function to generate a random Unicode character. """
      char = random.randint(MAP_RANGE[0], MAP_RANGE[1])
      return chr(char)
    
    # error handling
    if not self.name_is_set:
      print("Error creating cipher: no library name provided.")
      return

    # creating cipher lib directory + error handling if lib already exists
    if not os.path.exists(self.cipher_path):
      os.makedirs(self.cipher_path)
    else:
      print("Error: cipher library already exists.")
      return

    used = []

    for i in range(INPUT_RANGE[0], INPUT_RANGE[1]):
      # get a random character, make sure it doesn't already exist in the cipher map
      val = ""
      while val in used:
        val = get_char()
      
      # add this key/val pair to both encode & decode dicts
      key = chr(i)
      self.encode[key] = val 
      self.decode[val] = key
      used.append(val)
    
    # write all key value pairs to json files for later use
    with open(self.encode_name, 'w') as encode_file, open(self.decode_name, 'w') as decode_file:
      json.dump(self.encode, encode_file)
      json.dump(self.decode, decode_file)
  
  def read_map(self): 
    """ @brief Reads cipher map from files.
    """
    # error handling
    if not self.name_is_set:
      print("Error reading cipher library: no library name provided.")
      return

    # load both encode/decode dicts from json file
    try:
      with open(self.encode_name, "r") as encode_file, open(self.decode_name, "r") as decode_file:
        self.encode = json.load(encode_file)
        self.decode = json.load(decode_file)
    except FileNotFoundError:
      print("Error: unable to locate one or both cipher maps.\n")
      return

  def code_file(self, file_name, mode): 
    """ @brief Encodes/decodes source file to destination file using 
        the cipher map. Contents of file_name are modified as a side effect.
        @param file_name Type string contains path of file to encode or decode.
        @param mode Type string contains file operation type (encode or decode)
    """

    # error handling
    if not self.name_is_set:
      print("Error: no cipher library name provided.\n")
      return
    elif self.encode == {} or self.decode == {}:
      print("Error: cipher maps are emtpy.\n")
      return

    # read from source file, create a temp file to write the encoded/decoded file to
    try:
      with open(file_name, 'r') as file, open("temp.txt", "w") as temp:
        if mode == "encode":
          for line in file:
            for char_key in line: 
              val = self.encode.get(char_key)
              if val != None:
                temp.write(val)
              else:
                temp.write(char_key)

        elif mode == "decode":
          for line in file:
            for char_val in line: 
              key = self.decode.get(char_val)
              if key != None:
                temp.write(key)
              else:
                temp.write(char_val)

      # write to source file, read from temp file to overwrite original contents of source
      with open(file_name, 'w') as file, open("temp.txt", "r") as temp:
        # NOTE: this approach stores all data as a single string. 
        # not great for large files (>4096 bytes, maybe use a different approach?)
        data = temp.read()
        file.write(data)
    except FileNotFoundError:
      print("Error: file not found.")
        
    # we only want to modify the input file, so delete temp
    try:
      os.remove("temp.txt")
    except OSError as e:
      print(f'Error deleting file: {e}')
