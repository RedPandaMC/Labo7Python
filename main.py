import os
import md2html as md2h
import json

def dir_checker():
    """
    This function is used to check if the needed
    directories are already created
    """
    if not os.path.exists("_site"):
        os.mkdir("./_site")
    if not os.path.exists("_input-markdown-document-here"):
        os.mkdir("./_input-markdown-document-here")
        basefile = open(
            "./_input-markdown-document-here/site_base.md", "w", encoding="UTF-8"
        )
        basefile.write("---\nDate: 01/01/2000\nTitle: Main\nAuthor: AuthorName\nTemplateName: Name\nPageType: PageType\n---\n# start typing\n")
        basefile.close()
        exit("Created directories, please rerun the script.")


def write_html_to_json():
    directory = os.getcwd() + '/_site'
    html_files = [filename for filename
                  in os.listdir(directory) 
                  if filename.endswith(".html")]
    with open('_site/data.json', 'w',encoding='UTF-8') as file:
        json.dump(html_files, file)


if __name__ == "__main__":
    dir_checker()
    md2h.md2html_converter()
    write_html_to_json()
