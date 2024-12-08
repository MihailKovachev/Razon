>[!DEFINITION] Definition: Isohoric Process
>
>An **isohoric process** is a process in which the volume of the [gas](../Kinetic-Molecular%20Model%20of%20an%20Ideal%20Gas.md) does not change.
>

>[!THEOREM] Theorem: Work in an Isohoric Process
>
>An [ideal gas](../Kinetic-Molecular%20Model%20of%20an%20Ideal%20Gas.md) does no [work](../../../Mechanics/Classical%20Mechanics/Newtonian%20Formalism/Energy/Work.md) in an [isohoric process](Ideal%20Gases%20in%20Isohoric%20Processes.md).
>
>$$
>W = 0
>$$
>
>>[!PROOF]-
>>
>>According to [this theorem](../Work%20of%20an%20Ideal%20Gas.md)
>>
>>$$
>>W = \int_V^V p\mathop{\mathrm{d}V} = 0
>>$$
>>
>

>[!THEOREM] Theorem: Molar Heat Capacity in an Isohoric Process
>
>The [molar heat capacity](../../Temperature%20and%20Heat/Molar%20Heat%20Capacity.md) of an [ideal gas](../Kinetic-Molecular%20Model%20of%20an%20Ideal%20Gas.md) in an [isohoric process](Ideal%20Gases%20in%20Isohoric%20Processes.md) is denoted by $C_V$ and is
>
>$$
>C_V = \frac{f}{2}R
>$$
>
>where $f$ is the number of [degrees of freedom of a single gas particle](../Degrees%20of%20Freedom%20of%20Gas%20Particles.md) and $R$ is the [molar gas constant](../Molar%20Gas%20Constant.md).
>
>>[!PROOF]-
>>
>>The [internal energy](../../Internal%20Energy.md) of the gas is
>>
>>$$
>>U = \frac{f}{2}n R T
>>$$
>>
>>Since the gas does no work in an isohoric process, the [first law of thermodynamics](../../The%20First%20Law%20of%20Thermodynamics.md) tells us that the change in the internal energy depends only on the [heat](../../Heat.md) which enters / exits the gas.
>>
>>$$
>>\mathrm{d}U = \mathrm{d}Q
>>$$
>>
>>From this follows
>>
>>$$
>>\mathrm{d}Q = \frac{f}{2}n R \mathop{\mathrm{d}T} \implies \frac{\mathrm{d}Q}{\mathrm{d}T} = \frac{f}{2}n R
>>$$
>>
>>The left-hand side is just the gas's [heat capacity](../../Temperature%20and%20Heat/Heat%20Capacity.md) $C$.
>>
>>$$
>>C = \frac{\mathrm{d}Q}{\mathrm{d}T} = \frac{f}{2}n R
>>$$
>>
>> To obtain the *molar* heat capacity, we need to divide $C$ by the number of moles $n$.
>>
>>$$
>>C_V = \frac{C}{n} = \frac{f}{2}R
>>$$
>>
>