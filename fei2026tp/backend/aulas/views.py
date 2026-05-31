from rest_framework import mixins
from rest_framework import generics
from .models import carrera, profesor
from .serializers import carreraSerializer, profesorSerializer

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
    
# api rest detalle, actualizar y eliminar profesor
class profesorMixinDetail(mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          generics.GenericAPIView):
    
    queryset = profesor.objects.all()
    
    serializer_class = profesorSerializer

    # peticiones GET (detalle)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    # peticiones PUT (completo) o PATCH (algun campo) para actualizar
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    # peticiones DELETE (eliminar)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)