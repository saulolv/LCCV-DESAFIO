from rest_framework import viewsets, generics, status
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter

from core.models import Financiador, AreaTecnologica, Colaborador, Projeto
from core.serializers import (
    FinanciadorSerializer,
    AreaTecnologicaSerializer,
    ColaboradorSerializer,
    ProjetoSerializer,
    ProjetoFormSerializer,
    ProjetoEquipeSerializer,
    ProjetoEquipeUpdateSerializer
)


class FinanciadorViewSet(viewsets.ModelViewSet):
    """
    Viewset para gerenciamento de Financiadores
    """
    queryset = Financiador.objects.all()
    serializer_class = FinanciadorSerializer

    @extend_schema(
        summary="Lista todos os financiadores",
        description="Retorna uma lista de todos os financiadores cadastrados no sistema"
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Cadastra um novo financiador",
        description="Cria um novo financiador com os dados informados"
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary="Visualiza detalhes de um financiador",
        description="Retorna os detalhes de um financiador específico"
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="Atualiza um financiador",
        description="Atualiza todos os dados de um financiador específico"
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        summary="Atualiza parcialmente um financiador",
        description="Atualiza parcialmente os dados de um financiador específico"
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        summary="Remove um financiador",
        description="Exclui um financiador específico do sistema"
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
class AreaTecnologicaViewSet(viewsets.ModelViewSet):
    """
    Viewset para gerenciamento de Áreas Tecnológicas
    """
    queryset = AreaTecnologica.objects.all()
    serializer_class = AreaTecnologicaSerializer

    @extend_schema(
        summary="Lista todas as áreas tecnológicas",
        description="Retorna uma lista de todas as áreas tecnológicas cadastradas no sistema"
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Cadastra uma nova área tecnológica",
        description="Cria uma nova área tecnológica com os dados informados"
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary="Visualiza detalhes de uma área tecnológica",
        description="Retorna os detalhes de uma área tecnológica específica"
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="Atualiza uma área tecnológica",
        description="Atualiza todos os dados de uma área tecnológica específica"
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        summary="Atualiza parcialmente uma área tecnológica",
        description="Atualiza parcialmente os dados de uma área tecnológica específica"
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        summary="Remove uma área tecnológica",
        description="Exclui uma área tecnológica específica do sistema"
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class ColaboradorViewSet(viewsets.ModelViewSet):
    """
    Viewset para gerenciamento de Colaboradores
    """
    queryset = Colaborador.objects.all()
    serializer_class = ColaboradorSerializer

    @extend_schema(
        summary="Lista todos os colaboradores (método padrão)",
        description="Retorna uma lista não paginada de todos os colaboradores cadastrados no sistema"
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Cadastra um novo colaborador (método padrão)",
        description="Cria um novo colaborador com os dados informados"
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary="Visualiza detalhes de um colaborador (método padrão)",
        description="Retorna os detalhes de um colaborador específico"
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="Atualiza um colaborador completamente",
        description="Atualiza todos os dados de um colaborador específico"
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        summary="Remove um colaborador",
        description="Exclui um colaborador específico do sistema"
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    # Os demais métodos já estão documentados no código atual
class ProjetoViewSet(viewsets.ModelViewSet):
    """
    Viewset para gerenciamento de Projetos
    """
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer

    @extend_schema(
        summary="Lista todos os projetos (método padrão)",
        description="Retorna uma lista não paginada de todos os projetos cadastrados no sistema"
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Cadastra um novo projeto (método padrão)",
        description="Cria um novo projeto com os dados informados"
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary="Visualiza detalhes de um projeto (método padrão)",
        description="Retorna os detalhes de um projeto específico"
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="Atualiza um projeto completamente",
        description="Atualiza todos os dados de um projeto específico"
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        summary="Remove um projeto",
        description="Exclui um projeto específico do sistema"
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    # Os demais métodos já estão documentados no código atual
    """
    Viewset para gerenciamento de Projetos
    """
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer

    @extend_schema(
        summary="Retorna dados para formulário de projetos",
        description="Fornece listas de financiadores e áreas tecnológicas para construir formulários"
    )
    @action(detail=False, methods=['get'], url_path='form')
    def form(self, request):
        serializer = ProjetoFormSerializer({})
        return Response(serializer.data)

    @extend_schema(
        summary="Lista todos os projetos",
        description="Retorna uma lista paginada de todos os projetos cadastrados no sistema"
    )
    @action(detail=False, methods=['get'], url_path='listar')
    def listar(self, request):
        page = self.paginate_queryset(self.get_queryset())
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    @extend_schema(
        summary="Cadastra um novo projeto",
        description="Cria um novo projeto com os dados informados"
    )
    @action(detail=False, methods=['post'], url_path='cadastrar')
    def cadastrar(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @extend_schema(
        summary="Inativa um projeto",
        description="Define o status de um projeto como inativo (ativo=False)",
        parameters=[
            OpenApiParameter(name='id', location=OpenApiParameter.PATH, required=True, type=int)
        ]
    )
    @action(detail=True, methods=['post'], url_path='inativar')
    def inativar(self, request, pk=None):
        projeto = self.get_object()
        projeto.ativo = False
        projeto.save()
        return Response({'status': 'projeto inativado'})

    @extend_schema(
        summary="Edita um projeto",
        description="Atualiza os dados de um projeto específico",
        parameters=[
            OpenApiParameter(name='id', location=OpenApiParameter.PATH, required=True, type=int)
        ]
    )
    @action(detail=True, methods=['patch'], url_path='editar')
    def editar(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @extend_schema(
        summary="Visualiza detalhes de um projeto",
        description="Retorna os detalhes de um projeto específico",
        parameters=[
            OpenApiParameter(name='id', location=OpenApiParameter.PATH, required=True, type=int)
        ]
    )
    @action(detail=True, methods=['get'], url_path='visualizar')
    def visualizar(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @extend_schema(
        summary="Visualiza a equipe de um projeto",
        description="Retorna os membros da equipe de um projeto específico",
        parameters=[
            OpenApiParameter(name='id', location=OpenApiParameter.PATH, required=True, type=int)
        ]
    )
    @action(detail=True, methods=['get'], url_path='equipe')
    def equipe(self, request, pk=None):
        instance = self.get_object()
        serializer = ProjetoEquipeSerializer(instance)
        return Response(serializer.data)

    @extend_schema(
        summary="Atualiza a equipe de um projeto",
        description="Atualiza os membros da equipe de um projeto específico",
        parameters=[
            OpenApiParameter(name='id', location=OpenApiParameter.PATH, required=True, type=int)
        ],
        request=ProjetoEquipeUpdateSerializer
    )
    @action(detail=True, methods=['patch'], url_path='equipe/atualizar')
    def atualizar_equipe(self, request, pk=None):
        instance = self.get_object()
        serializer = ProjetoEquipeUpdateSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        # Retorna a equipe atualizada
        response_serializer = ProjetoEquipeSerializer(instance)
        return Response(response_serializer.data)