#!/usr/bin/env python3
"""
Script tự động quét các bài giảng trong `lectures/`, cập nhật Mục lục ở root `README.md`,
và thực hiện commit + push bài giảng lên GitHub.

Cách dùng:
    python scripts/publish_lecture.py --message "Cập nhật bài giảng Tuần 01"
"""

import os
import sys
import re
import argparse
import subprocess

def update_readme_toc():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    lectures_dir = os.path.join(root_dir, "lectures")
    readme_path = os.path.join(root_dir, "README.md")

    if not os.path.exists(lectures_dir):
        print("Chưa có thư mục lectures/")
        return

    lecture_folders = sorted(os.listdir(lectures_dir))

    toc_lines = [
        "## 📚 Danh sách Bài giảng & Tài liệu Thực hành\n",
        "| Tuần | Chủ đề | Bài giảng (.ipynb) | Slide | Bài tập Lab | Đáp án |",
        "|:---:|:---|:---:|:---:|:---:|:---:|"
    ]

    for folder in lecture_folders:
        folder_path = os.path.join(lectures_dir, folder)
        if os.path.isdir(folder_path) and folder.startswith("week-"):
            parts = folder.split("-", 2)
            week_num = parts[1] if len(parts) > 1 else "??"
            
            # Đọc tiêu đề từ README.md của tuần đó
            week_readme = os.path.join(folder_path, "README.md")
            title = folder
            if os.path.exists(week_readme):
                with open(week_readme, "r", encoding="utf-8") as f:
                    first_line = f.readline()
                    if first_line.startswith("# Tuần"):
                        title_parts = first_line.replace("# Tuần", "").strip().split(":", 1)
                        if len(title_parts) > 1:
                            title = title_parts[1].strip()

            rel_path = f"lectures/{folder}"
            ipynb_link = f"[📘 Notebook]({rel_path}/lecture.ipynb)"
            slides_link = f"[📊 Slides]({rel_path}/slides.md)"
            exercise_link = f"[💻 Lab]({rel_path}/lab_exercise.ipynb)"
            solution_link = f"[🔑 Đáp án]({rel_path}/lab_solution.ipynb)"

            toc_lines.append(f"| **{week_num}** | **{title}** | {ipynb_link} | {slides_link} | {exercise_link} | {solution_link} |")

    toc_content = "\n".join(toc_lines) + "\n\n"

    # Đọc README.md hiện tại
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Thay thế hoặc chèn mục lục
        if "## 📚 Danh sách Bài giảng" in content:
            new_content = re.sub(
                r"## 📚 Danh sách Bài giảng.*?(?=\n## |$)",
                toc_content.strip(),
                content,
                flags=re.DOTALL
            )
        else:
            new_content = content + "\n\n" + toc_content

        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Đã cập nhật mục lục bài giảng vào README.md!")

def run_git_publish(message):
    print("Đang đẩy dữ liệu lên GitHub...")
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", message], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("🎉 Đã xuất bản bài giảng lên GitHub thành công!")
    except subprocess.CalledProcessError as e:
        print(f"⚠️ Lỗi khi xuất bản bằng git: {e}")

if __name__ == "__main__":
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')

    parser = argparse.ArgumentParser(description="Cập nhật mục lục và đẩy bài giảng lên GitHub.")
    parser.add_argument("--message", "-m", default="feat(lecture): Cập nhật tài liệu bài giảng", help="Nội dung commit message")
    parser.add_argument("--no-push", action="store_true", help="Chỉ cập nhật README.md, không git commit & push")
    args = parser.parse_args()

    update_readme_toc()

    if not args.no_push:
        run_git_publish(args.message)
