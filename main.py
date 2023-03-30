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

if __name__ == "__main__":
    dir_checker()
    open("./_input-markdown-document-here/site_base.md","w",encoding="UTF-8")
