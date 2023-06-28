from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import BytesIO


def extract_text(pdf_file):
    resource_manager = PDFResourceManager()
    output_string = StringIO()
    laparams = LAParams()
    device = TextConverter(resource_manager, output_string, laparams=laparams)
    interpreter = PDFPageInterpreter(resource_manager, device)

    # create a BytesIO object to read the file
    pdf_data = BytesIO(pdf_file.read())

    for page in PDFPage.get_pages(pdf_data):
        interpreter.process_page(page)

    device.close()
    text = output_string.getvalue()
    output_string.close()

    return text
