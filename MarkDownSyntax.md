# Markdown Syntax Guide
(Another useful reference: https://www.markdownguide.org/basic-syntax/)

## Emphasis:
- Use *asterisks* or _underscores_ to italicize text.
- Use **double asterisks** or __double underscores__ to bold text.

## Headings:
Use `#` to denote headings. The number of `#` symbols indicates the heading level (from 1 to 6).

### Example:
```markdown
*Italic Text*
**Bold Text**

# Heading 1
## Heading 2
### Heading 3

## Lists:
Use 1. 2. and so on for ordered list and - for unordered lists.
Use numbers followed by a period for ordered lists.

### Example:
- Item 1
- Item 2
  - Subitem 1
  - Subitem 2
1. First item
2. Second item

## Links:
Use [text](url) syntax to create links.

### Example:
[Visit Josue's website](https://www.josueds.me)

## Images
Use ![alt text](image_url) syntax to insert images.

### Example
![Image](/assets/images/tux.png)

## Blockquotes:
Use `>` to denote blockquotes.

### Example:
> This is a blockquote.

## Code Blocks:
- Use triple backticks ``` for inline code and code blocks.
- Optionally specify the language after the opening triple backticks for syntax highlighting.

### Example:
Inline code: `print("Hello, World!")`

```python
# Python code block
def greet():
    print("Hello, World!")
```

Horizontal Rules:
-----------------

Use `---` or `___` to create horizontal rules.

### Example:

* * *

Tables:
-------

Use pipe `|` to separate columns and hyphens `-` to separate the header row from the content rows.

### Example:

| Header 1 | Header 2 |
| --- | --- |
| Content 1 | Content 2 |

Task Lists:
-----------

Use `- [ ]` for an incomplete task and `- [x]` for a completed task.

### Example:

*   [ ]  Task 1
*   [x]  Task 2






    