# Generated by Django 2.2.5 on 2019-09-29 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('status', models.BooleanField(verbose_name='Status')),
                ('env', models.CharField(max_length=20, verbose_name='Env')),
                ('version', models.CharField(max_length=5, verbose_name='Versão')),
                ('address', models.CharField(max_length=39, verbose_name='Endereço')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('last_login', models.DateTimeField(verbose_name='Last Login')),
                ('email', models.CharField(max_length=254, verbose_name='Email')),
                ('password', models.CharField(max_length=50, verbose_name='Senha')),
            ],
        ),
        migrations.CreateModel(
            name='GroupUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='groupUsers', to='api.Group')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='groupUsers', to='api.User')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=20, verbose_name='Level')),
                ('data', models.TextField(verbose_name='Dados')),
                ('arquivado', models.BooleanField(verbose_name='Arquivado')),
                ('date', models.DateTimeField(verbose_name='Data')),
                ('agent_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='events', to='api.Agent')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='events', to='api.User')),
            ],
        ),
    ]