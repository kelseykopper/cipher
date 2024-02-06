# @author Kelsey Kopper
import sys
import string
import cipher as c

if __name__ == '__main__':
  c_map = c.CipherMap("example")
  c_map.read_map()
  c_map.code_file("hw1_ex.txt", "decrypt")

  print("Input the name of the cipher library: ")
  name = input()

  c_map = c.CipherMap(name)
  
  print("Use preexisting library with this name? (y/n): ")
  ans = input()
  if (ans == "y"):
    c_map.read_map()
  elif (ans == "n"):
    print("Generating cipher...")
    c_map.create_cipher()

  print("Enter path to file to convert: ")
  file = input()

  print("Encrypt (en) or decrypt (de) this file?: ")
  ans = input()
  if (ans == "en"):
    c_map.code_file(file, "encrypt")
  elif (ans == "de"):
    c_map.code_file(file, "decrypt")