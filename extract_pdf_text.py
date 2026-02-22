import fitz  # PyMuPDF

def extract_text_from_pages(pdf_path, start_page, end_page):
    """Extract text from specific pages of a PDF."""
    doc = fitz.open(pdf_path)

    text_by_page = {}
    for page_num in range(start_page - 1, end_page):
        if page_num < len(doc):
            page = doc[page_num]
            text = page.get_text()
            text_by_page[page_num + 1] = text
            print(f"\n{'='*60}")
            print(f"PAGE {page_num + 1}")
            print(f"{'='*60}")
            print(text[:2000])  # Print first 2000 chars
            print("..." if len(text) > 2000 else "")

    doc.close()
    return text_by_page

if __name__ == "__main__":
    pdf_path = "./data/input/Pan-cancer scRNA-seq recurring programs cellular heterogeneity Kinker 2020.pdf"
    text_data = extract_text_from_pages(pdf_path, 1, 2)

    # Save full text
    with open("first_two_pages.txt", "w") as f:
        for page_num, text in text_data.items():
            f.write(f"\n{'='*60}\n")
            f.write(f"PAGE {page_num}\n")
            f.write(f"{'='*60}\n")
            f.write(text)

    print("\n[INFO] Saved to first_two_pages.txt")
