# Generated by Django 4.2.2 on 2023-08-21 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoCombustivel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_combustivel', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descricao', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo_carro', models.CharField(max_length=30)),
                ('km_carro', models.IntegerField()),
                ('tipo_combustivel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carGest.tipocombustivel')),
            ],
        ),
        migrations.CreateModel(
            name='Abastecimentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('km_atuais_carro', models.IntegerField()),
                ('litros', models.DecimalField(decimal_places=2, max_digits=10)),
                ('preco_combustivel', models.DecimalField(decimal_places=2, max_digits=10)),
                ('valor_pago', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data', models.CharField(max_length=50, null=True)),
                ('carro', models.ManyToManyField(to='carGest.carro')),
            ],
        ),
    ]