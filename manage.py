from utils import main, new_content
from pprint import pprint
import sys


try:
    command = sys.argv[1]
    if command == "build":
        pprint("If you build it, they will come...")
        if __name__ == "__main__":
            main()
        pprint("Build complete!")
    elif command == "new":
        pprint("Finding a perfect blank slate...")
        new_content()
        pprint('Voila! Start writin\'!')
    else:
        print("Usage:")
        print("     | Rebuild site: python manage.py build")
        print("     | Create new page: python manage.py new")
except IndexError:
    pprint("Oops, no argument found! Try 'build' to generate site or 'new' to make a new content file.", width=50)