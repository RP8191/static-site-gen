import os
import shutil
from pathlib import Path
import markdown
import frontmatter
from jinja2 import Environment, FileSystemLoader

class StaticSiteGenerator:
    def __init__(self, content_dir="content", local_output_dir="C:\\static-site-gen\\output", 
                 github_output_dir="docs", template_dir="templates", base_url=""):
        self.content_dir = Path(content_dir)
        self.local_output_dir = Path(local_output_dir)
        self.github_output_dir = Path(github_output_dir)
        self.template_dir = Path(template_dir)
        self.base_url = base_url.rstrip('/')  # Remove trailing slash if present
        
        # Initialize Jinja2 environment with base_url global
        self.env = Environment(loader=FileSystemLoader(self.template_dir))
        self.env.globals['base_url'] = self.base_url
        
        # Create necessary directories
        self.local_output_dir.mkdir(exist_ok=True, parents=True)
        self.github_output_dir.mkdir(exist_ok=True, parents=True)
        self.content_dir.mkdir(exist_ok=True)
        self.template_dir.mkdir(exist_ok=True)
        
        # Configure Markdown
        self.md = markdown.Markdown(extensions=['meta', 'fenced_code', 'codehilite'])

    def clear_output(self, output_dir):
        """Clear the output directory"""
        if output_dir.exists():
            shutil.rmtree(output_dir)
        output_dir.mkdir(parents=True)

    def copy_static_files(self, output_dir):
        """Copy static files to output directory"""
        static_dir = Path("static")
        if static_dir.exists():
            output_static = output_dir / "static"
            if output_static.exists():
                shutil.rmtree(output_static)
            shutil.copytree(static_dir, output_static)

    def generate_page(self, markdown_file, output_dir):
        """Generate a single page from a markdown file"""
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

    def generate_site(self, output_dir):
        """Generate the static site in the specified output directory"""
        self.clear_output(output_dir)
        self.copy_static_files(output_dir)
        
        # Process all markdown files
        markdown_files = list(self.content_dir.glob('**/*.md'))
        pages = []
        
        for md_file in markdown_files:
            output_path = self.generate_page(md_file, output_dir)
            # Get the title from the frontmatter
            post = frontmatter.load(md_file)
            title = post.get('title', output_path.stem.replace('_', ' ').title())
            
            # Create URL with base_url
            relative_url = str(output_path.relative_to(output_dir)).replace('\\', '/')
            full_url = f"{self.base_url}/{relative_url}"
            
            pages.append({
                'path': output_path,
                'url': full_url,
                'title': title
            })
        
        # Generate index page if it doesn't exist
        if not (output_dir / 'index.html').exists():
            template = self.env.get_template('index.html')
            index_content = template.render(pages=pages)
            (output_dir / 'index.html').write_text(index_content)

if __name__ == '__main__':
    # For GitHub Pages, set this to your repository name
    # e.g., "/static-site-gen" for https://username.github.io/static-site-gen/
    # or "" for https://username.github.io/
    base_url = os.getenv('SITE_BASE_URL', '')
    
    # If no base_url is set, try to get it from the current directory name
    if not base_url and os.path.exists('.git'):
        try:
            import subprocess
            # Get the remote URL
            remote_url = subprocess.check_output(['git', 'config', '--get', 'remote.origin.url']).decode().strip()
            # Extract repository name
            repo_name = remote_url.split('/')[-1].replace('.git', '')
            if repo_name != 'username.github.io':  # Only add base_url if not using the main GitHub Pages domain
                base_url = f'/{repo_name}'
        except:
            pass
    
    generator = StaticSiteGenerator(base_url=base_url)
    
    # Generate both local and GitHub Pages versions
    print("Generating local version...")
    generator.generate_site(generator.local_output_dir)
    
    print("Generating GitHub Pages version...")
    generator.generate_site(generator.github_output_dir)
    
    print(f"\nGitHub Pages URL will be: https://username.github.io{base_url}/") 