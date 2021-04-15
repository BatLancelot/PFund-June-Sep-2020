player_cards = input().split()
team_max_players = 11
max_players_sent_off = 4

sent_off_a_team = []
sent_off_b_team = []
individual_card = []

for _ in player_cards:
    individual_card = _.split('-')
    if 'A' in individual_card:
        if individual_card in sent_off_a_team:
            continue
        else:
            sent_off_a_team.append(individual_card)
    else:
        if individual_card in sent_off_b_team:
            continue
        else:
            sent_off_b_team.append(individual_card)

print(f"Team A - {team_max_players - len(sent_off_a_team)}; Team B - {team_max_players - len(sent_off_b_team)}")

if len(sent_off_a_team) > max_players_sent_off or len(sent_off_b_team) > max_players_sent_off:
    print('Game was terminated')
