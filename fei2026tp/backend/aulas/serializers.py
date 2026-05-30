from rest_framework import serializers
from .models import carrera, profesor, materia, aula

# serializador de carrera
class carreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = carrera
        fields = '__all__'

# serializador de profesor
class profesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = profesor
        fields = '__all__'

# serializador de materia
class materiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = materia
        fields = '__all__'

# serializador de aula
class aulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = aula
        fields = '__all__' 