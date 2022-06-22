import os 
import time

FILE_NAME = ""
TITLE = ""
OUTPUT_NAME = ""

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