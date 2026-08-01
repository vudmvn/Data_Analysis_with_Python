#!/usr/bin/env python3
"""
Script di chuyển toàn bộ ảnh lẻ từ `lectures/week-01-gioi-thieu-hoc-phan/` vào `images/`,
áp dụng quy tắc bảo vệ không ghi đè (Auto-rename) và cập nhật đường dẫn căn giữa trong các tệp .md.
"""

import os
import sys
import glob
import re
import shutil

def organize_images():
    week_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "lectures", "week-01-gioi-thieu-hoc-phan"))
    images_dir = os.path.join(week_dir, "images")
    os.makedirs(images_dir, exist_ok=True)

    loose_pngs = sorted(glob.glob(os.path.join(week_dir, "*.png")))
    
    file_mapping = {} # { old_basename: new_basename_in_images }

    for filepath in loose_pngs:
        basename = os.path.basename(filepath)
        dest_path = os.path.join(images_dir, basename)

        if os.path.exists(dest_path):
            # Tự động đổi tên để không ghi đè ảnh cũ
            name, ext = os.path.splitext(basename)
            counter = 1
            new_basename = f"{name}-v{counter}{ext}"
            new_dest_path = os.path.join(images_dir, new_basename)
            while os.path.exists(new_dest_path):
                counter += 1
                new_basename = f"{name}-v{counter}{ext}"
                new_dest_path = os.path.join(images_dir, new_basename)

            print(f"🔄 Trùng tên: '{basename}' -> Đổi tên thành '{new_basename}'")
            shutil.move(filepath, new_dest_path)
            file_mapping[basename] = new_basename
        else:
            print(f"📦 Di chuyển: '{basename}' -> 'images/{basename}'")
            shutil.move(filepath, dest_path)
            file_mapping[basename] = basename

    print("\n--- Đang cập nhật các tệp .md ---")
    md_files = glob.glob(os.path.join(week_dir, "*.md"))
    
    for md_file in md_files:
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()

        updated_content = content
        changes_made = False

        # 1. Cập nhật các link ảnh cũ chưa ở dạng images/
        for old_name, new_name in file_mapping.items():
            pattern = rf"!\[(.*?)\]\({re.escape(old_name)}\)"
            replacement = rf'<p align="center">\n  <img src="images/{new_name}" alt="\1" />\n</p>'
            if re.search(pattern, updated_content):
                updated_content = re.sub(pattern, replacement, updated_content)
                changes_made = True

        # 2. Cập nhật các link ảnh đã có cú pháp ![alt](images/filename.png) sang dạng <p align="center"> nếu chưa căn giữa
        pattern_already_images = r"(?<!<p align=\"center\">\n  )!\[(.*?)\]\(images/([^)]+)\)"
        def replace_images_markdown(match):
            alt_text = match.group(1) or "Hình ảnh minh họa"
            img_file = match.group(2)
            # Kiểm tra xem img_file có trong mapping không
            final_name = file_mapping.get(img_file, img_file)
            return f'<p align="center">\n  <img src="images/{final_name}" alt="{alt_text}" />\n</p>'

        if re.search(pattern_already_images, updated_content):
            updated_content = re.sub(pattern_already_images, replace_images_markdown, updated_content)
            changes_made = True

        if changes_made:
            with open(md_file, "w", encoding="utf-8") as f:
                f.write(updated_content)
            print(f"✅ Đã cập nhật tệp: {os.path.basename(md_file)}")

if __name__ == "__main__":
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    organize_images()
