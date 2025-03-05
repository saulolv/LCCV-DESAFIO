from django.db import models
from django.core.validators import MinValueValidator


class Financiador(models.Model):
    """Modelo que representa os financiadores dos projetos"""
    id_financiador = models.AutoField(primary_key=True)
    financiador = models.CharField(max_length=100, verbose_name='Financiador')

    class Meta:
        verbose_name = 'Financiador'
        verbose_name_plural = 'Financiadores'
        ordering = ['financiador']

    def __str__(self):
        return self.financiador


class AreaTecnologica(models.Model):
    """Modelo que representa as áreas tecnológicas dos projetos"""
    id_area_tecnologica = models.AutoField(primary_key=True)
    area_tecnologica = models.CharField(max_length=100, verbose_name='Área Tecnológica')

    class Meta:
        verbose_name = 'Área Tecnológica'
        verbose_name_plural = 'Áreas Tecnológicas'
        ordering = ['area_tecnologica']

    def __str__(self):
        return self.area_tecnologica


class Colaborador(models.Model):
    """Modelo que representa os colaboradores dos projetos"""
    id_colaborador = models.AutoField(primary_key=True)
    cpf = models.CharField(max_length=14, verbose_name='CPF', unique=True)
    nome = models.CharField(max_length=100, verbose_name='Nome')
    dt_nascimento = models.DateField(verbose_name='Data de Nascimento')

    class Meta:
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'
        ordering = ['nome']

    def __str__(self):
        return f"{self.nome} (CPF: {self.cpf})"


class Projeto(models.Model):
    """Modelo que representa os projetos"""
    id_projeto = models.AutoField(primary_key=True)
    projeto = models.CharField(max_length=100, verbose_name='Nome do Projeto')
    id_financiador = models.ForeignKey(
        Financiador, 
        on_delete=models.PROTECT, 
        related_name='projetos',
        verbose_name='Financiador'
    )
    id_area_tecnologica = models.ForeignKey(
        AreaTecnologica, 
        on_delete=models.PROTECT, 
        related_name='projetos',
        verbose_name='Área Tecnológica'
    )
    coordenador = models.CharField(max_length=100, verbose_name='Coordenador')
    ativo = models.BooleanField(default=True, verbose_name='Ativo')
    inicio_vigencia = models.DateField(verbose_name='Início da Vigência')
    fim_vigencia = models.DateField(verbose_name='Fim da Vigência')
    valor = models.DecimalField(
        max_digits=15, 
        decimal_places=2, 
        verbose_name='Valor', 
        validators=[MinValueValidator(0)]
    )
    qtd_membros = models.IntegerField(
        default=0, 
        verbose_name='Quantidade de Membros',
        editable=False,  # Campo não editável diretamente
    )
    equipe = models.ManyToManyField(
        Colaborador,
        related_name='projetos',
        verbose_name='Equipe',
        blank=True
    )

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
        ordering = ['-inicio_vigencia']

    def __str__(self):
        return f"{self.projeto} - {self.coordenador}"