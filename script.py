import os 
import time

import argparse as parsing


parser = parsing.ArgumentParser(description="Just an example",formatter_class=parsing.ArgumentDefaultsHelpFormatter)

parser.add_argument('--input', action='store', type=str, required=True)
parser.add_argument('--title', action='store', type=str, default='Progress')
parser.add_argument('--output', action='store', type=str, required=True)

args = parser.parse_args()

# print(args.input)
# print(args.title)
# print(args.output)


FILE_NAME = args.input
TITLE = args.title
OUTPUT_NAME = args.output

try:
    os.system('npm install github-readme-to-html')
except:
    print("NPM is not Installed")

time.sleep(5)
print("Wait While The File is Converting")
time.sleep(15)

try:
    os.system(f'npx github-readme-to-html -i {FILE_NAME} -t {TITLE} -o {OUTPUT_NAME}')
except:
    print("Please Check If file is exit")