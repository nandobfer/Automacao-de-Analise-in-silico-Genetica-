import PyPDF2, os
from Saida import *
from pathlib import Path

RED="\033[1;31m"
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
COLOR_OFF='\033[0m'

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
        try:
            if page_content[i] == 'S' and page_content[i+5] == ':':
                j = i + 6
                while not page_content[j] == '\n':
                    # print(page_content[j])
                    score += page_content[j]
                    j += 1
        except:
            return str('erro')
                
    return str(score)

def getORF(file):
    with open(file, "rb") as pdf_file:
        read_pdf = PyPDF2.PdfFileReader(pdf_file)
        number_of_pages = read_pdf.getNumPages()
        page = read_pdf.pages[0]
        page_content = page.extractText()
    # print(page_content)
    duplicate = False
    # extracting
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
        if page_content[i] == '2' and page_content[i+2] == '+' and page_content[i+7] == f'{counter}':
            duplicate = True
    
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
    
     # extracting duplicate lines
    if duplicate:
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
    os.system('color')

    try:
        getORF('data/'+file)
        print(GREEN + 'SUCESS: ' + COLOR_OFF + file_name)
    except Exception as e:
        print(RED + 'ERROR: ' + YELLOW + file_name + RED)
        print(e)
        print(COLOR_OFF, end='')
        with open("errors.txt", "a") as file_error:
            file_error.write(file_name + '\n')
    

saida.writeValues('saida.xlsx')
                