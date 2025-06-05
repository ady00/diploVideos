import os
import re

youtube_links = {
    "AustriaOne": "https://youtu.be/1GdJbd26hi4",
    "GermanyOne": "https://youtu.be/qhwbHH_gUs4",
    "EnglandOne": "https://youtu.be/jqk5l3U-cc4",
    "RussiaOne": "https://youtu.be/jNoGhQ5nLrA",
    "TurkeyOne": "https://youtu.be/06IBczNjSIk",
    "ItalyOne": "https://youtu.be/HExNim2Ul0A",
    "FranceOne": "https://youtu.be/dq3snNoYsW4",

    "AustriaTwo": "https://youtu.be/4_ZUQ8ubLbA",
    "GermanyTwo": "https://youtu.be/oB5Kzyfu8HI",
    "EnglandTwo": "https://youtu.be/raX6cwcXlEw",
    "RussiaTwo": "https://youtu.be/Q9Sz4QQyMbU",
    "TurkeyTwo": "https://youtu.be/cAVE50D0GzA",
    "FranceTwo": "https://youtu.be/spQUhGkpQX0",

    "ItalyTwoThree": "https://youtu.be/MNy-c2htXc4",  # ItalyTwo + Three combined


    "AustriaThree": "https://youtu.be/odQFHxp1Zws",
    "EnglandThree": "https://youtu.be/054pYZjdZqA",
    "RussiaThree": "https://youtu.be/oEszmA7adkk",
    "FranceThree": "https://youtu.be/2weX8lRc40g",

    "AustriaFinale": "https://youtu.be/ZXcoXVQ49-E",
    "EnglandFinale": "https://youtu.be/244jX6K7hoY",
    "RussiaFinale": "https://youtu.be/bJMx6nhkooQ",
    "ItalyFinale": "https://youtu.be/FqwHKVDJN3I",
    "FranceFinale": "https://youtu.be/KeD9xHfepdk"
}

def format_youtube_link(url, timestamp):
    minutes, seconds = map(int, timestamp.split(":"))
    return f"{url}?t={minutes}m{seconds}s"

def search_keywords_in_transcripts(keywords, directory="."):
    keywords = [kw.lower() for kw in keywords]
    results = []

    suffix_priority = ['One.txt', 'Two.txt', 'Three.txt', 'Finale.txt']

    def file_sort_key(name):
        for i, suffix in enumerate(suffix_priority):
            if name.endswith(suffix):
                return i
        return len(suffix_priority)

    filenames = sorted(
        [f for f in os.listdir(directory) if f.endswith(".txt")],
        key=file_sort_key
    )

    for filename in filenames:
        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as file:
            lines = file.readlines()

        current_timestamp = None
        for line in lines:
            stripped_line = line.strip()
            timestamp_match = re.match(r'^(\d{1,2}:\d{2})$', stripped_line)
            if timestamp_match:
                current_timestamp = timestamp_match.group(1)
            else:
                line_lower = stripped_line.lower()
                for keyword in keywords:
                    if keyword in line_lower and current_timestamp:
                        base_name = filename.replace('.txt', '')
                        video_url = youtube_links.get(base_name)
                        if video_url:
                            timestamp_url = format_youtube_link(video_url, current_timestamp)
                            results.append(f"{base_name} – {current_timestamp} – {stripped_line} – {timestamp_url}")
                        else:
                            results.append(f"{base_name} – {current_timestamp} – {stripped_line} – [No video link]")
                        break  # only 1 per line

    return results

keywords_to_search = ["russia", "Russia"] # change these to whatever you want :D

advay_search = [
    "Odde ", "odde ", "ODDE ",
    "Audrey", "audrey", "AUDREY",
    "Obbe", "obbe", "OBBE",
    "Odday ", "odday ", "ODDAY ",
    " Abe ", " abe ", " ABE ",
    "Agbe ", "agbe ", "AGBE ",
    "Augbe ", "augbe ", "AUGBE ",
    "Adve ", "adve ", "ADVE ",
    "Advay", "advay", "ADVAY"
    "Adv ", "adv ", "ADV "

]

slime_search = ["slime", "Slime", "SLIME", " slimy ", "Slimy", "SLIMY", "devil"] # why am i like 90% of these (skull emoji)

matches = search_keywords_in_transcripts(keywords_to_search)

print(f"\n\n\n\nAll variations of the keywords '{keywords_to_search[0]}' found in transcripts:\n\n")
for match in matches:
    print(match)
