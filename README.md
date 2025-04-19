# Static Site Generator

A Python-based static site generator that converts Markdown files to HTML websites. This project supports both local development and GitHub Pages deployment.

## Features

- Converts Markdown files to HTML
- Supports YAML frontmatter for metadata
- Uses Jinja2 templates for consistent styling
- Generates both local and GitHub Pages versions
- Supports code syntax highlighting
- Handles static assets

## Requirements

- Python 3.x
- Required packages (see requirements.txt)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/static-site-gen.git
cd static-site-gen
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Place your Markdown files in the `content/` directory
2. Add templates in the `templates/` directory
3. Add static assets in the `static/` directory
4. Run the generator:
```bash
python static_site_generator.py
```

The script will generate:
- Local version in `C:\static-site-gen\output\`
- GitHub Pages version in the `docs/` directory

## Project Structure

```
static-site-gen/
├── content/          # Markdown content files
├── templates/        # Jinja2 templates
├── static/          # Static assets
├── docs/            # GitHub Pages output
├── static_site_generator.py
└── requirements.txt
```

## GitHub Pages Setup

1. Enable GitHub Pages in your repository settings
2. Set the source to the `docs/` folder
3. Set the `SITE_BASE_URL` environment variable to your repository name (if needed)

## License

MIT License 