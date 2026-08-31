---
tags:
    - classical-mechanics
    - physics
---

# Newtonian Formalism

The **Newtonian formalism** of [classical mechanics](./Classical%20Mechanics.md) is a model of the *causes* behind movement. It is ubiquitously known and you have been taught it at school in one form or another using "Newton's laws of motion". Its popularity is due to several reasons:
- Historically, Newtonian formalism, described in Isaac Newton's *Principia Mathematica*, was the first such model to be rigorously defined and yielded predictions which agreed experimentally with observations.
- It is built on our direct observations of how solid objects move when we push or pull them and is therefore very intuitive.

Although the [Newtonian formalism](./Newtonian%20Formalism.md) is very intuitive and fairly simple, this does not make it the *only* true formalism. There are alternative ways to phrase [classical mechanics](./Classical%20Mechanics.md) which do not make any use of the notions that the [Newtonian formalism](./Newtonian%20Formalism.md) relies on. However, all of these are equivalent in the sense that they both yield the same predictions, agree equally well with experiments and can be mathematically derived from one another.

At the heart of the [Newtonian formalism](./Newtonian%20Formalism.md) lie the notions of an **inertial reference frames** and **forces**.

>[!DEFINITION] Definition: Inertial Motion
>
>An object is in **inertial motion** if it is *not* interacting with any other objects.
>

[Inertial motion](./Newtonian%20Formalism.md) is an idealization because for an object not to interact with anything else would require that the Universe be empty except for that single object. Nevertheless, we can still use this model as a very good approximation when an object interacts with other objects very weakly.

## Newton's First Law of Motion

>[!DEFINITION] Definition: Inertial Reference Frame
>
>A [reference frame](./Reference%20Frames.md) is **inertial** if a physical object under [inertial motion](./Newtonian%20Formalism.md) retains a constant [velocity](./Kinematics.md#Velocity).
>

We can think of an [inertial reference frame](./Newtonian%20Formalism.md) as the point of view of a ghost which interacts with nothing but is perfectly capable of perceiving the entirety of the Universe. No [reference frame](./Reference%20Frames.md) can be truly [inertial](./Newtonian%20Formalism.md) though because [inertial motion](./Newtonian%20Formalism.md) is an idealization. However, we can often approximate a [reference frame](./Reference%20Frames.md) as [inertial](./Newtonian%20Formalism.md) when the motion of objects closely approximating [inertial motion](./Newtonian%20Formalism.md) deviates very slightly from motion with constant [velocity](./Kinematics.md#Velocity). 

The definition of an [inertial reference frame](./Newtonian%20Formalism.md) is also known as **Newton's First Law of Motion** or the **Law of Inertia**. It states that, when viewed in an [inertial reference frame](./Newtonian%20Formalism.md), the [velocity](./Kinematics.md#Velocity) of objects which do not interact with other objects does not change. This manifests in one of two ways:
- If such an object has some non-zero [velocity](./Kinematics.md#Velocity) $\boldsymbol{v}$, then the [path](./Kinematics.md#Position) traced by it is a straight line and this line is traced with [speed](./Kinematics.md#Velocity) $||\boldsymbol{v}||$.
- If such an object has a zero [velocity](./Kinematics.md#Velocity), i.e. it is at rest, then it remains at rest.

To determine whether a given [reference frame](./Reference%20Frames.md) is [inertial](./Newtonian%20Formalism.md), we rely on empirical methods: If we have analyzed some object and have concluded that it interacts with no other objects but its [velocity](./Kinematics.md#Velocity) nevertheless changes, then we conclude that our [reference frame](./Reference%20Frames.md) is *not* [inertial](./Newtonian%20Formalism.md).

## Newton's Second Law of Motion

The interactions between objects are mediated by entities called **forces**.

>[!DEFINITION] Definition: Force
>
>A **force** is a [vector](../../Mathematics/Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md) which models a physical interaction.
>
>>[!NOTATION]
>>
>>[Forces](./Newtonian%20Formalism.md) are typically denoted using variations of the letter "F":
>>
>>$$
>>\mathbf{F} \qquad \boldsymbol{F} \qquad \vec{F}
>>$$
>>
>

One can think of forces as invisible arrows which push or pull stuff around. However, not much thought should be given as to whether forces "truly" exist in the philosophical sense because forces are just a model used by the [Newtonian formalism](./Newtonian%20Formalism.md) for calculating [kinematical quantities](./Kinematics.md). Other, equally correct formalisms, do not make use of forces. 

>[!AXIOM] Axiom: Newton's Second Law of Motion
>
>In an [inertial reference frame](./Newtonian%20Formalism.md), if $\boldsymbol{F}_1, \dotsc, \boldsymbol{F}_n$ are all the [forces](./Newtonian%20Formalism.md) acting on a [point mass](./Inertia.md#Point%20Masses) $m$, then its [instantaneous acceleration](./Kinematics.md#Acceleration) $\boldsymbol{a}$ is given by
>
>$$
>\boldsymbol{a} = \frac{1}{m} \sum_{i = 1}^n \boldsymbol{F}_i
>$$
>

This law tells us two very important things. First, [forces](./Newtonian%20Formalism.md) obey the superposition principle: the effect of $\boldsymbol{F}_1, \dotsc, \boldsymbol{F}_n$ is equivalent to the effect of a single net [force](./Newtonian%20Formalism.md) $\boldsymbol{F}_{\text{net}}$ which is the sum of $\boldsymbol{F}_1, \dotsc, \boldsymbol{F}_n$. Second, it makes apparent how [inertia](./Inertia.md) is the ability of an object to resist changes in its motion - the greater the [mass](./Inertia.md) $m$, the lesser the effect of the [forces](./Newtonian%20Formalism.md) $\boldsymbol{F}_1, \dotsc, \boldsymbol{F}_n$.

>[!IMPORTANT] Important: The Second Law in Non-Inertial Frames
>
>Consider a non-[inertial](./Newtonian%20Formalism.md) [reference frame](./Reference%20Frames.md) $\mathcal{R}_{\text{NI}}$ with [origin](./Reference%20Frames.md) $\mathcal{O}_{\text{NI}}$ and an [inertial reference frame](./Newtonian%20Formalism.md) $\mathcal{R}_{\text{I}}$ with [origin](./Reference%20Frames.md) $\mathcal{O}_{\text{I}}$.
>
>Since $\mathcal{R}_{\text{NI}}$ is not [inertial](./Newtonian%20Formalism.md), its [origin](./Reference%20Frames.md) $\mathcal{O}_{\text{NI}}$ must be subject to some [forces](./Newtonian%20Formalism.md) and by applying [Newton's second law](./Newtonian%20Formalism.md), we can determine the [acceleration](./Kinematics.md#Acceleration) ${}_{\mathcal{R}_{\text{I}}}\boldsymbol{a}_{\mathcal{O}_{\text{NI}}}$ of $\mathcal{O}_{\text{NI}}$ with respect to the [inertial reference frame](./Newtonian%20Formalism.md) $\mathcal{R}_{\text{I}}$. Similarly, if an object $O$ with [mass](../Mechanics/Inertia.md) $m$ is subject to [forces](./Newtonian%20Formalism.md) ${}_{\text{on } O}\boldsymbol{F}_1, \dotsc, {}_{\text{on } O}\boldsymbol{F}_n$, we can determine its [acceleration](./Kinematics.md#Acceleration) ${}_{\mathcal{R}_{\text{I}}}\boldsymbol{a}_{O}$ with respect to $\mathcal{R}_{\text{I}}$:
>
>$$
>{}_{\mathcal{R}_{\text{I}}}\boldsymbol{a}_{O} = \frac{1}{m} \sum_{i = 1}^n {}_{\text{on } O}\boldsymbol{F}_i
>$$
>
>Now we can use [Galilean relativity](./Galilean%20Transformations.md) to determine the [acceleration](./Kinematics.md#Acceleration) ${}_{\mathcal{R}_{\text{NI}}}\boldsymbol{a}_{O}$ of $O$ with respect to the non-[inertial](./Newtonian%20Formalism.md) [reference frame](./Reference%20Frames.md) $\mathcal{R}_{\text{NI}}$. Since $\mathcal{O}_{\text{NI}}$ has [acceleration](./Kinematics.md#Acceleration) ${}_{\mathcal{R}_{\text{I}}}\boldsymbol{a}_{\mathcal{O}_{\text{NI}}}$ with respect to $\mathcal{R}_{\text{I}}$, we know that the [acceleration](./Kinematics.md#Acceleration) of $\mathcal{O}_{\text{I}}$ with respect to $\mathcal{R}_{\text{NI}}$ is
>
>$$
>{}_{\mathcal{R}_{\text{NI}}}\boldsymbol{a}_{\mathcal{O}_{\text{I}}} = - {}_{\mathcal{R}_{\text{I}}}\boldsymbol{a}_{\mathcal{O}_{\text{NI}}}
>$$
>
>Using [Galilean relativity](./Galilean%20Transformations.md) again, we get that the [acceleration](./Kinematics.md#Acceleration) ${}_{\mathcal{R}_{\text{NI}}}\boldsymbol{a}_{O}$ of $O$ with respect to $\mathcal{R}_{\text{NI}}$ is
>
>$$
>\begin{aligned}
>{}_{\mathcal{R}_{\text{NI}}} \boldsymbol{a}_{O} &= {}_{\mathcal{R}_{\text{NI}}} \boldsymbol{a}_{\mathcal{O}_{\text{I}}} + {}_{\mathcal{R}_{\text{I}}}\boldsymbol{a}_{O} \\ &= {}_{\mathcal{R}_{\text{NI}}} \boldsymbol{a}_{\mathcal{O}_{\text{I}}} + \frac{1}{m}\sum_{i = 1}^n {}_{\text{on } O}\boldsymbol{F}_i
>\end{aligned}
>$$
>
>Therefore, in an non-[inertial](./Newtonian%20Formalism.md) [reference frame](./Reference%20Frames.md) objects appear to have additional [acceleration](./Kinematics.md#Acceleration) to the one predicted by [Newton's second law](./Newtonian%20Formalism.md). This [acceleration](./Kinematics.md#Acceleration) is *not* due to the [forces](./Newtonian%20Formalism.md) acting on the object itself, but rather due to the [forces](./Newtonian%20Formalism.md) acting on the [origin](./Reference%20Frames.md). However, we can still treat this [acceleration](./Kinematics.md#Acceleration) as if it were caused by [forces](./Newtonian%20Formalism.md) acting on the object by defining ${}_{\text{on } O} \boldsymbol{F}_{n+1} \overset{\text{def}}{=} m \cdot {}_{\mathcal{R}_{\text{NI}}} \boldsymbol{a}_{\mathcal{O}_{\text{I}}}$. Since $\frac{1}{m} {}_{\text{on } O} \boldsymbol{F}_{n+1} = {}_{\mathcal{R}_{\text{NI}}} \boldsymbol{a}_{\mathcal{O}_{\text{I}}}$, we can rewrite the previous equation as
>
>$$
>\begin{aligned}
>{}_{\mathcal{R}_{\text{NI}}} \boldsymbol{a}_{O} &= \frac{1}{m} {}_{\text{on } O} \boldsymbol{F}_{n+1} + \frac{1}{m}\sum_{i = 1}^n {}_{\text{on } O}\boldsymbol{F}_i \\ &= \frac{1}{m}\left({}_{\text{on } O} \boldsymbol{F}_{n+1} + \sum_{i=1}^n {}_{\text{on } O}\boldsymbol{F}_i \right) \\ &= \sum_{i = 1}^{n+1} {}_{\text{on } O}\boldsymbol{F}_i
>\end{aligned}
>$$
>
>The [vector](../../Mathematics/Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md) ${}_{\text{on } O} \boldsymbol{F}_{n+1}$ is not really a [force](./Newtonian%20Formalism.md) because it is not caused by the physical interactions of the object $O$, despite how we have abused the notation here. It is merely a [vector](../../Mathematics/Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md) we defined in order to be able to write the equation in a simpler form. As such, we often call ${}_{\text{on } O} \boldsymbol{F}_{n+1}$ a **fictitious force** or an **inertial force** and we usually write it as $\boldsymbol{F}_{\text{inertial}}$. Therefore, [Newton's second law](./Newtonian%20Formalism.md) in a non-[inertial](./Newtonian%20Formalism.md) [reference frame](./Reference%20Frames.md) is
>
>$$
>{}_{\mathcal{R}_{\text{NI}}} \boldsymbol{a}_{O} = \frac{1}{m}\left(\boldsymbol{F}_{\text{inertial}} + \sum_{i=1}^n {}_{\text{on } O}\boldsymbol{F}_i \right)
>$$
>

## Newton's Third Law of Motion

There is also one last law which tells us how interactions between objects happen.

>[!AXIOM] Axiom: Newton's Third Law of Motion
>
>Physical interactions between two [particles](./Classical%20Mechanics.md) $A$ and $B$ always manifest as a pair of [forces](./Newtonian%20Formalism.md): the [force](./Newtonian%20Formalism.md) $\boldsymbol{F}_{A\text{ on }B}$ which $A$ exerts on $B$ and and the [force](./Newtonian%20Formalism.md) $\boldsymbol{F}_{B\text{ on } A}$ which $B$ exerts on $A$. These [forces](./Newtonian%20Formalism.md) are equal in magnitude but opposite in direction:
>
>$$
>\boldsymbol{F}_{B\text{ on } A} = - \boldsymbol{F}_{A\text{ on } B}
>$$
>
>>[!WARNING] Warning: Inertial Forces
>>
>>This law does *not* apply to [inertial forces](./Newtonian%20Formalism.md) because they are not really [forces](./Newtonian%20Formalism.md).
>>
>

This phenomenon is quite easy to observe. When you push something, you feel it pushing you back in the opposite direction. Similarly, when you pull something, you feel it pulling back. Unfortunately, some people call this pair of [forces](./Newtonian%20Formalism.md) an "action" and a "reaction", implying that one [force](./Newtonian%20Formalism.md) precedes and causes the other. This stems largely from the way we are used to talking about things: *I* decided to push the box and so the box must be reacting to my decision. However, the reality is quite different. It is not *my decision* which caused the [force](./Newtonian%20Formalism.md) I exerted on the box which in turn caused the [force](./Newtonian%20Formalism.md)  which the box exerts on my hand, but rather the *physical interaction itself* causes both [forces](./Newtonian%20Formalism.md) simultaneously.
