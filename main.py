import os


def dir_checker():
    """
    This function is used to check if the needed
    directories are already created
    """
    if not os.path.exists("_site"):
        os.mkdir("./_site")
    if not os.path.exists("_input-markdown-document-here"):
        os.mkdir("./_input-markdown-document-here")
        basefile = open("./_input-markdown-document-here/site_base.md","w",encoding="UTF-8")
        basefile.write("Please only write markdown and YAML here.")
        basefile.close()


def splitfile():
    """
    This function is used to open the given markdown
    file and splits it into the yaml part and the markdown
    part
    """
    sitemarkdown = open("./_input-markdown-document-here/site_base.md","r",encoding="UTF-8")
    smlines = sitemarkdown.read()
    try:
        yaml_end = smlines.index('---', 4) + 4

        frontmatter = smlines[:yaml_end]
        backmatter = smlines[yaml_end:]
    except ValueError:
        frontmatter = ''
        backmatter = ''

    return {'yaml':frontmatter,'md':backmatter}



if __name__ == "__main__":
    dir_checker()
