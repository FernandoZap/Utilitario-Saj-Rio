# -*- coding: utf-8 -*-

import os
import datetime
from . import funcoes_gerais
from docx.shared import RGBColor

'''
4-omissao_tese_nulidade(dados_compl,dados_pasta):
5-omissao_tese_intimacao_mp():    
6-omissao_tese_coisa_julgada(dados_compl,dados_pasta):
7-omissao_tese_litispendencia(dados_compl,dados_pasta):
8-omissao_tese_ed_omissao_prescricao():
9-omissao_tese_omissao_pagamento_adm(dados_compl):
10-omissao_tese_omissao_inadimplente():
11-omissao_tese_omissao_lesao_preexistente(dados_compl):
12-omissao_tese_omissao_regulacao_8(dados_compl):
13-omissao_tese_omissao_dos_juro():    
14-omissao_tese_omissao_cm():        
'''

'''
dados_compl['juizo_compl']
'''



#[[1m prefixo e sufixo da formatacao
#sbbb bold
#siii italic
#suuu underline

#exemplo
#   [[1msbbbeste texto vai se escrito em bold.[[1m
#   [[1msbbieste texto vai se escrito em bold e em italic.[[1m
#   [[1msiiueste texto vai se escrito em underline em italic.[[1m


def teseConstrutor(dados_compl, dados_pasta,tese):
    publicando_nome_oab = dados_pasta['publicando_nome']+' - OAB: '+dados_pasta['publicando_oab']
    elementos = []
    if tese=='tese1':
        elementos = [
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "heading", "texto": [
                {
                    "descricao": "DA TEMPESTIVIDADE",
                    "posicao": "primeira",
                    "estilo": "estilo1"
                }]
            },
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Inicialmente, cumpre observar que foi publicado dia [[1msbbb"+dados_compl[
                        'data_public']+"[[1m, no Diário da " +
                                 "Justiça Eletrônico, a r. decisão exarada, como se verifica na colação abaixo:",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "texto_manual", "texto": [
                {
                    "descricao": "COLAR A PUBLICÃO",
                    "posicao": "primeira",
                    "estilo": "estilo3"
                }]
            },
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Desta feita, a Seguradora permanecia no aguardo da devida publicação para que pudesse verificar a " +
                                 "intenção em recorrer, e ofertar sua peça tempestivamente, o que o faz sob ancorada no princípio de " +
                                 "celeridade e economia processual.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Como se vê não foram respeitadas as exigências de Publicidade dos atos praticados, tendo em vista que foi " +
                                 "requerido na peça de bloqueio (fls.), que futuras publicações fossem feitas em nome do patrono da " +
                                 "Apelante [[1msbbb"+publicando_nome_oab + ".",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Conclui-se, portanto, que em nenhum momento o [[1msiiir. decisium[[1m esteve à disposição da Seguradora para " +
                                 "ciência e eventual manifestação nos autos.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Afinal não é possível que a Seguradora, com seu grandioso número de causas, possua o controle e tenha a " +
                                 "possibilidade de organizar suas publicações com seus números de processo.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Por tal motivo, inclusive, é que se indica os nomes dos patronos a saírem a publicação realizada, eis que se " +
                                 "torna uma forma mais fácil de proceder o acompanhamento processual.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Assim, repita-se, [[1msbbuNÃO HOUVE PUBLICAÇÃO DA D. SENTENÇA, [[1msbbbo que ocasionou a perda do prazo para " +
                                "manifestação nos autos.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Neste sentido, os requisitos formais para a validade do ato de comunicação processual, fundamental para " +
                                 "a aplicação dos regimes de preclusão e desenvolvimento dos atos processuais, não atendeu aos critérios " +
                                 "formais de sua realização.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Conclui-se, portanto, que [[1msbbuem nenhum momento o r. decisum esteve à disposição da Recorrente para ciência[[1m, "+
                            "haja vista que NÃO foi publicada em nome do patrono constituído nos autos.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            }
        ]
    elif tese=='tese2':            
        elementos = [
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "heading", "texto": [
                {
                    "descricao": "DA SÍNTESE DOS FATOS E DA OMISSÃO",
                    "posicao": "primeira",
                    "estilo": "estilo1"
                }]
            },
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Com a mais a respeitosa vênia, assim o fazendo, afigura-se a v. decisão omissa em pontos essenciais," +
                                 "justificando o cabimento dos presentes Embargos de Declaração, a fim de que essa V. Exa. decida-os e" +
                                 "confira os efeitos integrativos ao respeitável [[1msiiidecisum.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Frisa-se que na d. sentença exarada, verifica-se grave OMISSÃO, que devem ser supridas ou sanadas por " +
                                 "meio dos presentes embargos, sendo certo que o recurso não objetiva rediscutir a matéria, mas afastar os " +
                                 "vícios constatados no julgado.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Com todo o respeito, a Embargante informa que nos casos em que há interesses de incapazes sendo " +
                                 "discutido em determinada demanda, deve ser intimado o Ministério Público, órgão fiscalizador da Lei, para " +
                                 "que se pronuncie sobre a necessidade de sua intervenção.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Cumpre informar, no caso dos autos, o autor é menor, e figura como autor na presente demanda, figurando " +
                                 "como representante, seu genitor, contudo, em que pese tenha haja o pedido de intimação do MP na peça " +
                                 "de bloqueio, não se observa menção a este respeito na sentença prolatada.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Urge ressaltar, a necessidade da prática deste ato, de intimação do MP, não por uma faculdade, mas um " +
                                 "comando imposto pelo Código de Processo Civil, que traz inclusive, quando ausente tal intimação, uma " +
                                 "possibilidade do reconhecimento de uma nulidade.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Ante o exposto e da patente necessidade de intimação do Ministério Público para fins de atender ao " +
                                 "disposto nos artigos 178, II c/c 279 do CPC, requer seja verificada a omissão informada e a consequente " +
                                 "intimação do Parquet para acompanhar o feito.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "heading", "texto": [
                {
                    "descricao": "CONCLUSÃO",
                    "posicao": "primeira",
                    "estilo": "estilo1"
                }]
            },
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "São essas as razões pelas quais a embargante confia, espera e requer sejam acolhidos e providos os " +
                                 "presentes Embargos Declaratórios, enfrentado o ponto OMISSO, conferido efeitos integrativos para o fim " +
                                 "de prover integralmente, tudo por ser medida de direito e irretorquível JUSTIÇA!",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            }
        ]
    elif tese=='tese3':
        elementos = [
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "heading", "texto": [
                {
                    "descricao": "DA SÍNTESE DOS FATOS E DA OMISSÃO NA DECISÃO PROFERIDA:",
                    "posicao": "primeira",
                    "estilo": "estilo1"
                }]
            },
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Sem adentrar ao mérito do [[1msiiidecisum[[1m, informa a V. Exa. que constou na parte dispositiva desta o seguinte:",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },
            {
                "tipo": "texto_manual", "texto": [
                {
                    "descricao": "COLAR A SENTENÇA",
                    "posicao": "primeira",
                    "estilo": "estilo3"
                }]
            },
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Com a mais a respeitosa vênia, assim o fazendo, afigura-se a v. decisão omissa em pontos essenciais, " +
                                 "justificando o cabimento dos presentes Embargos de Declaração, a fim de que essa V. Exa. decida-os e " +
                                 "confira os efeitos integrativos ao respeitável [[1msiiidecisum.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Verifica-se grave OMISSÃO, que devem ser supridas ou sanadas por meio dos presentes embargos, sendo " +
                                 "certo que o recurso não objetiva rediscutir a matéria, mas afastar os vícios constatados no julgado.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao":"Preliminarmente, informa da existência de outra demanda idêntica a presente, ou seja, com as mesmas partes, pedido e causa de pedir, a qual fora registrada sob o número [[1msbbb"+dados_compl['num_processo_vinculado']+"[[1m, e tramitou perante o Juízo da "+dados_compl['juizo_vinculado']+", [[1msuuutendo havido trânsito em julgado de decisão de mérito, fazendo-se coisa julgada material[[1m, conforme comprovam as cópias inclusas.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao":"Desta feita, manifesta a tríplice identidade entre a presente demanda e aquela supramencionada, [[1msuuupelo que se requer o acolhimento desta preliminar, a fim de se julgar EXTINTO o feito, nos termos do art. 485, V, do CPC.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Por fim, pugna-se pela condenação da parte a todos os consectários legais, inclusive custas processuais, " +
                                 "honorários advocatícios e ainda, a condenação pela comprovada litigância de má-fé conforme disposto no " +
                                 "artigo 77 da Lei Processual Civil.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "heading", "texto": [
                {
                    "descricao": "CONCLUSÃO",
                    "posicao": "primeira",
                    "estilo": "estilo1"
                }]
            },
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "São essas as razões pelas quais a embargante confia, espera e requer sejam acolhidos e providos os " +
                                 "presentes Embargos Declaratórios, enfrentado o ponto OMISSO, conferido efeitos integrativos para o fim " +
                                 "de prover integralmente, tudo por ser medida de direito e irretorquível JUSTIÇA!",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            }
        ]
    elif tese=='tese4':
        pass    
    elif tese=='tese5':
        elementos = [
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "heading", "texto": [
                {
                    "descricao": "DA SÍNTESE DOS FATOS E DA OMISSÃO",
                    "posicao": "primeira",
                    "estilo": "estilo1"
                }]
            },
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Sem adentrar ao mérito informa a V. Exa. que constou na parte dispositiva desta o seguinte:",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },
            {
                "tipo": "texto_manual", "texto": [
                {
                    "descricao": "COLAR A SENTENÇA",
                    "posicao": "primeira",
                    "estilo": "estilo3"
                }]
            },
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Com a mais a respeitosa vênia, assim o fazendo, afigura-se a v. decisão omissa em pontos essenciais, " +
                                 "justificando o cabimento dos presentes Embargos de Declaração, a fim de que essa V. Exa. decida-os e " +
                                 "confira os efeitos integrativos ao respeitável [[1msiiidecisum.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Verifica-se grave OMISSÃO, que devem ser supridas ou sanadas por meio dos presentes embargos, sendo " +
                                 "certo que o recurso não objetiva rediscutir a matéria, mas afastar os vícios constatados no julgado.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao":"Preliminarmente, informa da existência de outra demanda idêntica a presente, ou seja, com as mesmas partes, pedido e causa de pedir, a qual fora registrada sob o número [[1mabbb"+dados_compl['num_processo_compl']+"[[1m, e tramita perante o Juízo da 1ª VARA CÍVEL DA COMARCA DE FLORES - PB, conforme comprovam as cópias inclusas.",
                                 
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao":"Desta feita, manifesta a tríplice identidade entre a presente demanda e aquela supramencionada, [[1msuuupelo que se requer o acolhimento desta preliminar, a fim de se julgar EXTINTO o feito, sem resolução de mérito, nos termos do art. 485, V, do CPC.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "heading", "texto": [
                {
                    "descricao": "CONCLUSÃO",
                    "posicao": "primeira",
                    "estilo": "estilo1"
                }]
            },
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "São essas as razões pelas quais a embargante confia, espera e requer sejam acolhidos e providos os " +
                                 "presentes Embargos Declaratórios, enfrentado o ponto OMISSO, conferido efeitos integrativos para o fim " +
                                 "de prover integralmente, tudo por ser medida de direito e irretorquível JUSTIÇA!",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            }
        ]
    elif tese=='tese6':
        elementos = [
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "heading", "texto": [
                {
                    "descricao": "DA SÍNTESE DOS FATOS E DA OMISSÃO",
                    "posicao": "primeira",
                    "estilo": "estilo1"
                }]
            },
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Com a mais a respeitosa vênia, na decisão proferida V. Exa. não se manifestou, expressamente, sobre " +
                                 "pontos importantes levantados na contestação, a respeito dos quais, deveria ter-se pronunciado, " +
                                 "justificando o cabimento dos presentes Embargos de Declaração, para que lhes confira os efeitos " +
                                 "integrativos ao respeitável [[1msiiidecisum.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Conforme sustentado pela Embargante em sua peça de bloqueio o direito postulatório está " +
                                 "IRREMEDIAVELMENTE PRESCRITO.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Verifica-se tal OMISSÃO, que deve ser suprida ou sanada por meio dos presentes embargos, sendo certo " +
                                 "que o recurso não objetiva rediscutir a matéria, mas afastar os vícios constatados no julgado.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Conforme amplamente demonstrado nos autos, trata-se, da chamada “prescrição extintiva”, donde se " +
                                 "depreende que o não uso do direito no tempo previsto, acarreta sua perda.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Neste ponto a r. sentença não dedicou uma palavra sequer à esta questão amplamente invocada." +
                                 "Quedando-se omisso a este respeito e merecendo reforma.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "São essas as razões pelas quais a embargante confia, espera e requer sejam acolhidos e providos os " +
                                 "presentes Embargos Declaratórios, enfrentado o ponto OMISSO, conferido efeitos integrativos para o fim " +
                                 "de prover integralmente, tudo por ser medida de direito e irretorquível JUSTIÇA!",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            }
        ]
    elif tese=='tese7':
        elementos = [
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "heading", "texto": [
                {
                    "descricao": "DA SÍNTESE DOS FATOS E DA OMISSÃO",
                    "posicao": "primeira",
                    "estilo": "estilo1"
                }]
            },
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Sem adentrar ao mérito da decisão, informa a V. Exa. que constou na parte dispositiva desta o seguinte:",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },
            {
                "tipo": "texto_manual", "texto": [
                {
                    "descricao": "COLACIONAR SENTENÇA",
                    "posicao": "primeira",
                    "estilo": "estilo3"
                }]
            },
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Com a mais a respeitosa vênia, assim o fazendo, afigura-se a v. decisão omissa em pontos essenciais," +
                                 "justificando o cabimento dos presentes Embargos de Declaração, a fim de que essa V. Exa. decida-os e" +
                                 "confira os efeitos integrativos ao respeitável [[1msiiidecisum.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Frisa-se que na d. decisão exarada , verifica-se grave OMISSÃO, que devem ser supridas ou sanadas por" +
                                 "meio dos presentes embargos, sendo certo que o recurso não objetiva rediscutir a matéria, mas afastar os" +
                                 "vícios constatados no julgado.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "heading", "texto": [
                {
                    "descricao": "RAZÕES DE EMBARGOS DE DECLARAÇÃO",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao":"Ocorre que na presente demanda que já houve pagamento administrativo no "+
                    "caso em tela, a Embargante, reitera que [[1msuuuo pagamento foi realizado em favor do Embargado, "+
                    "conforme consta dos documentos acostados – isto, após meticulosa análise da documentação "+
                    "apresentada foi liberado o valor da indenização na monta de [[1msbbu"+dados_compl['pagamento_adm']+", "+
                    "[[1msuuutrazemos a colação o comprovante de pagamento, vejamos:",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "texto_manual", "texto": [
                {
                    "descricao": "COLACIONAR O RECIBO DO PAGAMENTO ADM",
                    "posicao": "primeira",
                    "estilo": "estilo3"
                }]
            },
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Portanto, necessária a apreciação das provas trazidas ao processo pela ora Embargante, uma vez que não" +
                                 "foi considerado pelo juízo sentenciante que o pagamento administrativo ora noticiado.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao":"Destaca-se que o seguro DPVAT é alvo de fraudes a todo instante! Não que seja o caso desses autos, mas as evidencias se relevam como tentativa da requerente em receber valor além do estabelecido por lei, ocultando o fato de já ter recebido a quantia de [[1msbbu"+dados_compl['pagamento_adm']+"[[1m na via administrativa.",
                                 
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Ressalte-se que a Embargante não está se omitindo ou procrastinando na presente demanda, muito pelo" +
                                 "contrário, busca a veracidade dos fatos, para a perfeita aplicação da justiça.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "De acordo com os documentos anexados pela Embargante, nota-se que o pagamento da indenização ora" +
                                 "pleiteada já foi objeto de análise e pagamento em sede administrativa.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "heading", "texto": [
                {
                    "descricao": "DO PEDIDO",
                    "posicao": "primeira",
                    "estilo": "estilo1"
                }]
            },
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Diante do exposto, requer sejam acolhidos e providos os presentes Embargos Declaratórios, enfrentado-se" +
                                 "os pontos omissos suscitados, conferido-lhes efeitos integrativos, por via de consequência modificativos," +
                                 "para o fim de prover integralmente, para que sobre eles se pronuncie esse Ilustre Julgador, tudo por ser" +
                                 "medida de direito e justiça.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            }
        ]
    elif tese=='tese8':
        elementos = [
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "heading", "texto": [
                {
                    "descricao": "DA SÍNTESE DOS FATOS E DA OMISSÃO",
                    "posicao": "primeira",
                    "estilo": "estilo1"
                }]
            },
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Com a mais a respeitosa vênia, na decisão proferida V. Exa. não se manifestou, expressamente, sobre" +
                                 "pontos importantes levantados nos autos, a respeito dos quais, deveria ter-se pronunciado, justificando o" +
                                 "cabimento dos presentes Embargos de Declaração, para que lhes confira os efeitos integrativos ao " +
                                 "respeitável [[1msiiidecisum.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Conforme sustentado pela Embargante em sua peça de bloqueio a parte Embargada estava inadimplente" +
                                 "com o Seguro DPVAT. Verifica-se tal OMISSÃO, que deve ser suprida ou sanada por meio dos presentes" +
                                 "embargos, sendo certo que o recurso não objetiva rediscutir a matéria, mas afastar os vícios constatados" +
                                 "no julgado.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Conforme amplamente demonstrado, estando o pagamento do DPVAT em atraso, o veículo não é" +
                                 "considerado licenciado, o proprietário deixa de ter direito à cobertura em caso de acidente e, o proprietário" +
                                 "é obrigado a ressarcir as indenizações eventualmente pagas às vítimas do acidente.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Neste ponto a r. Decisão não dedicou uma palavra sequer à esta questão amplamente invocada nos autos." +
                                 "Quedando-se omissa a este respeito e merecendo reforma.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "São essas as razões pelas quais a embargante confia, espera e requer sejam acolhidos e providos os " +
                                 "presentes Embargos Declaratórios, enfrentado o ponto OMISSO, conferido efeitos integrativos para o fim" +
                                 "de prover integralmente, tudo por ser medida de direito e irretorquível JUSTIÇA!",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            }
        ]
    elif tese=='tese9':
        elementos = [
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "heading", "texto": [
                {
                    "descricao": "DA SÍNTESE DOS FATOS E DA OMISSÃO NA DECISÃO PROFERIDA:",
                    "posicao": "primeira",
                    "estilo": "estilo1"
                }]
            },
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Sem adentrar ao mérito da questão informa a V. Exa. que constou na parte dispositiva desta o seguinte:",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },
            {
                "tipo": "texto_manual", "texto": [
                {
                    "descricao": "COLACIONAR SENTENÇA",
                    "posicao": "primeira",
                    "estilo": "estilo3"
                }]
            },
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Com a mais a respeitosa vênia, assim o fazendo, afigura-se a v. decisão omissa em pontos essenciais," +
                                 "justificando o cabimento dos presentes Embargos de Declaração, a fim de que essa V. Exa. decida-os e" +
                                 "confira os efeitos integrativos ao respeitável [[1msiiidecisum.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Frisa-se que no [[1msiiid. decisum[[1m verifica-se grave OMISSÃO, que devem ser supridas ou sanadas por meio dos" +
                                 "presentes embargos, sendo certo que o recurso não objetiva rediscutir a matéria, mas afastar os vícios" +
                                 "constatados no julgado.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "heading", "texto": [
                {
                    "descricao": "DESCABIMENTO DE RENOVAÇÃO DE PLEITO INDENIZATÓRIO",
                    "posicao": "primeira",
                    "estilo": "estilo1"
                }]
            },
            {
                "tipo": "heading", "texto": [
                {
                    "descricao": "LESÃO PREEXISTENTE",
                    "posicao": "primeira",
                    "estilo": "estilo1"
                }]
            },

            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao":"Inicialmente, deve-se sopesar o fato da parte Embargada ter pleiteado "+
                            "judicialmente verba indenizatória DPVAT, cujo processo tramitou na [[1msbbb"+dados_compl['juizo_lpe']+
                            "[[1m, sendo autuado sob o nº. [[1msbbu"+dados_compl['num_proc_lpe']+"[[1m, em virtude de acidente automobilístico "+
                            "ocorrido em "+dados_compl['data_lpe']+".",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },
            
            
            

            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Frisa-se que a parte Embargada requereu o recebimento do Seguro Obrigatório DPVAT nos autos da ação" +
                                 "supracitada em decorrência de [[1msbbb"+dados_compl['desc_lpe']+"[[1m, ou seja, o requerente sustenta seu" +
                                 "pleito indenizatório em lesão idêntica a que fora recebida anteriormente.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Constata-se que os documentos acostados aos autos comprovam que o acidente que ocasionou a" +
                                 "debilidade permanente foi anterior ao narrado na inicial, não havendo, portanto, nexo de causalidade entre" +
                                 "o novo acidente e a lesão apresentada pela parte autora.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Deste modo, é irrefragável que a presente lide tem o mesmo pedido de outra ação que teve o mérito" +
                                 "julgado, uma vez que a parte sequer comprova que houve agravamento da lesão em virtude de um suposto" +
                                 "novo acidente automobilístico.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "São essas as razões pelas quais a embargante confia, espera e requer sejam acolhidos e providos os" +
                                 "presentes Embargos Declaratórios, enfrentado o ponto OMISSO, conferido efeitos integrativos para o fim"
                                 "de prover integralmente, tudo por ser medida de direito e irretorquível JUSTIÇA!",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            }
        ]
    elif tese=='tese10':
        elementos = [
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "heading", "texto": [
                {
                    "descricao": "DA SÍNTESE DOS FATOS E DA OMISSÃO",
                    "posicao": "primeira",
                    "estilo": "estilo1"
                }]
            },
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Sem adentrar ao mérito da sentença, informa a V. Exa. que constou na parte dispositiva desta o seguinte:",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },
            {
                "tipo": "texto_manual", "texto": [
                {
                    "descricao": "COLACIONAR SENTENÇA",
                    "posicao": "primeira",
                    "estilo": "estilo3"
                }]
            },

            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Assim, o i. Magistrado permaneceu silente quanto os pedidos de diligências solicitados pela embargante," +
                                 "qual seja, " + dados_compl['local_diligencia'] + ".",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Neste sentido, em virtude da ausência de análise do argumento relativo a fatos relevantes para o deslinde" +
                                 "da causa, restaram violados os Princípios da Ampla Defesa e do Contraditório, tendo em vista que as" +
                                 "alegações suscitadas quanto as irregularidades ocorridas no processo administrativo não foram objeto de" +
                                 "apreciação por este i. Juízo.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Vale destacar que o cerceamento do direito à produção da prova viola os direitos processuais da" +
                                 "Embargante, direitos instaurados no cerne da própria concepção do Estado de Direito Democrático e" +
                                 "protegidos pela ordem jurídica",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "A Embargante, faz lembrar ao atento juízo que o seguro DPVAT é alvo de milhares de fraudes em todo o" +
                                 "Brasil, não que seja o caso da presente demanda, sem contar que os argumentos da Embargante são de" +
                                 "substancial importância para se desvelar os fatos controvertidos.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Neste sentido requer seja sanada a omissão apontada e V. Exa. se digne a determinar " +
                                 dados_compl['local_diligencia'] + " a" +
                                 "fim de que sejam prestados os devidos esclarecimentos pelos responsáveis, sem prejuízo do" +
                                 "colhimento do depoimento pessoal da parte embargada.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            }
        ]
    elif tese=='tese11':
        elementos = [
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "heading", "texto": [
                {
                    "descricao": "DA SÍNTESE DOS FATOS E DA OMISSÃO",
                    "posicao": "primeira",
                    "estilo": "estilo1"
                }]
            },

            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Sem adentrar ao mérito da sentença, informa a V. Exa. que constou na parte dispositiva desta o seguinte:",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },
            {
                "tipo": "texto_manual", "texto": [
                {
                    "descricao": "COLACIONAR SENTENÇA",
                    "posicao": "primeira",
                    "estilo": "estilo3"
                }]
            },

            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Com a mais a respeitosa vênia, assim o fazendo, afigura-se a v. decisão omissa em pontos essenciais," +
                                 "justificando o cabimento dos presentes Embargos de Declaração, a fim de que essa V. Exa. decida-os e" +
                                 "confira os efeitos integrativos ao respeitável [[1msiiidecisum.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Frisa-se que na d. sentença exarada, verifica-se grave OMISSÃO, que devem ser supridas ou sanadas por" +
                                 "meio dos presentes embargos, sendo certo que o recurso não objetiva rediscutir a matéria, mas afastar os" +
                                 "vícios constatados no julgado.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Com todo o respeito a Embargante, vem, informar que houve omissão quanto a atualização do valor" +
                                 "indenizatório, ou seja, a sentença não se manifestou sobre a data inicial para o compito dos juros.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Em relação aos juros de mora, o Colendo Superior Tribunal de justiça editou a Súmula nº 426 pacificando a" +
                                 "incidência dos juros a partir da citação.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Neste ponto, requer seja verificada a omissão informada, devendo-se esclarecer se o valor arbitrado será " +
                                 "atualizado e caso sim, que seja observado os ditames legais previstos para a matéria in foco.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "heading", "texto": [
                {
                    "descricao": "CONCLUSAO",
                    "posicao": "primeira",
                    "estilo": "estilo1"
                }]
            },
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "São essas as razões pelas quais a embargante confia, espera e requer sejam acolhidos e providos os" +
                                 "presentes Embargos Declaratórios, enfrentado o ponto OMISSO, qual seja o marco inicial para a contagem" +
                                 "dos juros de mora, conferido efeitos integrativos para o fim de prover integralmente, tudo por ser medida" +
                                 "de direito e irretorquível JUSTIÇA!",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            }
        ]
    elif tese=='tese12':
        elementos = [
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "heading", "texto": [
                {
                    "descricao": "DA SÍNTESE DOS FATOS E DA OMISSÃO",
                    "posicao": "primeira",
                    "estilo": "estilo1"
                }]
            },

            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Sem adentrar ao mérito da sentença, informa a V. Exa. que constou na parte dispositiva desta o seguinte:",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },
            {
                "tipo": "texto_manual", "texto": [
                {
                    "descricao": "COLACIONAR SENTENÇA",
                    "posicao": "primeira",
                    "estilo": "estilo3"
                }]
            },

            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Com a mais a respeitosa vênia, assim o fazendo, afigura-se a v. decisão omissa em pontos essenciais," +
                                 "justificando o cabimento dos presentes Embargos de Declaração, a fim de que essa V. Exa. decida-os e" +
                                 "confira os efeitos integrativos ao respeitável [[1msiiidecisum.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Verifica-se grave OMISSÃO, que devem ser supridas ou sanadas por meio dos presentes embargos, sendo" +
                                 "certo que o recurso não objetiva rediscutir a matéria, mas afastar os vícios constatados no julgado.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Com todo o respeito a Embargante, vem, informar que houve omissão quanto a atualização do valor" +
                                 "indenizatório, de certo que o valor principal não venha a sofrer correção monetária, ante a ausência de" +
                                 "previsão legal, posto que não restou caracterizada a hipótese prevista no art. 5º, §7º | Lei nº 6.194/74.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },
            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Sendo diverso o entendimento deste d. juízo, que o termo a quo da correção monetária seja a data da" +
                                 "propositura da ação, na forma do art. 1º, §2º, da Lei 6.899/1981.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "Neste ponto, requer seja verificada a omissão informada, devendo-se esclarecer se o valor arbitrado será " +
                                 "corrigido e caso sim, que seja observado os ditames legais previstos para a matéria in foco.",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            },

            {
                "tipo": "heading", "texto": [
                {
                    "descricao": "CONCLUSÃO",
                    "posicao": "primeira",
                    "estilo": "estilo1"
                }]
            },

            {
                "tipo": "paragrafo", "texto": [
                {
                    "descricao": "São essas as razões pelas quais a embargante confia, espera e requer sejam acolhidos e providos os" +
                                 "presentes Embargos Declaratórios, enfrentado o ponto OMISSO, qual seja o marco inicial para a contagem" +
                                 "da corrção monetária, conferido efeitos integrativos para o fim de prover integralmente, tudo por ser" +
                                 "medida de direito e irretorquível JUSTIÇA!",
                    "posicao": "primeira",
                    "estilo": "estilo2"
                }]
            }
        ]
    return elementos
