#!/usr/bin/env python3

import requests
import json

URL = "https://resultados.tse.jus.br/oficial/ele2022/545/dados-simplificados/br/br-c0001-e000545-r.json"

def get_votes():
    data = requests.get(URL)
    json_data = json.loads(data.content)
    return_string = ""

    for index in range(0, 2):
        return_string += f"{json_data['cand'][index]['nm']}: " + f"{json_data['cand'][index]['pvap']}%"
        if index != 1:
            return_string += "\n"

    return return_string

def get_sessions():
    data = requests.get(URL)
    json_data = json.loads(data.content)

    return json_data["pst"]


if __name__ == "__main__":
    # print(get_sessions())
    # print(get_votes())
    ...
    