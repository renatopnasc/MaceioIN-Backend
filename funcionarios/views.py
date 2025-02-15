from .serializers import FuncionarioSerializer
from rest_framework import generics
from .models import Funcionario
from rest_framework.response import Response


class FuncionarioList(generics.ListAPIView):    
    queryset = Funcionario.objects.all().order_by("nome")
    serializer_class = FuncionarioSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({"funcionarios": serializer.data})