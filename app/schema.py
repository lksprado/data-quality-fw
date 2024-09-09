import pandera as pa
from pandera.typing import Index, Series

class SchemaCRM(pa.SchemaModel):
    id_produto: Series[int] = pa.Field(
        ge=1,
        le=10,
        nullable=False
    )
    nome: Series[str] = pa.Field(
        nullable=False
    )
    quantidade: Series[int] = pa.Field(
        ge=20,
        le=200,
        nullable=False
    )
    preco: Series[float] = pa.Field(
        ge=5.0,
        le=120.0,
        nullable=False
    )
    categoria: Series[str] = pa.Field(
        nullable=False
    )
    email: Series[str] = pa.Field(
        nullable=False
    )
    
    class Config:
        coerce = True
        strict = False
