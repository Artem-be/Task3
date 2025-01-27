from pprint import pprint
import random
import math

TIMESTAMPS_COUNT = 50000

PROBABILITY_SCORE_CHANGED = 0.0001

PROBABILITY_HOME_SCORE = 0.45

OFFSET_MAX_STEP = 3

INITIAL_STAMP = {
    "offset": 0,
    "score": {
        "home": 0,
        "away": 0
    }
}


def generate_stamp(previous_value):
    score_changed = random.random() > 1 - PROBABILITY_SCORE_CHANGED
    home_score_change = 1 if score_changed and random.random() > 1 - \
        PROBABILITY_HOME_SCORE else 0
    away_score_change = 1 if score_changed and not home_score_change else 0
    offset_change = math.floor(random.random() * OFFSET_MAX_STEP) + 1

    return {
        "offset": previous_value["offset"] + offset_change,
        "score": {
            "home": previous_value["score"]["home"] + home_score_change,
            "away": previous_value["score"]["away"] + away_score_change
        }
    }


def generate_game():
    stamps = [INITIAL_STAMP, ]
    current_stamp = INITIAL_STAMP
    for _ in range(TIMESTAMPS_COUNT):
        current_stamp = generate_stamp(current_stamp)
        stamps.append(current_stamp)

    return stamps


game_stamps = generate_game()

pprint(game_stamps)


def get_score(game_stamps, offset):
    if offset == 0:
        score_dict = INITIAL_STAMP.get('score', {})
        return {"away": score_dict.get('away'), "home": score_dict.get('home')}

    if offset >= game_stamps[-1].get('offset'):
        last_score = game_stamps[-1].get('score')
        return {"away": last_score.get('away'), "home": last_score.get('home')}

    start_index = offset // OFFSET_MAX_STEP
    closest_score = None
    closest_offset = None

    for index_search in range(start_index, len(game_stamps)):
        offset_value = game_stamps[index_search].get('offset')

        if offset_value == offset:
            score_dict = game_stamps[index_search].get('score', {})
            return {"away": score_dict.get('away'), "home": score_dict.get('home')}

        if offset_value < offset:
            if closest_offset is None or offset_value > closest_offset:
                closest_offset = offset_value
                closest_score = game_stamps[index_search].get('score', {})

        if offset_value > offset:
            break

    if closest_score is not None:
        print(f"Метка времени {offset} не найдена. Ближайшая метка: {closest_offset}")
        return {"away": closest_score.get('away'), "home": closest_score.get('home')}

offset = int(input("Введите положительное натуральное число до 150 000: "))

score = get_score(game_stamps, offset)

pprint(score)