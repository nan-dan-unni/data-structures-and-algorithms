# Stack

## Properties

- linear data structure
- follows LIFO principle
- only top element is accessible
- eg: pile of plates

## Computational Complexity

### Time Complexity

- `push()`, `pop()`, `peek()` - O(1)

### Space Complexity

- N.A

## Applications

- syntax checking in compilers
- postfix-infx-prefix conversions
- undo functionality in editors

## My life applications

- to parse event data from error logs
  - there was an outage in the company I worked for and we lost around 360 SIEM events
  - the logs was available in datadog and I downloaded it as CSV
  - then I used regex to parse the part where error data is present in the log
  - from the error data string, I used **Stack** to parse the event data
