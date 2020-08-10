import os


#TODO from INI
import subprocess


def doxy_build():
    try:
        subprocess.run(['doxygen', '-v'], stdout=subprocess.PIPE)
    except OSError as e:
        print(e)
        print("Doxygen not installed or not in path. Cannot continue")
        return False
    else:
        if not os.path.isdir('output'):
            os.mkdir('output')
        if not os.path.isdir('output/doxygen'):
            os.mkdir('output/doxygen')
        subprocess.run(['doxygen', 'doxygen.conf'])
        return True


def sphinx_build():
    from sphinx.application import Sphinx
# Main arguments
    srcdir = "./"
    confdir = "./"
    builddir = os.path.join(srcdir, "output/")
    doctreedir = os.path.join(builddir, "doctrees/")
    builder = "html"
# Create the Sphinx application object
    app = Sphinx(srcdir, confdir, builddir, doctreedir, builder)
# Run the build
    app.build()
