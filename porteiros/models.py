from django.db import models


class Concierge(models.Model):

    user = models.OneToOneField(
        "usuarios.User",
        verbose_name="Usuario",
        on_delete=models.PROTECT,
        null=False,
    )

    full_name = models.CharField(
        verbose_name="Nome Completo",
        max_length=194,
        null=False,
    )

    cpf = models.CharField(
        verbose_name="CPF",
        max_length=11,
        null=False,
    )

    phone = models.CharField(
        verbose_name="Telefone de Contato",
        max_length=11,
        null=False,
    )

    birth_date = models.DateField(
        verbose_name="Data de Nascimento",
        auto_now_add=False,
        auto_now=False,
        null=False,
    )

    class Meta:
        verbose_name = "Concierge"
        verbose_name_plural = "Concierges"
        db_table = "concierge"

    def __str__(self):
        return self.full_name
