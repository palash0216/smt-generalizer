"""Step 1: Collect the variables of an SMT problem."""
from z3 import (parse_smt2_file, And, is_const, is_int, is_real, is_bool,
                Z3_OP_UNINTERPRETED)


def load_problem(path):
    """Read an .smt2 file and return all assertions combined into one formula (phi)."""
    assertions = parse_smt2_file(path)
    return And(*assertions) if len(assertions) > 0 else And(True)


def collect_variables(phi):
    """Walk the formula and return {name: (z3_variable, type)}.

    type is one of "Int", "Real", "Bool", or "Unsupported".
    """
    found = {}
    seen = set()
    stack = [phi]

    while stack:
        e = stack.pop()
        if e.get_id() in seen:          # same sub-expression can appear many times
            continue
        seen.add(e.get_id())

        # A variable = a constant that the user declared (not a number like 20)
        if is_const(e) and e.decl().kind() == Z3_OP_UNINTERPRETED:
            found[str(e)] = (e, _type_of(e))
        else:
            stack.extend(e.children())   # go deeper into the expression

    return dict(sorted(found.items()))   # sorted by name -> stable output


def _type_of(var):
    if is_int(var):
        return "Int"
    if is_real(var):
        return "Real"
    if is_bool(var):
        return "Bool"
    return "Unsupported"


if __name__ == "__main__":
    import sys
    phi = load_problem(sys.argv[1])
    for name, (_, t) in collect_variables(phi).items():
        print(f"{name}: {t}")
