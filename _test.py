import os, re
import pdfplumber
from PyPDF2 import PdfWriter, PdfReader

def segunda_pag(pdf):
    pass

def pdf_get_name (page, pdf_file):

  '''  
  page é o número da página
  pdf_file é caminho até o arquivo original 
  ''' 

  #O método open retorna uma instância da classe pdfplumber.PDF.
  pdf_content = pdfplumber.open(pdf_file)

  #Seleciona a página.
  pdf_page = pdf_content.pages[page]

  #Extrai o texto dividido por quebras de linha  
  pdf_text = pdf_page.extract_text().split('\n')

  #O nome que precisa ser extraído está na posição 4 da lista 'pdf_text'.
 # for i, v in enumerate(pdf_text):
 #       print('linha: {} conteudo: {}'. format(i,v))
  try:
    name = pdf_text[13]
  except:
     print(f'Erro na pagina: {pdf_page}')
     return ''
  #Limpa o nome extraído removendo alguns números. Para isso é passado um filtro com a função lambda que verifica caractere por caractere. 
  #Caso o caractere não esteja em '0123456789', ele é retonado dentro de uma lista.
  #name = list(filter(lambda c: c not in '0123456789', name))
  #name = list(filter(lambda c: c not in '.,/\\', name))
  name = re.sub('[^0-9]', '', name)
  #O método join() une os caracteres em uma única string novamente. Em seguida, remove os espaços em excesso.
  name = ''.join(name).strip()

  return name
  

def pdf_sep (pdf_file, out_dir):
  '''
  pdf_file é o caminho do pdf orinal
  out_dir é a pasta onde os pdfs divididos serão salvos
  '''
  #Abre o pdf original no modo de leitura
  with open(pdf_file, 'rb'):

    #Cria dois objetos, o primeiro da classe PdfFileReader para leitura e o segundo, da classe PdfFileWriter, para escrita
    pdf_content = PdfReader(pdf_file)
    pdf_writer = PdfWriter()

    #Armazena o quantidade de páginas do pdf original
    num_pages = len(pdf_content.pages)
    
    #Faz uma iteração para cada uma das páginas
    for page in range(num_pages):
      
      pdf_writer = PdfWriter()
      #Adiciona a página da iteração atual ao objeto para escrita do PDF
      pdf_writer.add_page(pdf_content.pages[page])

      #Invoca a função pdf_get_name para extrair o nome contido na página atual
      pdf_name = pdf_get_name(page, pdf_file)
      
      #O médoto os.path.join() une o caminho para gravação, o nome e a extesão do arquivo pdf. 
      if not pdf_name == '':
        pdf_out = os.path.join(out_dir, pdf_name +'.pdf')
      
      else:
          continue
        
      if os.path.exists(pdf_out):
          continue
      
      else:
      #Grava o objeto de escrita no arquivo
        with open(pdf_out, 'wb') as pdf_named:
            pdf_writer.write(pdf_named)

#Testando as funções

#Caminho para o arquivo original
path = " "

#Pasta onde os PDFs serão salvos
out_dir = " "

#Invoca a função separador

pdf_sep(path,out_dir)