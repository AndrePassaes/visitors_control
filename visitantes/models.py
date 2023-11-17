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

    house_number = models.PositiveSmallIntegerField(
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

    leave_time = models.DateTimeField(
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
    
    def get_leave_time(self):
        if self.leave_time:
            return self.leave_time
        
        return "Horário de saída não registrado"
    
    def get_authorization_time(self):
        if self.authorization_time:
            return self.authorization_time
        
        return "Visitante aguardando autorização!"
    
    def get_responsible_resident(self):
        if self.responsible_resident:
            return self.responsible_resident
        
        return "Visitante aguardando autorização!"
    
    def get_license_plate(self):
        if self.license_plate:
            return self.license_plate
        
        return "Veículo não registrado"

    class Meta:
        verbose_name = "Visitor"
        verbose_name_plural = "Visitors"
        db_table = "visitor"

    def __str__(self):
        return self.full_name
