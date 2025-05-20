def construir_prompt(datos):
    return f"""
Tu objetivo como asistente es crear una campaña de growth marketing creativa, eficiente y atractiva para un cliente.

Datos del cliente:
- Nombre del negocio: {datos["nombre_negocio"]}
- Industria: {datos["industria"]}
- Descripción del negocio: {datos["descripcion_negocio"]}
- Público objetivo: {datos["publico_objetivo"]}
- Objetivo de la campaña: {datos["objetivo_marketing"]}
- Plataformas: {", ".join(datos["plataformas"])}
- Tipo de contenido a generar: {", ".join(datos["tipo_contenido"])}
- Duración estimada del video: {datos["duracion_video_seg"]} segundos
- Tono de comunicación: {datos["tono"]}
- Presupuesto aproximado: ${datos["presupuesto_campana"]}
- Idioma: {datos["idioma"]}
- Logo del negocio: {datos["logo_url"]}
- Historial contextual disponible: {"Sí" if datos["historial_contextual"] else "No"}

Quiero que generes una respuesta en formato JSON, estrictamente sin explicaciones adicionales.

El JSON debe contener los siguientes campos:

- concepto_central (string)
- contenido_creativo (lista de objetos con tipo, copy, visual, musica)
- estrategia_publicacion (objeto con plataformas, frecuencia y horarios)
- segmentacion_ideal (objeto con edad, intereses, comportamientos)
- metricas_clave (lista de strings)
- recomendaciones_extra (lista de recomendaciones útiles y creativas para mejorar el impacto)

No incluyas ningún texto fuera del JSON. Solo la respuesta serializada.
"""
