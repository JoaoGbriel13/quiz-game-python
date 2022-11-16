import requests

question_data = [
]
acesso = requests.get("https://opentdb.com/api.php?amount=10&category=21&type=boolean")
dados = acesso.json()
resultado = dados["results"]

for pergunta in resultado:
    newDict = {"text": pergunta["question"], "answer": pergunta["correct_answer"]}
    question_data.append(newDict)

