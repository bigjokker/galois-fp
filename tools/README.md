# Verification and regeneration

Run from the repository root with Python 3.11 and `requirements.txt`.
Lean and Tectonic are separate tools.

```sh
python tools/verify.py --quick
python tools/verify.py --full
```

Both modes save logs and a JSON report under `.build/verification/`.
`--output PATH` selects a new directory. Reports record environment,
dependency versions, Git HEAD, SHA-256 hashes of source/checkers/data,
timings, and exit codes. HEAD alone does not identify uncommitted changes;
the hashes do. Checks run sequentially and stop on failure. Run without
`-O` or `PYTHONOPTIMIZE`, since several checks use assertions.

| Checker | Scope | Full mode |
| --- | --- | --- |
| `verify_witnesses.py` | Complete prime coverage, bounds, `(5,19)` factorization, negative symbols | `--all --least` checks every row and every smaller odd candidate |
| `verify_jordan.py` | Complete coverage, squarefreeness, stored degrees, isolated prime cycle, odd sign | `--all` re-derives all 236 certificates |
| `verify_reference.py` | Independent SymPy products, discriminants, resultants, degrees, general-constant formula | Same in both modes |
| `verify_reduced.py` | Reduced versus direct resultant; negative, positive, zero branches | Samples across scales to `10^7`; quick uses modest degrees |
| `verify_group_facts.py` | Finite field-automorphism signs and `PGL_2(11)` | Same in both modes; supports the written proof |
| `verify_classes.py` | `q=3,5` tables and lift counts | `--full` checks every admissible class modulo upper period 15600 |
| `verify_periodicity.py` | Fibre identities, quadratic-fibre restriction, general/refined period bounds | Full only |
| `verify_periods.py` | Complete `q=7` period certificate and proper-divisor counterexamples | Full only |
| `verify_fibre_census.py` | Complete small-prime unit-class census; constant residues versus constant characters | Full only |
| `verify_fibre_orders.py` | `E_q` for `q=3,5,7,11,13` and finite fibre measurements | Full only; no asymptotic conclusion |
| `verify_joint357.py` | Full joint law on 725,760 units modulo 3,351,600 | Full only; standalone `--quick` is a consistency sample |
| `verify_disc_p97.py` | Integer discriminants and bounded ramification searches through degree 97 | Full only |
| `verify_ramification.py` | Fibre vanishing and integer-density bounds through `q=13` | Full only |
| `sweep_eps.py` | Stored measured prime-density counts | `--check-all` verifies all 45 rows; `--check` checks six |
| `verify_window.py` | Critical values, symmetry, exact Sturm counts and sampled irreducibility for `p=5,7,11,13,17,19` | Same in both modes |
| `tests/test_certificates.py` | Missing/duplicate/composite/invalid rows, false certificates, absent selections, affine types | Same in both modes |

Default witness/Jordan runs validate the entire population but check arithmetic
on deterministic samples. `--p P` requires a stored row. An absent selection
or failed certificate returns nonzero. `verify_witnesses.py --direct` uses the
slow degree-`p` resultant; the full direct audit is impractical.
Reduced and direct routines share `fpcore.py`; independent SymPy checks provide
a separate implementation at modest degrees.

Main-list minimality means least **odd prime `q<p`**, with `p=5` special.
The Jordan generator searches odd primes `q != p`. The full audit verifies
Jordan certificates themselves, not their least-witness property. Full checks
use at most four isolated CLI workers (`--jobs N` selects the count); serial
execution remains available with `--jobs 1`. Worker failure fails the audit.
Input hashes are recorded at the start of each check and at the end of the
run, so changes during an audit are visible in the report.

## Safe regeneration

Generators require explicit new output paths, refuse existing files, and fail
if any requested degree has no certificate in the search range. Coverage and
optional prefix comparisons complete before writing a successful table.
Create `.build/` first, or run the aggregate verifier to create it.

```sh
python tools/generate_witnesses.py --limit 10000000 --qmax 1000 --output .build/witnesses.txt --compare ancillary/witnesses.txt
python tools/generate_jordan.py --limit 1500 --qmax 400 --output .build/jordan_witnesses.txt --compare ancillary/jordan_witnesses.txt
python tools/sweep_eps.py --full --limit 100000 --output .build/sweep_results.txt
python tools/verify_periods.py --write .build/period_q7.json
```

## Arithmetic assumptions

`fpcore.py` uses ascending-degree NumPy `int64` coefficient arrays in `[0,q)`.
Exact packed multiplication requires `min(len(a),len(b))*(q-1)^2 < 2^63`;
the implementation checks this bound. The published ranges satisfy it.
`reduced.py` evaluates a degree-`q-1` resultant with repeated squaring instead
of forming the degree-`p` polynomial. Complexity estimates count finite-field
operations, not uniform bit complexity for unbounded `q`.

Finite checks do not prove the all-prime conjecture, an asymptotic coverage
law, novelty, or a full formal proof. The mathematical inputs remain explicit
in the paper.
