# Andy's Afternoon Amble — Jane Street puzzle, August 2026

**Answer: p = 11/20 = 0.55, exactly.**

## The puzzle

(Reconstructed from the puzzle page; the sequel to *Andy's Morning Stroll*, July 2022.)

Andy the ant lives on a sphere shaped like a **truncated tetrahedron**: 4 white
hexagons and 4 black triangles, each white hexagon surrounded by alternating
black triangles and white hexagons (three of each), each black triangle
surrounded by three white hexagons. Every afternoon he takes an **amble** from
his home hexagon: each step he moves to one of the three neighboring white
hexagons uniformly at random, and the amble ends as soon as he first returns
home. He remembers the **turns** he takes (each step after the first is a
left turn, a right turn, or going back the way he came). For instance, exactly
1/3 of his ambles are 2 steps long.

One afternoon he unknowingly wakes up on the infinite **football-pitch
tiling** — white hexagons where every white hexagon is surrounded by
alternating black and white hexagons, and every black hexagon by six white
ones — which is locally indistinguishable from home (three white neighbors per
white hexagon, alternating around it). He takes his usual amble. **What is the
probability p that, by the end of his amble, he has discovered that he is no
longer on the truncated tetrahedral sphere?**

## Solution

### 1. Setting

Andy's observations are: the sequence of turns (Back / Left / Right), plus
whether the hexagon he currently stands on is his home. Model each surface by
its white-hexagon adjacency graph *as an oriented map* (graph + clockwise
order of the three white-neighbor exits around each hexagon):

* **Truncated tetrahedron:** the four hexagons are pairwise adjacent — the
  complete graph K4, drawn on a sphere. The faces of this map are the four
  black triangles: turning consistently left (or right) brings you home in
  **3** steps.
* **Pitch:** the white cells form a honeycomb (graphene) lattice. The faces
  are the rings around black hexagons: consistent turning closes in **6**
  steps.

Given the turn sequence, the trajectory on either surface is completely
determined. On the pitch each step goes to a uniformly random neighbor, so the
turns are i.i.d. uniform on {B, L, R}.

### 2. A branched covering: the four-coloring

Write the pitch's white cells in graphene coordinates: A-cells `A(m,n)` at
`m·a + n·b` (with `a = (1,0)`, `b = (1/2, √3/2)`) and B-cells `B(m,n)` above
them, adjacency

```
A(m,n) ~ B(m,n), B(m,n−1), B(m+1,n−1)        (counterclockwise)
B(m,n) ~ A(m,n+1), A(m−1,n+1), A(m,n)        (counterclockwise)
```

Color the cells with the Klein four-group `V = Z2 × Z2 = {0, e1, e2, e1+e2}`:

```
c(A(m,n)) = (m mod 2)·e1 + (n mod 2)·e2
c(B(m,n)) = ((m+1) mod 2)·e1 + (n mod 2)·e2
```

and identify `V` with the tetrahedron's four hexagons, `0` = Andy's home.
Two finitely-checkable local facts (verified in `verify.py`):

1. **Proper:** the three neighbors of every cell carry exactly the three
   other colors.
2. **Rotation-equivariant:** around a cell of color `v`, the neighbor colors
   in counterclockwise order are `(v+e1, v+e1+e2, v+e2)` — and this same
   cyclic rule is a valid spherical rotation system for K4 (its face-tracing
   orbits are the four triangles). So the cyclic order of colors around any
   pitch cell matches the cyclic order of hexagons around the corresponding
   tetrahedron hexagon.

By induction on steps, for *every* turn sequence: **the color of Andy's pitch
cell at time t equals his position on the truncated tetrahedron at time t**
(started correspondingly). Geometrically the coloring realizes a branched
covering pitch → truncated tetrahedron: each black hexagon of the pitch wraps
twice around a black triangle of the sphere. Andy never stands on black cells,
so he cannot feel the branch points.

### 3. Discovery = reaching a false home

Call the color-0 cells **home-colored**; they sit at
`{A(2i, 2j)} ∪ {B(2i+1, 2j)}` — a honeycomb pattern at twice the scale.
By step 2, *"my turn record says I should be home right now"* is equivalent to
*"I am standing on a home-colored cell."*

Let S = the first time ≥ 1 Andy stands on a home-colored cell, and T = the
first time he actually returns home (the amble's end). The origin is
home-colored, so S ≤ T.

* Before S, the model predicts "not home" and he indeed isn't home:
  consistent, nothing to discover.
* If the cell at time S is his real home, model and reality agree, the amble
  ends there (T = S), and his entire record was consistent with the
  tetrahedron: he never discovers.
* If it is a **false home** — home-colored but not home — the model says he
  should be home and he plainly isn't: at that instant (and forever after)
  his record is inconsistent with the tetrahedron, so he has discovered.
  (Equivalently: at the amble's actual end T his turn word is not a
  first-return word on the tetrahedron. The two readings define the same
  event.)

So **p = P(the first home-colored cell the walk reaches is not the origin).**
The smallest example: after his first step, two lefts. On the tetrahedron
that circles a black triangle and lands home in 3 steps; on the pitch he is
only halfway around a black hexagon, standing on the false home `B(1,0)`.

### 4. The rings

Because the coloring is proper, **every non-home-colored cell has exactly one
home-colored neighbor**. Hence the non-home-colored cells span a 2-regular
graph — a disjoint union of cycles. Tracing the one through `B(0,0)`:

```
B(0,0) → A(0,1) → B(0,1) → A(−1,2) → B(−1,1) → A(−1,1) → B(0,0)
```

a 6-ring (it circles a black hexagon) that hits each of the six
non-home-colored residue classes mod 2Λ exactly once — so *every* component
is one of its lattice translates. The plane decomposes into disjoint hexagonal
6-rings, each ring cell wired to its own **distinct** home-colored absorber.

Andy's first step puts him on the ring cell adjacent to his home, and from
then on each step is: with probability 1/3, step onto the current cell's
absorber (ending the question — true home means "consistent amble over",
false home means "discovered"); with probability 1/3 each, move to a ring
neighbor. Of the ring's six absorbers, only his entry cell's absorber is the
true home.

### 5. Absorption on a hexagon

Let v_j = P(eventually absorbed at the entry cell's absorber | currently at
ring position j), entry at 0. By symmetry v₅ = v₁, v₄ = v₂:

```
v0 = 1/3 + (2/3)·v1
v1 = (v0 + v2)/3
v2 = (v1 + v3)/3
v3 = (2/3)·v2
```

Solving: v₃ = (2/3)v₂ ⇒ v₂ = (3/7)v₁ ⇒ v₁ = (7/18)v₀ ⇒
v₀ = 1/3 + (7/27)v₀ ⇒ **v₀ = 9/20**.

So the amble stays consistent with probability q = 9/20, and

**p = 1 − 9/20 = 11/20 = 0.55.**

## Consistency checks (all in `verify.py`, plus `bloch.py`)

* P(amble is 2 steps) = 1/3 — matches the statement.
* E[S] = 1 + 3 = 4 (absorption rate 1/3 on the ring) = expected return time
  of the walk on K4 = number of hexagons. ✓
* The ring picture predicts the number of home-color-avoiding t-step walks:
  back home a_{2k} = 4^{k−1} + 2, to false homes b_{2k} = 4^k/2 − 2 and
  b_{2k+1} = (3/2)·4^k, whose sums Σ a_t/3^t = 9/20 and Σ b_t/3^t = 11/20.
  An exact-rational lattice DP reproduces these counts and brackets
  p within (11/20 − 10⁻²¹, 11/20) by t = 120 (10⁻³⁵ by t = 200).
* Monte Carlo (2·10⁶ episodes): p ≈ 0.5502 ± 0.0004. ✓
* An independent Bloch–Fourier computation of the Green function of the walk
  killed on the home-colored set gives q = 0.45 to 30 digits. ✓

## Postscript

The morning stroll's soccer ball became an afternoon truncated tetrahedron,
and the "20" survives: on the ball, Andy's expected stroll was 20 steps; on
the tetrahedral sphere his ambles can no longer be confused with the pitch
with probability exactly 11/20.
