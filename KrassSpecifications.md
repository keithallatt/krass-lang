## Syntax

### Function Declarations

All function delarations are as follows. First comes the `function` keyword. Then comes the function name, which follows variable naming conventions (Alphanumeric with underscores, first character can't be a number, etc.) which will uniquely identify the function. For each parameter, a variable name will be supplied.

A sample function declaration looks as follows:

```
function foobar(foo, bar) {
  ...
}
```

### Control Flow

Most control flow elements are expressed similarly to Java and C variants. If statements and loops are fairly similar, less the type casting.

**If Statements:** `if (<cond>) { ... } else { ... }` or `if (<cond>) { ... }`

**For Loops:** `for (item : iterator) { ... }` or `for (index : range(n)) { ... }`

**While Loops:** `while (<cond>) { ... }`

## Semantics

Each Krass file has some sections are pure TeX and Krass blocks. Each Krass block starts with an open brace and identifier. A Krass block starts with `::?` and ends with `?::`

For example, a sample document could contain a block such as:

```
Some pure TeX...

::?

function foo(bar, baz) {
    return bar + baz
}

print(foo("Hello ", "World!"))

?::

Some more TeX...
```

Some important notes: 

- Krass blocks are run independently of one another.
- Pure Python can be used for function calls and builtins. Imports work for python libraries.
