import os
import shutil
import subprocess
from functools import cache

from logzero import logger

CHROME_EXECUTABLE = "chrome.exe"


def _get_program_files():
    for env_name in ["ProgramW6432", "ProgramFiles(x86)"]:
        folder = os.environ[env_name]
        logger.debug(f"Searching in: {folder}")
        if folder:
            yield folder


def _is_exe(fpath):
    return os.path.exists(fpath) and os.access(fpath, os.X_OK) and os.path.isfile(fpath)


@cache
def get_path():
    logger.debug("Searching for Google Chrome installations...")
    search_filename = CHROME_EXECUTABLE.casefold().strip()
    in_path = shutil.which(CHROME_EXECUTABLE)
    if in_path:
        return in_path
    for folder in _get_program_files():
        for root, dirs, files in os.walk(folder):
            for filename in files:
                if filename.casefold() == search_filename:
                    filepath = os.path.join(root, filename)
                    if _is_exe(filepath):
                        return filepath
    return None


@cache
def get_version():
    chrome_path = get_path()
    output = subprocess.check_output(
        'powershell -command "&{(Get-Item \'%s\').VersionInfo.ProductVersion}"' % (chrome_path), shell=True)
    version = output.decode(encoding='ascii').strip()
    logger.debug(f"Google Chrome Version: {version}")
    return version