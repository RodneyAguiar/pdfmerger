from PyPDF2 import PdfMerger
import os


def criaPdf(dir, saida):
    merger = PdfMerger()
    for arq in os.listdir(dir):
        diretorio = dir + arq
        print(diretorio)
        merger.append(diretorio)

    merger.write(f'{saida}PdfMerger.pdf')

    merger.close()

dir = '/home/rodney/pdf/' # Pasta onde se localiza os PDF's.
saida = '/home/rodney/Área de Trabalho/' # Local onde será salvo os PDF's unidos.

criaPdf(dir,saida)



