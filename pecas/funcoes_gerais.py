from datetime import date
from num2words import num2words
import datetime



def local_e_data(comarca):
    dados = str(date.today()).split('-')
    ano=dados[0]
    mes=dados[1]
    dia=dados[2]
    smes=mes_extenso(int(mes))
    return comarca.capitalize() + ', '+dia+' de '+smes+' de '+ano

def mes_extenso(mes):
    meses = {1:'janeiro',2:'fevereiro',3:'março',4:'abril',5:'maio',6:'junho',7:'julho',8:'agosto',9:'setembro',10:'outubro',11:'novembro',12:'dezembro'}
    return meses[mes]


def convert_data_br(data_us):
    ano = data_us[0:4]
    mes = data_us[5:7]
    dia = data_us[-2:]
    return dia+'/'+mes+'/'+ano


def number_to_long_number(number_p):
    if number_p.find(',')!=-1:
        number_p = number_p.split(',')
        number_p1 = int(number_p[0].replace('.',''))
        number_p2 = int(number_p[1])
    else:
        number_p1 = int(number_p.replace('.',''))
        number_p2 = 0

    if number_p1 == 1:
        aux1 = ' real'
    else:
        aux1 = ' reais'

    if number_p2 == 1:
        aux2 = ' centavo'
    else:
        aux2 = ' centavos'

    text1 = ''
    if number_p1 > 0:
        text1 = num2words(number_p1,lang='pt_BR') + str(aux1)
    else:
        text1 = ''

    if number_p2 > 0:
        text2 = num2words(number_p2,lang='pt_BR') + str(aux2)
    else:
        text2 = ''

    if (number_p1 > 0 and number_p2 > 0):
        result = text1 + ' e ' + text2
    else:
        result = text1 + text2

    return result

def data_doc():
    data = str(datetime.datetime.now().today())[0:19]
    data = data.replace("-","")
    data = data.replace(":","")
    data = data[-6:]
    return data



def valor_por_extenso(number_p):
    retorno=''
    if number_p!='':
        retorno=number_to_long_number(number_p)
        if retorno[0:3]=='mil':
            retorno = 'um '+retorno
            retorno = retorno.capitalize()
    return retorno
