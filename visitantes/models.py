from django.db import models


class Visitor(models.Model):
    full_name = models.CharField(
        verbose_name="Nome completo",
        max_length=100,
        blank=False,
        null=False
    )

    cpf = models.CharField(
        verbose_name="CPF",
        max_length=11,
        null=False
    )

    birth_date = models.DateField(
        verbose_name="Data de nascimento",
        auto_now_add=False,
        auto_now=False,
        null=False
    )

    house_number = models.PositiveBigIntegerField(
        verbose_name="Número da casa a ser visitada",
    )

    license_plate = models.CharField(
        verbose_name="Placa do veículo",
        max_length=7,
        blank=True,
        null=True
    )

    arrival_time = models.DateTimeField(
        verbose_name="Horário de chegada na portaria",
        auto_now_add=True
    )

    left_time = models.DateTimeField(
        verbose_name="Horário de saída da portaria",
        auto_now=False,
        blank=True,
        null=True
    )

    authorization_time = models.DateTimeField(
        verbose_name="Horário de autorização de entrada",
        auto_now=False,
        blank=True,
        null=True
    )

    responsible_resident = models.CharField(
        verbose_name="Nome do morador responsável por autorizar a entrada do visitante",
        max_length=194,
        blank=True,
    )

    registered_by = models.ForeignKey(
        "porteiros.Concierge",
        verbose_name="Responsável pelo registro",
        on_delete=models.PROTECT
    )

    class Meta:
        verbose_name = "Visitor"
        verbose_name_plural = "Visitors"
        db_table = "visitor"

        def __str__(self):
            return self.full_name
