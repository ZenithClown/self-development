# -*- encoding: utf-8 -*-

"""
A File to Automatically Update the `progress` Percentage

The `README.md` file is populated with a progress bar, and number of
solutions available in the directory. This code checks how many
solution files are available and updates the code.
"""

import os
import sys
import glob

def get_files(path : str, file_type : str) -> list:
    """
    Given a path and file type, checks and returns all
    the available file in the `path` and all its subdirectories.
    In addition, the code also tries to consider different
    styles of file names, however uniform `zfill(0)` is recommended.
    """

    path = os.path.join(path, "**", f"*.{file_type}")
    return glob.glob(path, recursive = True)


if __name__ == "__main__":
    ROOT = "."
    _, ftype = sys.argv
    
    # ! every week the total number of problem changes
    # let this be a constant for now, TODO create a pipeline
    TOTAL = 2489

    # get the count of total files available in the directory
    # currently try to implement with `.py` file, TODO generalize
    # ! ignore the current file as this is a automated pipeline script
    solved = len(get_files(ROOT, file_type = ftype)) - 1

    # calculate progress percentage
    progress = (solved * 100) // TOTAL

    # get the strings, and write them to the file
    progress_bar_l10 = f"![Solution Available: {float(progress)}%](https://progress-bar.dev/{progress}?title=progress)"
    progress_cnt_l11 = f"![Total Progress](https://img.shields.io/badge/progress-{solved}%20%2F%20{TOTAL}-ff69b4.svg)"

    with open("README.md", "r", encoding = "utf8") as f:
        lines = f.readlines()

    lines[9] = "  " + progress_bar_l10 + "\n"
    lines[10] = "  " + progress_cnt_l11 + "\n"

    with open("README.md", "w", encoding = "utf8") as f:
        f.writelines(lines)
