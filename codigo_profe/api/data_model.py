from pydantic import BaseModel

class DataModel(BaseModel):

    latitud: float
    longitud: float
    AnioConstruccion: float
    TarifaServicio: float
    MinimoDias: float
    Disponibilidad_365: float
    ReservaEnLinea: int
    Localidad: str
    TipoInmueble:str
    PoliticaCancelacion: str
