def create_list():
    game_platform = ["Playstation", "Xbox", "Steam", "iOS", "Google Play"]
    return game_platform

def get_info(my_list):
    first_element = my_list[0]
    second_last_element = my_list[-2]
    list_length = len(my_list)
    first_tuple = (first_element, second_last_element, list_length)
    return first_tuple

def get_partial(my_list):
    new_list = [my_list[1], my_list[2], my_list[3]]
    return new_list

def get_last_three(my_list):
    reversed_list = [my_list[-1], my_list[-2], my_list[-3]]
    
    return reversed_list

def double_list(my_list):
    combined_list = my_list
    combined_list.extend(my_list)
    return combined_list

def amend(my_list):
    newer_list = my_list
    newer_list[1] = "None"
    newer_list.append("Bye")
    return newer_list

print(create_list())
print(get_info(create_list()))
print(get_partial(create_list()))
print(get_last_three(create_list()))
print(double_list(create_list()))
print(amend(create_list()))