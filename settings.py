import os

from configparser import RawConfigParser
main_conf_parser = RawConfigParser()
main_conf_parser.optionxform = str
try:
    main_conf_parser.read('alveolus-config.ini')
    proj_name = main_conf_parser['PROJECT']['name']
    proj_version = main_conf_parser['PROJECT']['version']
    proj_src_input = main_conf_parser['CONFIG_DIRECTORIES']['src_code']
    proj_exclude = main_conf_parser['CONFIG_DIRECTORIES']['exclude']
    proj_output = main_conf_parser['CONFIG_DIRECTORIES']['output']
    proj_api = main_conf_parser['CONFIG_DIRECTORIES']['src_api']
except Exception as e:
    print("alveolus-config.ini encountered a problem")
    print(e)


def parse_doxy_config():
    doxy_parser = RawConfigParser()
    doxy_parser.optionxform = str
    with open("./tools/doxygen.conf.in") as stream:
        doxy_parser.read_string("[DEFAULT]\n" + stream.read())
        doxy_parser.set('DEFAULT', 'PROJECT_NAME', proj_name)
        doxy_parser.set('DEFAULT', 'PROJECT_NUMBER', proj_version)
        doxy_parser.set('DEFAULT', 'OUTPUT_DIRECTORY', proj_output + "/doxygen")
        doxy_parser.set('DEFAULT', 'INPUT', proj_src_input)
        doxy_parser.set('DEFAULT', 'EXCLUDE', proj_exclude)
    with open('./doxygen.conf', 'w') as doxyfile:
        doxy_parser.write(doxyfile)
    print("Doxygen Config file created")


def _delete_files_safe_(files):
    for file in files:
        if os.path.isfile(file):
            os.remove(file)


def _delete_dirs_safe_(dirs):
    for dir in dirs:
     if os.path.isdir(dir):
        os.system("rm -rf "+dir)


def clean_config():
    _delete_dirs_safe_([os.path.join(*[proj_api, "doxygen_src"]), "output"])
    _delete_files_safe_(['index.rst', 'doxygen.conf', 'Makefile', 'make.bat'])

#TODO add custom rsts
def parse_sphinx_config():
    proj_rsts = ""
    for file in os.listdir(proj_api):
        if file.endswith(".rst"):
            proj_rsts += os.path.join(proj_api, file) + '/\n'
    proj_rsts += os.path.join(*[proj_api, "doxygen_src", "library_root"])

    with open("./tools/index.rst.in", "rt") as sphinxMakefile:
        with open("./index.rst", "wt") as parsed_makefile:
            new_index = sphinxMakefile.read()
            new_index = new_index.replace("@Title", proj_name)
            new_index = new_index.replace("@toctree_depth", "1")
            new_index = new_index.replace("@MainDescription", "")
            if proj_rsts is not None:
                new_index = new_index.replace("@toctree_include", proj_rsts)
            else:
                new_index.replace("@toctree_include", " ")
            parsed_makefile.write(new_index)

    with open("./tools/Makefile.in", "rt") as sphinxMakefile:
        with open("./Makefile", "wt") as parsed_makefile:
            new_index = sphinxMakefile.read() \
                .replace("@source", proj_api) \
                .replace("@output", proj_output) \
                .replace("@exhale", proj_api + "/doxygen_src")
            parsed_makefile.write(new_index)

    # IF WINDOWS
    # with open("./tools/make.bat.in", "rt") as sphinxbat:
    #     with open("./make.bat", "wt") as parsed_bat:
    #         new_index = sphinxMakefile.read() \
    #             .replace("@source", proj_api) \
    #             .replace("@output", proj_output) \
    #         parsed_makefile.write(new_index)
    #
    # print("doxygen config file created")
