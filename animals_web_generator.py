import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def output_animals(animals):
    output =''
    for animal in animals:
        output += f"Name: {animal['name']}\n"
        output += f"Diet: {animal['characteristics']['diet']}\n"
        if "locations" in animal and len(animal["locations"]) > 0:
            output += f"Location: {animal['locations'][0]}\n"
        if 'characteristics' in animal and 'type' in animal['characteristics']:
            output += f"Type: {animal['characteristics']['type']}\n"
        output += '\n'
    return output


def main():
    animals_data = load_data('animals_data.json')
    print(output_animals(animals_data))
    
     # open and read file
    with open("animals_template.html", "r") as file:
        content = file.read()

    # replace __REPLACE_ANIMALS_INFO__
    content = content.replace("__REPLACE_ANIMALS_INFO__", output_animals(animals_data))

    # write back to file
    with open("animals_template.html", "w") as file:
        file.write(content)


if __name__ == '__main__':
    main()