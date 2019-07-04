from rest_framework import serializers

from .models import Usuario

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para atender las conversiones para Usuario """
    class Meta:
        # Se define sobre que modelo actua
        model = Usuario
        # Se definen los campos a incluir
        fields = ('id', 'nombre', 'apellidos', 'edad', 'genero', 'direccion')