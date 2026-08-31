---
title: Bourne-Again Shell (bash)
tags:
    - linux
    - computer-science
---

# Introduction

The [Bourne-Again Shell (bash)](https://www.gnu.org/software/bash/) is the most common [[../Shells|shell]] found on [[./index|Linux]] systems.

![[res/Shell.png]]

# Scripting

## Quoting

Quoting is used to tell [[Bourne-Again Shell (bash)#Introduction|bash]] to ignore any special meaning which characters or words may have and to treat them literally. There are a few ways to do this and they have certain differences.

A backslash (`\`) tells [[Bourne-Again Shell (bash)#Introduction|bash]] to treat the next character literally, ignoring any special meaning it might have. The only exception is the newline character. A backslash before a new line tells [[Bourne-Again Shell (bash)#Introduction|bash]] to completely ignore the newline character.

>[!TIP]- Tip: Backslash + New Line
>
>You know that the end of each [[Bourne-Again Shell (bash)#Introduction|bash]] command is signified by a new line. However, it is often useful to display a given command on multiple lines. This can be done by typing `\` and then hitting enter for the newline character. This will create a visual new line but will be completely ignored when the actual command is run by [[Bourne-Again Shell (bash)#Introduction|bash]].
>

Surrounding text with single quotes (`'text'`) is used to treat all characters between the single quotes literally. However, `text` itself is not allowed to contain single quotes because any single quote would just match with the single quote before it and terminate the quotation. Not even a backslash can be used to achieve this because a backslash between single quotes is treated literally just like any other character.

Double quotes (`"text"`) are used to treat all characters in `text` literally except for `$`, `\`, `` ` `` and `!`.