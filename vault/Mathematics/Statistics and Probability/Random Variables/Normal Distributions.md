
# The Standard Normal Distribution

>[!DEFINITION] Definition: Standard Normal Distribution
>
>We say that a [continuous random variable](Random%20Variables.md#Continuous%20Random%20Variables) $X$ has the **standard normal distribution** if its [probability density function](Random%20Variables.md#Probability%20Density%20Functions) $f$ can be written in terms of the [real exponential function](../../Analysis/Real%20Analysis/Real%20Functions/The%20Real%20Exponential%20Function.md) as follows:
>
>$$
>f(x) = \frac{1}{\sqrt{2\pi}} \mathrm{e}^{-x^2/2}
>$$
>
>>[!NOTATION]
>>
>>$$
>>X \sim \mathcal{N}(0,1) \qquad X \in \mathcal{N}(0,1)
>>$$
>>
>>In this case, it is also typical to denote the [probability density function](Random%20Variables.md#Probability%20Density%20Functions) of $X$ by $\varphi$ and its [cumulative distribution function](Random%20Variables.md#Cumulative%20Distribution%20Function) by $\Phi$.
>>
>

## Properties

>[!THEOREM]- Theorem: Expectation of the Standard Normal Distribution
>
>The [expectation](Expectation.md) of a [continuous random variable](Random%20Variables.md#Continuous%20Random%20Variables) which has the [standard normal distribution](Normal%20Distributions.md#The%20Standard%20Normal%20Distribution) is zero.
>
>$$
>X \sim \mathcal{N}(0,1) \implies \mathbb{E}[X] = 0
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Variance of the Standard Normal Distribution
>
>The [variance](Variance%20and%20Standard%20Deviation.md#Variance) of a [continuous random variable](Random%20Variables.md#Continuous%20Random%20Variables) which has the [standard normal distribution](Normal%20Distributions.md#The%20Standard%20Normal%20Distribution) is one.
>
>$$
>X \sim \mathcal{N}(0,1) \implies \operatorname{Var}(X) = 1
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

# General Normal Distributions

>[!DEFINITION] Definition: Normal Distribution
>
>We say that a [continuous random variable](Random%20Variables.md#Continuous%20Random%20Variables) $X$ has a **normal distribution** if there exist $\mu \in \mathbb{R}$, $\sigma \gt 0$ and a [continuous random variable](Random%20Variables.md#Continuous%20Random%20Variables) $Z$ which has the [standard normal distribution](Normal%20Distributions.md#Standard%20Normal%20Distribution) such that
>
>$$
>X = \mu + \sigma Z.
>$$
>
>>[!NOTATION]
>>
>>$$
>>X \sim N(\mu, \sigma^2) \qquad X \in N(\mu, \sigma^2)
>>$$
>>
>
>>[!DEFINITION] Definition: Standardization
>>
>>We call $Z$ the **standardization** of $X$.
>>
>

## Properties

>[!THEOREM]- Theorem: Cumulative Distribution Functions of Normal Distributions
>
>The [cumulative distribution function](Random%20Variables.md#Cumulative%20Distribution%20Function) $F$ of a [continuous random variable](Random%20Variables.md#Continuous%20Random%20Variables) $X$ which has the [normal distribution](Normal%20Distributions.md#General%20Normal%20Distributions) $\mathcal{N}(\mu, \sigma^2)$ is
>
>$$
>F(x) = \Phi\left(\frac{x - \mu}{\sigma}\right),
>$$
>
>where $Phi$ is the [cumulative distribution function](Random%20Variables.md#Cumulative%20Distribution%20Function) of $X$'s [standardization](Normal%20Distributions.md#General%20Normal%20Distributions).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Probability Density of Normal Distributions
>
>The [probability density function](Random%20Variables.md#Probability%20Density%20Functions) $f$ of a [continuous random variable](Random%20Variables.md#Continuous%20Random%20Variables) $X$ which has the [normal distribution](Normal%20Distributions.md#General%20Normal%20Distributions) $\mathcal{N}(\mu, \sigma^2)$ is
>
>$$
>f(x) = \frac{1}{\sigma \sqrt{2\pi}} \mathrm{e}^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2} = \frac{1}{\sigma}\varphi\left(\frac{x - \mu}{\sigma}\right),
>$$
>
>where $\mathrm{e}^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}$ is the [real exponential function](../../Analysis/Real%20Analysis/Real%20Functions/The%20Real%20Exponential%20Function.md) and $\varphi$ is the [probability density function](Random%20Variables.md#Probability%20Density%20Functions) of $X$'s [standardization](Normal%20Distributions.md#General%20Normal%20Distributions).
>
>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Expectation of Normal Distributions
>
>The [expectation](Expectation.md) of a [continuous random variable](Random%20Variables.md#Continuous%20Random%20Variables) $X$ which has the [normal distribution](Normal%20Distributions.md#General%20Normal%20Distributions) $\mathcal{N}(\mu, \sigma^2)$ is $\mu$.
>
>$$
>X \sim \mathcal{N}(\mu, \sigma^2) \implies \mathbb{E}(X) = \mu
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Variance of Normal Distributions
>
>The [variance](Variance%20and%20Standard%20Deviation.md) of a [continuous random variable](Random%20Variables.md#Continuous%20Random%20Variables) $X$ which has the [normal distribution](Normal%20Distributions.md#General%20Normal%20Distributions) $\mathcal{N}(\mu, \sigma^2)$ is $\sigma^2$.
>
>$$
>X \sim \mathcal{N}(\mu, \sigma^2) \implies \operatorname{Var}(X) = \sigma^2
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: The 68–95–99.7 Rule
>
>If a [continuous random variable](Random%20Variables.md#Continuous%20Random%20Variables) $X$ has the [normal distribution](Normal%20Distributions.md#General%20Normal%20Distributions) $\mathcal{N}(\mu, \sigma^2)$, then
>
>$$
>\begin{align*}
>P(|X - \mu| \lt 1\sigma) \approx 68.27 \% \\
>P(|X - \mu| \lt 2\sigma) \approx 95.45 \% \\
>P(|X - \mu| \lt 3\sigma) \approx 99.73 \%
>\end{align*}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>