with open(".\\Input\\Names\\invited_names.txt", mode="r") as names_file:
    raw_list = names_file.readlines()
    name_list = []
    for name in raw_list:
        cleaned_name = name.rstrip("\n")
        name_list.append(cleaned_name)
    with open(".\\Input\\Letters\\starting_letter.txt") as template:
        text = template.read()
    for name in name_list:
        final_text = text.replace("[name]", f"{name}")
        file_path = f".\\Output\\{name}.letter"
        with open(file_path, "w") as file:
            file.write(f"{final_text}")
