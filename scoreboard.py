def read_file():
    with open("scores.txt", "r+") as file:
        return file.readlines()

def get_scores():
    scores_list = read_file()
    scores_dict = {}
    for score in scores_list:
        time, player = score.split(" ")
        if player[-1] == "\n":
            player = player[:-1]
        scores_dict.update({time : player})
    return scores_dict
