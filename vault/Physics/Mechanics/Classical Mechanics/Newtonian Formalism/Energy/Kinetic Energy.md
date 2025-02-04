>[!DEFINITION] Definition: Kinetic Energy
>
>The **kinetic energy** of a physical object is the [work](Work.md) needed to bring the object from rest to its current state of motion.
>
>>[!NOTATION]-
>>
>>$$
>>E_{\text{kin}} \qquad E_{\text{k}} \qquad K
>>$$
>>
>

>[!THEOREM] Theorem: Non-Relativistic Kinetic Energy of a Point Mass
>
>The [kinetic energy](Kinetic%20Energy.md) of a [point mass](../../../../Physical%20Systems/Point%20Masses/Point%20Mass.md) $m$ moving with [speed](../../../../Kinematics/Translation/Speed.md) $v$ is given by the formula
>
>$$
>E_{\text{kin}} = \frac{1}{2}mv^2
>$$
>
>provided that $v$ is a lot smaller than the [speed of light](../../../Speed%20of%20Light%20in%20a%20Vacuum.md).
>
>>[!PROOF]-
>>
>>At time $t_1$, the [resultant force](../../../Force.md) $\boldsymbol{F}$ begins to accelerates the [point mass](../../../../Physical%20Systems/Point%20Masses/Point%20Mass.md) from 0 m/s and at time $t_2$ the [speed](../../../../Kinematics/Translation/Speed.md) reaches $v$ m/s, i.e. $||\boldsymbol{v}(t_1)|| = 0$ and $||\boldsymbol{v}(t_2)||=v$. During this time $\boldsymbol{F}$ does [work](Work.md)
>>
>>$$
>>W = \int_{t_1}^{t_2} \boldsymbol{F}\cdot \boldsymbol{v}\mathop{\mathrm{d}t}
>>$$
>>
>>According to [Newton's second laws of motion](../Newton's%20Laws%20of%20Translational%20Motion.md), $\boldsymbol{F}=m\boldsymbol{a}$.
>>
>>$$
>>W = \int_{t_1}^{t_2} m\boldsymbol{a}\cdot \boldsymbol{v}\mathop{\mathrm{d}t} = m \int_{t_1}^{t_2} \boldsymbol{a}\cdot \boldsymbol{v}\mathop{\mathrm{d}t}
>>$$
>>
>>And since [acceleration](../../../../Kinematics/Translation/Acceleration.md) is the temporal derivative of [velocity](../../../../Kinematics/Translation/Velocity.md), we have 
>>
>>$$
>>\frac{\mathrm{d}\boldsymbol{v}}{\mathrm{d}t} = \boldsymbol{a}
>>$$
>>
>>$$
>>\boldsymbol{a}\mathop{\mathrm{d}t} = \mathop{\mathrm{d}\boldsymbol{v}}
>>$$
>>
>>$$
>>\begin{align*}W = m \int_{t_1}^{t_2} \boldsymbol{a}\cdot \boldsymbol{v}\mathop{\mathrm{d}t} &= m \int_{t_1}^{t_2} (\boldsymbol{a}\mathop{\mathrm{d}t}) \cdot \boldsymbol{v} \\ &= m \int_{t_1}^{t_2} \boldsymbol{v} \cdot \mathop{\mathrm{d}\boldsymbol{v}}\end{align*}
>>$$
>>
>>Let's see what the temporal derivative of $\boldsymbol{v}\cdot\boldsymbol{v}$ is. Using the product rule, we obtain
>>
>>$$
>>\frac{\mathrm{d}}{\mathrm{d}t}(\boldsymbol{v}\cdot\boldsymbol{v}) = \frac{\mathrm{d}\boldsymbol{v}}{\mathrm{d}t} \cdot \boldsymbol{v} + \boldsymbol{v}\cdot \frac{\mathrm{d}\boldsymbol{v}}{\mathrm{d}t} = 2\left( \boldsymbol{v}\cdot\frac{\mathrm{d}\boldsymbol{v}}{\mathrm{d}t}\right)
>>$$
>>
>>$$
>>\boldsymbol{v}\cdot\mathop{\mathrm{d}\boldsymbol{v}} = \frac{1}{2}\mathop{\mathrm{d}(\boldsymbol{v}\cdot\boldsymbol{v})}
>>$$
>>
>>We just substitute this into the above formula for the [work](Work.md) $W$.
>>
>>$$
>>W = m\int_{t_1}^{t_2} \boldsymbol{v} \cdot \mathop{\mathrm{d}\boldsymbol{v}} = m\int_{t_1}^{t_2} \frac{1}{2}\mathop{\mathrm{d}(\boldsymbol{v}\cdot\boldsymbol{v})} = \frac{1}{2}m \int_{t_1}^{t_2} \mathop{\mathrm{d}(\boldsymbol{v}\cdot\boldsymbol{v})}
>>$$
>>
>>Solve the integral:
>>
>>$$
>>W = \frac{1}{2}m \int_{t_1}^{t_2} \mathop{\mathrm{d}}(\boldsymbol{v}\cdot\boldsymbol{v}) = \frac{1}{2}m[\boldsymbol{v}(t_2)\cdot\boldsymbol{v}(t_2)-\boldsymbol{v}(t_1)\cdot\boldsymbol{v}(t_1)]
>>$$
>>
>>Using the properties of the dot product, we obtain
>>
>>$$
>>\boldsymbol{v}(t_2)\cdot\boldsymbol{v}(t_2) = ||\boldsymbol{v}(t_2)||^2 = v^2
>>$$
>>
>>$$
>>\boldsymbol{v}(t_1)\cdot\boldsymbol{v}(t_1) = ||\boldsymbol{v}(t_1)||^2 = 0^2
>>$$
>>
>>Thus
>>
>>$$
>>W = \frac{1}{2}m(v^2-0^2) = \frac{1}{2}mv^2
>>$$
>>
>