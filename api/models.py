from django.db import models

from django.core.validators import MinLengthValidator

# Create your models here.

class User(models.Model):
    name = models.CharField('Nome', max_length=50) 
    last_login = models.DateTimeField('Last Login', null=True)
    email = models.EmailField('Email', max_length=254) 
    password = models.CharField('Senha', max_length=50, validators=[MinLengthValidator(8)]) 

    class Meta:
        db_table = 'api_user' 


class Agent(models.Model):
    name = models.CharField('Nome', max_length=50)
    status = models.BooleanField('Status', default=True) 
    env = models.CharField('Env', max_length=20) 
    version = models.CharField('Versão', max_length=5) 
    address = models.GenericIPAddressField('Endereço', max_length=39, protocol='IPv4') 

    class Meta:
        db_table = 'api_agent'


class Event(models.Model):
    level_choices = (
        ('critical', 'CRITICAL'),
        ('debug', 'DEBUG'),
        ('error', 'ERROR'),
        ('warning', 'WARNING'),
        ('info', 'INFO')
    )

    level = models.CharField('Level', max_length=20, choices=level_choices) 
    data = models.TextField('Dados') 
    arquivado = models.BooleanField('Arquivado', default=True) 
    date = models.DateTimeField('Data', null=True)

    agent = models.ForeignKey(
        Agent,
        on_delete = models.deletion.DO_NOTHING,
        related_name='agents'
    )
    
    user = models.ForeignKey(
        User,
        on_delete = models.deletion.DO_NOTHING,
        related_name='users'
    )

    class Meta:
        db_table = 'api_event'


class Group(models.Model):
    name = models.CharField('Nome', max_length=50)

    class Meta:
        db_table = 'api_group'


class GroupUser(models.Model):
    group = models.ForeignKey(
        Group,
        on_delete = models.deletion.DO_NOTHING,
        related_name='groups'
    )

    user = models.ForeignKey(
        User,
        on_delete = models.deletion.DO_NOTHING,
        related_name='users_group'
    )

    class Meta:
        db_table = 'api_group_user'
