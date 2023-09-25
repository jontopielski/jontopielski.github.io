from bs4 import BeautifulSoup
import json

def inject_game_cards():
    games_data = get_games_list_html('data/games.json')
    smaller_games_data = get_games_list_html('data/smaller_games.json')
    tool_data = get_games_list_html('data/tools.json')
    all_game_data = ''.join(games_data + smaller_games_data + tool_data)
    inject_html_into_file_at_target(all_game_data, 'base.html', 'index.html', 'gameData')

def get_games_list_html(file_location):
    game_template = get_html_at_file_location('templates/game_panel.html')
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

def inject_html_into_file_at_target(inject_html, source, destination, target_id):
    with open(source, 'r', encoding='utf-8') as file:
        current_html = file.read()

    soup = BeautifulSoup(current_html, 'html.parser')
    target_div = soup.find('div', id=target_id)

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

if __name__ == "__main__":
    inject_game_cards()