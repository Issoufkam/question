
from class_app import Question
liste_De_Question = [
   "Qui est le meilleur buteur en 2022\n(a) Paul\n (b) Alpha GT",
   "Qui est le meilleur buteur en 2022\n(a) Paul\n (b) Alpha GT",
   "Qui est le meilleur buteur en 2022\n(a) Paul\n (b) Alpha GT",
   "Qui est le meilleur menteur en 2022\n(a) Paul\n (b) Alpha GT",
   "Qui est le meilleur buteur en 2022\n(a) Paul\n (b) Alpha GT",
]

liste_des_questions_avec_reponse=[
    Question(liste_De_Question[0], 'a'),
    Question(liste_De_Question[1], 'b'),
    Question(liste_De_Question[2], 'b'),
    Question(liste_De_Question[3], 'a'),
    Question(liste_De_Question[4], 'b'),
]

def test(questions):
    name = input("Votre prénoms svp: ")
    score=0
    for question in questions:
        print(question.question)
        reponse = input("Entrez votre reponse: ")
        if reponse == question.reponse:
            score+=1
    if score == 3:
        print(f"{name} votre score est {score}/{len(questions)} Excellent")
    elif score == 2:
        print(f"{name} votre score est {score}/{len(questions)} Bien")
    else:
        print(f"{name} votre score est {score}/{len(questions)} Mauvais")
