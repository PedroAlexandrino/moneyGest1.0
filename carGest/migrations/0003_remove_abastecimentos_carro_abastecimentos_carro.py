# Generated by Django 4.2.2 on 2023-09-28 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carGest', '0002_carro_user_tipocombustivel_preco_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abastecimentos',
            name='carro',
        ),
        migrations.AddField(
            model_name='abastecimentos',
            name='carro',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='carGest.carro'),
        ),
    ]