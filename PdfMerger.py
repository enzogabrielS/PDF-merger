import PyPDF2
import os

merger = PyPDF2.PdfMerger()
arquive_list = os.listdir("arquivos")
arquive_list.sort()

for arquivo in arquive_list:
    if arquivo.endswith(".pdf"):
        merger.append(f"arquivos/{arquivo}")

merger.write("PDF_final.pdf")
print("O seu arquivo foi gerado com sucesso!")
