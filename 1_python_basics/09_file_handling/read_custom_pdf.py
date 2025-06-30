import PyPDF2

filename = "Python-Notes.pdf"

with open(filename, "rb") as file:
    reader = PyPDF2.PdfReader(file)

    for page_num, page in enumerate(reader.pages):
        text = page.extract_text()
        print(f"📄 Page {page_num + 1} content:")
        print(text)
        print("-" * 50)
 