# Generated by Django 4.2.4 on 2023-08-31 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarefa', models.CharField(max_length=20)),
                ('status', models.CharField(choices=[('F', 'menina'), ('M', 'menino')], max_length=12)),
                ('pessoa', models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.CASCADE, to='todo.pessoa')),
            ],
        ),
    ]
