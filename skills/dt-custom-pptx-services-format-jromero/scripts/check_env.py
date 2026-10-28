#!/usr/bin/env python3
"""
check_env.py — Verifica lo necesario para generar presentaciones con la skill
dt-custom-pptx-services-format-jromero. No instala nada: dice qué falta y cómo resolverlo.

  OK     listo
  AVISO  funciona, pero con limitaciones (p. ej. sin fuentes DT Flow el render no es fiel)
  FALTA  bloquea: hay que resolverlo antes de generar

Uso:  python scripts/check_env.py [--json]
Código de salida: 0 = listo, 1 = falta algo obligatorio.
"""
import argparse, glob, json, os, platform, re, shutil, subprocess, sys
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
HOME = Path.home()
AGENT_DIRS = [".claude", ".agents", ".codex", ".github", ".cursor", ".kiro", ".junie", ".opencode", ".config/opencode"]
SYSTEM = platform.system()


def skill_dirs():
    roots = [SKILL.parent]
    for base in (HOME, Path.cwd()):
        roots += [base / d / "skills" for d in AGENT_DIRS]
    roots += [Path(p) for p in glob.glob(str(HOME / ".claude/plugins/cache/*/*/*/skills"))]
    return [r for r in dict.fromkeys(roots) if r.is_dir()]


def find_skill(pred):
    for root in skill_dirs():
        for md in root.glob("*/SKILL.md"):
            try:
                head = md.read_text(encoding="utf-8", errors="ignore")[:1500]
            except OSError:
                continue
            if pred(md.parent.name, head):
                return md.parent
    return None


def drawio_cli():
    cands = []
    if SYSTEM == "Windows":
        for base in (os.environ.get("ProgramFiles", r"C:\Program Files"), os.environ.get("LOCALAPPDATA", "")):
            cands.append(Path(base) / "draw.io" / "draw.io.exe")
            cands.append(Path(base) / "Programs" / "draw.io" / "draw.io.exe")
    elif SYSTEM == "Darwin":
        cands.append(Path("/Applications/draw.io.app/Contents/MacOS/draw.io"))
    for name in ("drawio", "draw.io"):
        if shutil.which(name):
            cands.append(Path(shutil.which(name)))
    for c in cands:
        if c.exists():
            try:
                r = subprocess.run([str(c), "--version"], capture_output=True, text=True, timeout=30)
                v = (r.stdout or r.stderr).strip().splitlines()
                if r.returncode == 0 and v and re.search(r"\d+\.\d+", v[-1]):
                    return str(c), v[-1]
            except (OSError, subprocess.TimeoutExpired):
                continue
    return None, None


def dt_flow_fonts():
    dirs = []
    if SYSTEM == "Windows":
        dirs = [Path(os.environ.get("WINDIR", r"C:\Windows")) / "Fonts",
                Path(os.environ.get("LOCALAPPDATA", "")) / "Microsoft" / "Windows" / "Fonts"]
    elif SYSTEM == "Darwin":
        dirs = [HOME / "Library" / "Fonts", Path("/Library/Fonts")]
    else:
        if shutil.which("fc-list"):
            out = subprocess.run(["fc-list"], capture_output=True, text=True).stdout
            return sorted({l.split(":")[1].strip() for l in out.splitlines() if "DT Flow" in l})[:4]
        dirs = [HOME / ".fonts", HOME / ".local/share/fonts", Path("/usr/share/fonts")]
    found = []
    for d in dirs:
        if d.is_dir():
            found += [f.name for f in d.iterdir() if re.search(r"DT ?Flow", f.name, re.I)]
    return sorted(set(found))


def renderer():
    if SYSTEM == "Windows":
        for base in (os.environ.get("ProgramFiles", r"C:\Program Files"), os.environ.get("ProgramFiles(x86)", "")):
            hits = glob.glob(str(Path(base) / "Microsoft Office" / "root" / "Office*" / "POWERPNT.EXE"))
            if hits:
                return "PowerPoint", hits[0]
    soffice = shutil.which("soffice") or shutil.which("libreoffice")
    if not soffice and Path("/Applications/LibreOffice.app/Contents/MacOS/soffice").exists():
        soffice = "/Applications/LibreOffice.app/Contents/MacOS/soffice"
    if soffice and shutil.which("pdftoppm"):
        return "LibreOffice + pdftoppm", soffice
    return None, soffice


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass
    res = []

    def add(state, item, detail, fix=""):
        res.append({"estado": state, "requisito": item, "detalle": detail, "solucion": fix})

    ok_py = sys.version_info >= (3, 9)
    add("OK" if ok_py else "FALTA", "Python 3.9+", platform.python_version(), "" if ok_py else "Instala Python 3.9 o superior")
    try:
        import pptx
        add("OK", "python-pptx", pptx.__version__)
    except ImportError:
        add("FALTA", "python-pptx", "no instalado", "pip install python-pptx")
    try:
        import PIL
        add("OK", "Pillow", PIL.__version__)
    except ImportError:
        add("FALTA", "Pillow", "no instalado", "pip install Pillow")
    tpl = SKILL / "assets" / "template-dt-services.pptx"
    add("OK" if tpl.exists() else "FALTA", "Template", str(tpl) if tpl.exists() else "no encontrado",
        "" if tpl.exists() else "Reinstala la skill completa (assets/template-dt-services.pptx)")
    fonts = dt_flow_fonts()
    add("OK" if fonts else "AVISO", "Fuentes DT Flow", ", ".join(fonts[:3]) + (" …" if len(fonts) > 3 else "") if fonts else "no instaladas",
        "" if fonts else "Instala la familia DT Flow (brand assets de Dynatrace). Sin ella, PowerPoint y el render usan otra fuente.")
    eng, path = renderer()
    add("OK" if eng else "AVISO", "Render para revisión visual", f"{eng} ({path})" if eng else "sin PowerPoint ni LibreOffice + pdftoppm",
        "" if eng else "Windows: Microsoft PowerPoint · macOS: brew install --cask libreoffice && brew install poppler · Linux: apt install libreoffice poppler-utils")
    cli, ver = drawio_cli()
    add("OK" if cli else "AVISO", "draw.io Desktop (CLI)", f"{ver} -> \"{cli}\"" if cli else "no encontrado",
        "" if cli else "Para diagramas: Windows winget install JGraph.Draw · macOS brew install --cask drawio · Linux .deb/AppImage de github.com/jgraph/drawio-desktop")
    d = find_skill(lambda n, h: re.search(r"draw\.?io", n + h, re.I) is not None and n != SKILL.name)
    add("OK" if d else "AVISO", "Skill de draw.io", d.name if d else "no encontrada",
        "" if d else "npx skills add jgraph/drawio-mcp --skill drawio (o cualquier skill que genere .drawio)")
    p = find_skill(lambda n, h: n.lower() == "pptx" or re.search(r"^name:\s*pptx\s*$", h, re.M) is not None)
    add("OK" if p else "AVISO", "Skill pptx", p.name if p else "no encontrada",
        "" if p else "Recomendada para validar el archivo y para contenido fuera de los patrones (p. ej. anthropics/skills: pptx)")

    if a.json:
        print(json.dumps(res, ensure_ascii=True, indent=2))
    else:
        for r in res:
            print(f"[{r['estado']:5s}] {r['requisito']:28s} {r['detalle']}")
            if r["solucion"]:
                print(f"        -> {r['solucion']}")
        blocked = any(r["estado"] == "FALTA" for r in res)
        print("RESULTADO: " + ("NO LISTO: resuelve lo que dice FALTA." if blocked else "LISTO para generar presentaciones."))
    sys.exit(1 if any(r["estado"] == "FALTA" for r in res) else 0)


if __name__ == "__main__":
    main()
