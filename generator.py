from bs4 import BeautifulSoup
import json

GAMES_INDEX = 0
SMALLER_GAMES_INDEX = 1

def process_files():
    with open('template.html', 'r', encoding='utf-8') as file:
        existing_html = file.read()

    soup = BeautifulSoup(existing_html, 'html.parser')
    target_div = soup.find('div', id='gameData')

    game_template = """
    <div class="gridContainer">
        <a href={data_2}><div class="preview" style='background-image: url({data_1});'></div></a>
        <a class="link" href={data_2}><center>{data_0}</center></a>
    </div>
    """

    data_list = []
    json_files = ["data/games.json", "data/smaller_games.json"]

    for file_name in json_files:
        with open(file_name, 'r') as json_file:
            data = json.load(json_file)
            data_list.append(data['data'])

    if target_div:
        for child in target_div.find_all(): 
            child.decompose()

        generated_html = []
        generated_html += get_all_html_from_data_at_index(data_list, GAMES_INDEX, game_template)
        generated_html += get_all_html_from_data_at_index(data_list, SMALLER_GAMES_INDEX, game_template)

        concatenated_html = ''.join(generated_html)

        custom_soup = BeautifulSoup(concatenated_html, 'html.parser')
        target_div.append(custom_soup)

        with open('index.html', 'w', encoding='utf-8') as file:
            file.write(soup.prettify())
    else:
        print("Target div not found in the existing HTML.")

def get_all_html_from_data_at_index(data_list, index, template):
    html_list = []
    for game_idx, game_entry in enumerate(data_list[index]):
        custom_html = template
        for idx, data in enumerate(data_list[index][game_idx]):
            placeholder = f"{{data_{idx}}}"
            custom_html = custom_html.replace(placeholder, json.dumps(data_list[index][game_idx][data], indent=4))
        html_list.append(custom_html)
    return html_list

if __name__ == "__main__":
    process_files()