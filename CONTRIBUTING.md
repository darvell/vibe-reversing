# Contributing to Vibe Reversing

Thank you for your interest in contributing reverse engineering notes to this project!

## How to Add a New Note

1. **Create a Markdown File**
   
   Add a new `.md` file to the `notes/` directory with a descriptive filename:
   ```bash
   notes/my-binary-analysis.md
   ```

2. **Write Your Analysis**
   
   Start your file with a level-1 heading (`#`) which will be used as the title:
   ```markdown
   # My Binary Analysis - Descriptive Title
   
   Your content here...
   ```

3. **Use Standard Markdown**
   
   The generator supports:
   - **Headings** (`##`, `###`, etc.)
   - **Code blocks** with syntax highlighting:
     ````markdown
     ```c
     int main() {
         return 0;
     }
     ```
     ````
   - **Tables**
   - **Lists** (ordered and unordered)
   - **Links** and **images**
   - **Inline code** with backticks

4. **Test Locally** (Optional)
   
   ```bash
   ./build.sh
   # Open docs/index.html in your browser
   ```

5. **Commit and Push**
   
   ```bash
   git add notes/my-binary-analysis.md
   git commit -m "Add analysis of XYZ binary"
   git push
   ```

   The site will automatically rebuild and deploy via GitHub Actions.

## Note Structure Guidelines

### Recommended Sections

A well-structured reverse engineering note typically includes:

```markdown
# Binary Name - Short Description

Brief overview of what this binary does or what you're analyzing.

## Binary Information

- File type
- Architecture
- Security features
- Size, etc.

## Analysis

### Key Findings

Important discoveries...

### Code Analysis

Detailed examination of the code...

## Security Observations

Any vulnerabilities or security-relevant findings...

## Conclusion

Summary of your analysis...
```

### Best Practices

- **Clear titles**: Use descriptive titles that indicate what binary you analyzed
- **Code formatting**: Use proper syntax highlighting for code blocks (```asm, ```c, ```python, etc.)
- **Screenshots**: While markdown doesn't support embedded images by default in this setup, you can link to images hosted elsewhere
- **Links**: Link to relevant resources, tools, or documentation
- **Date**: The file modification date is used automatically; no need to add it manually

## Questions?

If you have questions or need help, feel free to open an issue!
