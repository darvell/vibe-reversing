#!/usr/bin/env python3
"""
Static blog generator for vibe-reversing
Generates HTML pages from markdown files in the notes/ directory
"""

import os
import re
import markdown
from datetime import datetime
from pathlib import Path
import shutil

# Configuration
NOTES_DIR = "notes"
OUTPUT_DIR = "docs"
TEMPLATES_DIR = "templates"
CSS_DIR = "css"

def read_template(template_name):
    """Read a template file"""
    template_path = os.path.join(TEMPLATES_DIR, template_name)
    with open(template_path, 'r', encoding='utf-8') as f:
        return f.read()

def parse_markdown_file(filepath):
    """Parse markdown file and extract metadata and content"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract title from first # heading or filename
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if title_match:
        title = title_match.group(1)
        # Remove the title from content to avoid duplication
        content = re.sub(r'^#\s+.+$', '', content, count=1, flags=re.MULTILINE).lstrip()
    else:
        title = Path(filepath).stem.replace('-', ' ').replace('_', ' ').title()
    
    # Get file modification time
    mtime = os.path.getmtime(filepath)
    date = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d')
    
    # Convert markdown to HTML
    md = markdown.Markdown(extensions=['fenced_code', 'codehilite', 'tables', 'toc'])
    html_content = md.convert(content)
    
    return {
        'title': title,
        'date': date,
        'content': html_content,
        'filename': Path(filepath).stem,
        'filepath': filepath
    }

def generate_post_page(post_data, template):
    """Generate HTML page for a single post"""
    html = template.replace('{{TITLE}}', post_data['title'])
    html = html.replace('{{DATE}}', post_data['date'])
    html = html.replace('{{CONTENT}}', post_data['content'])
    return html

def generate_index_page(posts, template):
    """Generate index page with list of all posts"""
    # Sort posts by date (newest first)
    posts_sorted = sorted(posts, key=lambda x: x['date'], reverse=True)
    
    # Generate post list HTML
    post_list_html = ""
    for post in posts_sorted:
        post_list_html += f'''
        <div class="post-item">
            <h2><a href="{post['filename']}.html">{post['title']}</a></h2>
            <p class="date">{post['date']}</p>
        </div>
        '''
    
    html = template.replace('{{POST_LIST}}', post_list_html)
    html = html.replace('{{TITLE}}', 'Vibe Reversing - Reverse Engineering Notes')
    return html

def copy_static_files():
    """Copy CSS and other static files to output directory"""
    # Copy CSS files
    if os.path.exists(CSS_DIR):
        css_output = os.path.join(OUTPUT_DIR, 'css')
        os.makedirs(css_output, exist_ok=True)
        for css_file in os.listdir(CSS_DIR):
            if css_file.endswith('.css'):
                shutil.copy(
                    os.path.join(CSS_DIR, css_file),
                    os.path.join(css_output, css_file)
                )

def main():
    """Main generator function"""
    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Read templates
    post_template = read_template('post.html')
    index_template = read_template('index.html')
    
    # Parse all markdown files
    posts = []
    if os.path.exists(NOTES_DIR):
        for filename in os.listdir(NOTES_DIR):
            if filename.endswith('.md'):
                filepath = os.path.join(NOTES_DIR, filename)
                post_data = parse_markdown_file(filepath)
                posts.append(post_data)
                
                # Generate individual post page
                post_html = generate_post_page(post_data, post_template)
                output_path = os.path.join(OUTPUT_DIR, f"{post_data['filename']}.html")
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(post_html)
                print(f"Generated: {output_path}")
    
    # Generate index page
    index_html = generate_index_page(posts, index_template)
    index_path = os.path.join(OUTPUT_DIR, 'index.html')
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_html)
    print(f"Generated: {index_path}")
    
    # Copy static files
    copy_static_files()
    
    print(f"\nBlog generated successfully!")
    print(f"Total posts: {len(posts)}")
    print(f"Output directory: {OUTPUT_DIR}/")

if __name__ == '__main__':
    main()
