# Board Setup

Chess is played on an 8 by 8 board of squares with alternating dark and light colours. The board has to be oriented such that the bottom left square from the perspective of each player is dark.

>[!DEFINITION] Definition: Rank
>
>Each row of the chessboard is known as a **rank**.
>

>[!DEFINITION] Definition: File
>
>Each column of the chessboard is known as a **file**.
>

After this, the pieces are placed as follows:
- Each player places their two rooks at the bottom corners of their half of the board.
- Next to the rooks, on the same rank, they place their knights.
- Next to the knights, on the same rank, they place their bishops.
- Each player places their king next to one of their bishops and on the same rank such that each king is on a square opposite its colour - the white king should be on a black square, and the black king should be on a white square.
- The queens are placed next to their kings, again on the same rank.
- Finally, a single pawn is placed directly in front of each piece.

If done correctly, the board should look like this:
- from White's perspective

```shaahmaat
format: fen
orientation: white

rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1
```

- from Black's perspective

```shaahmaat
format: fen
orientation: black

rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1
```


