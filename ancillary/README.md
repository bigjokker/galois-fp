# Certificate and measurement data

Degree bounds are exclusive unless specified otherwise. Comment lines start
with `#`. Certificates are sufficient conditions for `S_p`; failure does not
establish a smaller group.

| File | Schema and population | Checker |
| --- | --- | --- |
| `witnesses.txt` | `p q`; 664,577 primes `5 <= p < 10^7`. Least odd `q<p` with negative symbol, except `(5,19)`, a quadratic/cubic factorization. | `verify_witnesses.py --all --least` |
| `jordan_witnesses.txt` | `p q ell degrees`; 236 primes `7 <= p < 1500`. Comma-separated degrees sum to `p`, isolate a prime `3 <= ell <= p-3`, and have odd sign. Search uses odd `q != p`. | `verify_jordan.py --all` |
| `q3_q5_classes.txt` | Exact good classes: 6 of 12 units modulo 36 and 88 of 160 units modulo 600. | `verify_classes.py --full` |
| `period_q7.json` | Upper period 268128, minimal admissible even symbol period 134064, complete-table checksum, good-unit counts, and proper-period counterexamples. | `verify_periods.py` |
| `sweep_results.txt` | `q good eligible ramified epsilon_q balance_q`; 45 odd primes `q <= 199`. Eligible degrees are primes `5 <= p < 100000`, `p>q`. | `sweep_eps.py --check-all` |
| `disc_data_p97.txt` | Integer discriminants and statistics for odd primes `p <= 97`; a separate finite ramification-search bound. | `verify_disc_p97.py` |

The main witness rows are unchanged. SHA-256 depends on checkout line endings:

- Canonical Git/LF bytes: `afe3b06023b0b274425aa0ea85926de58b821381588a781966a43f4a8718145b`.
- Windows CRLF bytes: `c79c53410952e2fcaa3f44a13226b85c61ea818f317a89537978fec9ce610215`.

Both represent the same certificate rows; reports hash the actual input bytes.
Its population plus the separate `p=3` discriminant `-23` covers all 664,578
odd primes below `10^7`. The largest least smaller-prime witness is `q=73`
at `p=9683099`.

The period certificate concerns all odd integers `n>7` coprime to 7:
114,912 admissible classes modulo the upper period. A period must preserve
this domain, hence is a multiple of 14. Once a positive period is proved,
a smaller minimal period divides it, by taking the gcd of shifts on the
cyclic table. Checking proper admissible divisors is therefore sufficient.
The checksum uses byte 255 for excluded classes and `symbol+1` otherwise.
There are 18,088 good units among 36,288 units modulo the minimal period.

The measured table has `epsilon_q=good/eligible` and
`balance_q=good/(eligible-ramified)`. Symbol-zero rows belong in the first
denominator, and are excluded only from the second. These finite prime
measurements are not exact Dirichlet densities. At `q=7` the exact prime-class
certificate density is `323/648`, unramified balance `1/2`, and ramification
density `1/324`. The integer ramification density `50/3591` has a different measure.

`verify_joint357.py` recomputes the full joint law on 725,760 units modulo
3,351,600. Union density is `7117/8064`; the `q=3,7` intersection is
`787/3024`, so the events cannot be treated as independent.
