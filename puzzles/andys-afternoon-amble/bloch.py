"""
q = P(first visit to color-0 set is the origin) computed two ways:

(1) DP (float, killed walk, horizon L): exact-in-structure, ~1e-15 tail bound.
(2) Bloch/Fourier: q = (1/9) * sum_{x,z in N(o)} G_Omega(x,z), where G_Omega is the
    Green function of the graphene walk killed on the (2Lambda)-periodic color-0 set.
    G_Omega(x,z) = (2pi)^-2 int [ (I-Q(theta))^{-1} ]_{cx,cz} e^{i theta.(Rz-Rx)} dtheta
    with Q(theta) the 6x6 twisted transition matrix on alive classes.
    Integrand analytic on the torus => trapezoid rule converges geometrically.
"""
import math, cmath

def nbrs(cell):
    s, m, n = cell
    if s == 0:
        return [(1, m, n), (1, m, n - 1), (1, m + 1, n - 1)]
    else:
        return [(0, m, n + 1), (0, m - 1, n + 1), (0, m, n)]

def is_home_color(cell):
    s, m, n = cell
    if s == 0:
        return m % 2 == 0 and n % 2 == 0
    else:
        return (m + 1) % 2 == 0 and n % 2 == 0

o = (0, 0, 0)

# ---------------- (1) DP cross-check ----------------
def dp(L=120):
    cur = {}
    for x in nbrs(o):
        cur[x] = cur.get(x, 0.0) + 1.0 / 3.0
    q = 0.0
    p_other = 0.0
    for t in range(2, L + 1):
        nxt = {}
        for cell, w in cur.items():
            w3 = w / 3.0
            for y in nbrs(cell):
                if is_home_color(y):
                    if y == o:
                        q += w3
                    else:
                        p_other += w3
                else:
                    nxt[y] = nxt.get(y, 0.0) + w3
        cur = nxt
    leftover = sum(cur.values())
    return q, p_other, leftover

q_dp, p_dp, left = dp(140)
print(f"DP: q = {q_dp:.15f}   p_other = {p_dp:.15f}   leftover = {left:.3e}")
print(f"DP: p = 1-q in [{1-q_dp-left:.15f}, {1-q_dp:.15f}]")

# ---------------- (2) Bloch integral ----------------
import mpmath as mp
mp.mp.dps = 50

# classes: (s, m0, n0), m0,n0 in {0,1}; killed: (0,0,0) and (1,1,0)
classes = [(s, a, b) for s in (0, 1) for a in (0, 1) for b in (0, 1)]
killed = {(0, 0, 0), (1, 1, 0)}
alive = [c for c in classes if c not in killed]
aidx = {c: i for i, c in enumerate(alive)}
assert len(alive) == 6

def decomp(cell):
    """cell -> (class, R) with R in Z^2 (units of 2Lambda)"""
    s, m, n = cell
    a, b = m % 2, n % 2
    return (s, a, b), ((m - a) // 2, (n - b) // 2)

# edges between alive classes with translation offsets
edges = []  # (i, j, (dM,dN))
for c in alive:
    s, a, b = c
    base = (s, a, b)
    for y in nbrs((s, a, b)):
        cy, R = decomp(y)
        if cy in killed:
            continue
        edges.append((aidx[c], aidx[cy], R))

def Q_theta(t1, t2):
    M = mp.zeros(6)
    third = mp.mpf(1) / 3
    for i, j, (dM, dN) in edges:
        M[i, j] += third * mp.e**(1j * (t1 * dM + t2 * dN))
    return M

# spectral radius check on a grid (rough, float)
import numpy as np
maxrho = 0.0
for u in np.linspace(0, 2 * np.pi, 25):
    for v in np.linspace(0, 2 * np.pi, 25):
        M = np.zeros((6, 6), dtype=complex)
        for i, j, (dM, dN) in edges:
            M[i, j] += np.exp(1j 	* (u * dM + v * dN)) / 3.0
        r = max(abs(np.linalg.eigvals(M)))
        maxrho = max(maxrho, r)
print(f"max spectral radius of Q(theta) on grid: {maxrho:.6f}  (<1 required)")

# the three neighbors of origin, decomposed
N_o = [decomp(x) for x in nbrs(o)]
print("neighbors of o:", N_o)

def q_bloch(N):
    """trapezoid with N points per axis"""
    total = mp.mpf(0)
    twopi = 2 * mp.pi
    # accumulate sum over grid of  sum_{x,z} [ (I-Q)^{-1} ]_{cx,cz} e^{i th.(Rz-Rx)}
    for aidx1 in range(N):
        t1 = twopi * aidx1 / N
        for aidx2 in range(N):
            t2 = twopi * aidx2 / N
            Iq = mp.eye(6) - Q_theta(t1, t2)
            G = Iq**-1
            ssum = mp.mpf(0)
            for (cx, Rx) in N_o:
                for (cz, Rz) in N_o:
                    ph = mp.e**(1j * (t1 * (Rz[0] - Rx[0]) + t2 * (Rz[1] - Rx[1])))
                    ssum += (G[aidx[cx], aidx[cz]] * ph).real
            total += ssum
    return total / (N * N) / 9

for N in (24, 48, 96):
    qb = q_bloch(N)
    print(f"Bloch N={N:3d}:  q = {mp.nstr(qb, 30)}   p = {mp.nstr(1-qb, 30)}")
