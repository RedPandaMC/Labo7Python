import os
import shutil
import markdown
from jinja2 import Environment, FileSystemLoader


# region step (1)
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
# endregion
# region step (2)
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
    Copies specified files and moves them to directory _site, 
    along with home.html, style.css, reset.css, script.js 
    if not already present.
    """
    files = os.listdir("_site")
    index_exists = any(["home" in file.lower() for file in files])

    template = yaml_dic["TemplateName"].removesuffix(".html")
    html_files = get_html_files(template)
    source_file = f"_html-templates/{template}/{html_files[yaml_dic['PageType']]}"
    target_dir = "_site"
    shutil.copy2(source_file, target_dir)

    if not index_exists:
        shutil.copy2(f"_html-templates/{template}/home.html", target_dir)

    # Copy the CSS and JS files if they don't already exist in the _site directory
    css_files = ["style.css", "reset.css"]
    js_file = "script.js"
    for css_file in css_files:
        css_source_file = f"_html-templates/{template}/{css_file}"
        css_target_file = f"_site/{css_file}"
        if not os.path.isfile(css_target_file):
            shutil.copy2(css_source_file, css_target_file)
            
    js_source_file = f"_html-templates/{template}/{js_file}"
    js_target_file = f"_site/{js_file}"
    if not os.path.isfile(js_target_file):
        shutil.copy2(js_source_file, js_target_file)

# endregion
# region step (3)
def markdown2html(file_dic: dict):
    """
    Returns all html in specified file + added html from markdown
    """
    html = markdown.markdown(file_dic["md"])
    return html


# endregion
# region step (4)
def printer(full_dic: dict):
    """
    Prints the given markdown and yaml in a given file in _site
    """
    env = Environment(loader=FileSystemLoader("_site"))
    template = env.get_template(full_dic["PageType"] + ".html")
    output = template.render(data=full_dic)
    with open(f"_site/{full_dic['PageType']}.html", "w", encoding="UTF-8") as f:
        f.write(output)
    try:
        if 'post' not in full_dic['PageType']:
            os.rename(f"_site/{full_dic['PageType']}.html", f"_site/{full_dic['Title']}.html")
        else:
            os.rename(f"_site/{full_dic['PageType']}.html", f"_site/{full_dic['Title']}__{full_dic['Date'].replace('/','-')}.html")
    except FileExistsError:
        os.remove(f"_site/{full_dic['PageType']}.html")
        exit("Please change the title of your post in the markdown document.")
# endregion


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
    full_dic["Content"] = markdown2html(file_dic)
    printer(full_dic)
