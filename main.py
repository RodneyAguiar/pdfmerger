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

dir = '/d/OS695-19_PM-Angra-Reis/Cadastro/CartaNotificacao/42/20221028_4/'
# dir = '/o/OS898-21_PM-VitoriaConquista/Cadastro/CartaAutoAtendimento/CartasGeradas/67514/20221024_6/'
saida = '/home/rodney/Área de Trabalho/'

criaPdf(dir,saida)



