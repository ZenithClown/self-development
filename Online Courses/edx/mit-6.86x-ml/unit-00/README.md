# Brief Prerequisite Reviews, Homework 0, and Project 0

## 2. Sums and Products

### Summation Notation

```math
\sum_{k=1}^{K} \sum_{t=1}^{T} 1 = ?
```

then,

```math
\sum_{t=1}^{T} 1 = 1 + 1 + ... + 1 = T
```

finally,
```math
\sum_{k=1}^{K} \sum_{t=1}^{T} 1 = \sum_{k=1}^{K} T = KT
```

### Product Notation

```math
\begin{align}
\prod_{i=0}^{M} \frac{1}{\theta} &= \frac{1}{\theta} * \frac{1}{\theta} * \frac{1}{\theta} * ... * \frac{1}{\theta} \\
&= \frac{1}{\theta^M}
\end{align}
```

```math
\begin{align}
\prod_{k=1}^{K}
  &= \frac{k}{k+1}\\
  &= \frac{1}{2} * \frac{2}{3} * ... * \frac{K}{K+1} \\
  &= \frac{1}{K+1}
\end{align}
```

```math
\begin{align}
ln(\prod_{k=1}^{K} e^k)
  &= ln(e^1 * e^2 * e^3 * ... * e^K)\\
  &= ln(e^{1 + 2 + ... + K}) \\
  &= ln(e^{\frac{K(K+1)}{2}}) \because \text{AP Series Notation}\\
  &= \frac{K(K+1)}{2}
\end{align}
```

[AP Series Notation](https://byjus.com/question-answer/what-is-the-sum-of-1-2-3-n/)

## 4. Points and Vectors

### Dot Products and Norm

Length of a Matrix $a$ is given as $\sqrt{a_1^2 + a_2^2 + a_3^2 + ... + a_n^2}$ where,

```math
a = \begin{bmatrix}
  a_1 \\
  a_2 \\
  ... \\
  a_n
\end{bmatrix}
```

Also, $a.b = |a||b|cos\alpha$, thus: $\alpha = cos^{(-1)} \frac{a.b}{|a||b|}$ example,

Let,
```math
a = \begin{bmatrix}
  0.4 \\ 0.3
\end{bmatrix}

\\

b = \begin{bmatrix}
  -0.15 \\ 0.2
\end{bmatrix}
```

then, $a.b = 0.4 (-0.15) + (0.3)(0.2) = 0$ thus $cos^{-1} 0 = \pi/2$

### Dot Products and Orthogonality

```math
x^{(1)} = \begin{bmatrix}
  a_1 \\ a_2 \\ a_3
\end{bmatrix}

\\

x^{(2)} = \begin{bmatrix}
  a_1 \\ -a_2 \\ a_3
\end{bmatrix}
```

Simply, set $x^{(1)}.x^{(2)} = 0$ i.e., $a_1^2 - a_2^2 + a_3^2 = 0$.
