from typing import Any, List

from pydantic import BaseModel, Field, field_validator
from typing_extensions import Annotated

from Exceptions.ArgumentQuantityException import (
    too_many_arguments,
    insufficient_arguments,
)
from Exceptions.InsufficientArgumentException import (
    InsufficientArgumentException,
)
from Exceptions.TooManyArgumentsException import TooManyArgumentsException


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
