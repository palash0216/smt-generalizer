# Design decisions

## D1: Description = box of intervals
- Options considered: list of solutions, box, several boxes, intervals with steps,
  dependent ranges, octagons
- Chosen: box (main), several boxes (extension), list of solutions (baseline)
- Why: simple, readable, easy to check with Z3