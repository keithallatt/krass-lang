# Krass

Krass Programming language. Krass is designed to integrate into TeX documents to be more computably functional. Much like PHP adds to HTML code, Krass adds to TeX. 

Technically, TeX is Turing complete, but defining functions can be extremely difficult when they don't revolve around typesetting. Krass is designed to take file input and compute results to be typeset by TeX. The resulting plain TeX file is also kept to view results in TeX. 

## Syntax

**Reserved Keywords:** `struct`, `function`, `for`, `while`, `if`, `else`, `break`, `continue`, `try`, `catch`, `return`, `print`, `and`, `or`, `not`, `true`, `false`, `nil`, `global`, `read`. 

**Reserved Symbols:** `+`, `-`, `*`, `/`, `=`, `&`, `|`, `%`, `;`, `(`, `)`, `<`, `>`, `^`, `'`, `"`, `:`, `[`, `]`, `{`, `}`. 

## Grammar

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

### Exception Handling

Exception Handling will be fashioned like Java and C variants as well. Following a `try { ... }` block with at least one `catch (exceptionName) { ... }` block, specifying the name for the exception. If no Catch block is supplied, an empty catch-all block will be placed in automatically.

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

Some important notes: Krass blocks are run independently of one another. If values from one block are needed in another, that value must: *a*) be declared and initialized *before* referencing it later in code, and *b*) be initialized with the `global` keyword.


# Krass2pythonREADME.md 

Highlight how structs and functions and control flow are translated into Python 3 from pure Krass.


## Function Definitions

Function definitions in Krass begin with the function keyword, then a function name and parameters. The function body follows in braces.

```
function foo(bar) {
  ...
}
```

translates to:

```
def foo(bar):
  ...
```

## Structs

Structs are usually groups of typed members in C and derivatives of C, but in Krass, they are simply a grouping of many fields. These can be initialized or not, if they aren't, they will be initialized to `nil`. 

```
struct foo {
  bar;
  baz = 3;
}

```

These will be composed into classes in Python. For example, the above would be translated to:

```
class foo:
  def __init__(self):
    self.bar = None
    self.baz = 3
```

To initialize an instance of a struct in Krass:

```
foo_instance = foo(bar=3)
```

While would be translated into:

```
foo_instance = foo()
foo_instance.bar = 3
```

## Control Flow

### If Statements

If statements use Java-esque conditions, yet compiling is not too much of a challenge. A line in Krass such as:

```
if (<cond>) {
  ...
}
```

just gets compiled into:

```
if <cond>:
  ...
```

Of course the condition must be compiled seperately, yet that's not too much of a challenge.

### For Loops

Much like if statements, for loops have Java-esque features, but still get compiled down to Python.

```
for (item : iterator) {
  ...
}
```

gets compiled into:

```
for item in iterator:
  ...
```

### While Loops

Even with conditions needing to be formatted from Krass to Python, while loops share a lot of commonalities with if statements.

```
while (<cond>) {
  ...
}
```

compiles into:

```
while <cond>:
  ...
```

### Conditions

Some symbols in Krass need distinction between bitwise and logical operations, because of the lack of static typing. 

| Symbol     | Meaning                                 |
|------------|-----------------------------------------|
|  !         | Logical Not                             |
|  && / &    | Logical And / Bitwise And               |
|  \|\| / \| | Logical Or / Bitwise Or                 |
|  ^         | Logical / Bitwise XOR                   |
|  > / >=    | Greater than / Greater than or equal to |
|  < / <=    | Less than / Less than or equal to       |
|  == / !=   | Equal / Not equal                       |

All conditions are expressed as:

`<condition> = <true/false> |  <condition> <bool op> <condition> | <number> <num op> <number>`

where `<bool op>` refers to all binary operators that evaluate on boolean inputs, and `<num op>` refers to binary operations that take numerical values as input and returns a boolean.


## File IO

In Krass, writing to file is impossible. There is no reason to in the context of where Krass is used. Potentially later in Krass development, file output will be implemented. To read a file the following line should be used.

```
file_contents = read(<filename>);
```

which will compile into:

```
file_contents = open(<filename>,'r').read()
```

This leads the `read` function to extract the contents of a given file. 


