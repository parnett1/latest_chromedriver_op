import datetime
import glob
import io

from logzero import logger


def new_version():
    start_token = '__version__ ='
    end_token = '\n'
    updated_version = f"{start_token} '{datetime.datetime.now().strftime('%Y.%m.%d')}'"
    for filename in glob.glob("**/*.py", recursive=True):
        if 'change_version.py' in filename:
            continue
        changed = False
        with io.open(filename, 'rt', encoding='utf-8') as f_obj:
            data = f_obj.read()

        start = data.find(start_token)
        if start > -1:
            changed = True
            end = data.find(end_token, start)
            data = data.replace(data[start:end], updated_version)

        if changed:
            logger.info(f"Writing: {filename}")
            with io.open(filename, 'wt', encoding='utf-8') as f_obj:
                f_obj.write(data)


if __name__ == '__main__':
    new_version()
