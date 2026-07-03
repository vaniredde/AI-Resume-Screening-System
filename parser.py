from PyPDF2 import PdfReader

def extract_text(f):
 r=PdfReader(f);return '\n'.join((p.extract_text() or '') for p in r.pages)