import os

def dir_checker():
    """
    This function is used to check if the needed
    directories are already created and if not 
    they shall be created.
    """
    if not os.path.exists("_site"):
        os.mkdir("./_site")
    if not os.path.exists("_input-markdown-document-here"):
        os.mkdir("./_input-markdown-document-here")

if __name__ == "__main__":
    dir_checker()
