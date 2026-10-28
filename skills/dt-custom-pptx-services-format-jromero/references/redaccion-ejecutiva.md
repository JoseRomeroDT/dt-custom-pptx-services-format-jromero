# Redacción ejecutiva y estructuras de presentación

## Principios

1. **Primero la conclusión.** La audiencia ejecutiva decide en los primeros minutos: la slide `key-messages` va al inicio, con los 3 mensajes que deben recordar.
2. **Cada título es una conclusión, no un tema.** "Alert noise hides real incidents" en vez de "Alerting". Una línea, máximo ~60 caracteres. Leídos en orden, los títulos cuentan la historia completa.
3. **Una idea por slide.** Si una slide necesita dos títulos, son dos slides.
4. **Cifras con unidad y fuente.** "62% of problems from 5 sources", no "lots of noise". Cada cifra debe poder explicarse en las notas.
5. **Paralelismo.** Los elementos de una misma fila o lista tienen la misma forma gramatical y la misma longitud aproximada.
6. **Palabras de negocio.** El impacto se expresa en personas, operaciones, dinero o minutos. Las siglas técnicas se evitan en títulos y mensajes clave; si hacen falta, van en las notas.
7. **Sin culpas.** Los hallazgos describen sistemas y procesos, no personas.
8. **Notas del presentador en todas las slides.** Qué decir, de dónde sale cada cifra y qué preguntas anticipar. Las notas pueden ser más técnicas que la slide.

## Idioma

- La presentación va en el **idioma del pedido** (español o inglés), salvo que el usuario indique otro.
- Todo en ese idioma: títulos, etiquetas en MAYÚSCULAS, citas, diagramas y notas. Los nombres técnicos y de producto no se traducen.
- El template está en inglés. En español, cambia también los textos fijos que no son placeholders: `Thank You` → `Gracias`, `Agenda` se mantiene, `CONFIDENTIAL` se mantiene (es parte del layout).

## Confidencialidad

- Por defecto, los casos de clientes se anonimizan por industria ("Banking", "Public sector") y sin nombres de personas, hosts ni IDs.
- Solo se usa el nombre del cliente si el usuario lo pide y la presentación es para ese cliente.
- Las cifras reales se mantienen si el usuario las aporta; nunca se inventan. Si falta un dato, se pregunta o se deja fuera.

## Extensión

| Duración | Slides de contenido | Total aprox. |
|---|---|---|
| 10 min | 4–5 | 7–8 |
| 20 min | 7–9 | 10–12 |
| 45 min | 12–16 | 16–20 (con `section`) |

## Estructuras listas para usar

Secuencias de patrones para las presentaciones de servicios más comunes. Son un punto de partida: se ajustan al mensaje.

| Tipo | Secuencia de patrones |
|---|---|
| **Propuesta de servicios** | `cover` → `key-messages` (valor, alcance, inversión de tiempo) → `from-to` (situación actual → situación propuesta) → `cards-steps` (qué incluye y cómo se trabaja) → `phases-plan` → `risks-prereqs` → `kpis` (resultados esperados) → `roadmap` (próximos pasos y pedido) → `closing` |
| **Kickoff de proyecto** | `cover` → `agenda` → `statement` (objetivo) → `diagram-banner` (metodología) → `phases-plan` → `two-panels` (responsabilidades Dynatrace / cliente) → `risks-prereqs` → `roadmap` → `closing` |
| **Reporte de avance** | `cover` → `key-messages` (estado en 3 frases) → `kpis` (avance medido) → `cards-steps` (lo hecho y lo que sigue) → `risks-prereqs` (bloqueos y lo que se necesita) → `roadmap` → `closing` |
| **Resultados / cierre de servicio** | `cover` → `key-messages` → `from-to` (antes → después) → `kpis` → `case` (el caso más ilustrativo) → `roadmap` (recomendaciones) → `closing` |
| **Health check / assessment** | `cover` → `agenda` → `key-messages` → `from-to` (percepción → evidencia) → `diagram-banner` (método) → `kpis` → `two-panels` o `case` → `phases-plan` → `roadmap` → `closing` |
| **RCA ejecutivo** | `cover` → `key-messages` → `case` (uno por incidente) → `diagram-principles` (cómo se investigó) → `cards-steps` (plan de acción por tipo) → `roadmap` → `closing` |
| **Caso de negocio / innovación** | `cover` → `key-messages` → `from-to` (problema → propuesta) → `diagram-principles` (cómo funciona) → `case` (prueba real) → `kpis` → `roadmap` (pedido) → `closing` |

## Lista de control de contenido

- [ ] Leyendo solo los títulos se entiende la historia.
- [ ] Los 3 mensajes clave aparecen al inicio y se demuestran en las slides siguientes.
- [ ] Cada cifra tiene unidad y fuente (en la slide o en las notas).
- [ ] No hay datos inventados ni placeholders.
- [ ] La última slide de contenido pide algo concreto (decisión, accesos, responsables, fecha).
- [ ] Todas las slides tienen notas del presentador.
