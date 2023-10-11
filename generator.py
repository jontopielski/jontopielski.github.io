from bs4 import BeautifulSoup
import re, os, sys, json, markdown, yaml, markdown_it

def inject_game_cards():
    games_html = get_games_list_html('data/games.json', 'templates/large-panel.html')
    smaller_games_html = get_games_list_html('data/smaller_games.json', 'templates/small-panel.html')
    all_games_html = ''.join(games_html + smaller_games_html)
    inject_html_into_file_at_target(all_games_html, 'base.html', 'index.html', 'gameData')
    tools_html = ''.join(get_games_list_html('data/tools.json', 'templates/large-panel.html'))
    inject_html_into_file_at_target(tools_html, 'base.html', 'tools.html', 'gameData')

def inject_blog_links():
    blog_links_html = []
    blog_link_template = get_html_at_file_location('templates/blog-link.html')
    sorted_blog_paths = get_all_blog_paths()
    for blog_path in sorted_blog_paths:
        with open(blog_path, 'r', encoding='utf-8') as file:
            markdown_content = file.readlines()
        yaml_data = get_yaml_object_from_markdown_content(markdown_content)
        next_template = blog_link_template.format(data_0=yaml_data['link'], data_1=yaml_data['title'], data_2=yaml_data['date'])
        blog_links_html.append(next_template)
    blog_links_html = ''.join(blog_links_html)
    inject_html_into_file_at_target(blog_links_html, 'base.html', 'blog.html', 'blogLinks', 'ul')

def create_blog_pages():
    for blog_path in get_all_blog_paths():
        with open(blog_path, 'r', encoding='utf-8') as file:
            markdown_content = file.readlines()
        yaml_data = get_yaml_object_from_markdown_content(markdown_content)
        create_blog_page(blog_path, yaml_data['link'])

def create_blog_page(markdown_file, destination):
    md = markdown_it.MarkdownIt()
    with open(markdown_file, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()
    front_matter_end = md_content.find('---', 1)
    if front_matter_end != -1:
        md_content = md_content[front_matter_end + 3:]  # Skip "---"
    blog_html = md.render(md_content)
    inject_html_into_file_at_target(blog_html, 'base.html', destination, 'blogPost')
    make_links_relative_to_directory_level(destination)

def make_links_relative_to_directory_level(html_file):
    with open(html_file, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
    
    link_elements = soup.find_all('a', href=True) + soup.find_all('link', href=True)
    for link in link_elements:
        href = link['href']
        if not href.startswith('http') and not href.startswith('#'):
            link['href'] = '../' + href
    img_elements = soup.find_all('img', href=False)
    for img in img_elements:
        src = img['src']
        if not href.startswith('http') and not href.startswith('#'):
            img['src'] = '../' + src
    script_elements = soup.find_all('script', href=False)
    for script in script_elements:
        src = script['src']
        if not href.startswith('http') and not href.startswith('#'):
            script['src'] = '../' + src

    with open(html_file, 'w', encoding='utf-8') as file:
        file.write(soup.prettify())

def get_all_blog_paths():
    blog_dirs = []
    for dir_name in os.listdir('posts'):
        for filename in os.listdir(os.path.join('posts', dir_name)):
            if filename.endswith(".md"):
                blog_dirs.append(os.path.join('posts', dir_name, filename))
    return blog_dirs[::-1]

def get_yaml_object_from_markdown_content(markdown_lines):
    if markdown_lines[0].strip() == '---':
        front_matter_end = markdown_lines.index('---\n', 1)
        front_matter_content = ''.join(markdown_lines[1:front_matter_end])
        front_matter = yaml.safe_load(front_matter_content)
    return front_matter

def inject_art_panels():
    art_html = []
    art_template = get_html_at_file_location('templates/art-panel.html')
    for filename in os.listdir('art'):
        file_path = os.path.join('art', filename)
        next_template = art_template.format(data_0=file_path)
        art_html.append(next_template)
    art_html = ''.join(art_html)
    inject_html_into_file_at_target(art_html, 'base.html', 'art.html', 'gameData')

def get_games_list_html(file_location, template_location):
    game_template = get_html_at_file_location(template_location)
    with open(file_location, 'r') as json_file:
        data_list = json.load(json_file)
    return ''.join(get_populated_game_html(data_list, game_template))

def get_populated_game_html(game_data, template):
    games_html = []
    for game_idx, game_entry in enumerate(game_data):
        next_template = template.format(
            data_0=game_data[game_idx]['name'],
            data_1=game_data[game_idx]['image_location'],
            data_2=game_data[game_idx]['link'])
        games_html.append(next_template)
    return games_html

def inject_html_into_file_at_target(inject_html, source, destination, target_id, element_type='div'):
    with open(source, 'r', encoding='utf-8') as file:
        current_html = file.read()
    soup = BeautifulSoup(current_html, 'html.parser')
    target_div = soup.find(element_type, id=target_id)
    if not target_div:
        print("Target div not found in the existing HTML.")
        return
    for child in target_div.find_all(): 
        child.decompose()
    custom_soup = BeautifulSoup(inject_html, 'html.parser')
    target_div.append(custom_soup)
    with open(destination, 'w', encoding='utf-8') as file:
        file.write(soup.prettify())

def get_html_at_file_location(file_location):
    with open(file_location, 'r', encoding='utf-8') as file:
        return file.read()

def inject_footers():
    footer_html = get_html_at_file_location('templates/footer.html')
    inject_html_into_file_at_target(footer_html, 'index.html', 'index.html', 'footer')
    inject_html_into_file_at_target(footer_html, 'about.html', 'about.html', 'footer')

def inject_headers():
    header_html = get_html_at_file_location('templates/header.html')
    inject_html_into_file_at_target(header_html, 'index.html', 'index.html', 'header')
    inject_html_into_file_at_target(header_html, 'about.html', 'about.html', 'header')

def clean_generated_files():
    generated_pages = ['art.html', 'blog.html', 'tools.html', 'index.html']
    for page in generated_pages:
        os.remove(page)
    
    os.chdir('blog')
    for file in os.listdir():
        os.remove(file)

if __name__ == "__main__":
    if '--clean' in sys.argv:
        clean_generated_files()
    else:
        inject_game_cards()
        inject_art_panels()
        inject_blog_links()
        create_blog_pages()