# SMT Generalizer

Course project for *Formal Methods of Software Engineering* (Bauhaus-Universität Weimar).

SMT solvers such as Z3 return one solution (model) for a satisfiable problem.
This tool generalizes that single solution into a description of many solutions
(e.g. a range of values per variable).

## Setup
pip install -r requirements.txt

## Structure
- smtgen/    – source code
- examples/  – .smt2 test problems
- tests/     – automated tests
- eval/      – evaluation scripts and results
- docs/      – devlog, design decisions, report