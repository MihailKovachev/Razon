# What is a Pin

The **pin** is a chess [tactic](index.md) in which a player restricts the movement of an enemy piece by making such movement disadvantageous to the enemy. The name "pin" stems from the fact that the piece is usually "pinned" to its square and cannot move.

## Absolute Pins

An **absolute pin** is the most powerful type of pin and leverages the fact no player is allowed to put their own king in check. Whenever a piece is protecting its king from an enemy piece, it becomes pinned and cannot move because then the king would be in check.

```shaahmaat
orientation: black
format: fen

8/6k1/8/4r3/8/2B5/8/3K4 w - - 0 1
```

Here, Black's rook is pinned and cannot move from its square because, if it did, the black king would be in check.

## Relative Pins

A **relative pin** is a weaker form of pin which works similarly to the absolute pin. The difference lies in the fact that the movement of a piece is restricted not because it would result in a check but because it open an attack on a piece of higher value.

```shaahmaat
orientation: white
format: fen

8/6qk/8/4N3/8/2Q5/4K3/8 w - - 0 1
```

Here, White's knight is pinned - if it moves, then Black's queen would take White's queen.

 # Breaking Pins

The two main ways of breaking a pin are by either capturing the offending piece or moving the high-value piece so that it will no longer be under attack if the pinned piece moves.

