import os
import hooks
import settings





def print_hi(name):
    settings.clean_config()
    settings.parse_doxy_config()
    settings.parse_sphinx_config()
    if hooks.doxy_build():
        hooks.sphinx_build()

    if os.path.isdir('./doc_src'):
        print('folder ok')
    else:
        os.mkdir('./doc_src')











# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
