from typing import Any, List

from Exceptions.ArgumentQuantityException import (
    insufficient_arguments,
    too_many_arguments,
)
from Exceptions.InsufficientArgumentException import InsufficientArgumentException
from Exceptions.TooManyArgumentsException import TooManyArgumentsException
from pydantic import BaseModel, Field, field_validator
from typing_extensions import Annotated


class OptionConfiguration(BaseModel):
    parsing_function: Any
    process_function: Any = None
    max_number_of_arguments: Annotated[int, Field(ge=0)] = 0
    min_number_of_arguments: Annotated[int, Field(ge=0)] = 0


class OptionDefinition(BaseModel):
    name: str
    flag: str
    description: str = None
    value: Any = None
    arguments: List[str] = []
    configs: OptionConfiguration

    @field_validator("arguments")
    def validate_the_quantity_of_arguments(cls, arguments: List[str]):
        config = cls.model_fields.get("configs").get_default(call_default_factory=True)

        if too_many_arguments(arguments, config.max_number_of_arguments):
            raise TooManyArgumentsException(cls.model_fields.get("name"))

        if insufficient_arguments(arguments, config.min_number_of_arguments):
            raise InsufficientArgumentException(cls.model_fields.get("name"))
        return arguments
