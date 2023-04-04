import os
import yaml2html as y2h


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
        basefile.write(
        """---\nDate: 01/01/2000\n\
Title: Main\nAuthor: AuthorName\nTemplateName: Name\nPageType: PageType\n---
        \n# start typing\n"""
        )
        basefile.close()
        exit("Created directories, please rerun the script.")


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
    backmatter = backmatter.replace("\n", "")
    return {"yaml": frontmatter, "md": backmatter}


if __name__ == "__main__":
    dir_checker()
    file_dic = splitfile()
    y2h.yaml2html_converter(file_dic["yaml"])