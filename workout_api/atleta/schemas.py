from typing import Annotated
from pydantic import BaseModel, Field, PositiveFloat

from workout_api.contrib.schemas import BaseSchema


class AtletaSchema(BaseSchema):
    nome: Annotated[str, Field(description='Nome do atleta', examples='Nikolai', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do atleta', examples='12345678900', max_length=11)]
    idade: Annotated[int, Field(description='Idade do atleta', examples=20)]
    peso: Annotated[PositiveFloat, Field(description='Peso do atleta', examples=109.4)]
    altura: Annotated[PositiveFloat, Field(description='Altura do atleta', examples=1.88)]
    sexo: Annotated[str, Field(description='Sexo do atleta', examples='M', max_length=1)]