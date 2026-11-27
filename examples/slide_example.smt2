; Example from the project slides
(declare-const a Int)
(declare-const b Int)
(assert (< a 20))
(assert (< b a))
(assert (< (+ a b) 20))
(check-sat)
