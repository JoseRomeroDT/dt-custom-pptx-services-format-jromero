# AGENTS.md

Instrucciones para agentes de IA que trabajan con este repositorio.

## Usar la skill

Este repositorio contiene la skill **dt-custom-pptx-services-format-jromero** (estándar [agentskills.io](https://agentskills.io)) en `skills/dt-custom-pptx-services-format-jromero/`.

Cuando el usuario pida una **presentación, PPT, deck o slides con formato Dynatrace** (propuesta, kickoff, avance, cierre, health check, RCA ejecutivo, caso de negocio):

1. Lee `skills/dt-custom-pptx-services-format-jromero/SKILL.md` completo y síguelo. Carga cada archivo de `references/` cuando el SKILL.md lo indique.
2. Ejecuta `python skills/dt-custom-pptx-services-format-jromero/scripts/check_env.py`. Si el resultado es NO LISTO, detente e informa qué falta.
3. Arma la presentación solo con `scripts/build_deck.py` y el template `assets/template-dt-services.pptx`. No diseñes slides desde cero.
4. Antes de entregar, pasa `scripts/check_deck.py` sin errores y revisa el render de `scripts/render_deck.py`.
5. Escribe la presentación en el idioma del pedido (español o inglés), salvo que el usuario indique otro.

## Modificar este repositorio

- El `README.md` está en inglés. La skill (`SKILL.md` y `references/`) está en español.
- **Sin datos de clientes ni de personas** en el template, los ejemplos o las imágenes. Revisa también los metadatos del `.pptx` (`docProps`, `authors.xml`, textos alternativos).
- Si cambias el template, regenera las vistas previas (`assets/previews/`, `assets/template-preview.png`) con `render_deck.py` y actualiza `references/catalogo-patrones.md`.
- Si cambias los scripts o el template, verifica que el ejemplo se arme sin advertencias y pase el control:

  ```bash
  python skills/dt-custom-pptx-services-format-jromero/scripts/build_deck.py examples/health-check/spec.json -o /tmp/health-check.pptx --strict
  python skills/dt-custom-pptx-services-format-jromero/scripts/check_deck.py /tmp/health-check.pptx --strict
  ```
- Mantén el frontmatter de `SKILL.md` válido: `name` igual al nombre de la carpeta, `description` ≤ 1024 caracteres y `compatibility` ≤ 500.
- Los scripts usan Python 3.9+ con python-pptx y Pillow, y deben funcionar en Windows, macOS y Linux.
