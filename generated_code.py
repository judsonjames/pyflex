################################################################################
# START GENERATED HEADER
import sys
import os
import re
# END GENERATED HEADER
################################################################################



################################################################################
# CODE PROVIDED FROM PYFLEX FILE
################################################################################
num_words = 0

def CountWords(text: str) -> None:
    global num_words
    num_words += 1
    print('NUM WORDS: {}'.format(num_words))



################################################################################
# GENERATED DRIVER
################################################################################
if __name__ == '__main__':
    for files in sys.argv[1:]:
        print('FILE: {}'.format(files))
        lines_from_file = []
        with open(file=sys.argv[1]) as f:
            lines = f.readlines()
        for line in lines:
            for word in line.split(' '):
                if re.match(pattern='[^\d\W]', string=word) is not None:
                    CountWords(word)
################################################################################
# END GENERATED CODE
################################################################################
