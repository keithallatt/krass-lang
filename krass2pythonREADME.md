# krass2pythonREADME.md 

Highlight how structs and functions and control flow are translated into Python 3 from pure Krass.


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


