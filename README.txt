About

This is not a game, but a solver for a puzzle from the real world.
The puzzle has nine square cards with art of birds of prey.
Either side of each edge between cards has half a bird.
The goal is to put the cards into a 3x3 grid so that each
edge shows a complete bird (or matching edge).

The approach in the solver:
find a list of matching 3-in-a-row arrangements (permutate and rotate).
Then find a list of two rows of 3 that fit together.
Finally find a list of possible three rows of 3 that fit together.

I make no attempt to avoid duplication by removing symmetries, so there
are several solutions, though they are all equivalent under rotation.
