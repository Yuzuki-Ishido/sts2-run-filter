import sys
import os
from dotenv import load_dotenv
from pathlib import Path
import json

from sts2_filter.models.run import Run


def log(string):
    with open("outfile.txt", "a") as f:
        print(string, file=f)


load_dotenv()

raw = os.getenv('SAVE_HISTORY_PATH')

singleplayer = False

if singleplayer:
    test_file = os.getenv('TEST_SILENT_FILE_PATH')
else:
    test_file = os.getenv('TEST_MULTIPLAYER_FILE_PATH')

ROOT = Path(__file__).resolve().parents[2]

# if sys.platform == "linux":
#     path = raw.replace('\\','/').replace('C:', '/mnt/c')
# else:
#     # Windows native
#     path = raw

# basePath = Path(path)


# test file recording winning a10 silent shiv run
# test_file = basePath / "1778537051.run"


def main():
    open("outfile.txt", "w").close()
    with open(test_file, encoding="utf-8") as infile:
        data = json.load(infile)
        run = Run.from_json(data)
        log(run)

    

if __name__ == '__main__':
    main()