import os
import shutil


def string_to_dict(string: str):
    """
    This function turns a yaml string into a yaml dictionary
    """
    pairs = string.split(",")
    dir = {}
    for pair in pairs:
        key, value = pair.split(":")
        key = key.strip()
        value = value.strip().lower()
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


def cp_mv_specifiedfile(yaml_dic: dict):
    """
    Copies a specified file and moves it to directory _site
    """
    template = yaml_dic["TemplateName"].removesuffix(".html")
    html_files = get_html_files(template_name=template)

    source_file = f"_html-templates/{template}/{html_files[yaml_dic['PageType']]}"
    target_dir = "_site"
    shutil.copy2(source_file, target_dir)


# just in case the user writes something like templatename.html in frontmatter
def yaml2html_converter(yaml: str):
    """
    Converts yaml to html
    """
    yaml_dic = string_to_dict(yaml)
    template = yaml_dic["TemplateName"].removesuffix(".html")
    templates = get_template_names()
    if template not in templates:
        exit("Template doesn't exist in _html-templates")
    cp_mv_specifiedfile(yaml_dic)
