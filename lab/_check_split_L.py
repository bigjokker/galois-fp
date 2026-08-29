"""Checks A (split-fibre BAL) and B (independent PARI L). Run from lab/."""
from fractions import Fraction
from math import gcd

import core


def is_split(roots):
    return all(R.in_Fq for R in roots)


def bal_from_counts(neg, pos, zero):
    den = neg + pos
    if den == 0:
        return None, (neg, pos, zero)
    return Fraction(neg, den), (neg, pos, zero)


def find_split(qs):
    out = {q: [] for q in qs}
    for q in qs:
        for r in range(1, q):
            for m0 in range(q):
                roots, L = core.fibre(q, r, m0)
                ns = [R for R in roots if not R.in_Fq]
                nl = [R for R in roots if R.d > 1]
                split = (not ns)  # all roots in F_q
                if split:
                    out[q].append((r, m0, L, len(roots),
                                   tuple((R.d, R.in_Fq) for R in roots),
                                   bool(nl)))
                    if L != 1:
                        print("WARN split but L!=1", q, r, m0, L)
                    if nl:
                        print("WARN split but nonlinear present", q, r, m0)
    return out


def check_A():
    print("=" * 72)
    print("CHECK A: split fibres from definition, fibre_counts BAL")
    print("=" * 72)
    splits = find_split([5, 7, 11, 13])
    failures = []
    rows = []
    for q in (5, 7, 11, 13):
        print("\nq = %d  (q = %d mod 4)  split fibres: %d"
              % (q, q % 4, len(splits[q])))
        for r, m0, L, nroots, degs, has_nl in splits[q]:
            print("  (r,m0)=(%d,%d)  L=%d  nroots=%d  degs=%s  nonlinear=%s"
                  % (r, m0, L, nroots, degs, has_nl))
    # pick at least 4 at q=7 or 11, 4 at q=5 or 13
    pick_q3 = []
    for q in (7, 11):
        for t in splits[q]:
            pick_q3.append((q,) + t[:2])
    pick_q1 = []
    for q in (5, 13):
        for t in splits[q]:
            pick_q1.append((q,) + t[:2])
    print("\n--- fibre_counts on split fibres ---")
    print("%4s %4s %4s %6s %8s %8s %8s %10s %s"
          % ("q", "r", "m0", "qmod4", "neg", "pos", "zero", "BAL", "pred"))
    used_q3 = pick_q3[:max(4, min(8, len(pick_q3)))]
    used_q1 = pick_q1[:max(4, min(8, len(pick_q1)))]
    if len(used_q3) < 4:
        failures.append("fewer than 4 split fibres at q=7,11: %d" % len(used_q3))
    if len(used_q1) < 4:
        failures.append("fewer than 4 split fibres at q=5,13: %d" % len(used_q1))
    for q, r, m0 in used_q3 + used_q1:
        neg, pos, zero = core.fibre_counts(q, r, m0)
        bal, _ = bal_from_counts(neg, pos, zero)
        if q % 4 == 3:
            pred = "BAL=1/2"
            ok = (bal == Fraction(1, 2))
        else:
            pred = "BAL in {0,1}"
            ok = (bal in (Fraction(0), Fraction(1)))
        mark = "OK" if ok else "FAIL"
        print("%4d %4d %4d %6d %8d %8d %8d %10s %s %s"
              % (q, r, m0, q % 4, neg, pos, zero, bal, pred, mark))
        rows.append((q, r, m0, q % 4, neg, pos, zero, str(bal), pred, mark))
        if not ok:
            failures.append("BAL mismatch q=%d r=%d m0=%d BAL=%s pred %s"
                            % (q, r, m0, bal, pred))
    return failures, rows, splits


FIBRES_B = [
    # required q=11 fibres
    (11, 2, 6), (11, 2, 7), (11, 2, 8), (11, 2, 9), (11, 3, 6),
    # several r=1
    (5, 1, 0), (5, 1, 1), (5, 1, 2), (5, 1, 3),
    (7, 1, 0), (7, 1, 1), (7, 1, 2),
    (11, 1, 1), (11, 1, 2),
    (13, 1, 1),
]


def py_L_table():
    print("\n" + "=" * 72)
    print("CHECK B: core.fibre L for 15 fibres")
    print("=" * 72)
    rows = []
    for q, r, m0 in FIBRES_B:
        roots, L = core.fibre(q, r, m0)
        orders = []
        for R in roots:
            if R.in_Fq:
                orders.append("d=%d:inFq" % R.d)
            else:
                orders.append("d=%d:ord=%s" % (R.d, R.order))
        h = core.fibre_poly(q, r, m0)
        h_asc = [int(c) for c in h]
        print("  q=%d r=%d m0=%d  L=%s  %s  h=%s"
              % (q, r, m0, L, ", ".join(orders), h_asc))
        rows.append((q, r, m0, L, orders, h_asc))
    return rows


def write_pari_script(path):
    lines = [
        "\\ independent L: construct h from definition, factormod, fforder",
        "default(parisize, 256000000);",
        "default(realprecision, 38);",
        "",
        "fibre_h(q, r, m0) = {",
        "  my(x='x, B, C, u, h);",
        "  B = prod(k=0, r-1, x - Mod(k, q));",
        "  C = prod(a=r, q-1, x - Mod(a, q));",
        "  u = C * deriv(B);",
        "  h = u - Mod(m0, q);",
        "  h",
        "};",
        "",
        "fibre_L_pari(q, r, m0) = {",
        "  my(h, F, nr, L=1, i, f, d, a, g, o);",
        "  h = fibre_h(q, r, m0);",
        "  F = factormod(lift(h)*Mod(1,q), q);",
        "  nr = matsize(F)[1];",
        "  for(i=1, nr,",
        "    f = F[i,1];",
        "    d = poldegree(f);",
        "    if(d >= 2,",
        "      a = ffgen(f);",
        "      g = a^q - a;",
        "      if(g != 0,",
        "        o = fforder(g);",
        "        L = lcm(L, o)",
        "      )",
        "    )",
        "  );",
        "  L",
        "};",
        "",
        "fibres = [",
    ]
    for q, r, m0 in FIBRES_B:
        lines.append("  [%d, %d, %d]," % (q, r, m0))
    lines.append("];")
    lines += [
        "",
        "for(i=1, #fibres,",
        "  q = fibres[i][1]; r = fibres[i][2]; m0 = fibres[i][3];",
        "  L = fibre_L_pari(q, r, m0);",
        "  h = fibre_h(q, r, m0);",
        "  F = factormod(lift(h)*Mod(1,q), q);",
        "  degs = vector(matsize(F)[1], j, poldegree(F[j,1]));",
        "  print(Str(q,\",\",r,\",\",m0,\",\",L,\",\",degs));",
        ");",
        "quit;",
        "",
    ]
    with open(path, "w", encoding="ascii", newline="\n") as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    fa, rows, splits = check_A()
    py_L_table()
    write_pari_script("_check_L.gp")
    print("\nwrote _check_L.gp")
    print("A failures:", fa)
    n3 = sum(len(splits[q]) for q in (7, 11))
    n1 = sum(len(splits[q]) for q in (5, 13))
    print("split counts: q=3mod4 %d, q=1mod4 %d" % (n3, n1))
