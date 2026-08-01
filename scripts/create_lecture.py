#!/usr/bin/env python3
"""
Script tự động khởi tạo cấu trúc bài giảng theo tuần cho môn Phân tích dữ liệu với Python (DSAI1005).
Cách dùng:
    python scripts/create_lecture.py --week 1 --title "Giới thiệu học phần"
"""

import os
import sys
import json
import argparse
import re

def slugify(text):
    text = text.lower().strip()
    # Chuyển ký tự tiếng Việt đơn giản sang không dấu để làm tên thư mục
    vietnamese_map = {
        'à':'a', 'á':'a', 'ả':'a', 'ã':'a', 'ạ':'a', 'ă':'a', 'ằ':'a', 'ắ':'a', 'ẳ':'a', 'ẵ':'a', 'ặ':'a',
        'â':'a', 'ầ':'a', 'ấ':'a', 'ẩ':'a', 'ẫ':'a', 'ậ':'a', 'đ':'d', 'è':'e', 'é':'e', 'ẻ':'e', 'ẽ':'e', 'ẹ':'e',
        'ê':'e', 'ề':'e', 'ế':'e', 'ể':'e', 'ễ':'e', 'ệ':'e', 'ì':'i', 'í':'i', 'ỉ':'i', 'ĩ':'i', 'ị':'i',
        'ò':'o', 'ó':'o', 'ỏ':'o', 'õ':'o', 'ọ':'o', 'ô':'o', 'ồ':'o', 'ố':'o', 'ổ':'o', 'ỗ':'o', 'ộ':'o',
        'ơ':'o', 'ờ':'o', 'ớ':'o', 'ở':'o', 'ỡ':'o', 'ợ':'o', 'ù':'u', 'ú':'u', 'ủ':'u', 'ũ':'u', 'ụ':'u',
        'ư':'u', 'ừ':'u', 'ứ':'u', 'ử':'u', 'ữ':'u', 'ự':'u', 'ỳ':'y', 'ý':'y', 'ỷ':'y', 'ỹ':'y', 'ỵ':'y'
    }
    for char, replacement in vietnamese_map.items():
        text = text.replace(char, replacement)
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def make_notebook(cells):
    return {
        "cells": cells,
        "metadata": {
            "language_info": {
                "name": "python",
                "version": "3.10"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 2
    }

def create_lecture(week, title):
    week_str = f"{int(week):02d}"
    folder_slug = f"week-{week_str}-{slugify(title)}"
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "lectures", folder_slug))
    data_dir = os.path.join(base_dir, "data")
    images_dir = os.path.join(base_dir, "images")

    os.makedirs(data_dir, exist_ok=True)
    os.makedirs(images_dir, exist_ok=True)

    # 1. Tạo README.md trong thư mục tuần
    readme_content = f"""# Tuần {week_str}: {title}

## 🎯 Mục tiêu bài học
- Nắm vững kiến thức lý thuyết cốt lõi về **{title}**.
- Áp dụng các thư viện Python chuyên dụng vào bài toán thực tế.
- Thực hành xây dựng và chạy mã nguồn phân tích dữ liệu.

## 📁 Cấu trúc thư mục
- `lecture.ipynb`: Notebook bài giảng chi tiết (Lý thuyết + Minh họa Code).
- `slides.md`: Slide bài giảng dạng Markdown (Marp format).
- `lab_exercise.ipynb`: Bài tập thực hành dành cho sinh viên.
- `lab_solution.ipynb`: Đáp án bài tập thực hành.
- `data/`: Thư mục chứa tệp dữ liệu phục vụ bài học.

## 🚀 Hướng dẫn học tập
1. Đọc tệp `slides.md` hoặc xem `lecture.ipynb`.
2. Chạy từng cell code trong `lecture.ipynb` để hiểu cơ chế hoạt động.
3. Tự làm bài tập trong `lab_exercise.ipynb` trước khi đối chiếu với `lab_solution.ipynb`.
"""
    with open(os.path.join(base_dir, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme_content)

    # 2. Tạo slides.md (Marp Format)
    slides_content = f"""---
marp: true
theme: default
paginate: true
header: 'DSAI1005 - Phân tích dữ liệu với Python | TS. Vũ Đức Minh'
footer: 'Tuần {week_str}: {title}'
---

# Tuần {week_str}: {title}

**Học phần:** DSAI1005 – Phân tích dữ liệu với Python  
**Giảng viên:** TS. Vũ Đức Minh  
**Khoa:** Khoa học dữ liệu & Trí tuệ nhân tạo (NEU)

---

## 📌 Nội dung chính

1. Giới thiệu tổng quan
2. Các khái niệm & Lý thuyết cốt lõi
3. Minh họa tính toán & Code mẫu
4. Tổng kết & Bài tập thực hành

---

## 1. Giới thiệu tổng quan

- Đặt vấn đề trong phân tích dữ liệu thực tế (Kinh doanh, Tài chính, E-commerce).
- Vai trò của **{title}** trong quy trình Data Science.

---

## 2. Bài tập thực hành (Lab)

- Yêu cầu sinh viên mở file `lab_exercise.ipynb` để làm bài tập tuần này.
"""
    with open(os.path.join(base_dir, "slides.md"), "w", encoding="utf-8") as f:
        f.write(slides_content)

    # 3. Tạo lecture.ipynb
    lecture_cells = [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                f"# Bài giảng Tuần {week_str}: {title}\n",
                "**Học phần:** DSAI1005 - Phân tích dữ liệu với Python  \n",
                "**Giảng viên:** TS. Vũ Đức Minh (NEU)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 1. Khai báo các thư viện cần thiết"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "import numpy as np\n",
                "import pandas as pd\n",
                "import matplotlib.pyplot as plt\n",
                "import seaborn as sns\n",
                "\n",
                "# Cấu hình hiển thị đồ họa\n",
                "sns.set_theme(style='whitegrid')\n",
                "print('Đã nạp các thư viện thành công!')"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 2. Nội dung minh họa & Ví dụ mã nguồn"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# TODO: Nhập mã nguồn ví dụ tại đây\n"
            ]
        }
    ]
    with open(os.path.join(base_dir, "lecture.ipynb"), "w", encoding="utf-8") as f:
        json.dump(make_notebook(lecture_cells), f, ensure_ascii=False, indent=2)

    # 4. Tạo lab_exercise.ipynb
    lab_cells = [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                f"# Bài tập Thực hành Tuần {week_str}: {title}\n",
                "**Yêu cầu:** Sinh viên hoàn thành các bài tập bên dưới và nộp file `.ipynb` theo quy định."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Bài 1: Chuẩn bị dữ liệu và Tính toán cơ bản\n",
                "Viết code Python để thực hiện yêu cầu..."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# CODE CỦA SINH VIÊN TẠI ĐÂY\n"
            ]
        }
    ]
    with open(os.path.join(base_dir, "lab_exercise.ipynb"), "w", encoding="utf-8") as f:
        json.dump(make_notebook(lab_cells), f, ensure_ascii=False, indent=2)

    # 5. Tạo lab_solution.ipynb
    solution_cells = [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                f"# Đáp án Bài tập Thực hành Tuần {week_str}: {title}\n",
                "*(Dành cho Giảng viên/Trợ giảng đối chiếu)*"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Bài 1: Đáp án"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Lời giải chi tiết mẫu\n"
            ]
        }
    ]
    with open(os.path.join(base_dir, "lab_solution.ipynb"), "w", encoding="utf-8") as f:
        json.dump(make_notebook(solution_cells), f, ensure_ascii=False, indent=2)

    print(f"✅ Đã tạo thành công thư mục bài giảng: lectures/{folder_slug}")

if __name__ == "__main__":
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(description="Tạo cấu trúc bài giảng mới.")
    parser.add_argument("--week", required=True, help="Số tuần (vd: 1, 2, 3...)")
    parser.add_argument("--title", required=True, help="Tên chủ đề bài giảng")
    args = parser.parse_args()

    create_lecture(args.week, args.title)

