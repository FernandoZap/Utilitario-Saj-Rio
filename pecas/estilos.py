from docx.shared import RGBColor
from docx.shared import Pt
from docx.shared import Inches

def get_estilo(form):
    # heading padrao
    if form=="estilo1": 
        formatacao_form = {
        "bold":True,
        "italic":False,
        "underline":True,
        "name":"Calibri",
        "size":Pt(11),
        "indent":Inches(0.0),
        "space": Pt(11),
        "color":RGBColor.from_string('000000')
        }
    # paragraph padrao    
    elif form=="estilo2":
        formatacao_form = {
        "bold":False,
        "italic":False,
        "underline":False,
        "name":"Calibri",
        "size":Pt(11),
        "indent":Inches(0.0),
        "space": Pt(11),
        "color":RGBColor.from_string('000000')
        }
    # heading editavel    
    elif form=="estilo3":
        formatacao_form = {
        "bold":True,
        "italic":False,
        "underline":True,
        "name":"Calibri",
        "size":Pt(11),
        "indent":Inches(0.0),
        "space": Pt(11),
        "color":RGBColor.from_string('ff0000')
        }
    # paragraph editavel    
    elif form=="estilo4":
        formatacao_form = {
        "bold":False,
        "italic":False,
        "underline":False,
        "name":"Calibri",
        "size":Pt(11),
        "indent":Inches(0.0),
        "space": Pt(11),
        "color":RGBColor.from_string('FF0000')
        }
    # paragraph bold    
    elif form=="estilo5":
        formatacao_form = {
        "bold":True,
        "italic":False,
        "underline":False,
        "name":"Calibri",
        "size":Pt(11),
        "indent":Inches(0.0),
        "space": Pt(11),
        "color":RGBColor.from_string('000000')
        }
    # paragraph underline    
    elif form=="estilo6":
        formatacao_form = {
        "bold":False,
        "italic":False,
        "underline":True,
        "name":"Calibri",
        "size":Pt(11),
        "indent":Inches(0.0),
        "space": Pt(11),
        "color":RGBColor.from_string('000000')
        }      
    # paragraph bold e underline    
    elif form=="estilo7":
        formatacao_form = {
        "bold":True,
        "italic":False,
        "underline":True,
        "name":"Calibri",
        "size":Pt(11),
        "indent":Inches(0.0),
        "space": Pt(11),
        "color":RGBColor.from_string('000000')
        }
    # paragraph indent right    
    elif form=="estilo8":
        formatacao_form = {
        "bold":False,
        "italic":False,
        "underline":False,
        "name":"Calibri",
        "size":Pt(11),
        "indent":Inches(1.5748),
        "space": Pt(11),
        "color":RGBColor.from_string('000000')
        }
    # paragraph indent right bold   
    elif form=="estilo9":
        formatacao_form = {
        "bold":True,
        "italic":False,
        "underline":False,
        "name":"Calibri",
        "size":Pt(11),
        "indent":Inches(1.5748),
        "space": Pt(11),
        "color":RGBColor.from_string('000000')
        }
    # paragraph italic    
    elif form=="estilo10":
        formatacao_form = {
        "bold":False,
        "italic":True,
        "underline":False,
        "name":"Calibri",
        "size":Pt(11),
        "indent":Inches(0.0),
        "space": Pt(11),
        "color":RGBColor.from_string('000000')
        }
    # paragraph italic e bold    
    elif form=="estilo11":
        formatacao_form = {
        "bold":True,
        "italic":True,
        "underline":False,
        "name":"Calibri",
        "size":Pt(11),
        "indent":Inches(0.0),
        "space": Pt(11),
        "color":RGBColor.from_string('000000')
        }
    # paragraph italic e indent right    
    elif form=="estilo12":
        formatacao_form = {
        "bold":False,
        "italic":True,
        "underline":False,
        "name":"Calibri",
        "size":Pt(11),
        "indent":Inches(1.5748),
        "space": Pt(11),
        "color":RGBColor.from_string('000000')
        }
    # paragraph italic, bold e indent right    
    elif form=="estilo13":
        formatacao_form = {
        "bold":True,
        "italic":True,
        "underline":False,
        "name":"Calibri",
        "size":Pt(11),
        "indent":Inches(1.5748),
        "space": Pt(11),
        "color":RGBColor.from_string('000000')
        }                    
    return formatacao_form



def get_estilo_tabela(form):
    if form=="estilo1": 
        formatacao_form = {
        "num_linhas":2,
        "num_colunas":3,
        "largura":[3.0,.3,.4],
        "space": Pt(11)
        }
    elif form=="estilo2":
        formatacao_form = {
        "num_linhas":2,
        "num_colunas":2,
        "largura":[3.5,.5,.7],
        "space": Pt(11)
        }
    return formatacao_form
