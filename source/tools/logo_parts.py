RED="#D9342D"; NAVY="#13202E"
MARK = ('<path fill="{r}" d="M310 279 L400 181 L490 279 L460.5 279 L400 212 L339.5 279 Z"/>'
        '<path fill="{r}" d="M311 292 L400 388 L489 292 L459.5 292 L400 357 L340.5 292 Z"/>'
        '<path fill="{n}" d="M400 268 L417 284.5 L400 301 L383 284.5 Z"/>')
def A(dx): return f'M{178+dx} 534 L{215.5+dx} 452 L{253+dx} 534 L{239+dx} 534 L{215.5+dx} 483 L{192+dx} 534 Z'
WORD_RED = ('M147.2 465 A42 42 0 1 0 147.2 519 L137.2 510.6 A29 29 0 1 1 137.2 473.4 Z '  # C (annulus clipped at x=145)
            + A(0) + ' M281 450 H294 V521 H331 V534 H281 Z ' + A(283)
            + ' M563 450 H585 A25 25 0 0 1 585 500 H576 V534 H563 Z M576 464 V486 H585 A11 11 0 0 0 585 464 Z'
            + ' M586 497 H603 L623 534 H607 Z ' + A(473))
WORD_NAVY = 'M358 450 H372 L395.5 502.5 L419 450 H433 L395.5 534.5 Z'
def full(red=RED, navy=NAVY, sub=True, font="Jost, Futura, 'Century Gothic', Arial, sans-serif"):
    s = MARK.format(r=red, n=navy)
    s += f'<path fill="{red}" fill-rule="evenodd" d="{WORD_RED}"/><path fill="{navy}" d="{WORD_NAVY}"/>'
    s += f'<rect x="148" y="567" width="503" height="4.5" fill="{navy}"/>'
    if sub:
        s += (f'<text x="169" y="618" textLength="461" lengthAdjust="spacing" font-family="{font}" '
              f'font-size="32" font-weight="500" fill="{red}">LABS &amp; MINERALS</text>')
    return s
def svg(inner, vb="60 170 680 460", label="Calvara Labs & Minerals"):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="{label}"><title>{label}</title>{inner}</svg>'

def lockup(letters=RED, v=NAVY, outline=RED, core=NAVY, rule=NAVY, sub=RED, label="Calvara Labs & Minerals"):
    mark = MARK.format(r=outline, n=core)
    g = f'<g transform="translate(-352.7 312) scale(0.78)">{mark}</g>'
    g += f'<path fill="{letters}" fill-rule="evenodd" d="{WORD_RED}"/><path fill="{v}" d="{WORD_NAVY}"/>'
    g += f'<rect x="73" y="566" width="653" height="5" fill="{rule}"/>'
    g += (f'<text x="75" y="619" textLength="649" lengthAdjust="spacing" font-family="Jost, Futura, Arial, sans-serif" '
          f'font-size="33" font-weight="500" fill="{sub}">LABS &amp; MINERALS</text>')
    return f'<svg class="lockup" xmlns="http://www.w3.org/2000/svg" viewBox="-122 440 856 186" role="img" aria-label="{label}"><title>{label}</title>{g}</svg>'
def mark_svg(outline=RED, core=NAVY, label="Calvara"):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="306 177 188 215" role="img" aria-label="{label}"><title>{label}</title>{MARK.format(r=outline, n=core)}</svg>'
