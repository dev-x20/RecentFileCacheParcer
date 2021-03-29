'''
The MIT License (MIT)

Copyright (c) 2015 Patrick Olsen


'''

import struct
import os
import json
import argparse




def main():
    try:

        parser = argparse.ArgumentParser(description='Parse the RecentFileCache.bcf file on Windows 7 and Windows Server 2008.')
        parser.add_argument('-f', '--Inputfile', help='Path to RecentFileCache.bcf file.')
        parser.add_argument('-o', '--Outputfile', help='NameOfJSONOutputFile')
        args = parser.parse_args()

        if args.Inputfile:
            input_file = args.Inputfile
        else:
          print
          "You need to specify RecentFileCache.bcf file."
          exit(0)
        if args.Outputfile:
              Output_File = args.Outputfile
        else:
              print
              "You need to specify JSON Output File."
              exit(0)


    except ValueError:
        print("Usage: python RFCParser.py [-f PathToRecentFileCache.bcf] [-o NameOfJsonOutputFile")

    try:
        with open(input_file, "rb") as f:
            # Offset
            offset = 0x14
            # Go to beginning of file.
            f.seek(0)
            # Checking if signature is correct
            if (f.read(1) != b'\xfe'):
                print('filed')
            # Read forward 0x14 (20).
            f.seek(offset)

            while (read := f.read(1)):
                # Reading 3 bytes
                f.read(3)
                rl = struct.unpack('>B', read)[0]
                fnlen = (rl + 1) * 2
                foundpath = f.read(fnlen).replace(b'\x00', b'').decode()
                Paths = os.path.join(foundpath)
                WriteToJSONFile(Paths,Output_File)


    except FileNotFoundError:
        print("File not found")




def WriteToJSONFile(Paths,Output_File):

 P =os.path.split(Paths)

 data= {
     'Path':P[0],
     'FileName': P[1]
  }

 with open(Output_File +'.json', 'a') as fp:
    # To avoid duplication of backslash in the paths \\ 
     obj = json.dumps(data).encode('utf-8').decode('unicode_escape')
     fp.write('\n')
     fp.write(obj)


