from django.contrib import admin
from core.models import Financiador, AreaTecnologica, Colaborador, Projeto


@admin.register(Financiador)
class FinanciadorAdmin(admin.ModelAdmin):
    list_display = ('id_financiador', 'financiador')
    search_fields = ('financiador',)


@admin.register(AreaTecnologica)
class AreaTecnologicaAdmin(admin.ModelAdmin):
    list_display = ('id_area_tecnologica', 'area_tecnologica')
    search_fields = ('area_tecnologica',)


@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ('id_colaborador', 'nome', 'cpf', 'dt_nascimento')
    search_fields = ('nome', 'cpf')
    list_filter = ('dt_nascimento',)


class ColaboradorInline(admin.TabularInline):
    model = Projeto.equipe.through
    extra = 1
    verbose_name = 'Membro da Equipe'
    verbose_name_plural = 'Membros da Equipe'


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = (
        'id_projeto', 'projeto', 'coordenador', 'id_financiador', 
        'id_area_tecnologica', 'ativo', 'inicio_vigencia', 'fim_vigencia', 
        'valor', 'qtd_membros'
    )
    list_filter = ('ativo', 'id_financiador', 'id_area_tecnologica', 'inicio_vigencia')
    search_fields = ('projeto', 'coordenador')
    inlines = [ColaboradorInline]
    exclude = ('equipe',)  # Excluímos o campo equipe pois usamos o inline
    readonly_fields = ('qtd_membros',)