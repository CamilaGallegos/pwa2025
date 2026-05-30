from rest_framework import mixins
from rest_framework import generics
from .models import carrera
from .serializers import carreraSerializer

# api rest crear y listar carreras
class carreraMixin(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   generics.GenericAPIView):
    
    queryset = carrera.objects.all()
    
    serializer_class = carreraSerializer

    # peticiones GET (listar)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # peticiones POST (crear)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)