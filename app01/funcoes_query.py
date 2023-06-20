import pyodbc as p
from . import stringConnexao
from . import funcoes



def faturamento_01(datas):
    db_connection = p.connect(stringConnexao.strSqlServer())
    cursor = db_connection.cursor()
    cursor.execute("Select p.id_pasta,p.pasta,p.cod_cliente,\
    case when s1.fase IS NOT NULL then 'Sim' else 'Não' end as fase1,\
    case when s2.fase IS NOT NULL then 'Sim' else 'Não' end as fase2,\
    case when s3.fase IS NOT NULL then 'Sim' else 'Não' end as fase3,\
    case when s4.fase IS NOT NULL then 'Sim' else 'Não' end as exito,\
    case when s3.valor IS NOT NULL then s3.valor else 0 end as valor_fase3,\
    case when s4.valor IS NOT NULL then s4.valor else 0 end as valor_exito,\
    convert(varchar(10),s3.data_alteracao,103) as data_alteracao,\
    convert(varchar(10),s3.data_aprovacao,103) as data_aprovacao,\
    convert(varchar(10),t.data_alt,103) as data_alt, \
    dbo.dadosDaTramitacao(t.id_pasta,t.id_tramitacao,'desc_codigo_fase1') as desc_status1,\
    dbo.dadosDaTramitacao(t.id_pasta,t.id_tramitacao,'desc_codigo_fase2') as desc_status2,\
    dbo.dadosDaTramitacao(t.id_pasta,t.id_tramitacao,'desc_status3') as desc_status3, \
    convert(varchar(10),t.dat_evento,103) as data_tramitacao \
    from pastas p inner join tramitacoes t on t.id_pasta=p.id_pasta and t.id_cadtramitacao=481 and t.bativo=1 \
    left join sitCobranca s1 on s1.id_pasta=p.id_pasta and s1.fase='1P' \
    left join sitCobranca s2 on s2.id_pasta=p.id_pasta and s2.fase='2P' \
    left join sitCobranca s3 on s3.id_pasta=p.id_pasta and s3.fase='3P' \
    left join sitCobranca s4 on s4.id_pasta=p.id_pasta and s4.fase='4P' \
    where t.dat_evento between ? and ?",[datas['data_inicial_evento'],datas['data_final_evento']])
    return funcoes.dictfetchall(cursor)



def p_encerradas_situacao_01(datas,lote):

    data_i = datas['data_inicial_evento']
    data_f=datas['data_final_evento']+' 23:55:55'
    db_connection = p.connect(stringConnexao.strSqlServer())
    cursor = db_connection.cursor()
    cursor.execute("Select p.id_pasta,p.pasta,p.cod_cliente,\
    case when s1.fase IS NOT NULL then 'Sim' else 'Não' end as fase1,\
    case when s2.fase IS NOT NULL then 'Sim' else 'Não' end as fase2,\
    case when s3.fase IS NOT NULL then 'Sim' else 'Não' end as fase3,\
    case when s4.fase IS NOT NULL then 'Sim' else 'Não' end as exito,\
    convert(varchar(10),s3.data_alteracao,103) as data_alteracao,\
    convert(varchar(10),s3.data_aprovacao,103) as data_aprovacao,\
    convert(varchar(10),t.data_alt,103) as data_alt, \
    dbo.dadosDaTramitacao(t.id_pasta,t.id_tramitacao,'desc_codigo_fase1') as desc_status1,\
    dbo.dadosDaTramitacao(t.id_pasta,t.id_tramitacao,'desc_codigo_fase2') as desc_status2,\
    dbo.dadosDaTramitacao(t.id_pasta,t.id_tramitacao,'desc_status3') as desc_status3, \
    convert(varchar(10),t.dat_evento,103) as data_tramitacao \
    from pastas p inner join tramitacoes t on t.id_pasta=p.id_pasta and t.id_cadtramitacao=481 and t.bativo=1 \
    inner join tab_faturamento ft on ft.chave=p.pasta \
    left join sitCobranca s1 on s1.id_pasta=p.id_pasta and s1.fase='1P' \
    left join sitCobranca s2 on s2.id_pasta=p.id_pasta and s2.fase='2P' \
    left join sitCobranca s3 on s3.id_pasta=p.id_pasta and s3.fase='3P' \
    left join sitCobranca s4 on s4.id_pasta=p.id_pasta and s4.fase='4P' \
    where ft.lote = ? and t.dat_evento between ? and ?",[lote,data_i,data_f])
    return funcoes.dictfetchall(cursor)


def p_encerradas_situacao_02(lista,datas):

    data_i = datas['data_inicial_evento']
    data_f=datas['data_final_evento']+' 23:55:55'
    id_pasta=1222
    lista_tupla=tuple(lista)
    db_connection = p.connect(stringConnexao.strSqlServer())
    cursor = db_connection.cursor()
    q_string=f"Select p.id_pasta,p.pasta,p.cod_cliente,\
    case when s1.fase IS NOT NULL then 'Sim' else 'Não' end as fase1,\
    case when s2.fase IS NOT NULL then 'Sim' else 'Não' end as fase2,\
    case when s3.fase IS NOT NULL then 'Sim' else 'Não' end as fase3,\
    case when s4.fase IS NOT NULL then 'Sim' else 'Não' end as exito,\
    convert(varchar(10),s3.data_alteracao,103) as data_alteracao,\
    convert(varchar(10),s3.data_aprovacao,103) as data_aprovacao,\
    convert(varchar(10),t.data_alt,103) as data_alt, \
    dbo.dadosDaTramitacao(t.id_pasta,t.id_tramitacao,'desc_codigo_fase1') as desc_status1,\
    dbo.dadosDaTramitacao(t.id_pasta,t.id_tramitacao,'desc_codigo_fase2') as desc_status2,\
    dbo.dadosDaTramitacao(t.id_pasta,t.id_tramitacao,'desc_status3') as desc_status3, \
    convert(varchar(10),t.dat_evento,103) as data_tramitacao \
    from pastas p inner join tramitacoes t on t.id_pasta=p.id_pasta and t.id_cadtramitacao=481 and t.bativo=1 \
    left join sitCobranca s1 on s1.id_pasta=p.id_pasta and s1.fase='1P' \
    left join sitCobranca s2 on s2.id_pasta=p.id_pasta and s2.fase='2P' \
    left join sitCobranca s3 on s3.id_pasta=p.id_pasta and s3.fase='3P' \
    left join sitCobranca s4 on s4.id_pasta=p.id_pasta and s4.fase='4P' \
    where p.pasta in {lista_tupla}"
    cursor.execute(q_string)
    return funcoes.dictfetchall(cursor)


def conferencia_hr(lote):
    db_connection = p.connect(stringConnexao.strSqlServer())
    cursor = db_connection.cursor()
    cursor.execute("select item,s.cod_cliente,p.pasta,\
    case when s.fase='3ª Fase' and valor_exito>0 then '3ª Fase e Exito' else s.fase end as fase,\
    s.valor,s.valor_exito,s.cod_erro \
    as observacao,case when cod_erro='cadastro ok' then '' else 'Erro' end mensagem \
    from tab_sitConferencia s left join pastas p on p.id_pasta=s.id_pasta \
    where lote = ? order by s.item" , [lote])
    return funcoes.dictfetchall(cursor)

