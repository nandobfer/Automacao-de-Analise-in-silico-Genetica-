import pandas as pd

class Saida():
    def __init__(self) -> None:
        
        self.score = []
        self.inicio = []
        self.fim = []
        self.score_e = []
        self.orf_i = []
        self.orf_f = []
        self.pb = []   
        self.data = []  
        self.datas = []
    
    # add um lançamento nas listas        
    def addValues(self, score, inicio, fim, score_e, orf_i, orf_f, pb, line, file_name):
        self.score.append(score)
        self.inicio.append(inicio)
        self.fim.append(fim)
        self.score_e.append(score_e)
        self.orf_i.append(orf_i)
        self.orf_f.append(orf_f)
        self.pb.append(pb) # abs() absolute number, make it all positive
        
        data = {
            'Contig': file_name,
            'Score': score,
            f'Inicio {line+1}': inicio,
            f'Fim {line+1}': fim,
            f'Score Especifico {line+1}': score_e,
            f'ORF inicio {line+1}': orf_i,
            f'ORF fim {line+1}': orf_f,
            f'pb {line+1}': pb
        }
        self.data.append(data)
    
    def endFile(self):
        data = dict(self.data[0])
        for i in range(1, len(self.data)):
            data.update(self.data[i])
        self.datas.append(data)
        self.data = []
    
    # cria um arquivo novo com os lançamentos salvos nas listas    
    def writeValues(self, file):
        write = pd.DataFrame(self.datas)
        write.to_excel(file, index=False)
        # print(data)
  

# saida = Saida()
# print(saida.read['Lançamento'])