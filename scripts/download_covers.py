import os
import urllib.request

def download_covers():
    assets_dir = "assets/images"
    os.makedirs(assets_dir, exist_ok=True)
    
    books = {
        "python-data-analysis-3rd-cover.jpg": "https://static.packt-cdn.com/products/9781800564480/cover/smaller",
        "python-data-analysis-1st-cover.jpg": "https://static.packt-cdn.com/products/9781783552030/cover/smaller",
        "data-science-marketing-analytics-cover.jpg": "https://static.packt-cdn.com/products/9781800560475/cover/smaller",
        "data-analysis-business-economics-cover.jpg": "https://covers.openlibrary.org/b/isbn/9781108716208-M.jpg",
        "python-for-data-science-dummies-cover.jpg": "https://covers.openlibrary.org/b/isbn/9781119547624-M.jpg"
    }

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    for filename, url in books.items():
        filepath = os.path.join(assets_dir, filename)
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
                out_file.write(response.read())
            print(f"Downloaded {filename}: {os.path.getsize(filepath)} bytes")
        except Exception as e:
            print(f"Failed to download {filename}: {e}")

if __name__ == "__main__":
    download_covers()
