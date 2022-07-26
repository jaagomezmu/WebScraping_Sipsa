from bs4 import BeautifulSoup #  Webscraping
import urllib.request # Remplaza la libreria request
import wget # Administra la descarga
import pandas as pd
import os
import glob
import zipfile # Para descoscomprimir
import tabula # Scrap de pdf



# html download
url = 'https://www.dane.gov.co/index.php/estadisticas-por-tema/agropecuario/sistema-de-informacion-de-precios-sipsa/componente-precios-mayoristas'
page = urllib.request.urlopen(url)
# read the correct character encoding from `Content-Type` request header
charset_encoding = page.info().get_content_charset()
# apply encoding
page = page.read().decode(charset_encoding)

# bs4 format
soup = BeautifulSoup(page, 'html.parser')
#______________________________________________________________________

# Precios minimos y maximos
boletines = soup.find_all('a', title="Informes por ciudades")

# Ultimo Boletin
boletin = boletines[0].attrs['href']
# New url 

url_base = 'https://www.dane.gov.co'

new_url = url_base+boletin

print('Comenzando la descarga desde: {}'.format(new_url))

wget.download(new_url)

print('Descarga finalizada.')

list_of_files = glob.glob('*.zip') 
latest_file = max(list_of_files, key=os.path.getctime)
# print('El ultimo archivo es: {}'.format(latest_file))
filenames = list()
with zipfile.ZipFile(latest_file, mode="r") as archive:
    for filename in archive.namelist():
        filenames.append(filename)

combined = 't'.join(filenames)

if 'Bogotá' in combined:
    ## Filter Bogota
    sub = 'Bogotá'
    name_bogota = [s for s in filenames if sub in s][0]
    if sub in name_bogota:
        with zipfile.ZipFile(latest_file, mode='r') as  archive:
            archive.extract(name_bogota)

if 'Sincelejo' in combined:
    ## Filter Sincelejo
    sub = 'Sincelejo'
    name_sincelejo = [s for s in filenames if sub in s][0]
    if sub in name_sincelejo:
        with zipfile.ZipFile(latest_file, mode='r') as  archive:
            archive.extract(name_sincelejo)

if 'Armenia' in combined:
    ## Filter Armenia
    if [s for s in filenames if sub in s][0]:
        sub = 'Armenia'
        name_armenia = [s for s in filenames if sub in s][0]
        if sub in name_armenia:
            with zipfile.ZipFile(latest_file, mode='r') as  archive:
                archive.extract(name_armenia)

if 'Barranquilla' in combined:
    ## Filter Barranquilla
    sub = 'Barranquilla'
    name_barranquilla = [s for s in filenames if sub in s][0]
    if sub in name_barranquilla:
        with zipfile.ZipFile(latest_file, mode='r') as  archive:
            archive.extract(name_barranquilla)

if 'Cartagena' in combined:
    ## Filter Cartagena
    sub = 'Cartagena'
    name_cartagena = [s for s in filenames if sub in s][0]
    if sub in name_cartagena:
        with zipfile.ZipFile(latest_file, mode='r') as  archive:
            archive.extract(name_cartagena)

if 'Medellín' in combined:
    ## Filter Medellín
    sub = 'Medellín'
    name_medellin = [s for s in filenames if sub in s][0]
    if sub in name_medellin:
        with zipfile.ZipFile(latest_file, mode='r') as  archive:
            archive.extract(name_medellin)

if 'Montería' in combined:
    ## Filter Montería
    sub = 'Montería'
    name_monteria = [s for s in filenames if sub in s][0]
    if sub in name_monteria:
        with zipfile.ZipFile(latest_file, mode='r') as  archive:
            archive.extract(name_monteria)

list_of_pdf_files = glob.glob('*.pdf') 
combined2 = 't'.join(list_of_pdf_files)
print(combined2)
if 'Armenia' in combined2:
    # Open the pdf
    sub = 'Armenia' ## Suprimir fila
    name_armenia = [s for s in list_of_pdf_files if sub in s][0] ### Cambiar list_of_pdf_files for filename.
    armenia_df = tabula.read_pdf(name_armenia,pages='1')[0]
    armenia_df.rename(columns={'Unnamed: 0':'producto','Unnamed: 1':'presentacion','Unnamed: 2':'unidades', 'Unnamed: 3':'r1_minimo','Unnamed: 4':'r1_maximo','Unnamed: 5':'r2_minimo','Unnamed: 6':'r2_maximo'}, inplace = True)
    armenia_resultado = armenia_df[armenia_df['producto'] == 'Piña gold']


if 'Barranquilla' in combined2:
    # Open the pdf
    name_barranquilla = tabula.read_pdf(name_barranquilla,pages='1')[0]
    name_barranquilla.rename(columns={'Unnamed: 0':'producto','Unnamed: 1':'presentacion','Unnamed: 2':'unidades', 'Unnamed: 3':'r1_minimo','Unnamed: 4':'r1_maximo','Unnamed: 5':'r2_minimo','Unnamed: 6':'r2_maximo'}, inplace = True)
    barranquilla_resultado = name_barranquilla[name_barranquilla['producto'] == 'Piña perolera']


if 'Bogotá' in combined2:
    # Open the pdf
    name_bogota = tabula.read_pdf(name_bogota,pages='1')[0]
    name_bogota.rename(columns={'Unnamed: 0':'producto','Unnamed: 1':'presentacion','Unnamed: 2':'unidades', 'Unnamed: 3':'r1_minimo','Unnamed: 4':'r1_maximo','Unnamed: 5':'r2_minimo','Unnamed: 6':'r2_maximo'}, inplace = True)
    bogota_resultado = name_bogota[name_bogota['producto'] == 'Piña gold']


if 'Cartagena' in combined2:
    # Open the pdf
    name_cartagena = tabula.read_pdf(name_cartagena,pages='2')[0]
    name_cartagena.rename(columns={'Unnamed: 0':'producto','Unnamed: 1':'presentacion','Unnamed: 2':'unidades', 'Unnamed: 3':'r1_minimo','Unnamed: 4':'r1_maximo','Unnamed: 5':'r2_minimo','Unnamed: 6':'r2_maximo'}, inplace = True)
    cartagena_resultado = name_cartagena[name_cartagena['producto'] == 'Piña gold']
    

if 'Medellín' in combined2:
    # Open the pdf
    name_medellin = tabula.read_pdf(name_medellin,pages='1')[0]
    name_medellin.rename(columns={'Unnamed: 0':'producto','Unnamed: 1':'presentacion','PRECIOS DE VENTA MAYORISTA':'cambiar'}, inplace = True)
    name_medellin[['presentacion','numero','unidades','r1_minimo','r1_maximo','r2_minimo','r2_maximo']] = name_medellin['cambiar'].str.split(' ', expand=True)
    medellin_resultado = name_medellin[name_medellin['producto'] == 'Piña gold']


if 'Montería' in combined2:
    # Open the pdf
    name_monteria = tabula.read_pdf(name_monteria,pages='2')[0]
    name_monteria.rename(columns={'Unnamed: 0':'producto','Unnamed: 1':'presentacion','Unnamed: 2':'unidades', 'Unnamed: 3':'r1_minimo','Unnamed: 4':'r1_maximo','Unnamed: 5':'r2_minimo','Unnamed: 6':'r2_maximo'}, inplace = True)
    monteria_resultado = name_monteria[name_monteria['producto'] == 'Piña gold']


if 'Sincelejo' in combined2:
    # Open the pdf
    name_sincelejo = tabula.read_pdf(name_sincelejo,pages='2')[0]
    name_sincelejo.rename(columns={'Unnamed: 0':'producto','Unnamed: 1':'presentacion','Unnamed: 2':'unidades', 'Unnamed: 3':'r1_minimo','Unnamed: 4':'r1_maximo','Unnamed: 5':'r2_minimo','Unnamed: 6':'r2_maximo'}, inplace = True)
    sincelejo_resultado = name_sincelejo[name_sincelejo['producto'] == 'Piña gold']

if 'Armenia' in combined2:
    print('Armenia:',armenia_resultado)
if 'Barranquilla' in combined2:
    print('Barranquilla:', barranquilla_resultado)
if 'Bogotá' in combined2:
    print('Bogotá:', bogota_resultado)
if 'Cartagena' in combined2:
    print('Cartagena:', cartagena_resultado)
if 'Medellín' in combined2:
    print('Medellín:', medellin_resultado)
if 'Montería' in combined2:
    print('Monteria:', monteria_resultado)
if 'Sincelejo' in combined2:
    print('Sincelejo:', sincelejo_resultado)

