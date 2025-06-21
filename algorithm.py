
from scipy.optimize import linprog

def solve_linear_program(c1, c2, a11, a12, b1, a21, a22, b2):
    try:
        # Virgül yerine nokta kullanarak sayılara dönüştür
        c = [-float(c1.replace(",", ".")), -float(c2.replace(",", "."))]
        A = [
            [float(a11.replace(",", ".")), float(a12.replace(",", "."))],
            [float(a21.replace(",", ".")), float(a22.replace(",", "."))]
        ]
        b = [float(b1.replace(",", ".")), float(b2.replace(",", "."))]

        # Simplex yerine modern çözüm: highs
        result = linprog(c, A_ub=A, b_ub=b, method='highs')

        if result.success:
            x_vals = [round(v, 4) for v in result.x]
            max_val = round(-result.fun, 4)
            return True, x_vals, max_val
        else:
            return False, None, None
    except Exception as e:
        return False, str(e), None
