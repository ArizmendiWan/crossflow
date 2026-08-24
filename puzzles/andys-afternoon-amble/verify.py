#!/usr/bin/env python3
"""
Andy's Afternoon Amble — Jane Street puzzle, August 2026.
Answer: p = 11/20 = 0.55 exactly.

This script verifies every step of the solution in SOLUTION.md:

  [1] Geometry & turn semantics on the pitch (L = +60°, R = −60°, B = reverse),
      pitch faces are 6-rings, truncated-tetrahedron white-map is K4 on the
      sphere with triangular faces.
  [2] The Klein-group 4-coloring of the pitch's white cells is a proper coloring,
      equivariant with the cyclic (rotation) structure of the truncated
      tetrahedron => branched covering: cell color == position on tetrahedron,
      for every turn sequence (checked directly on random paired walks).
  [3] Non-home-colored cells form disjoint 6-rings, each ring cell having its
      own distinct home-colored absorber, exactly one of which is the true home.
  [4] Ring absorption probability v0 = 9/20 (exact linear algebra), and the
      closed-form path counts it implies match an exact-rational lattice DP,
      which brackets p within 11/20 ± 3^-something tiny.
  [5] Monte Carlo sanity check.

Run: python3 verify.py   (pure stdlib; ~1 minute)
"""
import math
import random
from fractions import Fraction
from itertools import product

# ----------------------------------------------------------------------------
# The pitch's white cells: graphene lattice.
# A-cell (0,m,n) at m*a+n*b with a=(1,0), b=(1/2,√3/2); B-cell (1,m,n) above it.
# CCW neighbor orders (verified against coordinates below):
#   A(m,n): B(m,n) @90°, B(m,n-1) @210°, B(m+1,n-1) @330°
#   B(m,n): A(m,n+1) @30°, A(m-1,n+1) @150°, A(m,n) @270°
# ----------------------------------------------------------------------------
def nbrs_ccw(cell):
    s, m, n = cell
    if s == 0:
        return [(1, m, n), (1, m, n - 1), (1, m + 1, n - 1)]
    return [(0, m, n + 1), (0, m - 1, n + 1), (0, m, n)]

def pos(cell):
    s, m, n = cell
    return (m + n * 0.5, n * (math.sqrt(3) / 2) + (s / math.sqrt(3)))

def rho(v, u, k=1):
    ns = nbrs_ccw(v)
    return ns[(ns.index(u) + k) % 3]

def step_arc(arc, turn):
    """arc=(u,v): last move u->v. Right = next CCW exit, Left = next CW, B = back."""
    u, v = arc
    if turn == 'B':
        return (v, u)
    return (v, rho(v, u, 1 if turn == 'R' else -1))

# [1] geometry checks
for cell in [(0, 0, 0), (0, 2, -1), (1, 0, 0), (1, -3, 5)]:
    p0 = pos(cell)
    expect = [90, 210, 330] if cell[0] == 0 else [30, 150, 270]
    for nb, e in zip(nbrs_ccw(cell), expect):
        p1 = pos(nb)
        assert abs(math.hypot(p1[0] - p0[0], p1[1] - p0[1]) - 1 / math.sqrt(3)) < 1e-9
        ang = math.degrees(math.atan2(p1[1] - p0[1], p1[0] - p0[0])) % 360
        assert abs(ang - e) < 1e-6
for cell in [(0, 0, 0), (1, 4, -2)]:
    for u in nbrs_ccw(cell):
        pu, pv = pos(u), pos(cell)
        h_in = math.atan2(pv[1] - pu[1], pv[0] - pu[0])
        for t, dh in [('R', -60), ('L', +60)]:
            a2 = step_arc((u, cell), t)
            q0, q1 = pos(a2[0]), pos(a2[1])
            d = (math.degrees(math.atan2(q1[1] - q0[1], q1[0] - q0[0]) - h_in) + 540) % 360 - 180
            assert abs(d - dh) < 1e-6
arc0 = ((1, 0, 0), (0, 0, 0))
for t in 'LR':
    a, k = arc0, 0
    while True:
        a, k = step_arc(a, t), k + 1
        if a == arc0:
            break
    assert k == 6  # pitch faces: 6-rings around black hexagons
print("[1] pitch geometry, turn semantics, 6-cycle faces: OK")

# Truncated tetrahedron white-map: K4 with spherical rotation system.
RHO_T = {0: (1, 2, 3), 1: (0, 3, 2), 2: (0, 1, 3), 3: (0, 2, 1)}
def t_rho(v, u, k=1):
    c = RHO_T[v]
    return c[(c.index(u) + k) % 3]
def t_step(arc, turn):
    u, v = arc
    if turn == 'B':
        return (v, u)
    return (v, t_rho(v, u, 1 if turn == 'R' else -1))

for t in 'LR':  # all faces triangles, 4 of them  =>  sphere; black triangles
    seen, faces = set(), 0
    for a0 in [(u, v) for u in range(4) for v in range(4) if u != v]:
        if a0 in seen:
            continue
        a, k = a0, 0
        while True:
            seen.add(a)
            a, k = t_step(a, t), k + 1
            if a == a0:
                break
        assert k == 3
        faces += 1
    assert faces == 4
print("[1] truncated-tetrahedron map (K4, triangular faces, sphere): OK")

# ----------------------------------------------------------------------------
# [2] The coloring (Klein group V = Z2 x Z2, identified with the 4 hexagons via
#     0=(0,0), 1=(1,0), 2=(1,1), 3=(0,1)):
#     c(A(m,n)) = (m%2, n%2),  c(B(m,n)) = ((m+1)%2, n%2)
# ----------------------------------------------------------------------------
V2F = {(0, 0): 0, (1, 0): 1, (1, 1): 2, (0, 1): 3}
def color(cell):
    s, m, n = cell
    return V2F[((m + s) % 2, n % 2)]

for m, n, s in product(range(-6, 7), range(-6, 7), (0, 1)):
    v = (s, m, n)
    cv, ns = color(v), nbrs_ccw(v)
    assert sorted(color(x) for x in ns) == sorted(set(range(4)) - {cv})
    for u in ns:  # equivariance with the rotation structure (both directions)
        assert color(rho(v, u, 1)) == t_rho(cv, color(u), 1)
        assert color(rho(v, u, -1)) == t_rho(cv, color(u), -1)
print("[2] proper 4-coloring, rotation-equivariant (branched covering exists): OK")

rng = random.Random(12345)
o = (0, 0, 0)
for _ in range(4000):  # paired walks: color == tetrahedron position, always
    first = rng.choice(nbrs_ccw(o))
    g_arc, t_arc = (o, first), (0, color(first))
    for _ in range(40):
        assert color(g_arc[1]) == t_arc[1]
        w = rng.choice('BLR')
        g_arc, t_arc = step_arc(g_arc, w), t_step(t_arc, w)
print("[2] 4000 random paired walks, 40 steps each: color == tetra position: OK")

# ----------------------------------------------------------------------------
# [3] Ring structure of the non-home-colored cells
# ----------------------------------------------------------------------------
def home(cell):
    return color(cell) == 0

for s, m, n in product((0, 1), range(-8, 9), range(-8, 9)):
    c = (s, m, n)
    assert sum(home(x) for x in nbrs_ccw(c)) == (0 if home(c) else 1)
start, ring = (1, 0, 0), [(1, 0, 0)]
prev, cur = None, start
while True:
    nxts = [x for x in nbrs_ccw(cur) if not home(x) and x != prev]
    prev, cur = cur, nxts[0]
    if cur == start:
        break
    ring.append(cur)
assert len(ring) == 6
assert len({(s, m % 2, n % 2) for s, m, n in ring}) == 6  # a transversal of the
# six alive classes mod 2Λ  =>  every component is a 2Λ-translate of this ring.
absorbers = [next(x for x in nbrs_ccw(c) if home(x)) for c in ring]
assert len(set(absorbers)) == 6 and absorbers.count(o) == 1
print("[3] alive cells = disjoint 6-rings; 6 distinct absorbers, one true home: OK")

# ----------------------------------------------------------------------------
# [4] Ring absorption: v0 = 9/20; exact-rational lattice DP bracket for p
# ----------------------------------------------------------------------------
# v0 = 1/3 + (2/3)v1; v1 = (v0+v2)/3; v2 = (v1+v3)/3; v3 = (2/3)v2
# => v2 = (3/7)v1 => v1 = (7/18)v0 => v0 = (1/3)/(1 - 7/27) = 9/20
v0 = Fraction(1, 3) / (1 - Fraction(7, 27))
assert v0 == Fraction(9, 20)
print(f"[4] ring linear system: q = v0 = {v0}, p = {1 - v0}")

L = 120
cur_cnt = {x: 1 for x in nbrs_ccw(o)}   # path counts, denominator 3^t implicit
q_ex, p_ex = Fraction(0), Fraction(0)
for t in range(2, L + 1):
    nxt, a_t, b_t = {}, 0, 0
    for cell, w in cur_cnt.items():
        for y in nbrs_ccw(cell):
            if home(y):
                if y == o:
                    a_t += w
                else:
                    b_t += w
            else:
                nxt[y] = nxt.get(y, 0) + w
    q_ex += Fraction(a_t, 3 ** t)
    p_ex += Fraction(b_t, 3 ** t)
    cur_cnt = nxt
    if t <= 14:  # closed forms implied by the ring picture
        if t % 2 == 0:
            assert a_t == 4 ** (t // 2 - 1) + 2 and b_t == 4 ** (t // 2) // 2 - 2
        else:
            assert a_t == 0 and b_t == 3 * 4 ** ((t - 1) // 2) // 2
leftover = Fraction(sum(cur_cnt.values()), 3 ** L)
assert q_ex < Fraction(9, 20) < q_ex + leftover
assert p_ex < Fraction(11, 20) < p_ex + leftover
print(f"[4] exact DP to t={L}: p in (11/20 - {float(leftover):.2e}, 11/20): OK")

# ----------------------------------------------------------------------------
# [5] Monte Carlo
# ----------------------------------------------------------------------------
N, hit_home = 500_000, 0
rng = random.Random(987654321)
for _ in range(N):
    cur = rng.choice(nbrs_ccw(o))
    while not home(cur):
        cur = rng.choice(nbrs_ccw(cur))
    hit_home += (cur == o)
q_mc = hit_home / N
print(f"[5] Monte Carlo N={N}: p ≈ {1 - q_mc:.4f} ± {2*math.sqrt(q_mc*(1-q_mc)/N):.4f}")

print("\nAnswer: p = 11/20 = 0.55")
