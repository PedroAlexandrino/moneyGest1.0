# Generated by Django 4.2.2 on 2023-10-26 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0002_transacao_carteira_valor_pago_alter_carteira_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='transacao_carteira',
            name='quantidade',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='transacao_carteira',
            name='carteira',
            field=models.ManyToManyField(null=True, to='perfil.carteira'),
        ),
    ]
