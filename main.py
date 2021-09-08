from os import listdir


def file_str_count(file: str) -> int:
    return sum(1 for line in open(file, 'r'))


def sort_dict(dict: dict) -> dict:
    sorted_dict = {}
    processed_keys = []
    for value in sorted(dict.values()):
        for key in dict.keys():
            if key not in processed_keys and dict[key] == value:
                sorted_dict[key] = value
                processed_keys.append(key)
    return sorted_dict


def files_union(files: list) -> object:
    files_dict = {}
    for file in files:
        files_dict[file] = file_str_count(file)
    for key, value in sort_dict(files_dict).items():
        with open(key) as reading_file:
            text = reading_file.read()
        with open("result.txt", "a") as result_file:
            result_file.write(key + "\n")
            result_file.write(str(value) + "\n")
            result_file.write(text + "\n")


files_list = []
for file in listdir("files/"):
    files_list.append(f"files/{file}")

files_union(files_list)
