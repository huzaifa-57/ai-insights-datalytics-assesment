class AnswerScoring:
    def __init__(self):
        pass

    def rank_answers(self, answers, query):
        ranked_answers = sorted(answers, key=lambda x: self.score(x, query), reverse=True)
        return ranked_answers

    def score(self, answer, query):
        relevance_score = self.calculate_relevance(answer, query)
        numerical_accuracy = self.check_numerical_consistency(answer)
        return relevance_score + numerical_accuracy

    def calculate_relevance(self, answer, query):
        return len(set(query.split()).intersection(set(answer.split())))

    def check_numerical_consistency(self, answer):
        numerical_matches = re.findall(r'\$?\d+(?:,\d{3})*(?:\.\d+)?%', answer)
        return len(numerical_matches)