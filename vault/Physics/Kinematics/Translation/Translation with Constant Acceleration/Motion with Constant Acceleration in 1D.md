>[!THEOREM] Theorem: Motion with Constant Acceleration in 1D
>
>In one-dimensional [motion with constant acceleration](Motion%20with%20Constant%20Acceleration.md) the [position](../Position.md), [velocity](../Velocity.md) and [acceleration](../Acceleration.md) vectors become scalars $r(t),v(t),a$.
>
>In addition to the general laws of [motion with constant acceleration](Motion%20with%20Constant%20Acceleration.md), in one dimension we also have:
>
>$$
>v_{\text{avg}}(t)=\frac{v(t)+v_0}{2}
>$$
>
>$$
>r(t) = r_0+t\cdot v_{\text{avg}}(t)
>$$
>
>$$
>v^2 = v_0^2 +2a(r-r_0)
>$$
>
>The last law makes it possible to compute the [velocity](../Velocity.md) $v=v(t)$ of a [point mass](../../../Physical%20Systems/Point%20Masses/Point%20Mass.md) as a function of its [position](../Position.md) $r=r(t)$.
>
>>[!PROOF]- Proof: First Law
>>
>>$$
>>v_{\text{avg}}(t) = \frac{r(t)-r(0)}{t-0}=\frac{r(t)-r_0}{t}=\frac{r_0+v_0t+\frac{1}{2}at^2-r_0}{t}=v_0+\frac{1}{2}at
>>$$
>>
>>We add $v_0$ to both sides of the following equation and then multiply by $2$.
>>
>>$$
>>v_{\text{avg}}(t) = v_0 + \frac{1}{2}at
>>$$
>>
>>$$
>>v_{\text{avg}}(t) + v_0 = 2v_0 + \frac{1}{2}at
>>$$
>>
>>$$
>>2v_{\text{avg}}(t) + 2v_0 = 4v_0 + at
>>$$
>>
>>$$
>>2v_{\text{avg}}(t) + 2v_0 = 3v_0 + (v_0 + at) = 3v_0 + v(t)
>>$$
>>
>>$$
>>2v_{\text{avg}}(t)= v_0+v(t)
>>$$
>>
>>$$
>>v_{\text{avg}}(t)=\frac{v(t)+v_0}{2}
>>$$
>>
>
>>[!PROOF]- Proof: Second Law
>>
>>$$
>>r(t) = r_0 + v_0 t + \frac{1}{2} at^2 = r_0 + t\left(v_0+\frac{1}{2}at\right)=r_0+t\cdot v_{\text{avg}}(t)
>>$$
>>
>>For an explanation for the last step, see the proof of the first law.
>>
>
>>[!PROOF]- Beweis: Third Law
>>
>>Rearrange the law for the [velocity](../Velocity.md):
>>
>>$$
>>t = \frac{v(t)-v_0}{a}
>>$$
>>
>>Susbtitute for $t$ in the law for [position](../Position.md):
>>
>>$$
>>r(t) = r_0+ v_0\frac{v(t)-v_0}{a} + \frac{1}{2}a\left(\frac{v(t)-v_0}{a}\right)^2
>>$$
>>
>>$$
>>2a r(t) = 2ar_0 + 2v_0(v(t)-v_0)+(v(t)-v_0)^2
>>$$
>>
>>$$
>>2a(r(t)-r_0)=2v_0v(t)-2v_0^2+ v(t)^2 - 2v_0v(t) + v_0^2
>>$$
>>
>>$$
>>2a(r(t)-r_0)=v(t)^2-v_0^2
>>$$
>>
>>$$
>>v(t)=2a(r(t)-r_0)+v_0^2
>>$$
>>
>