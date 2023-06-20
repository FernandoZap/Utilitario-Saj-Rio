# -*- encoding: utf-8 -*-
from django import forms
from django.forms.widgets import Select, Widget
#from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from . import incluirTramitacao,incluirHonPericiais #,historicoLogRoboRE
import datetime
from . import choices
from . models import Decisao_01


class f001_Tramitacoes(forms.Form):
    OPERACAO_CHOICES=(
        ('BRANCO',''),
        ('EXCLUIR','Excluir tramitacao'),
        ('REAGENDAR','Reagendar tramitacao'),
        ('STATUS','Alterar Status'),
        ('INCLUIR','Incluir tramitacoes'),
        ('STATUS/INCLUIR','Alterar Status/Incluir tramitacoes'),
        ('TESTE','Teste')
    )

    operacao = forms.CharField(
        label = 'Operacao',
        widget=forms.Select(choices=OPERACAO_CHOICES),
        max_length=18
        )    
    tramitacao = forms.CharField(
        label = 'Tipo da tramitacao',
        widget=forms.Select(choices=choices.TRAMITACAO),
        max_length=50
        )
    documento = forms.FileField(label='Arquivo Excel')

    def clean_operacao(self):
        operation = self.cleaned_data.get('operacao')
        if(operation=='BRANCO'):
            raise forms.ValidationError("Informe ass operacao")
        return operation

    def execute(self,current_user):
        operacao = self.cleaned_data.get('operacao')
        tramitacao = self.cleaned_data.get('tramitacao')
        planilha = self.cleaned_data.get('documento')
        if(operacao=='INCLUIR' or operacao=='STATUS/INCLUIR'):
            incluirTramitacao.incluir(planilha,operacao,tramitacao,current_user)
        elif (operacao=='REAGENDAR' or operacao=='EXCLUIR'):
            #importarDecisoes3.exc_Tramitacao(planilha,operacao,tramitacao,current_user)
            incluirTramitacao.incluir(planilha,operacao,tramitacao,current_user)
        elif (operacao=='STATUS' or operacao=='STATUS/INCLUIR'):
            #importarDecisoes3.tramitacao_alterarStatus(planilha,operacao,tramitacao,current_user)
            incluirTramitacao.incluir(planilha,operacao,tramitacao,current_user)



class f002_dadosGeraisDoProcesso(forms.Form):
    OPERACAO_CHOICES=(
        ('BRANCO',''),
        ('DP1','Dados do processo'),
    )

    operacao = forms.CharField(
        label = 'Operacao',
        widget=forms.Select(choices=OPERACAO_CHOICES),
        max_length=18
    )    
    documento = forms.FileField(label='Arquivo Excel')

    def execute(self):
        operacao = self.cleaned_data.get('operacao')
        planilha = self.cleaned_data.get('documento')
        return planilha


class f003_HonPericiais(forms.Form):
    OPERACAO_CHOICES=(
        ('BRANCO',''),
        ('EXCLUIR','Excluir honorarios periciais'),
        ('INCLUIR','Incluir honorarios periciais'),
    )

    operacao = forms.CharField(
        label = 'Operacao',
        widget=forms.Select(choices=OPERACAO_CHOICES),
        max_length=18
        )    
    documento = forms.FileField(label='Arquivo Excel')

    def execute(self,current_user):
        operacao = self.cleaned_data.get('operacao')
        planilha = self.cleaned_data.get('documento')
        if (operacao=='INCLUIR'):
            if (1==1):
                incluirHonPericiais.incluirHonPericiais(planilha,operacao,current_user)


class f008_baseAtiva(forms.Form):
    OPERACAO_CHOICES=(
        ('BRANCO',''),
        ('BA1','Base Ativa'),
    )

    operacao = forms.CharField(
        label = 'Operacao',
        widget=forms.Select(choices=OPERACAO_CHOICES),
        max_length=18
    )    

    def execute(self):
        operacao = self.cleaned_data.get('operacao')




class f010_InserirHonRecebidos(forms.Form):
    OPERACAO_CHOICES=(
        ('BRANCO',''),
        ('INSERIR','Inserir'),
        ('TESTE','Teste')
    )

    operacao = forms.CharField(
        label = 'Operacao',
        widget=forms.Select(choices=OPERACAO_CHOICES),
        max_length=18
        )
    fase = forms.CharField(
        label = 'Fase',
        widget=forms.Select(choices=choices.FASES),
        max_length=50
        )

    aba_planilha = forms.CharField(
        label = 'Aba da Planilha',
        widget=forms.Select(choices=choices.ABA_PLANILHA),
        max_length=50
        )


    documento = forms.FileField(label='Arquivo Excel')

    def clean_operacao(self):
        operation = self.cleaned_data.get('operacao')
        if(operation=='BRANCO'):
            raise forms.ValidationError("Informe ass operacao")
        return operation

    def execute(self,current_user):
        operacao = self.cleaned_data.get('operacao')
        fase = self.cleaned_data.get('fase')
        planilha = self.cleaned_data.get('documento')
        '''
        if(operacao=='INSERIR'):
            incluirTramitacao.incluir(planilha,operacao,fase,aba_planilha,current_user)
            '''

class f011_honorarios(forms.Form):
    OPERACAO_CHOICES=(
        ('BRANCO',''),
        ('BA','Toda base ativa'),
        ('PL','Planilha'),
    )

    operacao = forms.CharField(
        label = 'Operacao',
        widget=forms.Select(choices=OPERACAO_CHOICES),
        max_length=18
    )    
    documento = forms.FileField(label='Arquivo Excel')

    def execute(self):
        operacao = self.cleaned_data.get('operacao')
        planilha = self.cleaned_data.get('documento')
        return planilha



class form_amarracao(forms.Form):
    OPERACAO_CHOICES=(
        (0,''),
        (1,'Amarracao'),
    )

    operacao = forms.CharField(
        label = 'Operação',
        widget=forms.Select(choices=OPERACAO_CHOICES),
        max_length=50
    )
    
    plan_pastas = forms.FileField(label='Arquivo Excel Pastas')
    def execute(self,current_user):
        operacao = self.cleaned_data.get('operacao')
        planilha2 = self.cleaned_data.get('plan_pastas')



class Form006_decisao(forms.ModelForm):
            
    class Meta:
        model = Decisao_01
        
        fields = [
            "tipo_decisao",
            "decisao",
            "data_inicial",
            "data_final",
            "estado",
        ]               


class f009_Custas(forms.Form):
    
    OPERACAO_CHOICES=(
        ('BRANCO',''),
        ('CUSTAS','Alterar Status'),
    )

    operacao = forms.CharField(
        label = 'Operacao',
        widget=forms.Select(choices=OPERACAO_CHOICES),
        max_length=18
        )    
    status = forms.CharField(
        label = 'Status',
        widget=forms.Select(choices=choices.CUSTAS_STATUS),
        max_length=50
        )
    documento = forms.FileField(label='Arquivo Excel')

    def clean_operacao(self):
        operation = self.cleaned_data.get('operacao')
        if(operation=='BRANCO'):
            raise forms.ValidationError("Informe ass operacao")
        return operation

