import json
import requests
from urllib.parse import urljoin

def fetch_song():
    try:
        playlist = {}
        valid = set()
        ranking = requests.get(
            urljoin(info["api"], "/user/record"),
            headers={"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36 Edg/131.0.0.0"},
            cookies={"MUSIC_U": info["MUSIC_U"]},
            params={"uid": info["id"], "type": 1}
        ).json()["weekData"]
        
        for song in ranking:
            percent = int(song["score"])
            playlist[song["song"]["name"]] = percent
            valid.add(percent)
        return (playlist, valid)
    except:
        print("Error fetching song data. Please check your configuration.")
        exit(1)

def calculate(valid):
    count = [sum(100 * num // pred in valid for num in range(1, pred + 1)) for pred in range(1, 101)]
    return count.index(max(count)) + 1

def get_result(playlist, answer):
    table = [100 * num // answer for num in range(1, 101)]
    result = {}
    for name, percent in playlist.items():
        result[name] = table.index(percent) + 1
    return result

if __name__ == "__main__":
    with open('config.json', 'r', encoding='utf-8') as config:
        info = json.load(config)

    playlist, valid = fetch_song()
    answer = calculate(valid)
    result = get_result(playlist, answer)
    for name, count in result.items():
        print(f"{count:>3} {name}")

