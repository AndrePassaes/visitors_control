# Generated by Django 4.2.2 on 2023-09-15 01:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("porteiros", "0002_alter_concierge_options_concierge_birth_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="concierge",
            name="birth_date",
            field=models.DateField(verbose_name="Data de Nascimento"),
        ),
        migrations.AlterField(
            model_name="concierge",
            name="cpf",
            field=models.CharField(max_length=11, verbose_name="CPF"),
        ),
        migrations.AlterField(
            model_name="concierge",
            name="full_name",
            field=models.CharField(max_length=194, verbose_name="Nome Completo"),
        ),
        migrations.AlterField(
            model_name="concierge",
            name="phone",
            field=models.CharField(max_length=11, verbose_name="Telefone de Contato"),
        ),
        migrations.AlterField(
            model_name="concierge",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.PROTECT,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Usuario",
            ),
        ),
    ]