# 📈 Generador de Campañas de Growth Marketing con LLM (Together.ai)

Este script usa un modelo de lenguaje grande (LLM) vía Together.ai para generar **campañas de marketing digital creativas y personalizadas**, a partir de los datos de un negocio. La respuesta se devuelve en **formato JSON estructurado**, ideal para usar directamente en frontends, paneles o automatizaciones.

---

## 🚀 ¿Qué hace este proyecto?

- Recibe como entrada un JSON con datos del negocio, objetivos y preferencias.
- Construye dinámicamente un prompt bien detallado y claro.
- Consulta un LLM (por defecto `Mixtral-8x7B-Instruct` de Together.ai).
- Devuelve una **propuesta completa de campaña** con:
  - Concepto creativo
  - Contenidos sugeridos (copy, visual, música)
  - Estrategia por plataforma
  - Segmentación ideal
  - Métricas clave a medir
  - Recomendaciones adicionales de alto valor

---

## 📥 Formato de entrada esperado (`input_data`)

```json
{
  "user_id": "uuid-1234",
  "nombre_negocio": "Zapatos Urban",
  "industria": "Moda",
  "descripcion_negocio": "Tienda online de zapatillas urbanas modernas",
  "tipo_contenido": ["video_promocional", "redes_sociales"],
  "plataformas": ["Instagram", "TikTok", "Meta Ads"],
  "objetivo_marketing": "Engagement",
  "publico_objetivo": "Jóvenes entre 18-25 años que siguen tendencias de moda urbana",
  "tono": "informal",
  "idioma": "es",
  "presupuesto_campana": 500,
  "duracion_video_seg": 30,
  "logo_url": "https://mirael-datalake.s3.amazonaws.com/logos/zapatosurban.png",
  "historial_contextual": true
}

Formato de salida generado por el modelo:

{
  "concepto_central": "Título y descripción creativa de la campaña",
  "contenido_creativo": [
    {
      "tipo": "video_promocional",
      "copy": "Texto publicitario del video",
      "visual": "Descripción de la estética visual",
      "musica": "Sugerencia musical (si aplica)"
    }
  ],
  "estrategia_publicacion": {
    "plataformas": {
      "Instagram": {
        "frecuencia": "3 publicaciones semanales",
        "horario_sugerido": "6-8 PM"
      }
    },
    "duracion_total": "2 semanas"
  },
  "segmentacion_ideal": {
    "edad": "18-25",
    "intereses": ["moda urbana", "zapatillas", "tendencias"],
    "comportamientos": ["usuarios que siguen cuentas de streetwear"]
  },
  "metricas_clave": [
    "CTR",
    "Engagement",
    "Retención de video",
    "Costo por resultado"
  ],
  "recomendaciones_extra": [
    "Usar música en tendencia para aumentar alcance",
    "Agregar llamados a la acción al final del video"
  ]
}


Variables de entorno necesarias
El script usa la API de Together.ai. Necesitás definir:

TOGETHER_API_KEY=tu_api_key_de_together

Instalación:

git clone https://github.com/VictorManuelRodriguezDelahoz-IA/growth_ai.git
cd growth_ai
python -m venv .venv
source .venv/bin/activate  # o .venv\Scripts\activate en Windows
pip install -r requirements.txt


