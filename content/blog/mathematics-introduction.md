---
title: "Introduction to Mathematical Concepts"
date: 2024-04-15
lastmod: 2024-04-15
author: Alexander Saavedra
description: "A brief introduction to some fundamental mathematical concepts using LaTeX"
tags: [mathematics, linear-algebra, statistics]
draft: true
---

# Introduction to Mathematical Concepts

This post demonstrates LaTeX support in the bear blog theme with some basic mathematical concepts.

## Linear Algebra

### Vectors and Matrices

A vector in $$\mathbb{R}^n$$ can be represented as:

$$
\mathbf{v} = \begin{bmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{bmatrix}
$$

Matrix multiplication is defined as:

$$
\mathbf{C} = \mathbf{A}\mathbf{B} \quad \text{where} \quad c_{ij} = \sum_{k=1}^{n} a_{ik}b_{kj}
$$

### Eigenvalues and Eigenvectors

For a square matrix $$\mathbf{A}$$, an eigenvector $$\mathbf{v}$$ and its corresponding eigenvalue $$\lambda$$ satisfy:

$$
\mathbf{A}\mathbf{v} = \lambda\mathbf{v}
$$

## Statistics

### Probability Distributions

The normal distribution with mean $$\mu$$ and variance $$\sigma^2$$ has the probability density function:

$$
f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}
$$

### Linear Regression

In simple linear regression, we model the relationship between a dependent variable $$y$$ and an independent variable $$x$$ as:

$$
y = \beta_0 + \beta_1x + \epsilon
$$

where $$\epsilon$$ is the error term.

### Maximum Likelihood Estimation

The likelihood function for a set of independent observations $$x_1, x_2, \ldots, x_n$$ is:

$$
L(\theta) = \prod_{i=1}^{n} f(x_i|\theta)
$$

where $$\theta$$ represents the parameters of the distribution.

## Conclusion

This post demonstrates various LaTeX mathematical expressions that can be used in your blog posts. You can use:

- Inline math with double dollar signs: $$\mathbf{v}$$
- Display math with double square brackets: $$\mathbf{A}\mathbf{v} = \lambda\mathbf{v}$$
- Complex mathematical expressions with various LaTeX commands

Remember to set `draft: false` when you're ready to publish the post! 