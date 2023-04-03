import os


def string_to_dict(string: str):
    """
    This function turns a yaml string into a yaml dictionary
    """
    pairs = string.split(",")
    dir = {}
    for pair in pairs:
        key, value = pair.split(":")
        key = key.strip()
        value = value.strip()
        dir[key] = value
    return dir


def get_html_files(template_name: str):
    """
    This function gives returns a dictionary with all
    our html files in a given template group
    """
    html_files = {}
    for file in os.listdir(f"_html-templates/{template_name}"):
        if file.endswith(".html"):
            file_name = file.removesuffix(".html")
            html_files[file_name] = file
    return html_files

def get_template_names():
    """
    This function gives returns a list of all of our templates
    """
    html_files = []
    for directory in os.listdir("_html-templates"):
        if os.path.isdir(os.path.join("_html-templates", directory)):
            html_files.append(directory)
    return html_files

# just in case the user writes something like templatename.html in frontmatter
def yaml2html_converter(yaml: str):
    """
    Converts yaml to html
    """
    yaml_dic = string_to_dict(yaml)
    templates = get_template_names()
    if yaml_dic["Template"].removesuffix(".html") not in templates:
        exit("Template doesn't exist in _html-templates")
    html_files = get_html_files(yaml_dic["Template"].removesuffix(".html"))
    # get the specified page in the yaml_dic then paste
    # the front matter in a copy of the html file
    # from _html-templates in _site 
