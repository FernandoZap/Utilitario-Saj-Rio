import mimetypes
from django.http import StreamingHttpResponse
from wsgiref.util import FileWrapper
from django.views.generic import View

from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
#from . import funcoes_banco,funcoes_gerais,peticao_des_dev_hon_dup,peticao_teste,peticao_dev_hp_improc,peticao_dev_hp_extinto_sem_resolucao,peticao_disponibilizacao_comprovante_transf,teses,dados_informados,funcoes_teses,embargos_omissao
#from .classes import Pasta
import pyodbc as p
import os
import json


def download_file(request,docmto):
    pass
    '''
    #the_file ='c:/projetos/proj02/static/docs/'+docmto
    the_file='/home/ubuntu/documentos/'+docmto
    #the_file = docmto
    filename = os.path.basename(the_file)
    chunk_size = 8192
    response = StreamingHttpResponse(FileWrapper(open(the_file, 'rb'), chunk_size),
                            content_type=mimetypes.guess_type(the_file)[0])
    response['Content-Length'] = os.path.getsize(the_file)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
    '''



def v003_dados_da_pasta(request):
    pass
    ''' 
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        cod_pasta_saj = request.GET.get('opcao')
        lista=funcoes_banco.f001_sql(cod_pasta_saj)
        pasta=lista[0]
        cod_cliente=lista[1]
        autor=lista[2]
        comarca=lista[3]
        uf=lista[4]
        orgao=lista[5]
        num_orgao=lista[6]
        juizo=lista[7]
        secao=lista[8]
        nr_processo=lista[9]
        empresa=lista[10]
        oabjb=lista[11]
        publicando_nome=lista[12]
        publicando_oab=lista[13]
        publicando_sexo=lista[14]
        conveniado_nome=lista[15]
        conveniado_oab=lista[16]

        data=[]
        data.append({'key':0,'value':pasta})
        data.append({'key':1,'value':cod_cliente})
        data.append({'key':2,'value':autor})
        data.append({'key':3,'value':comarca})
        data.append({'key':4,'value':uf})
        data.append({'key':5,'value':orgao})
        data.append({'key':6,'value':num_orgao})
        data.append({'key':7,'value':juizo})
        data.append({'key':8,'value':secao})

        data.append({'key':9,'value':nr_processo})
        data.append({'key':10,'value':empresa})
        data.append({'key':11,'value':oabjb})
        data.append({'key':12,'value':publicando_nome})
        data.append({'key':13,'value':publicando_oab})
        data.append({'key':14,'value':publicando_sexo})
        data.append({'key':15,'value':conveniado_nome})
        data.append({'key':16,'value':conveniado_oab})


        data = json.dumps(data)
    else:
        data=[]
    return HttpResponse(data, content_type='application/json')
    '''



def v004_peticoes(request):
    pass
    '''
    if (request.method == "POST"):
        pasta=request.POST['pasta']
        autor=request.POST['autor']
        tipo=request.POST["tipo"]
        nr_processo=request.POST['nr_processo']
        cliente=request.POST['cliente']
        comarca=request.POST['comarca']
        conv_nome=request.POST['conveniado_nome']
        conv_oab=request.POST['conveniado_oab']
        uf=request.POST['uf']
        juizo=request.POST['juizo']
        cod_cliente=request.POST['cod_cliente']
        #pasta_saj='0000'
        lista=funcoes_banco.view_pasta(pasta)
        pasta_saj = Pasta(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5],lista[6],lista[7],lista[8],lista[9],lista[10],lista[11],lista[12],lista[13],lista[14],lista[15],lista[16],lista[17],lista[18])
        if tipo=='Desarquivamento DHD':
            file=peticao_des_dev_hon_dup.fun_peticao_01(pasta_saj)
        elif tipo=='Devolucao HPIMPROC':
            file=peticao_dev_hp_improc.fun_peticao_01(pasta,cod_cliente,autor,nr_processo,comarca,uf,cliente,juizo)
        elif tipo=='Devolucao HPEXTSEMRESOLUCAO':
            file=peticao_dev_hp_extinto_sem_resolucao.fun_peticao_01(pasta,cod_cliente,autor,nr_processo,comarca,uf,cliente,juizo)
        elif tipo=='Disp COMPROVANTETRANSF':
            file=peticao_disponibilizacao_comprovante_transf.fun_peticao_01(pasta,cod_cliente,autor,nr_processo,comarca,uf,cliente,juizo)
        return redirect('pecas:download', docmto=file)
        #return redirect('pecas:peticao_01')
    else:
        dados = {
            'tipo_da_pecao': 'Peticões'
        }
        return render(request, 'pecas/peticoes.html', dados)
    '''

def peticoes_teste(request):
    pass
    '''
    if (request.method == "POST"):
        pasta=request.POST['pasta']
        autor=request.POST['autor']
        tipo=request.POST["tipo"]
        nr_processo=request.POST['nr_processo']
        cliente=request.POST['cliente']
        comarca=request.POST['comarca']
        uf=request.POST['uf']
        juizo=request.POST['juizo']
        cod_cliente=request.POST['cod_cliente']
        conv_nome=request.POST['conveniado_nome']
        conv_oab=request.POST['conveniado_oab']
        if tipo=='Desarquivamento DHD':
            file=peticao_teste.fun_peticao_01(pasta,cod_cliente,autor,nr_processo,comarca,uf,cliente,juizo,conv_nome,conv_oab)
        return redirect('pecas:download', docmto=file)
        #return redirect('pecas:peticao_01')
    else:
        dados = {
            'tipo_da_pecao': 'Peticões Teste'
        }
        return render(request, 'pecas/peticoes_teste.html', dados)
    '''


def v005_contrarrazoes(request):
    pass
    '''
    if request.method == 'POST':
        pasta = request.POST['pasta']
        if request.POST['tipoDaSentenca']=='Terminativa':
            return redirect('pecas:contrarecapelacao', pasta=pasta)
    dados = {
         'tipo_da_peca': 'Contrarrazoes'
    }
    return render (request,'pecas/contrarrazoes.html',dados)
    '''




def v006_contraRecApelacao(request,pasta):
    pass
    '''
    if (request.method == "POST"):
        teses_contrar = teses.teses_contrar_rec_apelacao
        pasta=request.POST['pasta']
        dados_complementares = dados_informados.dados_contrar_rec_apelacao()

        tipo_da_fundamentacao=request.POST['fundamentacao']
        ha_nulidade_publicacao=request.POST['nulidade']
        inovacaoRec=request.POST['inovacaoRec']
        prescricao=request.POST['prescricao']  # nenhuma tese para inseri
        pedido_pagto_adm=request.POST['pedidoPagtoAdm']
        houve_pagtoAdm=request.POST['pagamentoAdm']
        pedido_dano_moral=request.POST['pedidoDanoMoral']
        return HttpResponse("<h1>ContraRecApelacao</h1>")

        if tipo_da_fundamentacao=="AuAP":
            teses_contrar['tese8']='S'
            teses_contrar['tese20']='S'
        elif tipo_da_fundamentacao=="AuIA":
            teses_contrar['tese9']='S'
            teses_contrar['tese22']='S'
            teses_contrar['tese23']='S'
        elif tipo_da_fundamentacao=="AuNC":
            teses_contrar['tese10']='S'
            teses_contrar['tese27']='S'
        elif tipo_da_fundamentacao=="AuLIML":
            teses_contrar['tese8']='S'
            teses_contrar['tese28']='S'
        elif tipo_da_fundamentacao=="AuS":
            teses_contrar['tese11']='S'
            teses_contrar['tese21']='S'
        elif tipo_da_fundamentacao=="CM":
            teses_contrar['tese12']='S'
            teses_contrar['tese24']='S'
            teses_contrar['tese26']='S'

        if ha_nulidade_publicacao=="SIM":
            teses_contrar['tese13']='S'
            dados_complementares['dtPublic']=funcoes_gerais.convert_data_br(request.POST['dtPublic'])

        if inovacaoRec=="SIM":
            teses_contrar['tese14']='S'

        if prescricao=="SIM":
            teses_contrar['tese14']='S'

        if pedido_pagto_adm=="1":
            teses_contrar['tese15']='S'
            teses_contrar['tese16']='S'
            dados_complementares['dtSinistro']=funcoes_gerais.convert_data_br(request.POST['dtSinistro1'])
            dados_complementares['dtPedidoAdm']=funcoes_gerais.convert_data_br(request.POST['dtPedidoAdm'])
            dados_complementares['tempoDecorrido']=request.POST['tempoDecorrido']
            dados_complementares['dtFinalCausaSusp']=funcoes_gerais.convert_data_br(request.POST['dtFinalCausaSusp'])
            dados_complementares['dtAjuizamento']=funcoes_gerais.convert_data_br(request.POST['dtAjuizamento1'])
        elif pedido_pagto_adm=="2":
            teses_contrar['tese17']='S'
            teses_contrar['tese18']='S'
            dados_complementares['dtSinistro']=funcoes_gerais.convert_data_br(request.POST['dtSinistro2'])
            dados_complementares['dtDistribuicao']=funcoes_gerais.convert_data_br(request.POST['dtDistribuicao'])
        elif pedido_pagto_adm=="3":
            teses_contrar['tese19']='S'
            dados_complementares['dtSinistro']=funcoes_gerais.convert_data_br(request.POST['dtSinistro3'])
            dados_complementares['dtPagamentoAdm']=funcoes_gerais.convert_data_br(request.POST['dtPagamentoAdm'])
            dados_complementares['dtAjuizamento']=funcoes_gerais.convert_data_br(request.POST['dtAjuizamento3'])
        elif pedido_pagto_adm=="4":
            teses_contrar['tese20']='S'
        elif pedido_pagto_adm=="5":
            teses_contrar['tese21']='S'

        if houve_pagtoAdm=="SIM":
            teses_contrar['tese29']='S'

        if pedido_dano_moral=="SIM":
            teses_contrar['tese30']='S'

        file = contrar_rec_apelacao_1_1.peticoes('pet01', teses=teses_contrar,dados_compl=dados_complementares,pasta=pasta)

        return redirect('pecas:download', docmto=file)
    else:
        lista=funcoes_banco.view_pasta(pasta)
        pasta_saj = Pasta(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5],lista[6],lista[7],lista[8],lista[9],lista[10],lista[11],lista[12],lista[13],lista[14],lista[15],lista[16],lista[17],lista[18])
        dados = {
           'pasta': pasta_saj.pasta,
           'nr_processo': pasta_saj.nr_processo,
           'autor': pasta_saj.autor
        }
    return render (request,'pecas/contraRecApelacao.html',dados)
    '''


def v007_embargos(request):
    pass
    '''
    if (request.method == "POST"):
        #request.session['pasta']=request.POST['pasta']
        data_publicacao=request.POST['data_publicacao']

        hanulidadepublic=request.POST['hanulidadepublic']
        motivo_embargos=request.POST['motivo_embargos']
        pasta = request.POST['pasta']

        if hanulidadepublic=='S':
            request.session['nulidade'] = 'S'
        else:
            request.session['nulidade'] = 'N'

        if motivo_embargos=='OMISSAO':
            return redirect('pecas:embargos-omissao', pasta=pasta, hanulidadepublic = hanulidadepublic,data_publicacao = data_publicacao)
        elif motivo_embargos=='ULTRA PETITA-CE':
            return redirect('pecas:embargos-ultrapetita')
        elif motivo_embargos=='CONTRADICAO':
            return redirect('pecas:embargos-contradicao')
    else:
        dados = {
            'tipo_da_peca': 'Embargos'
        }
        return render(request, 'pecas/embargos.html', dados)
    '''


#@login_required
def v008_embargos_omissao(request,pasta,hanulidadepublic,data_publicacao):
    pass
    '''
    if (request.method == "POST"):
        pasta = request.POST['pasta']
        #hanulidadepublic = request.POST['hanulidadepublic']
        data_publicacao = request.POST['data_publicacao']

        teses_emb_omissao = teses.teses_embargos_omissao

        respostas = {
            'intimacao_mp':request.POST['intimacao_mp'],
            'cj_peremp_litisp':request.POST['cj_peremp_litisp'],
            'prescricao':request.POST['prescricao'],
            'pagamento_adm':request.POST['pagamento_adm'],
            'prop_inadimp':request.POST['prop_inadimp'],
            'prop_inadimp_com_pagto_Adm':request.POST['prop_inadimp_com_pagto_Adm'],
            'lesao_pre':request.POST['lesao_pre'],
            'omissao':request.POST['omissao_reg8'],
            'juros_citacao':request.POST['juros_citacao'],
            'correcao':request.POST['correcao']
        }
        data='2000-01-01'

        if hanulidadepublic=='S':
            teses_emb_omissao['tese1']='S'
            data=data_publicacao


        teses_emb_omissao = funcoes_teses.f002_teses_embargos_omissao(respostas,teses_emb_omissao)

        dados_complementares = dados_informados.dados_embargos_omissao()

        dados_complementares['data_public']=funcoes_gerais.convert_data_br(data)
        dados_complementares['valor_pagamento_adm']=request.POST['valor_pagamento_adm']
        valor = request.POST['valor_pagamento_adm']
        dados_complementares['num_processo_vinculado']=request.POST['num_processo_vinculado']
        dados_complementares['juizo_vinculado']=request.POST['juizo_vinculado']
        dados_complementares['juizo_lpe']=request.POST['juizo_lpe']
        dados_complementares['num_proc_lpe']=request.POST['num_proc_lpe']
        dados_complementares['data_lpe']=request.POST['data_lpe']
        dados_complementares['desc_lpe']=request.POST['desc_lpe']
        dados_complementares['local_diligencia']=request.POST['local_diligencia']

        dados_pasta = funcoes_banco.f002_sql(request.POST['pasta'])

        dados_complementares['adv_publicando'] = dados_pasta['publicando_nome']
        dados_complementares['nr_processo'] = dados_pasta['nr_processo']
        dados_complementares['cod_cliente'] = dados_pasta['cod_cliente']

        pasta = request.POST['pasta']

        valor_extenso=funcoes_gerais.valor_por_extenso(valor)

        if valor!="":
            dados_complementares['pagamento_adm']="R$ "+valor+" ("+valor_extenso+")"
        else:
            dados_complementares['pagamento_adm']=''

        #return HttpResponse("<h1>Teste</h1>")


        file = embargos_omissao.peticoes('pet01', teses=teses_emb_omissao,dados_compl=dados_complementares,pasta=pasta)

        #file = templates.embargosOmissao(context=dados_complementares)


        #return redirect('pecas:templatepeca', docmto=file)

        return redirect('pecas:download', docmto=file)
    else:

        #pasta = request.session.get('pasta')
        tese_nulidade = 'S' #request.session.get('tese_nulidade')


        autor='nome do autor'
        comarca='nome da comarca'
        uf=' uf '
        nr_processo='0000000'
        dados={
            'pasta':pasta,
            'autor':autor,
            'comarca':comarca,
            'uf':uf,
            'tese_nulidade':tese_nulidade,
            'nr_processo': nr_processo,
            'data_publicacao':data_publicacao,
            'tipo_da_peca':'Embargos Omissao'
            }
        return render(request, 'pecas/embargos_omissao.html', dados)
    '''

def v009_embargos_ultrapetita(request):
    return HttpResponse("<h1>Embargo Ultra-Petita</h1>")

def v010_embargos_contradicao(request):
    return HttpResponse("<h1>Embargo Contradição</h1>")
