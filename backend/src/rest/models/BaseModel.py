from pydantic import BaseModel as _BaseModel


class BaseModel(_BaseModel):
    """
    Base project API-model
    """
    class Config:
        alias_generator = lambda s: s.split('_')[0] + ''.join(word.capitalize() for word in s.split('_')[1:])
        allow_population_by_field_name = True
