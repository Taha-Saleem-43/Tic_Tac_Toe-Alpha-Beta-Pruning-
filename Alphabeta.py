# alpha_beta.py
class AlphaBetaPruning:
    def __init__(self):
        self.win_conditions=[
            (0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)
        ]
        self.human_player = 'X'
        self.ai_player = 'O'
        self.evaluated_nodes=0

    def is_terminal(self, state):
        for condition in self.win_conditions:
            if state[condition[0]]==state[condition[1]]==state[condition[2]]!=' ':
                return True
        return ' ' not in state

    def utility(self, state):
        for condition in self.win_conditions:
            if state[condition[0]]==state[condition[1]]==state[condition[2]]!=' ':
                if state[condition[0]]==self.ai_player:
                    return 1
                elif state[condition[0]]==self.human_player:
                    return -1
        return 0

    def heuristic(self, state):
        score = 0
        for condition in self.win_conditions:
            line = [state[condition[0]], state[condition[1]], state[condition[2]]]
            if line.count(self.ai_player)>0 and line.count(self.human_player)==0:
                score += 10**(line.count(self.ai_player)-1)
            elif line.count(self.human_player)>0 and line.count(self.ai_player)==0:
                score -= 10**(line.count(self.human_player)-1)

        forks = 0
        for condition in self.win_conditions:
            line = [state[condition[0]], state[condition[1]], state[condition[2]]]
            if line.count(self.ai_player) == 2 and line.count(' ') == 1:
                forks += 1

        if forks > 1:
            score += 40

        return score

    def alpha_beta_pruning(self, state, depth, maximizing_player, alpha, beta):
        self.evaluated_nodes+=1

        if self.is_terminal(state):
            return self.utility(state)

        if depth == 0:
            return self.heuristic(state)

        if maximizing_player:
            max_eval = float('-inf')
            for i in range(9):
                if state[i] == ' ':
                    state[i] = self.ai_player
                    eval = self.alpha_beta_pruning(state, depth - 1, False, alpha ,beta)
                    state[i] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, max_eval)
                    if beta <= alpha:
                        break
            return max_eval
        else:
            min_eval = float('inf')
            for i in range(9):
                if state[i] == ' ':
                    state[i] = self.human_player
                    eval = self.alpha_beta_pruning(state, depth - 1, True, alpha ,beta)
                    state[i] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta , min_eval)
                    if beta <= alpha:
                        break
            return min_eval

    def best_move(self, state):
        best_score = float('-inf')
        move = -1

        for i in range(9):
            if state[i] == ' ':
                state[i] = self.ai_player
                score = self.alpha_beta_pruning(state, depth=1, maximizing_player=False, alpha=float('-inf'), beta=float('inf'))
                state[i] = ' '
                if score > best_score:
                    best_score = score
                    move = i

        return move
