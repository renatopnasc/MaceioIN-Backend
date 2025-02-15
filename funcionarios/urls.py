from django.urls import path

from .views import (
    FuncionarioList
)

urlpatterns = [
    path(
        "funcionarios/",
        FuncionarioList.as_view(),
        name="get-funcionarios",
    ),
]