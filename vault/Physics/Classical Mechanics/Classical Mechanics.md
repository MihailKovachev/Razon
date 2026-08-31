---
tags:
    - classical-mechanics
    - physics
---

# Classical Mechanics

**Classical mechanics** is the branch of [physics](../Physics.md) that aims to model and describe the motion and interactions of everyday objects. 

## Space and Time

Space is modelled as an [infinitely large](../../Mathematics/Set%20Theory/Cardinality.md#Infinite%20Sets) [set](../../Mathematics/Set%20Theory/Sets.md) of points which is [homeomorphic](../../Mathematics/Analysis/Continuity/Homeomorphism.md) to the [Euclidean space](../../Mathematics/Analysis/Real%20Analysis/Euclidean%20Space/Euclidean%20Space.md) $\mathbb{R}^3$. This description seems rather complex but it basically means that space has the following properties:
- It is possible to assign a 3-dimensional [real vector](../../Mathematics/Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md) to each point in space such that no two points are assigned the same [real vector](../../Mathematics/Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md).
- Distances between points behave "normally".

Time is modelled as an [infinitely large](../../Mathematics/Set%20Theory/Cardinality.md#Infinite%20Sets) [set](../../Mathematics/Set%20Theory/Sets.md) of moments which is [homeomorphic](../../Mathematics/Analysis/Continuity/Homeomorphism.md) to the [real number line](../../Mathematics/Analysis/Real%20Analysis/Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line). This essentially means that time has two properties:
- It is possible to identify each moment with a [real number](../../Mathematics/Algebra/Fields/The%20Real%20Numbers/The%20Real%20Numbers.md) such that no two moments are assigned the same number.
- Durations between moments behave "normally".

Objects are then said two exist within a specific region in space and at a specific moment in time.

>[!NOTE] Note: The meaning of "normally"
>
>At this point, it is very difficult to provide a definition for what is "normal" in the above context because it is unlikely that you have encountered anything other than the "normal" behaviour of distances and durations. The best one can do is to probably provide a hand-wavy example of what "abnormal" would be: In Einstein's theories of relativity, the two separate models of space and time are unified into a single 4-dimensional model in which distances and durations behave very differently from the way you would expect. For example, two people can drastically disagree about the distance between two points or the duration between two moments. They might even disagree about the order in which a sequence of events occur. Paradoxically, however, none would be more or less correct than the other.
>

## Point Particles

In the framework of [classical mechanics](./Classical%20Mechanics.md), at any given [moment](./Classical%20Mechanics.md), physical objects occupy a region of [space](./Classical%20Mechanics.md). It turns out, however, that describing objects with volume is a very difficult task. This is why we often resort to modelling objects as infinitesimally small point particles, with no size.

>[!DEFINITION] Definition: Point Particle
>
>A **point particle** is a model of a physical object as an infinitesimally small point without any size.
>

Obviously, this is a very rough approximation. After all, both you, the car you drive, the Earth and so on are certainly *not* infinitesimally small and certainly occupy *some* volume. Nevertheless, this approximation is very accurate in many cases because, when viewed from a sufficiently great distance, objects behave more or less like point particles. Similarly, if the sizes of the objects are much smaller than the distances between them, objects can also be modelled by point particles quite well. Whenever this accuracy is not sufficient, we resort to modelling objects as collections of a very large number of point particles, which is not far from the truth given that all matter is made up of tiny atoms and molecules.

### Physical Systems

>[!DEFINITION] Definition: Physical System
>
>A **physical system** is a [set](../../Mathematics/Set%20Theory/Sets.md) of physical objects which we have chosen to [model](./Classical%20Mechanics.md) because we are interested in them.
>

>[!DEFINITION] Definition: Isolated Physical System
>
>A [physical system](./Classical%20Mechanics.md) is **isolated** if its objects do not interact with any objects outside it.
>