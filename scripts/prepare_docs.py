import os
import shutil

def prepare_docs():
    docs_dir = "docs"
    if os.path.exists(docs_dir):
        shutil.rmtree(docs_dir)
    os.makedirs(docs_dir, exist_ok=True)

    # Process README.md into docs/index.md (removing internal guideline links)
    if os.path.exists("README.md"):
        with open("README.md", "r", encoding="utf-8") as f:
            content = f.read()
        
        # Remove reference to QUY_TRINH_SOAN_BAI_GIANG.md and English version link for student site
        cleaned_content = content.replace("- ⚙️ **Quy trình soạn bài giảng & Quản lý ảnh:** Xem tệp [QUY_TRINH_SOAN_BAI_GIANG.md](QUY_TRINH_SOAN_BAI_GIANG.md)\n", "")
        cleaned_content = cleaned_content.replace("| [🇬🇧 English Version (README-en.md)](README-en.md)", "")
        
        with open(os.path.join(docs_dir, "index.md"), "w", encoding="utf-8") as f:
            f.write(cleaned_content)

    # Copy student-facing documentation
    if os.path.exists("syllabus-vn.md"):
        shutil.copy("syllabus-vn.md", os.path.join(docs_dir, "syllabus-vn.md"))

    # Copy lectures & javascripts directories
    if os.path.exists("lectures"):
        shutil.copytree("lectures", os.path.join(docs_dir, "lectures"))
    if os.path.exists("javascripts"):
        shutil.copytree("javascripts", os.path.join(docs_dir, "javascripts"))

    print("Docs folder prepared successfully for student site!")

if __name__ == "__main__":
    prepare_docs()
