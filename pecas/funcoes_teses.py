
def f002_teses_embargos_omissao(respostas,teses):
    if respostas['intimacao_mp']=='N':
        teses['tese2']='S'
    if respostas['cj_peremp_litisp']=='1':
        teses['tese3']='S'
    elif respostas['cj_peremp_litisp']=='2':
        teses['tese4']='S'
    elif respostas['cj_peremp_litisp']=='3':
        teses['tese5']='S'
    if respostas['prescricao']=='S':
        teses['tese6']='S'
    if respostas['pagamento_adm']=='N':
        teses['tese7']='S'
    if respostas['prop_inadimp_com_pagto_Adm']=='N':
        teses['tese8']='S'
    if respostas['lesao_pre']=='S':
        teses['tese9']='S'
    if respostas['omissao']=='S':
        teses['tese10']='S'
    if respostas['juros_citacao']=='2':
        teses['tese11']='S'
    if respostas['correcao']=='2':
        teses['tese12']='S'
    return teses
