# LinkedList

## Properties

- Linear data structure
- Self referential data type
- no random access

## Types

- Singly Linked List
- Doubly Linked List
- Double Ended Linked List

## Computational Complexity

### Time Complexity

| Operation         | Singly LL | Doubly LL | Double-Ended LL |
| ----------------- | --------- | --------- | --------------- |
| Insert at head    | O(1)      | O(1)      | O(1)            |
| Insert at tail    | O(n)      | O(n)      | O(1)            |
| Delete at head    | O(1)      | O(1)      | O(1)            |
| Delete at tail    | O(n)      | O(n)      | O(1)            |
| Search by value   | O(n)      | O(n)      | O(n)            |
| Insert after node | O(1)      | O(1)      | O(1)            |
| Delete by value   | O(n)      | O(n)      | O(n)            |

### Space Complexity

| List Type          | Extra Space Per Node                                    |
| ------------------ | ------------------------------------------------------- |
| Singly Linked List | 1 pointer (next) → O(n) total                           |
| Doubly Linked List | 2 pointers (prev, next) → O(2n) total                   |
| Double-Ended List  | Same as singly/doubly, plus tail ref → Negligible extra |

## Applications

- polynomial arithmetics
- adjency list in graphs
- job scheduling or task management

## My life applications

- N.A
