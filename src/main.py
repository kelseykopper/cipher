# @author Kelsey Kopper
import sys
import string
import cipher as c

if __name__ == '__main__':
  c_map = c.CipherMap("shit")
  c_map.create_cipher()
  c_map.code_file("hw1_ex.txt", "decrypt")
  # testing mode
  # if len(sys.argv) == 2 and sys.argv[1] == "-test":
  #   print("Testing functions ---------------------------------------------")
  #   sys.exit()

  # if len(sys.argv) < 5: 
  #    print(f"Usage: python3 {sys.argv[0]} src.txt dst.txt <mode> -rot x")

  #    print("Cipher may be specified by indicating the number of rotations. For Caesar cipher, use -rot 3")

  #    print("\nModes are as follows:")
  #    print("\t-en -> encode source file to destination")
  #    print("\t-de -> decode source file to destination")

  #    print("\nOptionally, you may choose to provide your own map using the following syntax:")
  #    print(f"Usage: {sys.argv[0]} src.txt dst.txt <mode> map.txt\n")
  #    sys.exit()

  # src_name = sys.argv[1]
  # dst_name = sys.argv[2]
  # mode = sys.argv[3]

  # # error handling
  # if mode != "-en" and mode != "-de":
  #   print("Unknown mode.")

  #   print("\nModes are as follows:")
  #   print("\t-en -> encode source file to destination")
  #   print("\t-de -> decode source file to destination")
  #   sys.exit()

  # # obtaining cipher map
  # if len(sys.argv) == 6: 
  #   # need to generate a cipher map, rotation has been provided
  #   rot = int(sys.argv[5])
  #   cipher_map = gen_cipher(rot, mode)
    
  # elif len(sys.argv) == 5: 
  #   # map file was provided, read file
  #   map_name = sys.argv[4]
  #   cipher_map = read_map(map_name, mode)

  # print("Path to source file: ")
  # src_name = input()

  # print("Path to dst file (if left blank, source file will be overwritten): ")
  # dst_name = input()

  # print("Path to cipher map: ")
  # map_path = input()

  # cipher_map = read_map(map_path, "-en")

  # code_file(src_name, dst_name, cipher_map)

  # code_file("tests/inputs/fox.txt", "tests/outputs/dst.txt", test_map)