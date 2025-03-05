from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from core.models import Projeto


@receiver(m2m_changed, sender=Projeto.equipe.through)
def update_qtd_membros(sender, instance, action, **kwargs):
    """
    Signal para atualizar automaticamente o campo qtd_membros
    quando a relação M2M com Colaboradores for alterada
    """
    if action in ['post_add', 'post_remove', 'post_clear']:
        instance.qtd_membros = instance.equipe.count()
        # Usando update() para evitar um loop infinito
        Projeto.objects.filter(id_projeto=instance.id_projeto).update(
            qtd_membros=instance.qtd_membros
        )