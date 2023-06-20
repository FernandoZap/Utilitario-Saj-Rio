from django.urls import include, path
from django.contrib import admin
from . import views as v1

app_name = 'pecas'

urlpatterns = [
    path('download/<str:docmto>', v1.download_file, name='download'),
    path('v003_ajax', v1.v003_dados_da_pasta, name='v003_ajax'),
    path('peticoes', v1.v004_peticoes,name='peticoes'),
    path('contrarrazoes',v1.v005_contrarrazoes,name='contrarrazoes'),
    path('contrarecapelacao/<str:pasta>',v1.v006_contraRecApelacao,name='contrarecapelacao'),
    path('embargos', v1.v007_embargos,name='embargos'),
    path('embargos/omissao/<str:pasta>/<str:hanulidadepublic>/<str:data_publicacao>:', v1.v008_embargos_omissao, name='embargos-omissao'),
    path('embargos/ultrapetita', v1.v009_embargos_ultrapetita, name='embargos-ultrapetita'),
    path('embargos/contradicao', v1.v010_embargos_contradicao, name='embargos-contradicao'),
    path('peticoes_teste',v1.peticoes_teste, name='peticoes_teste'),

]
