import pyodbc as p
import os
from . import stringConnexao


def f001_sql(cod_pasta):
    db_connection = p.connect(stringConnexao.strSqlServer())
    db_cursor = db_connection.cursor()
    result=[]

    sql_command =   """
        select p.pasta,p.cod_cliente,
        dbo.desc_autor(p.id_pasta,'NOME') as autor,
        dbo.desc_comarca(p.id_comarca) as comarca,
        dbo.desc_estado(p.id_estado) as uf,
        p.orgao,
        p.num_orgao,
        dbo.desc_juizo(p.num_orgao,p.orgao) as juizo,
        case when secao in ('A','B') then ' - SEÇAO '+secao else '' end as seccao,
        p.nr_processo,
        c.empresa,
        f.oab,
        t01_nome as publicando_nome,t01_oab as publicando_oab,t01_sexo as publicando_sexo,
        ad.nome as conveniado_nome,ad.oab+'/'+ad.estoab as conveniado_oab
        from pastas p left join clientes c on c.id_cliente=p.id_cliente
		 left join cnpjuf f on f.id_estado=p.id_estado
		 left join publicando pub on pub.t01_id=p.id_publicando
		 left join advogados ad on ad.id_advogado=p.id_adv_conveniado
        where p.pasta=?

   """

    try:
        db_cursor.execute(sql_command, [cod_pasta])
        row = db_cursor.fetchone()

        result.append(row[0])
        result.append(row[1])
        result.append(row[2])
        result.append(row[3])
        result.append(row[4])
        result.append(row[5])
        result.append(row[6])
        result.append(row[7])
        result.append(row[8])
        result.append(row[9])
        result.append(row[10])
        result.append(row[11])
        result.append(row[12])
        result.append(row[13])
        result.append(row[14])
        result.append(row[15])
        result.append(row[16])

        db_cursor.close()
        del db_cursor
        db_connection.close()

    except p.IntegrityError:
        print ("Erro na inclusao")
    return result



def f002_sql(cod_pasta):
    db_connection = p.connect(stringConnexao.strSqlServer())
    db_cursor = db_connection.cursor()

    sql_command =   """
        Select * from view_pecasUtilitarios_01 where pasta = ?
    """
    try:
        db_cursor.execute(sql_command,[cod_pasta])
        row = db_cursor.fetchone()
        result = {
            "pasta":row[0],
            "codigoSaj":row[1],
            "cod_cliente":row[2],
            "num_orgao":row[3],
            "orgao":row[4],
            "preposicaoOrgao":row[5],
            "secao":row[6],
            "nr_processo":row[7],
            "valor_inicial":row[8],
            "dat_citacao":row[9],
            "dat_distribuicao":row[10],
            "situacaoSaj":row[11],
            "comarca":row[12],
            "estado":row[13],
            "estadouf":row[14],
            "advConveniado":row[15],
            "oabConveniado":row[16],
            "advExAdverso":row[17],
            "oabExAdverso":row[18],
            "reu":row[19],
            "enderecoReu":row[20],
            "cnpjReu":row[21],
            "coreu":row[22],
            "enderecoCoReu":row[23],
            "cnpjCoReu":row[24],
            "autor":row[25],
            "vitima":row[26],
            "cobertura":row[27],
            "consorcio":row[28],
            "contrato":row[29],
            "merito":row[30],
            "advSupervisor":row[31],
            "oabJbUF":row[32],
            "dataDoAcordo":row[33],
            "valorDoAacordo":row[34],
            "percentualDeSucumbencia":row[35],
            "valorDaParte":row[36],
            "valorHonorariosAdvogado":row[37],
            "representado":row[38],
            "formaDePagamento":row[39],
            "dataReclamacao":row[40],
            "subjudice":row[41],
            "valor_indenizacao":row[42],
            "dataSinistro":row[43],
            "dataSinistroJudicial":row[44],
            "representacao":row[45],
            "dataRegistroBO":row[46],
            "publicando_nome":row[47],
            "publicando_oab":row[48],
            "num_processoSE":row[49],
            "camara_civel":row[50]
        }
        db_cursor.close()
        del db_cursor
        db_connection.close()

    except p.IntegrityError:
        print ("Erro na inclusao")

    return result



def view_pasta(cod_pasta):
    db_connection = p.connect(stringConnexao.strSqlServer())
    db_cursor = db_connection.cursor()
    result=[]

    sql_command =   """
        select * from view_pasta_redator
        where pasta=?
   """

    try:
        db_cursor.execute(sql_command, [cod_pasta])
        row = db_cursor.fetchone()

        result.append(row[0])
        result.append(row[1])
        result.append(row[2])
        result.append(row[3])
        result.append(row[4])
        result.append(row[5])
        result.append(row[6])
        result.append(row[7])
        result.append(row[8])
        result.append(row[9])
        result.append(row[10])
        result.append(row[11])
        result.append(row[12])
        result.append(row[13])
        result.append(row[14])
        result.append(row[15])
        result.append(row[16])
        result.append(row[17])
        result.append(row[18])
        db_cursor.close()
        del db_cursor
        db_connection.close()

    except p.IntegrityError:
        print ("Erro na inclusao")
    return result


