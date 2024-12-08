>[!DEFINITION] Definition: Potential Energy
>
>A **potential energy function** $U$ of a [conservative force](Conservative%20Force.md) $\boldsymbol{F}$ is a scalar field such that
>
>$$\boldsymbol{F} = -\nabla U$$
>
>There are infinitely many such functions but we are free to choose where $U = 0$ and thus fix a particular one, so long as we are consistent with our choice. Once $U$ is fixed, we call $U(\boldsymbol{r})$ the **potential energy** of a [point mass](../../../../Physical%20Systems/Point%20Masses/Point%20Mass.md) at the [position](../../../../Kinematics/Translation/Position.md) $\boldsymbol{r}$ due to $\boldsymbol{F}$.
>
>>[!NOTATION]
>>
>>$$E_{\text{p}} \qquad E_{\text{pot}} \qquad U$$
>>
>

>[!THEOREM] Theorem: Work of a Conservative Force
>
>The [work](Work.md) done by a [conservative force](Conservative%20Force.md) $\boldsymbol{F}$ acting on a [physical system](../../../../Physical%20Systems/Physical%20System.md) is equal to the negative change in its [potential energy](Potential%20Energy.md).
>
>$$
>W = -\Delta U
>$$
>
>>[!NOTE]
>>
>>The exact choice of the potential energy function is irrelevant.
>
>>[!PROOF]-
>>
>>$$W = \int_{t_1}^{t_2} \boldsymbol{F} \cdot \boldsymbol{v} \mathop{\mathrm{d}t} = -U(\boldsymbol{r}(t_2)) - (-U(\boldsymbol{r}(t_1))) = -U(\boldsymbol{r}(t_2)) + U(\boldsymbol{r}(t_1)) = -\Delta U$$
>>
>