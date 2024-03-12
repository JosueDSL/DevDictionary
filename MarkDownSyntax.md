# Markdown Syntax Guide
(Another useful reference: https://www.markdownguide.org/basic-syntax/)

## Emphasis:
- Use *asterisks* or _underscores_ to italicize text.
- Use **double asterisks** or __double underscores__ to bold text.

### Example:
```markdown
*Italic Text*
**Bold Text**
```

## Headings:
Use `#` to denote headings. The number of `#` symbols indicates the heading level (from 1 to 6).

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
Use `[text](url)` syntax to create links.

### Example:
`[Visit Josue's website](https://www.josueds.me)`
[Visit Josue's website](https://www.josueds.me)
## Images
Use `![alt text](image_url)` syntax to insert images.

### Example
`![Image](/assets/images/tux.png)`
![Image](/assets/images/tux.png)
## Blockquotes:
Use `>` to denote blockquotes.

### Example:
> This is a blockquote.

## Code Blocks:
- Use single backticks ` for inline code and triple ``` for code blocks, don't forget to close the code blocks!.
- Optionally specify the language after the opening triple backticks for syntax highlighting. As: ```python

### Example:
Inline code: `print("Hello, World!")`

```python
# Python code block
def greet():
    print("Hello, World!")
```

## Horizontal Rules:
-----------------

Use `---` or `___` or `* * *` to create horizontal rules.

### Example:

* * *
___
- - -

## Tables:
Use pipe `|` to separate columns and hyphens `-` to separate the header row from the content rows.

### Example:
```markdown
| Header 1 | Header 2 |
| --- | --- |
| Content 1 | Content 2 |
```
## Task Lists:
Use `- [ ]` for an incomplete task and `- [x]` for a completed task.

### Example:

*   [ ]  Task 1
*   [x]  Task 2

# Conventions of a Good README File
The README file should be as good as your project itself.

Make the project stand out and look professional by at least including the following elements in your README:

* **Project Title:** the name of your project
* **Description:** This is an extremely important component of the README. You should describe the main purpose of your project. Answer questions like “why did you build this project?” and “what problem(s) does it solve?”. It also helps to include your motivations for the project and what you learned from it.
* **Features:** If your project has multiple features, list them here. Don’t be afraid to brag if your project has unique features that make it stand out. You can even add screenshots and gifs to show off the features.
* **How to use:** Here, you should write step-by-step instructions on how to install and use your project. Any software or package requirements should also be listed here.
* **Technologies:** List all the technologies and/or frameworks you used and what purpose they serve in your project.
* **Collaborators:** If others have contributed to your project in any way, it is important to give them credit for their work. Write your team members’ or collaborators’ names here along with a link to their GitHub profile.
* **License:** It’s also important to list a license on your README so other developers can understand what they can and cannot do with your project. You can use this guide to help you choose a license.

    
