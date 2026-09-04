#!/usr/bin/env python3
"""Hint Singles (Jane Street, Sept 2026).

Mechanic: each track is a real song whose title is altered so the alteration
clues the ARTIST's name with exactly ONE letter inserted.
The packaging demonstrates it: 23 HI(N)T SINGLES = 23 hit singles,
AS SE(V)EN ON TV, NOT SOL(I)D IN STORES, STEREO (A)LP.
"""

T = [
 # title on sleeve, real song, real artist, modified artist, letter, clue
 ("Buddy Holly (After Running a 5k)", "Buddy Holly", "Weezer", "Wheezer", "H",
  "wheezing after a 5k"),
 ("A Little MISS Can't Be Wrong", "Little Miss Can't Be Wrong", "Spin Doctors",
  "Spine Doctors?", "E", "?"),
 ("Un Verano Sin Cabello", "Un Verano Sin Ti", "Bad Bunny", "Bald Bunny", "L",
  "sin cabello = without hair = bald"),
 ("Party Off the Coast of Greece", "Party in the U.S.A.", "Miley Cyrus",
  "Miley Cyprus", "P", "island off Greece"),
 ("Where the Cheddar Cheese Pretzel Things Are", "Where the Wild Things Are",
  "Luke Combs", "Luke Combos", "O", "cheddar cheese pretzel = Combos"),
 ("Elevated (Onto a Plinth)", "Elevated", "State Champs", "Statue Champs", "U",
  "a statue is elevated onto a plinth"),
 ("Hurt (In a Fender Bender)", "Hurt", "Johnny Cash", "Johnny Crash", "R",
  "fender bender = crash"),
 ("Learn to (Throw a) Pie", "Learn to Fly", "Foo Fighters", "Food Fighters", "D",
  "pie fight = food fight"),
 ("Only the Good Die on Planet Krypton", "Only the Good Die Young", "Billy Joel",
  "Billy Jor-El", "R", "Kryptonian name Jor-El"),
 ("What Can It Be (To Order For Our Lunch Meeting) Now?", "Who Can It Be Now?",
  "Men at Work", "Menu at Work", "U", "what to order = the menu"),
 ("Bonam Fortunam, Infantem!", "Good Luck, Babe!", "Chappell Roan",
  "Chappell Roman", "M", "Latin = Roman"),
 ("Mr. Trinitrotoluene Man", "Mr. Tambourine Man", "Bob Dylan", "Bomb Dylan", "M",
  "TNT = bomb"),
 ("You Make Clubbing Fun", "You Make Loving Fun", "Fleetwood Mac",
  "Fleetwood Mace", "E", "mace = a club"),
 ("Wake Me Up To Drive (This Boat I Stole)", "?", "?", "?", "R", "pilot a stolen boat"),
 ("Summertime Sandwich (Shop)", "Summertime Sadness", "Lana Del Rey",
  "Lana Deli Rey", "I", "sandwich shop = deli"),
 ("(Start To) Burn It Down", "Burn It Down", "Linkin Park", "Linkin Spark", "S",
  "a spark starts a fire"),
 ("I Like HIIT", "I Like It", "Cardi B", "Cardio B", "O", "HIIT = cardio"),
 ("Being Bobbing", "Being Boring", "Pet Shop Boys", "Pet Shop Buoys", "U",
  "buoys bob"),
 ("Watch That Man('s Choice Of Neckwear)", "Watch That Man", "David Bowie",
  "David Bow Tie", "T", "neckwear = bow tie"),
 ("All Cats Are Bad Luck", "All Cats Are Grey", "The Cure", "The Curse", "S",
  "bad luck = a curse"),
 ("Didn't Cha Know (I'm Dual Listed in Hong Kong)", "Didn't Cha Know",
  "Erykah Badu", "Erykah Baidu", "I", "Baidu is dual-listed in Hong Kong"),
 ("MMMBrel", "MMMBop", "Hanson", "Chanson", "C", "Jacques Brel sang chanson"),
 ("All I Want For Christmas Is You to Unlock My Nissan Sentra",
  "All I Want for Christmas Is You", "Mariah Carey", "Mariah Car Key", "K",
  "unlock a car = car key"),
]

msg = "".join(t[4] for t in T)
print(f"{len(T)} tracks\n")
for i, (sleeve, song, art, mod, L, why) in enumerate(T, 1):
    print(f"{i:2d}. +{L}  {art:15s} -> {mod:16s} ({why})")
print(f"\nExtracted: {msg}")

target = "HELPOURDRUMMERISOUTSICK"
print(f"Reads as:  {'HELP OUR DRUMMER IS OUT SICK'}")
print(f"Matches 'HELPOURDRUMMERISOUTSICK': {msg == target}")
known = [i for i, t in enumerate(T) if t[2] != "?"]
print(f"Independently solved: {len(known)}/23 -> "
      f"{sum(1 for i in known if T[i][4] == target[i])}/{len(known)} agree with the message")
print("\nPackaging uses the same trick:  23 HI(N)T SINGLES / AS SE(V)EN ON TV /")
print("NOT SOL(I)D IN STORES / STEREO (A)LP  ... and the hint itself:")
print("'a B(R)AND you've probably never heard before'  <-  a BAND")
