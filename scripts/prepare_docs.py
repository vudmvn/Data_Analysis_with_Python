import os
import shutil

def prepare_docs():
    docs_dir = "docs"
    if os.path.exists(docs_dir):
        shutil.rmtree(docs_dir)
    os.makedirs(docs_dir, exist_ok=True)

    # Copy root markdown files
    if os.path.exists("README.md"):
        shutil.copy("README.md", os.path.join(docs_dir, "index.md"))
    if os.path.exists("syllabus-vn.md"):
        shutil.copy("syllabus-vn.md", os.path.join(docs_dir, "syllabus-vn.md"))
    if os.path.exists("QUY_TRINH_SOAN_BAI_GIANG.md"):
        shutil.copy("QUY_TRINH_SOAN_BAI_GIANG.md", os.path.join(docs_dir, "QUY_TRINH_SOAN_BAI_GIANG.md"))
    if os.path.exists("README-en.md"):
        shutil.copy("README-en.md", os.path.join(docs_dir, "README-en.md"))

    # Copy directories
    if os.path.exists("lectures"):
        shutil.copytree("lectures", os.path.join(docs_dir, "lectures"))
    if os.path.exists("javascripts"):
        shutil.copytree("javascripts", os.path.join(docs_dir, "javascripts"))

    print("Docs folder prepared successfully!")

if __name__ == "__main__":
    prepare_docs()
