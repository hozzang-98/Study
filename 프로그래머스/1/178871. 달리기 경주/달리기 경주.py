def solution(players, callings):

    players_dic = {name:idx for idx, name in enumerate(players)}

    for calling in callings:

        before = players_dic[calling]
        players[before], players[before-1] = players[before-1], players[before]

        players_dic[players[before]] = before
        players_dic[players[before-1]] = before-1

    return players