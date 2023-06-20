import os


def strSqlServer():
     server = os.environ.get('SQL_SERVER')
     database = os.environ.get('SQL_DATABASE')
     username = os.environ.get('SQL_USERNAME')
     password = os.environ.get('SQL_PASSWORD')
     return 'DRIVER={'+os.environ.get('SQL_DRIVER')+'};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password +';TrustServerCertificate=Yes'



def strMySql():
     lista1=['user','password','host','database']
     lista2=[os.environ.get('MYSQL_USER'),os.environ.get('MYSQL_PASSWORD'),os.environ.get('MYSQL_HOST'),os.environ.get('MYSQL_DATABASE')]
     return dict(zip(lista1,lista2))
