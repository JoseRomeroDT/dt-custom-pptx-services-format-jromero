#!/usr/bin/env python3
"""
render_deck.py — Exporta cada slide de un .pptx a PNG y arma una lámina resumen (contact sheet)
para la revisión visual (skill dt-custom-pptx-services-format-jromero).

- Windows con PowerPoint: usa PowerPoint (render fiel, con las fuentes DT Flow instaladas).
- macOS / Linux: LibreOffice (soffice) → PDF → pdftoppm. Si faltan las fuentes DT Flow, el render
  usa otra fuente y los anchos cambian: la revisión de texto cortado es aproximada.

Uso:
  python scripts/render_deck.py deck.pptx -o render/              # todas las slides + render/grid.png
  python scripts/render_deck.py deck.pptx -o render/ --slides 2,5 # solo algunas
"""
import argparse, glob, os, platform, shutil, subprocess, sys, tempfile
from pathlib import Path


def render_powerpoint(pptx, out, slides, width):
    sel = ",".join(str(s) for s in slides) if slides else ""
    ps = f"""
$ErrorActionPreference = 'Stop'
$ppt = New-Object -ComObject PowerPoint.Application
$pres = $ppt.Presentations.Open('{pptx}', $true, $false, $false)
$sel = @({sel})
$h = [int]({width} * $pres.PageSetup.SlideHeight / $pres.PageSetup.SlideWidth)
for ($i = 1; $i -le $pres.Slides.Count; $i++) {{
  if ($sel.Count -eq 0 -or $sel -contains $i) {{
    $pres.Slides.Item($i).Export((Join-Path '{out}' ('slide-{{0:D2}}.png' -f $i)), 'PNG', {width}, $h)
  }}
}}
$pres.Close()
"""
    r = subprocess.run(["powershell", "-NoProfile", "-NonInteractive", "-Command", ps], capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(r.stderr.strip() or r.stdout.strip())


def render_soffice(pptx, out, slides, width):
    soffice = shutil.which("soffice") or shutil.which("libreoffice") or "/Applications/LibreOffice.app/Contents/MacOS/soffice"
    if not Path(soffice).exists() and not shutil.which(soffice):
        raise RuntimeError("No se encontró LibreOffice (soffice).")
    if not shutil.which("pdftoppm"):
        raise RuntimeError("No se encontró pdftoppm (Poppler).")
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run([soffice, "--headless", "--convert-to", "pdf", "--outdir", tmp, str(pptx)],
                       check=True, capture_output=True)
        pdf = next(Path(tmp).glob("*.pdf"))
        subprocess.run(["pdftoppm", "-png", "-scale-to-x", str(width), "-scale-to-y", "-1", str(pdf),
                        str(Path(tmp) / "p")], check=True)
        for f in sorted(Path(tmp).glob("p-*.png")):
            n = int(f.stem.split("-")[-1])
            if not slides or n in slides:
                shutil.copy(f, Path(out) / f"slide-{n:02d}.png")


def contact_sheet(out, cols=4, w=480):
    try:
        from PIL import Image, ImageDraw
    except ImportError:
        return None
    files = sorted(glob.glob(str(Path(out) / "slide-*.png")))
    if not files:
        return None
    first = Image.open(files[0])
    h = int(w * first.height / first.width)
    rows = (len(files) + cols - 1) // cols
    g = Image.new("RGB", (cols * w + (cols + 1) * 12, rows * (h + 30) + 12), "white")
    d = ImageDraw.Draw(g)
    for k, f in enumerate(files):
        x, y = 12 + (k % cols) * (w + 12), 12 + (k // cols) * (h + 30)
        g.paste(Image.open(f).convert("RGB").resize((w, h)), (x, y + 18))
        d.rectangle([x, y + 18, x + w - 1, y + 18 + h - 1], outline="#9ea0aa")
        d.text((x, y + 2), Path(f).stem, fill="black")
    path = Path(out) / "grid.png"
    g.save(path)
    return path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pptx")
    ap.add_argument("-o", "--out", default="render")
    ap.add_argument("--slides", help="lista separada por comas, p. ej. 1,4,7")
    ap.add_argument("--width", type=int, default=1600)
    a = ap.parse_args()
    pptx = Path(a.pptx).resolve()
    out = Path(a.out).resolve()
    out.mkdir(parents=True, exist_ok=True)
    slides = [int(s) for s in a.slides.split(",")] if a.slides else []
    if not slides:
        for f in out.glob("slide-*.png"):
            f.unlink()
    engine = "PowerPoint"
    try:
        if platform.system() == "Windows":
            render_powerpoint(str(pptx), str(out), slides, a.width)
        else:
            raise RuntimeError("no es Windows")
    except Exception as e:  # sin PowerPoint: LibreOffice
        if platform.system() == "Windows":
            print(f"AVISO: PowerPoint no disponible ({e}); se usa LibreOffice.", file=sys.stderr)
        engine = "LibreOffice"
        render_soffice(pptx, out, slides, a.width)
    pngs = sorted(out.glob("slide-*.png"))
    grid = contact_sheet(out)
    print(f"OK ({engine}): {len(pngs)} PNG en {out}" + (f" | lámina: {grid}" if grid else ""))
    for p in pngs:
        print(f"   {p}")


if __name__ == "__main__":
    main()
