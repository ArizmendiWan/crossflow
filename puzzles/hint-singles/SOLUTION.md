# Hint Singles — Jane Street puzzle, September 2026

**Answer: REMO** (R.E.M. + O — a drumhead brand).

## The puzzle

A photo of a record sleeve: *Jane Street Presents: 23 Hint Singles!* — "ALL
ORIGINAL RECORDINGS" — with 23 mangled song titles, a bonus track "from
??‌??" hidden under a $19.65 price sticker, and three corner stickers. The
caption: *"(The answer to this month's puzzle is a brand you've probably never
heard before…)"*

## The mechanic

Each track is a real song whose title has been altered. The alteration doesn't
clue the title — it clues the **artist's name with exactly one letter
inserted**. Weezer wheezes after a 5k; Bad Bunny goes *sin cabello*; Mariah
Carey unlocks a Nissan.

The sleeve teaches you this before you start. Every piece of packaging is the
same trick:

| Printed | Should read | Inserted |
|---|---|---|
| 23 **HIN**T SINGLES | 23 hit singles | N |
| AS SE**V**EN ON TV | as seen on TV | V |
| NOT SOL**I**D IN STORES | not sold in stores | I |
| STEREO **A**LP | stereo LP | A |

…and so does the caption itself: *a B**R**AND you've probably never heard
before* ← **a band**.

## The 23 tracks

| # | Sleeve title | Song | Artist → | + |
|---|---|---|---|---|
| 1 | Buddy Holly (After Running a 5k) | Buddy Holly | Weezer → W**h**eezer | H |
| 2 | A Little MISS Can't Be Wrong | Little Miss Can't Be Wrong | Spin Doctors → ? | E |
| 3 | Un Verano Sin Cabello | Un Verano Sin Ti | Bad Bunny → Ba**l**d Bunny | L |
| 4 | Party Off the Coast of Greece | Party in the U.S.A. | Miley Cyrus → Miley Cy**p**rus | P |
| 5 | Where the Cheddar Cheese Pretzel Things Are | Where the Wild Things Are | Luke Combs → Luke Comb**o**s | O |
| 6 | Elevated (Onto a Plinth) | Elevated | State Champs → Stat**u**e Champs | U |
| 7 | Hurt (In a Fender Bender) | Hurt | Johnny Cash → Johnny C**r**ash | R |
| 8 | Learn to (Throw a) Pie | Learn to Fly | Foo Fighters → Foo**d** Fighters | D |
| 9 | Only the Good Die on Planet Krypton | Only the Good Die Young | Billy Joel → Billy Jo**r**-El | R |
| 10 | What Can It Be (To Order For Our Lunch Meeting) Now? | Who Can It Be Now? | Men at Work → Men**u** at Work | U |
| 11 | Bonam Fortunam, Infantem! | Good Luck, Babe! | Chappell Roan → Chappell Ro**m**an | M |
| 12 | Mr. Trinitrotoluene Man | Mr. Tambourine Man | Bob Dylan → Bo**m**b Dylan | M |
| 13 | You Make Clubbing Fun | You Make Loving Fun | Fleetwood Mac → Fleetwood Mac**e** | E |
| 14 | Wake Me Up To Drive (This Boat I Stole) | ? | ? | R |
| 15 | Summertime Sandwich (Shop) | Summertime Sadness | Lana Del Rey → Lana Del**i** Rey | I |
| 16 | (Start To) Burn It Down | Burn It Down | Linkin Park → Linkin **S**park | S |
| 17 | I Like HIIT | I Like It | Cardi B → Cardi**o** B | O |
| 18 | Being Bobbing | Being Boring | Pet Shop Boys → Pet Shop B**u**oys | U |
| 19 | Watch That Man('s Choice Of Neckwear) | Watch That Man | David Bowie → David Bow **T**ie | T |
| 20 | All Cats Are Bad Luck | All Cats Are Grey | The Cure → The Cur**s**e | S |
| 21 | Didn't Cha Know (I'm Dual Listed in Hong Kong) | Didn't Cha Know | Erykah Badu → Erykah Ba**i**du | I |
| 22 | MMMBrel | MMMBop | Hanson → **C**hanson (Jacques Brel) | C |
| 23 | All I Want For Christmas Is You to Unlock My Nissan Sentra | All I Want for Christmas Is You | Mariah Carey → Mariah Car **K**ey | K |

Reading the inserted letters down the sleeve:

```
H E L P O U R D R U M M E R I S O U T S I C K

        HELP OUR DRUMMER IS OUT SICK
```

22 of the 23 were identified independently of the message, and all 22 agree
with it, which pins the last clue (#14 = R) even without cracking it.

## The answer

The album is a plea: the band's drummer is down. The band whose drummer went
down is the obvious one — **R.E.M.**, whose drummer Bill Berry collapsed
mid-show in Lausanne on 1 March 1995 with a ruptured brain aneurysm, ending
the European leg of the *Monster* tour. That's who the bonus track is "from",
hidden under the price sticker.

Now apply the album's own house style — every artist on this record gets one
letter inserted:

```
R.E.M.  +  O   →   REMO
```

**Remo** is the drumhead company founded by Remo Belli in 1957, whose Mylar
WeatherKing heads are on a large share of the drums ever recorded — and whose
name almost nobody outside drumming knows. Which is the caption's joke twice
over: it is *a brand you've probably never heard before*, and it's also *a
band you've certainly heard before*, plus a letter. The one thing a band with
no drummer needs, and the only major drum brand that is a famous band's name
with a single letter inserted.

## Loose ends

One clue I did not crack; its letter is fixed by the message:

- **#14 "Wake Me Up To Drive (This Boat I Stole)"** → artist + **R**.
  No artist with a "Wake Me Up" song (Avicii, Girls Aloud, Ed Sheeran, Aloe
  Blacc, Foals, Twice, Simple Plan, Billy Currington, Remy Ma, Speed, Taeyang,
  B.A.P, The Weeknd & Justice) takes an R insertion, nor does Wham!
  ("Wake Me Up Before You Go-Go") or Green Day ("…When September Ends"), so
  the base song is probably one I haven't identified.

Also unresolved: the joke in **#2 "A Little MISS Can't Be Wrong"**. The letter
is E and Spin Doctors → Spin**e** Doctors is the only sensible insertion, but
how "a little MISS" clues a spine specialist is still opaque to me.

`tracks.py` reproduces the extraction and checks it against the message.
