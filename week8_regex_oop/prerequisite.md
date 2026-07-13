# Week 8 Prerequisites: Describing Patterns and Modeling Things

Week 8 gives you two big tools: regular expressions for describing text patterns, and classes for grouping data and behavior into your own types. Both feel abstract at first, so lean on concrete examples.

## 1. Regex describes a shape of text, not exact text

Instead of checking a string letter by letter, you describe the *pattern* once.

```text
"a phone number" -> three digits, dash, three digits, dash, four digits
```

Ask yourself:

```text
Can I say the pattern in plain English first?
```

If you can say it, you can usually write it.

## 2. Read a pattern left to right as a checklist

Each symbol is one demand the text must satisfy in order.

```text
^   start
\d  a digit
.+  one or more of anything
@   a literal @
$   end
```

A real dot must be written `\.`, because a plain `.` means "any character."

## 3. Anchors keep junk from sneaking in

`^` and `$` pin the pattern to the start and end.

```text
without anchors -> matches if the pattern appears anywhere
with ^ and $   -> the WHOLE string must fit the pattern
```

Ask:

```text
Do I want a match anywhere, or must the entire string match?
```

## 4. Groups let you pull pieces back out

Parentheses `( )` remember a chunk so you can grab it later.

```text
group 1 -> first ( )
group 2 -> second ( )
```

Use groups when you need to *extract* or *rearrange*, like turning "Last, First" into "First Last".

## 5. A class is a blueprint; an object is one built copy

Think cookie cutter versus cookie.

```text
class  -> the cutter (describes the shape)
object -> a real cookie stamped from it
```

You can stamp many separate objects from one class, each with its own data.

## 6. `self` means "this particular object"

`self` is how each object keeps its own values separate.

```python
self.name = name   # store name ON this object
```

Ask:

```text
Whose data is this line touching right now?
```

You never pass `self` yourself; Python fills it in when you call a method.

## 7. `__init__` is the setup that runs at birth

When you create an object, `__init__` runs once to fill in its starting data.

```text
Student("Sagar", "Python") -> __init__ stores name and house
```

Think of it as the "unboxing and setup" step.

## 8. Inheritance means "start from an existing type, then change what differs"

```text
class Dog(Animal): Dog gets everything Animal has
then Dog can override the parts it wants different
```

Python checks the child first, then falls back to the parent.

Ask:

```text
Is this a special kind of something I already built?
```

## 9. Week 8 thinking habit

For text: ask "what pattern am I really describing?"
For classes: ask "what data and what actions naturally belong together?"

If a task is simple, a plain function or string method may beat both.
