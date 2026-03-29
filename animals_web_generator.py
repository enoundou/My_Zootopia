import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def serialize_animal(animal_obj) :
    # append information to each string
    output_obj =''
    output_obj += '<li class="cards__item">\n'
    output_obj += f'<div class="card__title">{animal_obj["name"]}</div>\n'
    output_obj += '<div class="card__text">'
    output_obj += '<ul>'
    if 'characteristics' in animal_obj and 'diet' in animal_obj['characteristics']:
        output_obj += f"<li><strong>Diet:</strong> {animal_obj['characteristics']['diet']}</li>\n"
    if "taxonomy" in animal_obj :
        if "kingdom" in animal_obj["taxonomy"]:
            output_obj += f"<li><strong>Kingdom:</strong> {animal_obj["taxonomy"]['kingdom']}</li>\n"
        if "scientific_name" in animal_obj["taxonomy"]:
            output_obj += f"<li><strong>Scientific name:</strong> {animal_obj["taxonomy"]['scientific_name']}</li>\n"
    if "locations" in animal_obj and len(animal_obj["locations"]) > 0:
        output_obj += f"<li><strong>Location:</strong> {animal_obj['locations'][0]}</li>\n"
    if 'characteristics' in animal_obj :
        if'type' in animal_obj['characteristics']:
            output_obj += f"<li><strong>Type:</strong> {animal_obj['characteristics']['type']}</li>\n"
        if'group' in animal_obj['characteristics']:
            output_obj += f"<li><strong>Group:</strong> {animal_obj['characteristics']['group']}</li>\n"
        if'skin_type' in animal_obj['characteristics']:
            output_obj += f"<li><strong>Skin type:</strong> {animal_obj['characteristics']['skin_type']}</li>\n"
    output_obj += '</ul>'
    output_obj += '</div>'
    output_obj += '</li>'

    return output_obj


def main():
    data = load_data('animals_data.json')
    output = ''
    for animal_obj in data:
        output += serialize_animal(animal_obj)

     # open and read file
    with open("animals_template.html", "r") as file:
        content = file.read()

    # replace __REPLACE_ANIMALS_INFO__
    content = content.replace("__REPLACE_ANIMALS_INFO__", output)

    # write back to file
    with open("animals_template.html", "w") as file:
        file.write(content)


if __name__ == '__main__':
    main()