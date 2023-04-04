import os
import shutil
import markdown

from jinja2 import Environment, FileSystemLoader

#region step (1)
def splitfile():
    """
    This function is used to open the given markdown
    file and splits it into the yaml part and the markdown
    part
    """
    sitemarkdown = open(
        "./_input-markdown-document-here/site_base.md", "r", encoding="UTF-8"
    )
    smlines = sitemarkdown.read()
    try:
        yaml_end = smlines.index("---", 1)
        frontmatter = smlines[3:yaml_end]
        backmatter = smlines[yaml_end + 3 :]
    except ValueError:
        yaml_end = 0
        frontmatter = ""
        backmatter = smlines[yaml_end:]
        print("No yaml found in markdown document")
    frontmatter = frontmatter.replace("\n", ",").removeprefix(",").removesuffix(",")
    return {"yaml": frontmatter, "md": backmatter}
#endregion
#region step (2)
def string_to_dict(string: str):
    """
    This function turns a yaml string into a yaml dictionary
    """
    pairs = string.split(",")
    dire = {}
    for pair in pairs:
        key, value = pair.split(":")
        key = key.strip()
        value = value.strip().lower()
        dire[key] = value
    return dire


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
    Copies a specified file and moves it to directory _site, if it doesn't exist
    """
    if not os.path.isfile(os.path.join("_site", yaml_dic["PageType"] + ".html")):
        template = yaml_dic["TemplateName"].removesuffix(".html")
        html_files = get_html_files(template_name=template)

        source_file = f"_html-templates/{template}/{html_files[yaml_dic['PageType']]}"
        target_dir = "_site"
        shutil.copy2(source_file, target_dir)
#endregion
#region step (3)
def markdown2html(file_dic: dict):
    """
    Returns all html in specified file + added html from markdown
    """
    html = markdown.markdown(file_dic["md"])
    return html
#endregion
#region step (4)
def printer(full_dic: dict):
    """
    Prints the given markdown and yaml in a given file in _site
    """
    env = Environment(loader=FileSystemLoader("_site"))
    template = env.get_template(full_dic['PageType'] + ".html")
    output = template.render(data=full_dic)
    with open(f"_site/{full_dic['PageType']}.html", "w", encoding="UTF-8") as f:
        f.write(output)
#endregion

def md2html_converter():
    """
    Main function for converting markdown + yaml -> html
    """
    file_dic = splitfile()
    yaml_dic = string_to_dict(file_dic["yaml"])

    template = yaml_dic["TemplateName"].removesuffix(".html")
    templates = get_template_names()
    if template not in templates:
        exit("Template doesn't exist in _html-templates")
    cp_mv_specifiedfile(yaml_dic)

    full_dic = yaml_dic
    full_dic["content"] = markdown2html(file_dic)
    printer(full_dic)
