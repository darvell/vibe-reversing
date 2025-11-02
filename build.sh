#!/bin/bash
# Simple build script for vibe-reversing blog generator

echo "🔨 Building vibe-reversing blog..."
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed"
    exit 1
fi

# Install dependencies if needed
if ! python3 -c "import markdown" 2>/dev/null; then
    echo "📦 Installing dependencies..."
    pip install -r requirements.txt
fi

# Generate the site
echo "⚙️  Generating static site..."
python3 generate.py

echo ""
echo "✅ Build complete!"
echo "📂 Output directory: docs/"
echo "🌐 Open docs/index.html in your browser to preview"
