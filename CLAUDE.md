# CLAUDE.md: import toolkit, generic core

The portfolio half of the Onboarding & Import Toolkit. The CYB4 adapter is `~/ws/10_cyberangels/ops/import-toolkit-cyb4/` and imports this package.

## Boundary
- Nothing here names CYB4, Cyberangels, their endpoints, fields or customers.
- The target system is an interface (`Target`: `push(records)`, `fetch(ids)`), implemented by the adapter. Tests use a fake target.
- Samples in `samples/` are synthetic: invented companies, `example.com` domains, documentation IP ranges (192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24).

## Plan
Follow `learning-plan.md` in the Engineering Lab project (week by week: loader, validator, mapping and dedup, SQLite store, reconciler, pusher interface, CLI and README, CI).
This is a learning project: I write the code. Give hints first, full solutions only if I write SOLVE.
