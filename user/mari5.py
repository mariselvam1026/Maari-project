from weasyprint import HTML
def makepdf(html):
#"""Generate a PDF file from a string of HTML."""
    htmldoc = HTML(string=html, base_url="file:///D:/user/Table.html")
    return htmldoc.write_pdf()