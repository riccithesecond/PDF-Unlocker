import os
import fitz  # PyMuPDF module

# Request file path including the file name
pdf_file_path = input("Enter the path to the PDF file: ")

# Check file path existance
if not os.path.exists(pdf_file_path):
    print("Error: The provided file path does not exist.")
    exit(1)

try:
    # Open PDF
    pdf_document = fitz.open(pdf_file_path)

    # Check if PDF is password-protected
    if pdf_document.isEncrypted:
        # Request password
        pdf_password = input("Enter the password for the PDF: ")
        try:
            pdf_document.authenticate(pdf_password)
        except Exception as e:
            print(f"Password authentication failed: {e}")
            exit(1)

    # Get the original file name without the extension
    file_name, file_extension = os.path.splitext(os.path.basename(pdf_file_path))

    # Generate new name for the unlocked PDF file
    output_pdf_path = f"{file_name}_UNLOCKED.pdf"

    # Create new PDF
    new_pdf = fitz.open()

    # Add all pages from the original PDF to the new PDF
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        new_pdf.insert_pdf(pdf_document, from_page=page_num, to_page=page_num)

    # Save new PDF with the "unlocked" file name
    new_pdf.save(output_pdf_path)
    new_pdf.close()

    # Close the original PDF document
    pdf_document.close()

    print(f"Unlocked PDF saved as '{output_pdf_path}'")

except Exception as e:
    print(f"An error occurred: {e}")


