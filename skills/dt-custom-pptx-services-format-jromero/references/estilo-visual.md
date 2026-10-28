# Estilo visual — Dynatrace Services

El estilo sale del template corporativo `PPT Template.pptx` y del deck ejecutivo de referencia (`RCA-journey-executive-EN-short-v2.pptx`). Todo está ya dentro del template de la skill: **la regla principal es no rediseñar**. Se elige un patrón, se escribe el texto y, si hace falta, se cambia el diagrama.

## Formato

| Elemento | Valor |
|---|---|
| Tamaño | 16:9 · 13.33 × 7.5 in |
| Masters | Los 3 masters del template corporativo (no se agregan ni se quitan) |
| Fuentes | **DT Flow** para el cuerpo y **DT Flow Extrabold** para títulos y cifras. No usar otras. |
| Pie de las slides de contenido | `CONFIDENTIAL` abajo a la izquierda, logo de Dynatrace y número de página abajo a la derecha (vienen del layout) |

## Dos familias de slides

| Familia | Patrones | Cómo se ve |
|---|---|---|
| **Degradado de marca** | `cover`, `agenda`, `key-messages`, `section`, `statement`, `closing` | Fondo azul → violeta → verde, texto blanco. Para abrir, separar, remarcar y cerrar. |
| **Contenido** | todos los demás | Fondo blanco, título arriba a la izquierda con una barra corta en degradado debajo, tarjetas y diagramas. |

Ritmo recomendado: degradado al inicio (portada, agenda, mensajes clave), contenido en el medio, degradado al final (cierre). Un `section` cada 3 a 5 slides de contenido en decks largos.

## Paleta (tokens)

| Rol | Color | Dónde |
|---|---|---|
| Texto principal | `#00092F` (navy) | Títulos, cifras, textos de tarjeta |
| Texto de cuerpo | `#1A2050` | Párrafos largos |
| Texto secundario | `#6B7088` | Etiquetas, significados de KPI, citas |
| Borde de tarjeta | `#DDE1EC` | Tarjetas blancas |
| Fondo suave | `#F3F4F8` | Banners claros, cajas de resultado |
| Azul Dynatrace | `#1866FE` | Acento 1, degradados |
| Violeta Dynatrace | `#7F1AFE` | Acento 2, palabras destacadas en banners |
| Verde Dynatrace | `#01D393` · oscuro `#00936A` | Acento 3, resultados positivos, etiquetas |
| Degradado de pasos | `#7F1AFE` → `#5F38FE` → `#3657FE` → `#1673F4` → `#0AA4D2` → `#03C69F` | Chevrons y círculos numerados, siempre en este orden |
| Banner principal | degradado `#7F1AFE` → `#1866FE` | Banners de cierre de idea y del pedido |

Colores semánticos (solo en diagramas): rojo `#D81E44` = causa o falla · ámbar `#E69500` sobre `#FFF4DC` = disparador o factor contribuyente · azul `#1866FE` sobre `#E8F0FF` = cambio · gris `#8A90A6` punteado = sin visibilidad.

## Jerarquía de texto

| Elemento | Tamaño aproximado |
|---|---|
| Título de slide de contenido | 28 pt, Extrabold, una línea |
| Título sobre degradado | 34–48 pt |
| Cifra de KPI | 34–48 pt, en color de acento |
| Texto de tarjeta, mensajes, acciones | 14–18 pt |
| Etiquetas de sección (MAYÚSCULAS) | 10–11 pt, gris o color, con espaciado |
| Pie y fuentes | 6–10 pt |

Los tamaños ya están en el template: no se cambian. Si un texto no cabe, se acorta; no se achica la fuente.

## Componentes del sistema

- **Tarjeta**: rectángulo redondeado blanco, borde `#DDE1EC`, sombra suave. Título en color de acento y texto en navy.
- **Chevron de paso**: degradado de la paleta de pasos, texto blanco en negrita.
- **Banner**: rectángulo redondeado a todo el ancho; claro (`#F3F4F8`) con una frase destacada en violeta, o degradado violeta → azul con texto blanco.
- **Pill (etiqueta)**: rectángulo muy redondeado de color con texto blanco en MAYÚSCULAS (`CUSTOMER SAID`, `Correct`, `Detect`).
- **Círculo numerado**: óvalo con degradado y número blanco, unido por una línea para roadmaps.
- **KPI**: cifra grande en color + significado en gris debajo + fuente en MAYÚSCULAS.
- **Cita**: entre comillas tipográficas “…”, en itálica gris.

## Reglas

1. No mover, redimensionar ni recolorear las formas de un patrón. Las excepciones las hace el script: la imagen se ajusta al marco y las listas hacen crecer su caja.
2. No agregar colores, fuentes, sombras ni efectos fuera de esta guía.
3. Una idea por slide. Si el contenido no cabe en el patrón, divide en dos slides o elige otro patrón; no lo comprimas.
4. Mismo patrón, misma estructura: si dos slides comparan cosas, usa el mismo patrón y el mismo orden.
5. Las fotos y logos de clientes solo con autorización; por defecto, los casos se nombran por industria ("Banking", "Energy").
6. Si de verdad hace falta algo que ningún patrón cubre (una tabla grande o un gráfico nativo), créalo con la skill `pptx` en un slide del layout de contenido, con esta paleta y DT Flow, y revísalo en el render con el mismo cuidado.
