# Generated by Django 3.0.6 on 2020-05-31 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finan', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classifica_pagar',
            name='pagar',
        ),
        migrations.RemoveField(
            model_name='forma_pagar',
            name='pagar',
        ),
    ]