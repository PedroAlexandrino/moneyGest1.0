# Generated by Django 4.2.2 on 2023-09-27 12:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carGest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carro',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tipocombustivel',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='carro',
            name='tipo_combustivel',
            field=models.CharField(max_length=30),
        ),
    ]
