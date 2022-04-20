from tokenize import Number
from tabula import read_pdf
import PyPDF2, os
from Saida import *
from pathlib import Path

valid = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
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

# def getORF(file):
#     pdf = read_pdf(file, pages=1)
#     table = pdf[0].values
#     for j in range(len(table)):
#         line = []
#         for i in range(2, 8):
#             value = str(table[j][i]).replace('-', '')
#             value = value.replace(' ', '')
#             line.append(value) 
        
#         saida.addValues(getScore(file), line[0], line[1], line[2], line[3], line[4], line[5], j, file_name)
#     saida.endFile()
#     return True

def getORF(file):
    with open(file, "rb") as pdf_file:
        read_pdf = PyPDF2.PdfFileReader(pdf_file)
        number_of_pages = read_pdf.getNumPages()
        page = read_pdf.pages[0]
        page_content = page.extractText()
    # print(page_content)
    # extracting lines
    line = []
    counter = 1
    for i in range(len(page_content)):
        if page_content[i] == '1' and page_content[i+2] == '+' and page_content[i+7] == f'{counter}':
            line.append('')
            j = i + 8
            while not page_content[j] == '\n':
                # print(page_content[j])
                line[counter-1] += page_content[j]
                j += 1
            else:
                counter += 1
    
    # parsing lines
    number = ''
    data = []
    new_line = []
    for string in line:
        valid_flag = False
        for char in string:
            if char in valid:
                number += char
                valid_flag = True
            else:
                if valid_flag:
                    new_line.append(number)
                    number = ''
                valid_flag = False
                
        new_line.append(number)
        number = ''
        data.append(new_line)
        # send new line to OUT
        saida.addValues(getScore(file), new_line[0], new_line[1], new_line[2], new_line[3], new_line[4], new_line[5], data.index(new_line), file_name)
        new_line = []
        
    saida.endFile()
    # print(data)

path = 'data/'
dir_list = os.listdir(path)
for file in dir_list:
    file_name = Path('data/'+file).stem

    try:
        getORF('data/'+file)
        print(file_name)
    except Exception as e:
        print('ERRO em ' + file_name)
        print(e)
    

saida.writeValues('saida.xlsx')
                