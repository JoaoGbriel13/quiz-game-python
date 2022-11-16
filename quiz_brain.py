class QuizBrain:
    def __init__(self, q_list):
        self.number = 0
        self.list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.number < len(self.list)

    def next_question(self):
        questao_atual = self.list[self.number]
        self.number += 1
        resposta = input(f"Q.{self.number} - {questao_atual.text} (True or False): ").lower()
        self.check_answer(resposta, questao_atual.answer)

    def check_answer(self, resposta, gabarito):
        if resposta == "t" and gabarito == "True" or resposta == "f" and gabarito == "False":
            self.score += 1
            print(f"Resposta correta")
        else:
            print(f"Resposta incorreta")
        print(f"Sua pontuação atual é de {self.score}/{self.number}")
        print("\n")
