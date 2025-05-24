from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from llm_client import generar_campania
from mangum import Mangum
from fastapi.openapi.docs import get_swagger_ui_html

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
    
@app.get("/documentation", include_in_schema=False)
async def custom_swagger_ui_html():
    """Custom Swagger UI HTML."""
    openapi_url = "/Prod/openapi.json"
    print(openapi_url)
    return get_swagger_ui_html(openapi_url=openapi_url, title="")


handler = Mangum(app)