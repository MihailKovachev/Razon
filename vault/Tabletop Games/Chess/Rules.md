# Players

Chess is played by two players. The player with the white pieces is called White and the player with the black pieces is called Black.

# Moves

A **move** in chess consists of each player playing out their turn. On each turn, a player can either move one of their pieces (and potentially capture one of the enemy pieces in the process) or castle. 

On each move, it is always White's turn first and no player may skip their turn.

## Capturing

A player **captures** an enemy piece by moving one of their pieces to the square on which the enemy piece resides, the only exception being [en passant](Pieces.md#en%20passant). Once a piece is captured, it is removed from the board and cannot be played anymore.

A piece is said to be **under attack** if it is in such a position that it can be captured by an enemy piece.

## Castling

**Castling** is when a player moves their king and one of their rooks simultaneously in a specific way, usually in order to increase the safety of their king. It is possible only if said player has not moved their king or rook since the start of the game and the squares between the two pieces are free.

With the king-side rook, castling looks like this:

```shaahmaat
orientation: white
format: fen

rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQK2R w KQkq - 0 1
```

```shaahmaat
orientation: white
format: fen

rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQ1RK1 w Qkq - 0 1
```

With the queen-side rook, castling looks like this:

```shaahmaat
orientation: white
format: fen

rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/R3KBNR w KQkq - 0 1
```

```shaahmaat
orientation: white
format: fen

rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/2KR1BNR w Kkq - 0 1
```

Black castles analogously.

>[!NOTE]
>
>If the player has moved only one of their rooks but not their king, they are still allowed to castle with the unmoved rook.
>

# Check and Checkmate

We say that a player is in **check** if their king is under attack. In this case, the player in check *must* make a move which brings their king out of harm's way - any move which does not accomplish this is not allowed. Similarly, a player is *not* allowed to make a move which will put their own king in check. 

A player can escape from a check by either moving their king, capturing the attacking piece or blocking the check by breaking the line of sight between their king and the attacker with another piece.

>[!NOTE]- Note: Knight Checks
>
>If the king is being attacked by a knight, then the check cannot be blocked with another piece, since knights can jump over pieces. In such cases, the player must either move their king or capture the attacking knight.
>

>[!NOTE]- Note: Checks and Pins
>
>Consider the following position:
>
>```shaahmaat
>orientation: white
>format: fen
>
>2K5/8/1R2b1k1/8/8/8/8/8 w - - 0 1
>```
>
>Is White in check? Surprisingly, yes. Black's bishop is [pinned](Chess%20Theory/Tactics/Pin.md) - it cannot *actually* move to capture White's king, since then White's rook would be attacking Black's king and Black would be in check. Nevertheless, White's king is still considered to be in check and must try to escape it somehow.
>

If the player cannot do anything to bring their king out of check, then they have been **checkmated** and lose the game.

# Game Outcome

A player wins when they checkmate their opponent or their opponent surrenders. Conversely, a player loses if they get checkmated or surrender.

A chess game can also end in a draw in any one of the following ways:
- Stalemate - the player on turn is not in check but has no other valid moves.
- A player offers a draw on their turn and the opponent accepts.
- Draw by threefold repetition - the same position occurs three times in the same game. Two positions are considered the same if all of the following conditions are met: it is the same player's turn, pieces of the same kind and colour reside on the same squares, the possible moves of all pieces are the same (including en passant and castling). This draw is not automatic - it must be claimed by the player whose next intended move will result in the third repetition, if they want it. The player writes down their intended move, but does not actually play it, and then claims the draw. If they do not claim the draw, the game continues and they can no longer claim the draw for this position (unless the position appears another three times).
- Draw by fivefold repetition - the same position occurs fives times in the same game. What constitutes identical positions is governed by the same rules as those which dictate threefold repetition. However, this draw is automatic and needs not be claimed.
- Fifty-move rule - if in the previous 50 turns of each player no pawns have been moved and no captures have been made, either player can claim a draw. If the player on turn has made only 49 such moves, they claim the draw by writing down their move, but not actually playing it, and then claiming the draw.
- Seventy-five rule - if in the previous 75 turns of each player no pawns have been moved and no captures have been made, the game automatically ends in a draw.
- Impossible checkmate - if the position is such that checkmate is impossible for both players, the game is a draw. This may occur very late in the endgame.


