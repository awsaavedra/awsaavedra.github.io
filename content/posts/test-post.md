---
title: "LaTeX Math Examples"
date: 2025-11-10T19:58:37-08:00
lastmod: 2025-11-10T19:58:37-08:00
author: Alexander Saavedra
tags: ["math", "latex"]
draft: false
enableDisqus: false
enableMathJax: false
disableToC: false
disableAutoCollapse: true
---

This post demonstrates how to write mathematical equations using LaTeX syntax in Hugo.

## Inline Math

Use single dollar signs `$...$` for inline math. For example, Einstein's mass-energy equivalence $E=mc^2$ appears inline with text. You can also reference variables like $x$, $y$, and $\alpha$ within sentences.

## Block Equations

Use double dollar signs `$$...$$` for centered display equations:

$$E=mc^2$$

## Common Mathematical Expressions

### Fractions

The quadratic formula uses fractions:

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

Inline fractions work too: $\frac{1}{2}$ or $\frac{a}{b}$.

### Exponents and Subscripts

- Exponents: $x^2$, $e^{i\pi}$, $2^{n-1}$
- Subscripts: $x_1$, $a_i$, $v_{\text{max}}$
- Combined: $x_1^2$, $\sum_{i=1}^{n} i$

### Greek Letters

Lowercase: $\alpha$, $\beta$, $\gamma$, $\delta$, $\epsilon$, $\theta$, $\lambda$, $\mu$, $\pi$, $\sigma$, $\phi$, $\omega$

Uppercase: $\Gamma$, $\Delta$, $\Theta$, $\Lambda$, $\Sigma$, $\Phi$, $\Omega$

### Summations and Products

$$\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$$

$$\prod_{i=1}^{n} i = n!$$

### Integrals

The Gaussian integral:

$$\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}$$

Definite integral: $\int_0^1 x^2 dx = \frac{1}{3}$

### Matrices

$$\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}$$

Or with different brackets:

$$\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix}$$

### Square Roots and Radicals

$$\sqrt{2} \approx 1.414$$

$$\sqrt[3]{8} = 2$$

### Limits

$$\lim_{x \to \infty} \frac{1}{x} = 0$$

$$\lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n = e$$

### Derivatives

First derivative: $\frac{dy}{dx}$

Second derivative: $\frac{d^2y}{dx^2}$

Partial derivatives: $\frac{\partial f}{\partial x}$

### Complex Equations

Euler's identity:

$$e^{i\pi} + 1 = 0$$

Schrödinger equation:

$$i\hbar\frac{\partial}{\partial t}\Psi(\mathbf{r},t) = \hat{H}\Psi(\mathbf{r},t)$$

Maxwell's equations:

$$\nabla \cdot \mathbf{E} = \frac{\rho}{\epsilon_0}$$

$$\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$$

### Chemical Equations

Use `\text{}` for regular text in equations. Nuclear fusion in the Sun:

$$4 \, \text{H} \rightarrow \text{He} + 2 \, \text{e}^+ + 2 \, \nu_e + \gamma$$

### Sets and Logic

Set notation: $\{1, 2, 3, \ldots, n\}$

Set operations: $A \cup B$, $A \cap B$, $A \subset B$

Logic: $\forall x \in \mathbb{R}$, $\exists y$, $\Rightarrow$, $\Leftrightarrow$

### Special Symbols

- Infinity: $\infty$
- Approximately: $\approx$
- Not equal: $\neq$
- Less/greater than or equal: $\leq$, $\geq$
- Plus/minus: $\pm$
- Times: $\times$
- Dots: $\cdot$, $\cdots$, $\ldots$, $\vdots$, $\ddots$

## Quick Reference

| Type | Syntax | Result |
|------|--------|--------|
| Inline math | `$x^2$` | $x^2$ |
| Block math | `$$x^2$$` | (centered) |
| Fraction | `$\frac{a}{b}$` | $\frac{a}{b}$ |
| Superscript | `$x^2$` | $x^2$ |
| Subscript | `$x_i$` | $x_i$ |
| Square root | `$\sqrt{2}$` | $\sqrt{2}$ |
| Sum | `$\sum_{i=1}^{n}$` | $\sum_{i=1}^{n}$ |
| Integral | `$\int_a^b$` | $\int_a^b$ |

## Tips

1. Always balance your dollar signs - one `$` at start and end for inline, two `$$` for block
2. Use curly braces `{}` to group multi-character sub/superscripts: `x^{10}` not `x^10`
3. Use `\text{}` for regular text inside equations: `$\text{speed} = \frac{d}{t}$`
4. Escape special characters if needed with backslash: `\$` for literal dollar sign
5. Leave blank lines before and after block equations `$$...$$` for proper spacing
