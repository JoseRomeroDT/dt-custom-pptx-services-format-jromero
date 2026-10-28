# Diagramas draw.io para las presentaciones

Los diagramas de las slides se hacen con **draw.io**, con cualquier skill de draw.io (la oficial `drawio` de jgraph, `drawio-skill` u otra), y se exportan con **draw.io Desktop**. No se usan capturas, Mermaid renderizado ni imágenes externas.

## Cuándo un diagrama

- Un proceso, un journey o una metodología → `diagram-banner`.
- Cómo funciona algo (actores, datos, resultado) → `diagram-principles`.
- La cadena causal de un caso → `case`.
- Si la idea cabe en tarjetas o en una lista, no hace falta un diagrama: usa el patrón de tarjetas.

## Kit de partida (`assets/drawio/`)

| Archivo | Estructura | Patrón | Proporción del marco |
|---|---|---|---|
| `journey-6-steps.drawio` | 6 chevrons con tarjeta (qué pasa / resultado), principio y bucle de retorno | `diagram-banner` | ≈ 3.2 : 1 (12.43 × 3.9 in) |
| `flow-actors.drawio` | 4 cajas conectadas (personas → motor → datos → resultado), un elemento de apoyo y 4 garantías | `diagram-principles` | ≈ 3.4 : 1 (12.43 × 3.61 in) |
| `causal-loop.drawio` | Disparador, bucle que se refuerza, causa en rojo y punto ciego | `case` | ≈ 1 : 1 (4.48 × 4.3 in) |
| `causal-chain.drawio` | Cambio → efecto → causa → síntoma visible, con factor contribuyente y señal | `case` | ≈ 1 : 1 |

Cada archivo tiene su vista previa `.png` al lado. Los textos están entre corchetes: hay que reemplazarlos todos.

## Cómo se hace

1. **Copia** el archivo del kit que más se parece a la carpeta del deck (`<deck>/diagrams/`), con un nombre propio.
2. **Cambia solo los textos** (atributo `value` de cada celda): no cambies estilos, colores ni posiciones salvo que la idea lo exija. Para un número distinto de pasos o cajas, duplica o borra celdas conservando los estilos del kit.
3. **Exporta** a PNG con el XML embebido, escala 2 y borde 6:

   ```bash
   # DRAWIO = ruta de draw.io Desktop (Windows: "C:\Program Files\draw.io\draw.io.exe";
   #          macOS: /Applications/draw.io.app/Contents/MacOS/draw.io; Linux: drawio, con xvfb-run -a si no hay pantalla)
   "$DRAWIO" -x -f png -e -s 2 -b 6 -o <deck>/diagrams/mi-diagrama.png <deck>/diagrams/mi-diagrama.drawio
   ```
4. **Revisa** el PNG: textos completos, sin solapes ni flechas sueltas, y legible al tamaño de la slide.
5. **Úsalo** en el spec: `"images": {"diagram": "diagrams/mi-diagrama.png"}`. El script lo ajusta al marco sin deformarlo. Para que llene el marco, mantén la proporción indicada en la tabla.

## Estilo (igual al del deck de referencia)

| Elemento | Estilo |
|---|---|
| Fuente | `fontFamily=DT Flow`; títulos de caja en negrita 15–18 pt, detalle 11–14 pt |
| Texto | `#00092F`; secundario `#6B7088` |
| Tarjeta | blanco, borde `#DDE1EC`, `arcSize` 6–10 |
| Chevrons | `shape=step`, degradados de la paleta de pasos: `#7F1AFE→#6B2CFE`, `#5F38FE→#4A4BFE`, `#3657FE→#1866FE`, `#1673F4→#0E8FE6`, `#0AA4D2→#05B9B4`, `#03C69F→#01D393` |
| Caja principal (motor) | degradado `#7F1AFE → #1866FE`, texto blanco |
| Caja de datos / cambio | `#E8F0FF` con borde `#1866FE` |
| Caja de resultado | `#E0FAF1` con borde `#01D393` |
| Caja de apoyo | `#F2E9FF` con borde `#7F1AFE` |
| Causa / falla | relleno `#D81E44`, texto blanco, borde grueso; flechas de falla en `#D81E44` |
| Disparador / contribuyente | `#FFF4DC` con borde `#E69500` |
| Sin visibilidad / señal débil | `#F3F4F8` con borde punteado `#8A90A6` |
| Pills de garantías | `#F3F4F8` sin borde, `arcSize=50`, texto en negrita |

## Reglas

- Máximo ~15 cajas. Si hay más, agrupa.
- Textos en el idioma de la presentación, sin IDs técnicos ni nombres de hosts.
- El rojo se reserva para causa o falla.
- Guarda siempre el `.drawio` junto al `.png`: el PNG lleva el XML embebido, pero el `.drawio` facilita los cambios.
