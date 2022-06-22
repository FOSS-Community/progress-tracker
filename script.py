import os 
import time

import argparse as parsing


parser = parsing.ArgumentParser(description="ReadME.md to .html writer",formatter_class=parsing.ArgumentDefaultsHelpFormatter)

parser.add_argument('-i', '--input', action='store', type=str, required=True, help="name of the input file eg. template.html")
parser.add_argument('-t', '--title', action='store', type=str, default='Progress', help="title of the html page." )
parser.add_argument('-o', '--output', action='store', type=str, required=True, help="the generated output file name , which is generated in dist folder. eg. template.html")

args = parser.parse_args()

FILE_NAME = args.input
TITLE = args.title
OUTPUT_NAME = args.output

try:
    os.system('npm install github-readme-to-html')
except:
    print("NPM is not Installed")
    print("Try : sudo apt install nodejs | sudo apt install npm ")

time.sleep(5)
print("Wait While The File is Converting")
time.sleep(15)

try:
    os.system(f'npx github-readme-to-html -i {FILE_NAME} -t {TITLE} -o {OUTPUT_NAME}')
except:
    print("Please Check If file is exit")