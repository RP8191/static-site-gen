import os
import shutil
from pathlib import Path
import markdown
import frontmatter
from jinja2 import Environment, FileSystemLoader

class StaticSiteGenerator:
    def __init__(self, content_dir="content", output_dir="output", template_dir="templates", base_url=""):
        self.content_dir = Path(content_dir)
        self.output_dir = Path(output_dir)
        self.template_dir = Path(template_dir)
        self.base_url = base_url.rstrip('/')  # Remove trailing slash if present
        
        # Initialize Jinja2 environment with base_url global
        self.env = Environment(loader=FileSystemLoader(self.template_dir))
        self.env.globals['base_url'] = self.base_url
        
        # Create necessary directories
        self.output_dir.mkdir(exist_ok=True, parents=True)
        self.content_dir.mkdir(exist_ok=True)
        self.template_dir.mkdir(exist_ok=True)
        
        # Configure Markdown
        self.md = markdown.Markdown(extensions=['meta', 'fenced_code', 'codehilite'])

    def clear_output(self, output_dir):
        """Clear the output directory"""
        print(f"Clearing output directory: {output_dir}")
        if output_dir.exists():
            shutil.rmtree(output_dir)
        output_dir.mkdir(parents=True)

    def copy_static_files(self, output_dir):
        """Copy static files to output directory"""
        print(f"Copying static files to {output_dir}")
        static_dir = Path("static")
        if static_dir.exists():
            output_static = output_dir / "static"
            if output_static.exists():
                shutil.rmtree(output_static)
            shutil.copytree(static_dir, output_static)

    def generate_page(self, markdown_file, output_dir):
        """Generate a single page from a markdown file"""
        print(f"Generating page from {markdown_file}")
        # Read the markdown file with frontmatter
        post = frontmatter.load(markdown_file)
        
        # Convert markdown to HTML
        html_content = self.md.convert(post.content)
        
        # Get template
        template_name = post.get('template', 'page.html')
        template = self.env.get_template(template_name)
        
        # Render the template
        rendered = template.render(
            content=html_content,
            title=post.get('title', 'Untitled'),
            **post.metadata
        )
        
        # Determine output path
        rel_path = markdown_file.relative_to(self.content_dir)
        output_path = output_dir / rel_path.with_suffix('.html')
        
        # Create parent directories if they don't exist
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Write the file
        output_path.write_text(rendered)
        return output_path

    def generate_site(self):
        """Generate the static site"""
        print(f"Generating site in {self.output_dir}")
        self.clear_output(self.output_dir)
        self.copy_static_files(self.output_dir)
        
        # Process all markdown files
        markdown_files = list(self.content_dir.glob('**/*.md'))
        print(f"Found {len(markdown_files)} markdown files")
        pages = []
        
        for md_file in markdown_files:
            print(f"Processing {md_file}")
            output_path = self.generate_page(md_file, self.output_dir)
            # Get the title from the frontmatter
            post = frontmatter.load(md_file)
            title = post.get('title', output_path.stem.replace('_', ' ').title())
            
            # Create URL with base_url
            relative_url = str(output_path.relative_to(self.output_dir)).replace('\\', '/')
            full_url = f"{self.base_url}/{relative_url}"
            
            pages.append({
                'path': output_path,
                'url': full_url,
                'title': title
            })
        
        # Generate index page
        print("Generating index page...")
        template = self.env.get_template('index.html')
        index_content = template.render(pages=pages, base_url=self.base_url)
        index_path = self.output_dir / 'index.html'
        print(f"Writing index.html to {index_path}")
        index_path.write_text(index_content)
        print("Site generation complete!")

if __name__ == '__main__':
    # For local testing
    base_url = os.getenv('SITE_BASE_URL', '')
    generator = StaticSiteGenerator(base_url=base_url)
    generator.generate_site() 