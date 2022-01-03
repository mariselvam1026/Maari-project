import PyPDF2
mergeFile = PyPDF2.PdfFileMerger()


mergeFile.append(PyPDF2.PdfFileReader('string1.pdf', 'rb'))
mergeFile.append(PyPDF2.PdfFileReader('string2.pdf', 'rb'))

mergeFile.write("NewMergedFile.pdf")