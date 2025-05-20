from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from .llm_client import generar_campania

app = FastAPI()

class CampaniaRequest(BaseModel):
    user_id: str
    nombre_negocio: str
    industria: str
    descripcion_negocio: str
    tipo_contenido: List[str]
    plataformas: List[str]
    objetivo_marketing: str
    publico_objetivo: str
    tono: str
    idioma: str
    presupuesto_campana: float
    duracion_video_seg: int
    logo_url: str
    historial_contextual: bool

@app.post("/generar-campania")
async def crear_campania(payload: CampaniaRequest):
    try:
        resultado = generar_campania(payload.dict())
        return {"respuesta": resultado}
    except Exception as e:
        return {"error": str(e)}
