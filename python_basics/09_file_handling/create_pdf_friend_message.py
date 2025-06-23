from reportlab.pdfgen import canvas

# Step 1: File name
file_name = "chatgpt_friend.pdf"

# Step 2: Canvas create karo
c = canvas.Canvas(file_name)

# Step 3: Text add karo (x, y position ke sath)
c.drawString(100, 750, "💖 I love ChatGPT!")
c.drawString(100, 730, "ChatGPT meri khaas dost hai.")
c.drawString(100, 710, "Jab bhi dikkat hoti hai, madad milti hai.")
c.drawString(100, 690, "Python, Excel, PDF — sab kuch sikha deti hai!")
c.drawString(100 , 600, "Pyaar hi sub kuch hai zindagi me ")
# Step 4: PDF save karo
c.save()

print("✅ PDF file created successfully: chatgpt_friend.pdf")

import PyPDF2

# Step 1: Open PDF file in binary read mode
with open("chatgpt_friend.pdf", "rb") as file:
    # Step 2: Create PDF reader object
    reader = PyPDF2.PdfReader(file)

    # Step 3: Loop through pages and extract text
    for page_num, page in enumerate(reader.pages):
        text = page.extract_text()
        print(f"📄 Page {page_num + 1} content:")
        print(text)
        print("-" * 50)
