from typing import Annotated

from pydantic import Field
from workout_api.contrib.schemas import BaseSchema


class CentroTreinamentoSchema(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', example='CT Iron Berg', max_length=20)]
    endereco: Annotated[str, Field(description='Endereço do centro de treinamento', example='Rua X, Q10', max_length=60)]
    proprietario: Annotated[str, Field(description='Proprietário do centro de treinamento', example='Cariri', max_length=30)]