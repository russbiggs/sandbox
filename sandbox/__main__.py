import os
import subprocess
import sys
import tempfile

def clean_extension(ext):
    ext = ext.replace('.', '')
    ext = ext.lower()
    return ext

def main(arg = None):
    if arg is None:
        if len(sys.argv) > 1:
            ext = clean_extension(sys.argv[1])
            tempdir = tempfile.gettempdir()
            filepath = tempdir + '/sandbox-temp.' + ext
            if os.path.exists(filepath):
                os.remove(filepath)
            subprocess.call(['code', filepath], shell=True)
        else:
            print "no file extension given"
            exit()

if __name__ == '__main__':
    sys.exit(main() or 0)
