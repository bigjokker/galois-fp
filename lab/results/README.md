# results — provenance, and which files are superseded

Computed data. Several files predate corrections made later; a reader who picks
the wrong one gets a refuted claim. Check here before citing anything.

| file | written by | status |
|---|---|---|
| `02_d2_coset.txt` | `02_d2_coset.py` | current |
| `02_orders.txt` | `02_d2_coset.py` | current — the `d = 2` order law |
| `03_r1.txt` | `03_r1.py` | **densities are EPS, not BAL** — see below |
| `03_r1_rules.txt` | `03_r1.py` | **rule D refuted** — see below |
| `04_r2.txt` | `04_r2.py` | current |
| `05_imbalance.txt` | `_imb.py` | orphan: there is no `05_*.py`, it came from scratch |
| `06_small_L.txt` | `06_small_L.py` | current |
| `07_census.txt` | `07_census.py` | superseded by `census_q29_q37.txt` (older, pre-BSGS run: 442 s / 1195 s against 199 s / 725 s) |
| `census_q29_q37.txt` | `07_census.py` | current census, `L ≤ 2000`, BSGS orders |
| `exhaustive_53_61.txt` | `_q1k.py` | current — cited in `pairing_lemma.md` |
| `jclass_scan.txt` | `09_jclass.py` | current for `q ≡ 1`; its **`q ≡ 3` rows are off-fibre** and superseded by `onfibre_q3.txt` |
| `onfibre_q3.txt` | `10_onfibre_q3.py` | current — the on-fibre `q ≡ 3` run, 70 pairs |
| `q1_rule_41_53_61.txt` | `_q1f.py` | superseded: it reports 53 and 61 as "predicted-only", but `exhaustive_53_61.txt` later did them exhaustively |
| `witness_offfibre_SUPERSEDED.txt` | `08_witness.py` | **do not use** — sampled `m` off-fibre |
| `witness_onfibre.txt` | `08_witness.py` | current — on-fibre, 2716/2716 |

## The two traps these files fell into

**EPS vs BAL.** Two different densities, equal only when nothing ramifies:

* **BAL** — the `−1 : +1` balance with ramified `m` excluded. The structural object.
* **EPS** — the fraction of primes of the fibre yielding a `−1` certificate; a
  ramified `p` certifies nothing, so it belongs in the denominator. What `ε_q`
  needs.

`03_r1.txt` reports EPS. So its `q ≡ 3` rows showing `4/9`, `12/25`, `40/81`
look like non-`1/2` densities; converting, `q = 7, d = 3` is `8:8` plus 2
ramified, `q = 11, d = 5` is `24:24` plus 2, `q = 19, d = 9` is `80:80` plus 2 —
**all BAL = 1/2**, as the two-translation theorem requires.

Consequently **rule D in `03_r1_rules.txt` is refuted**: it claims
`q ≡ 3 (mod 4)`, `ord(c)` odd gives density `1/2 − 1/(2·ord²)` ("34 hold, 4
fail"). Under BAL every `q ≡ 3` fibre is exactly `1/2`, for every `c`. See
`../notes/pairing_lemma.md`, "q ≡ 3 (mod 4): the extension to ALL c".

**Off-fibre sampling.** The fibre is `m ≡ m0 (mod q)`. Iterating `m` by 2 from
the right parity does not enforce it. Harmless at `q ≡ 1` (no archimedean
factor, `gcd(q,L) = 1`), wrong at `q ≡ 3`. This is why `witness.txt` was
renamed and re-run, and why `jclass_scan.txt`'s `q ≡ 3` half was redone in
`onfibre_q3.txt`.

## Note

Neither census file contains a `split … density 1/2` line, because both cover
`q ≡ 1 (mod 4)` only, where split fibres are constant. The split-fibre fix in
`07_census.py` (split is density `1/2` for `q ≡ 3`, not `0` or `1`) has
therefore never run on a real `q ≡ 3` census — open item **D14** in
`../notes/OPEN.md`.
