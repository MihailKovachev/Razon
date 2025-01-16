# Pieces

Traditionally, there are chess is played with six types of pieces - rooks, knights, bishops, kings, queens and pawns. However, some variants add additional pieces with special moves.

# Pawns

Pawns always move forward. If a pawn has not been moved since the start of the game, then it can move either one or two squares forward.

```shaahmaat
format: fen
orientation: white
arrows: d2->d3 d2->d4

rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1
```

After its initial move, a pawn can only move forward, one square at a time.

```shaahmaat
format: fen
orientation: white
arrows: d3->d4

rnbqkbnr/pppppppp/8/8/8/3P4/PPP1PPPP/RNBQKBNR w KQkq - 0 1
```

A pawn can capture a piece if the piece is directly in front and either to the left or right of it.

```shaahmaat
format: fen
orientation: black
arrows: d4->c3 d4->e3

rnbqkb1r/ppp2ppp/5n2/4p3/3pP3/2NPB3/PPP2PPP/R2QKBNR w KQkq - 0
```

When capturing, the pawn moves on to the square of the enemy's piece, thus moving one square to the side and one square forward at the same time.

## En Passant

There is also a special way in which a pawn can sometimes capture another pawn called **en passant** (from French "in passing"). If an enemy pawn just moved two squares forward during it initial move and landed on a square adjacent to your pawn, you can capture it. In this case, your pawn moves to the square which the enemy pawn skipped in exactly the same way as during a normal pawn capture.

```shaahmaat
format: fen
orientation: white
highlights: d7 d5
arrows: e5->d6

rnbqkbnr/ppp1pppp/8/3pP3/8/8/PPPP1PPP/RNBQKBNR w KQkq - 0 1
```

>[!WARNING]
>
>En passant is not possible unless done immediately after the enemy pawn moves.
>

## Promotion

If you manage to get your pawn to the final rank of the enemy's half of the board, you must promote it to another piece. This means that you replace your pawn with a brand new piece which can be either a queen, rook, bishop or knight.

>[!DEFINITION] Definition: Underpromotion
>
>Promoting a pawn to a piece other than a queen is known as **underpromotion**.


Promotion happens on the same turn as the pawn move.

# Rooks

A rook can move an arbitrary number of squares either vertically or horizontally, so long as its path is not obstructed by another piece. If an enemy piece is on the square to which the rook moves, then the piece gets captured.

```shaahmaat
orientation: white
format: fen
highlights: d1 d2 d3 d5 d6 d7 d8 a4 b4 c4 e4 f4 g4 h4

8/8/8/8/3R4/8/8/8 w - - 0 1
```

# Knights

Knights are quite versatile due to their unique ability to skip over other pieces. A knight moves two squares in either the vertical or horizontal direction and then one square either left or right, essentially following an "L" pattern.

```shaahmaat
orientation: white
format: fen
highlights: b3 b5 c2 c6 e2 e6 f3 f5

8/8/8/8/3N4/8/8/8 w - - 0 1
```

If there is an enemy piece on the square to which the knight moves, then the piece gets captured.

# Bishops

Each player has two bishops - a dark-squared and a light-squared one. Each bishop can move an arbitrary number of squares diagonally, so long as its path is not obstructed by another piece. If an enemy piece is on the square to which the bishop moves, then the piece gets captured.

```shaahmaat
orientation: white
format: fen
highlights: a1 b2 c3 e5 f6 g7 h8 a7 b6 c5 e3 f2 g1

8/8/8/8/3B4/8/8/8 w - - 0 1
```

# Queen

The queen moves either as a bishop or a rook.

```shaahmaat
orientation: white
format: fen
highlights: a1 b2 c3 e5 f6 g7 h8 a7 b6 c5 e3 f2 g1 d1 d2 d3 d5 d6 d7 d8 a4 b4 c4 e4 f4 g4 h4

8/8/8/8/3Q4/8/8/8 w - - 0 1
```

# King

The king moves like a queen but only one square at a time, except when [castling](Rules.md#castling).

```shaahmaat
orientation: white
format: fen
highlights: c3 e5 c5 e3 d3 d5 c4 e4

8/8/8/8/3K4/8/8/8 w - - 0 1
```