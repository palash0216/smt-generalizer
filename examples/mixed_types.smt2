; Int, Real and Bool variables together
(declare-const x Int)
(declare-const y Real)
(declare-const flag Bool)
(assert (=> flag (> x 5)))
(assert (< (+ x y) 10.5))
(check-sat)
