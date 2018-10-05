from django.db import models


# Create your models here.


class Documento(models.Model):
    num_doc = models.CharField(max_length=50)

    def __str__(self):
        return self.num_doc


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=7, decimal_places=2)
    bio = models.TextField()
    photo = models.ImageField(upload_to='clients_photos', null=True, blank=True)
    doc = models.OneToOneField(Documento, null=True, blank=True, on_delete=models.CASCADE,)

    def __str__(self):
        return self.first_name


class Produto(models.Model):
    descricao = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.descricao


class Venda(models.Model):
    numero = models.CharField(max_length=7)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    desconto = models.DecimalField(max_digits=7, decimal_places=2)
    impostos = models.DecimalField(max_digits=7, decimal_places=2)
    pessoa = models.ForeignKey(Person, null=True, blank=True, on_delete=models.PROTECT)
    produtos = models.ManyToManyField(Produto, blank=True)

    def __str__(self):
        return self.numero


class Py_Log_mssql(models.Model):
    _DATABASE = 'mssql'
    class Meta:

        db_table = "[DW].[PY_LOG]"
        #print(db_table)
    pylog_id = models.IntegerField(primary_key=True)
    pylog_etapa_id = models.IntegerField()
    pylog_desc = models.CharField(max_length=200)
    pylog_datetime = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.title


class Sistema_Reload_mssql(models.Model):
    _DATABASE = 'mssql'
    class Meta:

        db_table = "[DW].[SISTEMA_RELOAD]"

    sistema_id = models.IntegerField(primary_key=True)
    sistema_database = models.CharField(max_length=50)
    sistema_server = models.CharField(max_length=15)
    sistema_dw_desc = models.CharField(max_length=50)
    sistema_datetime_start = models.DateTimeField(auto_now=False)
    sistema_datetime_finish = models.DateTimeField(auto_now=False)
    sistema_erro_flag = models.BooleanField()
    def __str__(self):
        return self.title