# PDF to HTML (or TXT - commented out) formats with pdfminer.six

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
#from pdfminer.converter import TextConverter
from pdfminer.converter import HTMLConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO, BytesIO
#import regex
import csv, re, os, sys
from timeit import default_timer as timer
import datetime as dt
#import multiprocessing

def readPDF(pdfFile):
    rsrcmgr = PDFResourceManager()
    #retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    #device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)

    output = BytesIO()
    print("stage1")
    converter = HTMLConverter(rsrcmgr, output, codec=codec, laparams=LAParams())

    interpreter = PDFPageInterpreter(rsrcmgr, converter)
    print("stage2")
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    for page in PDFPage.get_pages(pdfFile, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)
    converter.close()
    print("stage3")
    #textstr = retstr.getvalue()
    convertedPDF = output.getvalue()
    print("stage4")
    #retstr.close()
    output.close()
    #device.close()
    return convertedPDF
    #return textstr


if __name__ == "__main__":
    path1 = "U:\\pdfs\\"
    path2 = "U:\\pdfs\\dir\\"
    
## data = list(csv.DictReader(open("U:\\pdfs\\doc_list.csv", "r", encoding="UTF-8", errors="ignore")))    
##    doc_list = []
##    for row in data:
##        doc = row['FILE'].strip()
##        docs = doc + '.pdf'
##        doc_list.append(docs)

    doc_list = ['_cr15178.pdf']
    
    for doc in doc_list:
        print("working with doc: {}".format(doc))
        fileHTML = doc.replace('pdf','html')
        path1 = path1 + doc
        
        scrape = open(path1, 'rb')
        pdfFile = BytesIO(scrape.read())
        convertedPDF = readPDF(pdfFile)
        path2 = path2 + fileHTML
        fileConverted = open(path2, "wb")
        fileConverted.write(convertedPDF)
        fileConverted.close()
        print("Done with file {}".format(fileHTML))
        
