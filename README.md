# Krass

Krass Programming language. Krass is designed to integrate into TeX documents to be more computably functional. Much like PHP adds to HTML code, Krass adds to Tex. 

Technically, TeX is Turing complete, but defining functions can be extremely difficult when they don't revolve around typesetting. Krass is designed to take file input and compute results to be typeset by TeX. The resulting plain TeX file is also kept to view results in TeX. 

## Syntax

**Reserved Keywords:** `struct`, `function`, `for`, `while`, `if`, `else`, `import`, `break`, `continue`, `try`, `catch`, `return`, `print`, `and`, `or`, `not`, `true`, `false`, `nil`, `global`. 

**Reserved Symbols:** `+`, `-`, `*`, `/`, `=`, `&`, `|`, `%`, `;`, `(`, `)`, `<`, `>`, `^`, `'`, `"`, `:`, `[`, `]`, `{`, `}`. 

**Primitive Data Types:** `int`, `float`, `char`, `boolean`, `array`.

## Grammar

### Import Statements

An import statement (`import <package>`) imports sections of Krass code, which will usually contain function declarations and structs. When the code segment is evaluated, the imported sections of code will be inserted wherever the import statement lies. Any non-function and non-struct code will still be run.

### Function Declarations

All function delarations are as follows. First comes the `function` keyword. Then comes the function name, which follows variable naming conventions (Alphanumeric with underscores, first character can't be a number, etc.) which will uniquely identify the function. For each parameter, type and variable name will be laid out in a `name: type` format.

A sample function declaration looks as follows:

```
function foobar(foo: <type>, bar: <type>) {
  ...
}
```


## Semantics

Each Krass file has some sections are pure TeX and Krass blocks. Each Krass block starts with an open brace and identifier. A Krass block starts with `::?` and ends with `?::`

For example, a sample document could contain a block such as:

```
Some pure TeX...

::?

-- insert some Krass Code Here --

?::

Some more TeX...
```

Some important notes: Krass blocks are run independently of one another. If values from one block are needed in another, that value must: *a*) be declared and initialized *before* referencing it later in code, and *b*) be initialized with the `global` keyword.
