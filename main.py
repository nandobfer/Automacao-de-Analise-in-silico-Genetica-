from tabula import read_pdf
import PyPDF2, os
from Saida import *
from pathlib import Path

saida = Saida()
# file = filedialog.askopenfilename()
# print(read_pdf(file))
def getScore(file):
    with open(file, "rb") as pdf_file:
        read_pdf = PyPDF2.PdfFileReader(pdf_file)
        number_of_pages = read_pdf.getNumPages()
        page = read_pdf.pages[0]
        page_content = page.extractText()
    # print(page_content)
    score = ''
    for i in range(len(page_content)):
        if page_content[i] == 'S' and page_content[i+5] == ':':
            j = i + 6
            while not page_content[j] == '\n':
                # print(page_content[j])
                score += page_content[j]
                j += 1
                
    return str(score)

def getORF(file):
    pdf = read_pdf(file)
    table = pdf[0].values
    for j in range(len(table)):
        line = []
        for i in range(2, 8):
            value = str(table[j][i]).replace('-', '')
            value = value.replace(' ', '')
            line.append(value) 
        
        saida.addValues(getScore(file), line[0], line[1], line[2], line[3], line[4], line[5], j, file_name)
    saida.endFile()

path = 'data/'
dir_list = os.listdir(path)
for file in dir_list:
    file_name = Path('data/'+file).stem
    getORF('data/'+file)
    

saida.writeValues('saida.xlsx')
                