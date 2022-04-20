import os

def getModules():
    # MODULO PyPDF2
    try:
        import PyPDF2
        print('Modulo PyPDF2 ja instalado')
    except:
        print('Modulo nao encontrado: PyPDF2')
        print('Tentando instalar automaticamente')
        try:
            os.system('pip install PyPDF2')
            print('Modulo instalado: PyPDF2')
        except:
            print('Não foi possivel baixar o modulo: PyPDF2')
            
    # MODULO pandas
    try:
        import pandas
        print('Modulo pandas ja instalado')
    except:
        print('Modulo nao encontrado: pandas')
        print('Tentando instalar automaticamente')
        try:
            os.system('pip install pandas')
            print('Modulo instalado: pandas')
        except:
            print('Não foi possivel baixar o modulo: pandas')
            
getModules()
os.system('python main.py')