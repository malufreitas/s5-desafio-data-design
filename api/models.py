from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField('Nome', max_length=50) 
    last_login = models.DateTimeField('Last Login')
    email = models.CharField('Email', max_length=254) 
    password = models.CharField('Senha', max_length=50) 


class Agent(models.Model):
    name = models.CharField('Nome', max_length=50)
    status = models.BooleanField('Status') 
    env = models.CharField('Env', max_length=20) 
    version = models.CharField('Versão', max_length=5) 
    address = models.CharField('Endereço', max_length=39) 


class Event(models.Model):
    level = models.CharField('Level', max_length=20) 
    data = models.TextField('Dados') 
    arquivado = models.BooleanField('Arquivado') 
    date = models.DateTimeField('Data')

    agent_id = models.ForeignKey(
        Agent,
        on_delete = models.deletion.DO_NOTHING,
        related_name='events'
    )
    
    user_id = models.ForeignKey(
        User,
        on_delete = models.deletion.DO_NOTHING,
        related_name='events'
    )


class Group(models.Model):
    name = models.CharField('Nome', max_length=50)


class GroupUser(models.Model):
    group_id = models.ForeignKey(
        Group,
        on_delete = models.deletion.DO_NOTHING,
        related_name='groupUsers'
    )

    user_id = models.ForeignKey(
        User,
        on_delete = models.deletion.DO_NOTHING,
        related_name='groupUsers'
    )
