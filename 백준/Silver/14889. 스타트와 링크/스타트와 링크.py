from itertools import combinations


def main():

    min_score = float('inf')

    members = list(range(N))
    team_combinations = list(combinations(members, N//2))

    for team in team_combinations:
        start_team = team
        link_team = []
        for member in members:
            if member not in start_team:
                link_team.append(member)

        start_score = calculate_team_score(start_team)
        link_score = calculate_team_score(link_team)

        min_score = min(min_score, abs(start_score - link_score))

        if min_score == 0:
            print(min_score)
            return
    print(min_score)

def calculate_team_score(team):
    score = 0
    for i in range(len(team)):
        for j in range(i+1, len(team)):
            score += team_scores[team[i]][team[j]] + team_scores[team[j]][team[i]]

    return score



if __name__ == '__main__':
    N = int(input())  # N은 짝수
    team_scores = [list(map(int, input().split())) for _ in range(N)]
    main()
