# Brief Prerequisite Reviews, Homework 0, and Project 0

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

x^{(2)} = \begin{bmatrix}
  a_1 \\ -a_2 \\ a_3
\end{bmatrix}
```

Simply, set $x^{(1)}.x^{(2)} = 0$ i.e., $a_1^2 - a_2^2 + a_3^2 = 0$.
