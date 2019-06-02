from config import setup


def input_method(total_lines):
    input_list = []
    input_dict = {}
    for i in range(setup.orbit_dict[total_lines] + 1):
        input_list.append(input())

    for line in input_list:
        words = line.split()
        if words[0] == "Weather":
            input_dict[words[0]] = words[2]
        else:
            speed = [int(s) for s in line.split() if s.isdigit()]
            input_dict[words[0]] = speed[0]

    return input_dict
