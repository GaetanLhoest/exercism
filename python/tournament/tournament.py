import string


TITLE_BAR = 'Team                           | MP |  W |  D |  L |  P'
empty_score_dict = {
    "match_played": 0,
    "win": 0,
    "draw": 0,
    "loose": 0,
    "points": 0
}


def add_win(team_score: dict):
    team_score["match_played"] = team_score["match_played"] + 1
    team_score["win"] = team_score["win"] + 1
    team_score["points"] = team_score["points"] + 3
    return team_score


def add_loss(team_score: dict):
    team_score["match_played"] = team_score["match_played"] + 1
    team_score["loose"] = team_score["loose"] + 1
    return team_score


def add_draw(team_score: dict):
    team_score["match_played"] = team_score["match_played"] + 1
    team_score["draw"] = team_score["draw"] + 1
    team_score["points"] = team_score["points"] + 1
    return team_score


def tally(rows):
    tally = {}
    for row in rows:
        res = row.split(';')
        firs_team_name = res[0]
        second_team_name = res[1]
        match_result = res[2]
        if match_result == 'win':
            tally[firs_team_name] = add_win(tally.get(
                firs_team_name, empty_score_dict.copy()))
            tally[second_team_name] = add_loss(tally.get(
                second_team_name, empty_score_dict.copy()))
        elif match_result == 'draw':
            tally[firs_team_name] = add_draw(tally.get(
                firs_team_name, empty_score_dict.copy()))
            tally[second_team_name] = add_draw(tally.get(
                second_team_name, empty_score_dict.copy()))
        elif match_result == 'loss':
            tally[firs_team_name] = add_loss(tally.get(
                firs_team_name, empty_score_dict.copy()))
            tally[second_team_name] = add_win(tally.get(
                second_team_name, empty_score_dict.copy()))
    sorted_tally = sorted(list(tally.items()), key=lambda k: (k[1]["points"], k[0].lower().translate(
        str.maketrans(string.ascii_lowercase, string.ascii_lowercase[::-1]))), reverse=True)

    tally_array = [f'{key:30} | {value["match_played"]:2} | {value["win"]:2} | {value["draw"]:2} | {value["loose"]:2} | {value["points"]:2}' for key,
                   value in sorted_tally]
    tally_array.insert(0, TITLE_BAR)
    return tally_array
