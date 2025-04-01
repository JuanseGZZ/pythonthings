# rrhh_utils.py

keywords_rrhh = {
    # Español
    "rrhh", "recursos humanos", "reclutador", "reclutadora", "reclutamiento", "selección de personal",
    "reclutamiento y selección it", "talento humano", "gestión del talento", "captación de talento",
    "analista de rrhh", "analista de selección", "psicología laboral", "psicología organizacional",
    "consultor rrhh", "consultoría de rrhh", "headhunter", "atracción de talento", "hiring", "staffing",
    "acquisition analyst", "especialista en selección", "responsable de rrhh", "partner de rrhh",
    "business partner rrhh", "generalista de rrhh", "talent acquisition",

    # Inglés
    "hr", "human resources", "hr specialist", "hr generalist", "hrbp", "recruiter",
    "recruitment analyst", "sourcing specialist", "talent manager", "people operations", "head hunter",
    "hiring manager", "hr consultant", "people & culture", "hr analyst", "hr coordinator", "talent sourcer",
    "personnel management", "recruiter | hr analyst | hrbp"
}

def es_reclutador(texto: str) -> bool:
    texto_lower = texto.lower()
    return any(kw in texto_lower for kw in keywords_rrhh)

def coincidencias_rrhh(texto: str) -> list:
    texto_lower = texto.lower()
    return [kw for kw in keywords_rrhh if kw in texto_lower]
