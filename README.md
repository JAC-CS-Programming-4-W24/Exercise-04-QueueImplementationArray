# Objectives

**Implement** a queue data structure.

# Context

There is a complete simulation algorithm in the file `main.py`. There is
one big missing piece: it relies in the `Queue` we\'ve designed, but
that class is not complete!

# TODO

If you are not in class right now, read the notes on Queue API. There
are two techniques that we\'re going to use.

## Idea 1: try implementing all `IntQueue` operations using the technique we did in `IntStack`.

<https://jac-cs-programming-4-w24.github.io/Notes/#/4-Queues/?id=implementing-a-queue-using-an-array>

1.  Implement the methods of the `IntQueue` API: `enqueue(..)`,
    `dequeue()`, `front()`.
2.  Remember to `raise` exceptions
    `QueueOverflowError and ~QueueUnderflowError` when the caller has
    not met the operation preconditions.
3.  Implement `is_empty()` and `is_full()`.

The class `IntStack` is included for reference in the file
`our_stack.py`.

## Idea 2: try implementing `IntQueue` using the \"circular\" array idea.

<https://jac-cs-programming-4-w24.github.io/Notes/#/4-Queues/?id=%e2%ad%95%ef%b8%8f-circular-array>

1.  Re-implement the methods of the `IntQueue` API: `enqueue(..)`,
    `dequeue()`, `front()`.
2.  Raise exceptions `QueueOverflowError and ~QueueUnderflowError` when
    the caller has not met the operation preconditions.
3.  Challenge: re-implement `is_empty()` and `is_full()`.
