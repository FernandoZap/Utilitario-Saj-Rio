from  django.urls import include, path
from django.contrib import admin
from . import views as v1

app_name = 'app01'

urlpatterns = [
    path('tramitacoes', v1.v001_cadastro_tramitacoes, name='cadastro_tramitacoes'),
    path('dadosGeraisDoProcesso', v1.v002_dadosGeraisDoProcesso, name='dadosGeraisDoProcesso'),  
    path('baseAtiva', v1.v008_baseAtiva, name='baseAtiva') ,
    path('inserir-hr', v1.v010_honRecebidos, name="inserir-hon-recebidos"),
    path('honorarios', v1.v011_honorarios, name="honorarios"),
    path('honpericiais', v1.v003_honorariosPericiais, name='incluirHp'), 
    path('amarracao/', v1.view003_amarracao, name='v_amarracao'),
    path('decisao_rel/', v1.view004_reldecisao, name='vv_decisao'),
    path('decisao_ajax_01/', v1.view006_decisoes_ajax, name="ajax01"),
    path('decisao_ajax_02/', v1.view007_decisoes_ajax, name="ajax02"),
    path('custas', v1.v009_custas, name="custas_status"),
    path('faturamento', v1.v012_faturamento, name="faturamento"),
    path('p_encerradas',v1.v014_p_encerradas,name='p_encerradas'),
    path('abrirDocumento/<int:id_arquivo>', v1.v013_abrirDocumento, name="abrirDocumento"),
    path('conferencia-hr', v1.v015_conferencia_hr, name="conferencia-hr"),

]
