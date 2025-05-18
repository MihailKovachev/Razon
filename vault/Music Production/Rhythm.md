---
title: Rhythm
tags:
    - music-production
---

# Rhythm

**Rhythm** is the temporal structure of music. It describes when and for how long [sounds](Sound.md) are to be played during the course of a given musical piece.

# Beats

To indicate when and for how long notes should be played, we need a way of measuring time. In music, this is not done using seconds or minutes because these are actually rather unnatural and not particularly suitable for describing how music progresses through time. Instead, we use **beats**. 

>[!DEFINITION] Definition: Beat
>
>The **beat** is the fundamental unit for measuring time in a given piece of music.
>

Instead of saying that a note should be played starting at second $3.0$ since the beginning of the piece and that it should last $1.5$ seconds, we say that the note should begin playing on beat $9.0$ of the piece and should last $4.5$ beats.

The duration of a note is known as the **note value**. 

>[!NOTATION] Notation: Note Value
>
>Different symbols are used to denote different durations. In a similar manner, we also use to denote silence, i.e. the absence of notes, using different symbols.
>
>These durations, however, are not absolute - they are defined relative to each other. In the following table, each note is half of the duration of the note / rest above it and twice the duration of the note / rest below it. The relative duration is given in terms of the duration of the whole note / rest.
>
>|Note|Rest|Relative Duration|American Name|British Name|
>|:--:|:--:|:--:|:--:|:--:|
>|||$8$|large note, duplex longa, maxima|large, duplex longa, maxima|
>|||$4$|long note, longa|long note, longa|
>|||$2$|double whole note, double note|breve|
>|||$1$|whole note|semibreve|
>|||$\displaystyle \frac{1}{2}$|half note|minim|
>|||$\displaystyle \frac{1}{4}$|quarter note|crotchet, semiminim|
>|||$\displaystyle \frac{1}{8}$|eighth note|quaver|
>|||$\displaystyle \frac{1}{16}$|sixteenth note|semiquaver|
>|||$\displaystyle \frac{1}{32}$|thirty-second note|demisemiquaver|
>|||$\displaystyle \frac{1}{64}$|sixty-fourth note|hemidemisemiquaver|
>|||$\displaystyle \frac{1}{128}$|hundred twenty-eighth note|semihemidemisemiquaver|
>|||$\displaystyle \frac{1}{256}$|two hundred fifty-sixth note|demisemihemidemisemiquaver|
>
>In practice, you will probably never encounter durations shorter than $\frac{1}{64}$ or longer than $4$.
>



Since beats are just measurement units for time, they can be converted into seconds and vice versa. However, the question of how many beats correspond to one second (or, equivalently, how many seconds correspond to one beat) is rather complicated and its answer depends on the [tempo](Rhythm.md#Tempo) of the music being played.

>[!NOTATION] Notation: Dot Extensions
>
>More irregular note durations can be achieved via the addition of dots to the right of the note symbol. The $n$-th dot from left to right shows that the duration of the note should be extended by $\frac{1}{2^n}$ of the duration indicated by the note symbol. The first dot corresponds to an extension of $\frac{1}{2}$ of the original duration, the second dot corresponds to an additional extension of $\frac{1}{4}$ of the original duration, the third corresponds to an additional extension of $\frac{1}{8}$ of the original duration and so on.
>

## Tempo

Some pieces naturally sound faster than others because they contain a greater number of notes in a given time interval.

>[!DEFINITION] Definition: Tempo
>
>The **tempo** of a piece of music refers to how fast or slow the music is perceived to be.
>

Since time in music is measured in [beats](Rhythm.md#Beats), a faster tempo means that more notes are played during a given number of beats and a slower tempo means that fewer notes are played during the same number of beats.

However, If we defined one beat to be strictly equal to one second or half a second or whatever, then we could end up in situations where we have notes lasting $\frac{1}{100}$ of a beat or $100$ beats depending on how many notes per second are contained in the music. This would completely defeat the purpose of using [beats](Rhythm.md#Beats) because we are not used to counting in multiples of $\frac{1}{100}$ nor are we used to counting up to $100$ in a short time span.

The solution to this is to allow the duration of one beat to vary. Instead of strictly defining one beat to always be equal to one second or half a second or whatever, for each piece of music we specify a conversion rate which tells us how many beats correspond to one second (or, equivalently, how many seconds correspond to one beat) in the context of the piece. Since the choice of this conversion rate is arbitrary, we can pick a conversion rate which results in "nice" numbers that are easy for us to handle.

### Beats per Minute (BPM)

Most commonly, this conversion rate is given in **beats per minute (bpm)**.

>[!DEFINITION] Definition: Beats per Minute (BPM)
>
>The **beats per minute (bpm)** of a piece of music is a number which specifies how many [beats](Rhythm.md#Beats) are contained in one minute of the music.
>

For example, a bpm of 180 means that 180 beats correspond to one minute, which amounts to 3 beats every second, since there are 60 seconds in a minute.

>[!NOTATION] Notation: Beats per Minute (BPM)
>
>In sheet music, it is quite common to combine the assignment of the beat to a given note duration with the bpm of the piece in the following way:
>
>![](res/BPM%20Basic%20Notation.png)
>
>The above notation shows us that the duration of one beat is assigned to the [quarter note](Rhythm.md#Beats) and that the bpm is 120.
>
>Although much more uncommon, we could also assign the duration of one beat to the [half note](Rhythm.md#Beats) or the [eighth note](Rhythm.md#Beats), etc., using the same notation, but changing the note symbol.
>
>![](res/Alternative%20BPM%20Notation.png)
>

>[!NOTATION] Notation: Historical Tempo Markings
>
>Specifying the [tempo](Rhythm.md#Tempo) of a piece of music by its [bpm](Rhythm.md#Beats%20Per%20Minute(BPM)) is a relatively new practice. Historically, tempo was only approximate and was specified using one or two Italian words. These words and the approximate [bpm](Rhythm.md#Beats%20Per%20Minute(BPM)) ranges which they correspond to are given in the table below.
>
>|Tempo Marking|BPM Range|Explanation|
>|:--:|:--:|:--:|
>|Larghissimo|under 24|Extremely slow, close to the point at which our ears stop perceiving individual [beats](Rhythm.md#Beats) as a part of a rhythmic whole.|
>
>