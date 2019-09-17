# Krass2pythonREADME.md 

Highlight how structs and functions and control flow are translated into Python 3 from pure Krass.

## Imports

As mentioned before, Krass imports will be compiled as inserted code. To prevent shadowing, imported scripts will be bundled in classes when compiled down to Python. Therefore the class name must be referenced to access functions.

foo.krass
```
function foo() {
  return "foo";
}
```

bar.krass
```
import foo

foo.foo()
```

will get compiled into:

```
class foo:
  @staticmethod
  def foo():
    return "foo"

foo.foo()
```


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

| Symbol    | Meaning                                 |
|-----------|-----------------------------------------|
|  ! / b!   | Logical Not / Bitwise Not               |
|  & / b&   | Logical And / Bitwise And               |
|  \| / b\| | Logical Or / Bitwise Or                 |
|  ^        | Logical / Bitwise XOR      |
|  > / >=   | Greater than / Greater than or equal to |
|  < / <=   | Less than / Less than or equal to       |
|  == / !=  | Equal / Not equal                       |

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

