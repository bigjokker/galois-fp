# Frobenius certificates for falling factorials

**Author: Open.** Working revision, September 2026.

[Read the paper](galois_fp.pdf) | [TeX source](galois_fp.tex) | [Verification guide](tools/README.md) | [Data](ancillary/README.md)

This paper studies `f_p(x) = x(x-1)...(x-p+1) + 1` for odd primes `p`.
It develops certificates for `Gal(f_p/Q) = S_p`, a periodic discriminant
calculation, and applications to `(x)_p+c`. The identification for **every**
odd prime remains a conjecture.

- An odd Frobenius with a fixed-point count different from one certifies `S_p`
  in odd prime degree, using classification of transitive groups.
  Every `q <= p` supplies the no-root condition for this family.
- Exact congruence coverage has Dirichlet density `1/2` using `q=3`,
  `31/40` using `q=3,5`, and `7117/8064` using `q=3,5,7`.
  The last two involve finite enumeration. The three events are dependent.
- Certificates cover the **664,577 primes `5 <= p < 10^7`**.
  The special row `(5,19)` uses a quadratic/cubic factorization.
  The separate cubic discriminant argument handles `p=3`, completing all
  **664,578 odd primes** below the bound. The largest least smaller-prime
  witness is `q=73` at `p=9683099`.
- A classical Jordan and Dedekind certificate, without classification, covers
  the **236 primes `7 <= p < 1500`**, using witnesses `q <= 61`.
- For `(x)_p+c`, prime `p >= 5`, `p` not dividing `c`, and
  `mu_(m-1) < |c| < mu_(m-2)` with `m=(p-1)/2`, exactly two roots are
  non-real and complex conjugation gives `S_p`. The paper proves a
  superexponential lower bound on the number of admissible integer constants.
  The value `c=1` lies below this window.

Finite computations do not prove the all-prime conjecture. Divergent marginal
densities alone do not prove density-one coverage. Dependencies and open
questions are stated in the manuscript.

## Reproduce the computations

Use Python 3.11 and run from the repository root:

```sh
python -m pip install -r requirements.txt
python tools/verify.py --quick
python tools/verify.py --full
```

The pinned dependencies were tested with Python 3.11.9 on Windows.
Linux and Windows quick checks are configured in CI.
Quick mode validates complete data coverage and runs deterministic certificate
samples, independent SymPy comparisons, small group and root-count checks,
and failure regressions. Full mode additionally checks every main witness
and its minimality, every Jordan certificate, complete period and joint-class
computations, discriminants through degree 97, ramification, and all stored
density counts.

Expect seconds for quick mode and tens of minutes for full mode; Jordan
factorizations and the density sweep dominate. Full Jordan checks use up to
four isolated workers; pass `--jobs 1` to its standalone command for serial execution. Timings, environment, hashes,
exit codes and logs are saved in `.build/verification/`. Failures return
nonzero. Run without `python -O` or `PYTHONOPTIMIZE`: several checks use assertions.
Individual checks and safe data regeneration are described in
[tools/README.md](tools/README.md). [Data schemas](ancillary/README.md) specify
populations and the treatment of ramification.

## Build the PDF

Install [Tectonic 0.17.0](https://github.com/tectonic-typesetting/tectonic/releases/tag/tectonic%400.17.0)
and put it on `PATH`:

```sh
python tools/build_paper.py
```

The PDF and build record are in `.build/paper/`. Use `--update-pdf` to
replace the repository PDF after a successful build, `--tectonic PATH` for
an explicit executable, and `--only-cached` with an existing TeX resource cache.
The first build may download TeX resources. Standard LaTeX can also compile
this AMS article.

## Contents

```text
galois_fp.tex / galois_fp.pdf  Paper source and matching working-revision PDF
ancillary/                   Certificate and measurement data
tools/                       Verification, regeneration and build commands
tests/                       Certificate-validation regressions
formal/                      Optional Lean affine fixed-point lemma
.github/workflows/           Quick checks, PDF build and manual full audit
CITATION.cff / .zenodo.json   Citation and prospective archive metadata
LICENSE / CHANGELOG.md       License notice and revision history
```

The [Lean supplement](formal/README.md) covers only the affine fixed-point
step. It is not a formalization of the full paper. Its toolchain and mathlib
commit are pinned, with a separate build and axiom-inspection procedure.
Exploratory experiments and reference PDFs are outside this publication repository.

## Cite this revision

This is an **unreleased working revision**. Grok's AI-assisted mathematical
and bibliography review has been incorporated; the paper has not been
independently refereed. It is not the previously archived v1.2.0. Specify a Git commit when
citing the working source; `CITATION.cff` supplies the author and title.

```bibtex
@misc{open_frobenius_certificates,
  author = {Open},
  title = {Frobenius certificates for the Galois group of
           x(x-1)...(x-p+1)+1},
  year = {2026},
  note = {Working revision; specify the Git commit used},
  url = {https://github.com/bigjokker/galois-fp}
}
```

Historical identifiers recorded in the project are
[concept DOI](https://doi.org/10.5281/zenodo.22135245),
[v1.2.0](https://doi.org/10.5281/zenodo.22150227),
[v1.1.0](https://doi.org/10.5281/zenodo.22136373), and
[v1.0.0](https://doi.org/10.5281/zenodo.22135246).
They are retained as historical references; this local revision has not been
deposited or assigned a new DOI. Licensed under [CC BY 4.0](LICENSE).
AI assistance is acknowledged in the paper.
