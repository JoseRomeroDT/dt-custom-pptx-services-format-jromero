---
name: dt-custom-pptx-services-format-jromero
description: Genera presentaciones PowerPoint con el formato de Dynatrace Services (template corporativo + estilo del deck ejecutivo de referencia) a partir de un template definitivo de 16 patrones de slide, con diagramas draw.io en la paleta Dynatrace. El agente escribe el contenido en un spec JSON y build_deck.py arma el .pptx sin romper el diseño; check_deck.py y render_deck.py controlan calidad. Usar cuando el usuario pida "presentación", "PPT", "PowerPoint", "deck", "slides", "presentación estilo Dynatrace", "presentación de servicios", "propuesta en PPT", "kickoff", "reporte de avance", "presentación ejecutiva", "Dynatrace-style deck" o "services presentation". La presentación sale en el idioma del pedido (español o inglés). Usa la skill pptx para validar el archivo y una skill de draw.io para los diagramas.
license: MIT
compatibility: Cualquier agente compatible con agentskills.io que ejecute comandos de shell (Claude Code, OpenAI Codex, GitHub Copilot, Cursor, Kiro, Junie, OpenCode, etc.). Requiere Python 3.9+ con python-pptx y Pillow. Recomendado - fuentes DT Flow, PowerPoint o LibreOffice para el render, draw.io Desktop con una skill de draw.io y la skill pptx.
metadata:
  author: Edunzz (Jose Eduardo Romero Jimenez)
  version: "1.0.0"
  language: es, en
  repository: https://github.com/JoseRomeroDT/dt-custom-pptx-services-format-jromero
---

# dt.custom.PPTX.services-format.jromero — Presentaciones con formato Dynatrace Services

## Qué es y qué no es

| Esta skill **SÍ** | Esta skill **NO** |
|---|---|
| Trae el **template definitivo** (`assets/template-dt-services.pptx`): 16 patrones de slide con el diseño de Dynatrace Services | Diseña slides desde cero ni inventa estilos |
| Guía la historia: qué decir, en qué orden y con qué patrón | Inventa datos, cifras o casos |
| Arma el `.pptx` desde un **spec JSON** con `build_deck.py`, conservando fuentes, colores y posiciones | Reemplaza a la skill `pptx` (la usa para validar) ni a la de draw.io (la usa para diagramas) |
| Controla la calidad: placeholders, notas, fuentes, texto que no cabe y render visual | Publica ni envía la presentación |

**Principio rector:** el diseño ya está resuelto en el template. El trabajo del agente es **el mensaje**: elegir patrones, escribir textos claros y hacer los diagramas. Si algo no cabe, se acorta o se divide; no se rediseña.

## Archivos

| Archivo | Para qué |
|---|---|
| `assets/template-dt-services.pptx` | Template definitivo: un patrón por slide; el id del patrón es el nombre del slide |
| `assets/template-preview.png` · `assets/previews/` | Vista de los 16 patrones (para elegir con visión) |
| `assets/drawio/` | Kit de diagramas: `journey-6-steps`, `flow-actors`, `causal-loop`, `causal-chain` (.drawio + .png) |
| `assets/spec.example.json` | Spec mínimo de ejemplo |
| `scripts/check_env.py` | Verifica el entorno (python-pptx, fuentes, draw.io, render, skills) |
| `scripts/build_deck.py` | Arma la presentación desde el spec |
| `scripts/check_deck.py` | Control de calidad del `.pptx` |
| `scripts/render_deck.py` | Exporta las slides a PNG y una lámina resumen para revisarlas |
| `scripts/inspect_deck.py` | Lista formas, nombres y textos de cualquier `.pptx` |
| `references/catalogo-patrones.md` | **Los 16 patrones**: cuándo usarlos, límites de texto y claves |
| `references/redaccion-ejecutiva.md` | Principios de redacción y estructuras listas por tipo de presentación |
| `references/estilo-visual.md` | Paleta, tipografía, componentes y reglas del estilo |
| `references/diagramas-drawio.md` | Cómo hacer los diagramas con el kit y exportarlos |

## Flujo

```
1. Entorno ─────► python scripts/check_env.py  (si algo FALTA: detenerse y decir cómo resolverlo)
2. Encargo ─────► audiencia, objetivo, decisión que se busca, duración, idioma y datos disponibles
3. Historia ────► mensajes clave + títulos-conclusión + secuencia de patrones
4. Diagramas ───► con el kit draw.io, exportados a PNG
5. Spec ────────► <deck>/spec.json con textos, imágenes y notas
6. Armado ──────► python scripts/build_deck.py <deck>/spec.json -o <deck>/<nombre>.pptx
7. Calidad ─────► check_deck.py + render_deck.py + revisión visual; corregir y repetir
8. Entrega ─────► ruta del .pptx, lámina resumen y supuestos que el usuario debe confirmar
```

### 1. Entorno

```bash
python <skill>/scripts/check_env.py
```

`FALTA` bloquea: muéstrale al usuario el comando que propone el script y espera. `AVISO` no bloquea, pero se informa. Por ejemplo, sin las fuentes DT Flow la presentación se ve con otra fuente en ese equipo, y sin draw.io no se pueden hacer diagramas: en ese caso usa patrones sin imagen.

### 2. Encargo

Antes de escribir, ten claro (pregunta **una sola vez** solo lo que falte y no se pueda deducir):
- **Audiencia** (ejecutiva, técnica, cliente, interna) y **objetivo**: qué debe pensar, sentir o decidir al final.
- **Tipo**: propuesta, kickoff, avance, cierre, health check, RCA, caso de negocio…
- **Duración** o número de slides, e **idioma**: el del pedido (español o inglés), salvo que el usuario indique otro.
- **Datos reales**: cifras, casos, fechas, nombres. **Nunca inventes datos.** Si falta uno, pregúntalo o deja fuera esa slide.
- **Confidencialidad**: por defecto, los clientes se nombran por industria.

### 3. Historia

Sigue `references/redaccion-ejecutiva.md`:
1. Escribe los **3 mensajes clave**: van en `key-messages`, al inicio.
2. Elige la **estructura** de la tabla "Estructuras listas para usar" que corresponde al tipo y ajústala.
3. Escribe el **título-conclusión** de cada slide de contenido (≤ 60 caracteres). Leídos en orden, deben contar la historia.
4. Asigna un **patrón** a cada slide con `references/catalogo-patrones.md`. Si puedes ver imágenes, mira `assets/template-preview.png`.

Muestra al usuario el esquema (título por slide y patrón) antes de armar, salvo que haya pedido el resultado directo.

| Patrón | Para |
|---|---|
| `cover` · `closing` | Abrir y cerrar (siempre) |
| `agenda` · `section` | Ordenar decks largos |
| `key-messages` | Los 3 mensajes que deben recordar |
| `statement` | Una idea fuerza o contexto |
| `from-to` | Síntoma → causa, antes → después, pedido → propuesta (4 filas) |
| `diagram-banner` · `diagram-principles` | Un proceso o cómo funciona algo, con diagrama |
| `cards-steps` | Qué incluye (4 tarjetas) y cómo se actúa (4 pasos) |
| `case` | Un caso: cita, 3 KPIs, diagrama causal, 3 acciones y lección |
| `two-panels` | Dos frentes u opciones con la misma estructura |
| `kpis` | 4 cifras de impacto y 3 beneficios |
| `phases-plan` | Plan por fases tipo Gantt |
| `risks-prereqs` | Riesgos y prerrequisitos |
| `roadmap` | 4 próximos pasos y el pedido |

### 4. Diagramas

Solo para `diagram-banner`, `diagram-principles` y `case`. Sigue `references/diagramas-drawio.md`:
1. Copia un archivo del kit a `<deck>/diagrams/`.
2. Cambia solo los textos.
3. Exporta con `-x -f png -e -s 2 -b 6`.
4. Revisa el PNG.

Respeta la proporción del marco de cada patrón.

### 5. Spec

Crea una carpeta de trabajo por presentación:

```
<deck>/
├── spec.json          contenido de la presentación (la fuente de verdad: para cambiar algo, se edita y se vuelve a armar)
├── diagrams/          .drawio + .png
├── render/            PNG de revisión (se regenera)
└── <nombre>.pptx      resultado
```

Formato del spec (ver `assets/spec.example.json` y el catálogo):

```json
{
  "output": "propuesta-servicios.pptx",
  "slides": [
    {"pattern": "cover",
     "text": {"[Presentation title]": "…", "[Subtitle: what the audience will get]": "…"},
     "notes": "Qué dice el presentador."},
    {"pattern": "diagram-banner",
     "text": {"[Slide title: the takeaway in one sentence]": "…", "[Banner lead-in]": "…", "[Banner message]": "…"},
     "images": {"diagram": "diagrams/metodologia.png"},
     "notes": "…"}
  ]
}
```

Reglas:
- Las claves de `text` son los placeholders del patrón, tal como aparecen en el catálogo. **Reemplaza todos.**
- Una lista crea varios párrafos y un `""` borra el párrafo.
- `remove` quita formas opcionales por nombre o por placeholder (ver el catálogo).
- `notes` en **todas** las slides: qué decir, de dónde sale cada cifra y qué preguntas anticipar.

### 6. Armado

```bash
python <skill>/scripts/build_deck.py <deck>/spec.json -o <deck>/<nombre>.pptx
```

El script copia los patrones, reemplaza textos e imágenes y borra lo que no se usa. Avisa de:
- claves que no existen en el patrón;
- placeholders sin reemplazar;
- diagramas de ejemplo que siguen en el deck;
- slides sin notas.

Corrige el spec hasta que no haya advertencias. `--list-patterns` muestra los ids.

### 7. Calidad (obligatoria)

```bash
python <skill>/scripts/check_deck.py <deck>/<nombre>.pptx                  # errores = no se entrega
python <skill>/scripts/render_deck.py <deck>/<nombre>.pptx -o <deck>/render
python <skill-pptx>/scripts/office/validate.py <deck>/<nombre>.pptx --original <skill>/assets/template-dt-services.pptx
```

Revisa **cada** PNG del render (o `render/grid.png`) con ojos frescos:
- [ ] Ningún texto cortado, desbordado o encima de otra forma. Si no cabe, acorta el texto; no cambies la fuente.
- [ ] Ningún placeholder `[…]`, texto en otro idioma o dato inventado.
- [ ] Los diagramas se leen y llenan su marco.
- [ ] Los títulos caben en una línea y cuentan la historia.
- [ ] Las cifras tienen unidad y la misma forma en todo el deck.

Si el modelo no puede ver imágenes, apóyate en `check_deck.py` y pide al usuario que revise el render antes de compartir. Corrige el spec, vuelve a armar y vuelve a revisar solo lo que cambió.

### 8. Entrega

Responde con:
- la ruta del `.pptx`;
- la lámina `render/grid.png`;
- la lista de slides (título y patrón);
- los supuestos o datos que el usuario debe confirmar.

Para cambios posteriores, edita el `spec.json` y vuelve a armar. No edites el `.pptx` a mano salvo que el usuario lo pida. En ese caso usa la skill `pptx`, conserva los estilos y vuelve a pasar el control de calidad.

## Reglas de oro

1. **No rediseñar:** patrones del template, paleta y fuentes DT Flow (`references/estilo-visual.md`).
2. **El mensaje primero:** 3 mensajes clave al inicio y un título-conclusión por slide.
3. **Nada inventado:** cifras y casos solo si los aporta el usuario o salen de una fuente que se cita en las notas.
4. **Idioma del pedido** en todo el deck, incluidos los diagramas.
5. **Notas del presentador** en todas las slides.
6. **Cero placeholders y cero texto cortado** antes de entregar.
