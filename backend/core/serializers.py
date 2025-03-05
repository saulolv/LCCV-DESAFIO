from rest_framework import serializers
from core.models import Financiador, AreaTecnologica, Colaborador, Projeto


class FinanciadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Financiador
        fields = '__all__'


class AreaTecnologicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaTecnologica
        fields = '__all__'


class ColaboradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colaborador
        fields = '__all__'


class ProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projeto
        fields = '__all__'
        read_only_fields = ('qtd_membros',)


class ProjetoFormSerializer(serializers.Serializer):
    """
    Serializer para fornecer dados necessários para construir formulários de projetos
    """
    financiadores = serializers.SerializerMethodField()
    areas_tecnologicas = serializers.SerializerMethodField()

    def get_financiadores(self, obj):
        financiadores = Financiador.objects.all()
        return FinanciadorSerializer(financiadores, many=True).data

    def get_areas_tecnologicas(self, obj):
        areas = AreaTecnologica.objects.all()
        return AreaTecnologicaSerializer(areas, many=True).data


class ProjetoEquipeSerializer(serializers.ModelSerializer):
    """
    Serializer para visualização e atualização da equipe de um projeto
    """
    equipe = ColaboradorSerializer(many=True, read_only=True)
    
    class Meta:
        model = Projeto
        fields = ['id_projeto', 'projeto', 'equipe', 'qtd_membros']
        read_only_fields = ('id_projeto', 'projeto', 'qtd_membros')


class ProjetoEquipeUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer para atualização da equipe de um projeto
    """
    equipe_ids = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True,
        required=True,
        help_text="Lista de IDs dos colaboradores que farão parte da equipe"
    )
    
    class Meta:
        model = Projeto
        fields = ['equipe_ids']
        
    def update(self, instance, validated_data):
        equipe_ids = validated_data.pop('equipe_ids', [])
        
        # Atualiza a equipe do projeto
        if equipe_ids is not None:
            colaboradores = Colaborador.objects.filter(id_colaborador__in=equipe_ids)
            instance.equipe.set(colaboradores)
        
        return instance