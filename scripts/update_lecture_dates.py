import os
import re

def update_lecture_dates():
    lectures_dir = "lectures"
    vn_date_str = "**Cập nhật lần cuối:** 2 tháng 8 năm 2026"
    en_date_str = "**Last updated:** August 2, 2026"

    count = 0
    for root, dirs, files in os.walk(lectures_dir):
        for file in files:
            if file.endswith(".md") and file != "README.md" and file != "slides.md":
                filepath = os.path.join(root, file)
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()

                if file.endswith("-en.md"):
                    # Replace English Last updated line
                    new_content = re.sub(r"\*\*Last updated:\*\*.*", en_date_str, content)
                else:
                    # Replace Vietnamese Cập nhật lần cuối line
                    new_content = re.sub(r"\*\*Cập nhật lần cuối:\*\*.*", vn_date_str, content)

                if new_content != content:
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"Updated date in: {filepath}")
                    count += 1

    print(f"Finished updating {count} lecture files.")

if __name__ == "__main__":
    update_lecture_dates()
