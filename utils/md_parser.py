def extract_text_from_md(file) -> str:
    """Extract plain text from a Markdown file."""
    try:
        content = file.read().decode("utf-8")
        return content
    except Exception as e:
        return f"Error reading markdown file: {str(e)}"