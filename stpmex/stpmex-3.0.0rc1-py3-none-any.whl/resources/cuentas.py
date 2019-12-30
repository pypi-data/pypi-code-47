import datetime as dt
import unicodedata
from typing import Any, ClassVar, Dict, Optional

from pydantic import conint, constr, validator
from pydantic.dataclasses import dataclass

from ..auth import CUENTA_FIELDNAMES, compute_signature, join_fields
from ..types import Clabe, Genero, digits, truncated_str
from .base import Resource


@dataclass
class Cuenta(Resource):
    """
    Based on:
    https://stpmex.zendesk.com/hc/es/articles/360038242071-Registro-de-Cuentas-de-Personas-f%C3%ADsicas
    """

    _endpoint: ClassVar[str] = '/cuentaModule'

    nombre: truncated_str(50)
    apellidoPaterno: truncated_str(50)
    cuenta: Clabe
    rfcCurp: constr(max_length=18)

    apellidoMaterno: Optional[truncated_str(50)] = None
    genero: Optional[Genero] = None
    fechaNacimiento: Optional[dt.date] = None
    # Esperanda para STP que agregan Nacido en Extranjero
    entidadFederativa: Optional[conint(ge=1, le=32)] = None
    actividadEconomica: Optional[conint(ge=28, le=74)] = None
    calle: Optional[truncated_str(60)] = None
    numeroExterior: Optional[digits(max_length=10)] = None
    numeroInterior: Optional[digits(max_length=5)] = None
    colonia: Optional[truncated_str(50)] = None
    alcaldiaMunicipio: Optional[truncated_str(50)] = None
    cp: Optional[digits(5, 5)] = None
    pais: Optional[conint(ge=1, lt=242)] = None
    email: Optional[constr(max_length=150)] = None
    idIdentificacion: Optional[digits(max_length=20)] = None
    telefono: Optional[digits(max_length=10)] = None

    id: Optional[int] = None

    @classmethod
    def alta(cls, **kwargs) -> 'Cuenta':
        """Dar de alta"""
        cuenta = cls(**kwargs)
        endpoint = cuenta._endpoint + '/fisica'
        resp = cuenta._client.put(endpoint, cuenta.to_dict())
        cuenta.id = resp['id']
        return cuenta

    def baja(self) -> Dict[str, Any]:
        """Dar de baja"""
        endpoint = self._endpoint + '/fisica'
        data = dict(
            cuenta=self.cuenta,
            empresa=self.empresa,
            rfcCurp=self.rfcCurp,
            firma=self.firma,
        )
        return self._client.delete(endpoint, data)

    @property
    def firma(self):
        joined_fields = join_fields(self, CUENTA_FIELDNAMES)
        return compute_signature(self._client.pkey, joined_fields)

    @validator('nombre', 'apellidoPaterno', 'apellidoMaterno', each_item=True)
    def _unicode_to_ascii(cls, v):
        v = unicodedata.normalize('NFKD', v).encode('ascii', 'ignore')
        return v.decode('ascii')
