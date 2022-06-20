import os

import auto_chromedriver


def demo():
    # Path test
    auto_chromedriver.safely_set_chromedriver_path()
    print("\nThe Path would be transformed to:")
    print(os.environ['PATH'])


if __name__ == '__main__':
    demo()
