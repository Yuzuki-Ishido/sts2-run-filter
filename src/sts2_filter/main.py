import sys
import os
from dotenv import load_dotenv
from pathlib import Path
import json

from sts2_filter.models.run import Run


load_dotenv()

raw = os.getenv('SAVE_HISTORY_PATH')

if sys.platform == "linux":
    path = raw.replace('\\','/').replace('C:', '/mnt/c')
else:
    # Windows native
    path = raw

basePath = Path(path)

print(basePath)


# test file recording winning a10 silent shiv run
testFile = basePath / "1778537051.run"

def main():
    # run = Run()
    with open(testFile, encoding="utf-8") as infile:
        data = json.load(infile)

        run = Run.from_json(data)
        # run.set_seed(data)
        print("seed = |", run.seed, '|')
        print("acts = |", run.acts, '|')
        for act in run.acts:
            print(act, type(act))






# with open(testFile, "r") as infile, open("outfile.txt", "w") as outfile:
#     for line in infile:
#         outfile.write(line)



if __name__ == '__main__':
    main()