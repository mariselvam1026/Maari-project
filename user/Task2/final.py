import PyPDF2
mergeFile = PyPDF2.PdfFileMerger()

mergeFile.append(PyPDF2.PdfFileReader('book.pdf', 'rb'))

mergeFile.append(PyPDF2.PdfFileReader('book1.pdf', 'rb'))
mergeFile.append(PyPDF2.PdfFileReader('book2.pdf', 'rb'))
mergeFile.append(PyPDF2.PdfFileReader('book3.pdf', 'rb'))

mergeFile.write("NewMergedFile.pdf")