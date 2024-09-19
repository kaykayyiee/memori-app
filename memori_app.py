from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('The state language of Brazil', 'Portugese', 'English', 'Spanish', 'Brazilian'))
question_list.append(Question('which color does not appear on the american flag?', 'Green', 'Red', 'white', 'Blue'))
question_list.append(Question('A tradisional residence pf the Yakult people', 'Urasa', 'Yurt', 'Igloo', 'Hut'))


app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memori')
main_win.resize(4000, 2000)

question = QLabel('Guess the wrong char')
answer = QPushButton('Answer')

RadioGroupBox = QGroupBox('Answer')
btn_ans1 = QRadioButton('Basket')
btn_ans2 = QRadioButton('Soccer')
btn_ans3 = QRadioButton('Volly')
btn_ans4 = QRadioButton('Tennnis')

layout_ansmain = QHBoxLayout()
layout_ans1 = QHBoxLayout()
layout_ans2 = QHBoxLayout()

RadioGroup = QButtonGroup()
RadioGroup.addButton(btn_ans1)
RadioGroup.addButton(btn_ans2)
RadioGroup.addButton(btn_ans3)
RadioGroup.addButton(btn_ans4)

layout_ans1.addWidget(btn_ans1)
layout_ans1.addWidget(btn_ans2)
layout_ans2.addWidget(btn_ans3)
layout_ans2.addWidget(btn_ans4)

layout_ansmain.addLayout(layout_ans1)
layout_ansmain.addLayout(layout_ans2)
RadioGroupBox.setLayout(layout_ansmain)


# Create a results panel
AnsGroupBox = QGroupBox("Test result")
lb_Result = QLabel('Are you correct or not?') # “Correct” or “Incorrect” text will be here
lb_Correct = QLabel('the answer will be here!') # correct answer text will be written here  

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout() # question
layout_line2 = QHBoxLayout() # answer option or test result
layout_line3 = QHBoxLayout() # 'answer' button

layout_line1.addWidget(question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()
layout_line3.addStretch(1)
layout_line3.addWidget(answer, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    answer.setText('Next Question')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    answer.setText('Answer')
    RadioGroup.setExclusive(False)
    btn_ans1.setChecked(False)
    btn_ans2.setChecked(False)
    btn_ans3.setChecked(False)
    btn_ans4.setChecked(False)
    RadioGroup.setExclusive(True)

def test():
    if 'Answer' == answer.text():
        show_result()
    else:
        show_question 
answers = [btn_ans1, btn_ans2, btn_ans3, btn_ans4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_Correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_Correct('Correct!')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_Correct('Incorrect!')

def next_question():
    main_win.cur_question = main_win.cur_question + 1
    if main_win.cur_question >= len(question_list):
        main_win.cur_question = 0 
    q = question_list[main_win.cur_question]
    ask(q)

def click_OK():
    if answer.text() == 'Answer':
        check_answer()
    else:
        next_question()


main_win.setLayout(layout_card)
main_win.cur_question = -1
answer.clicked.connect(click_OK)
next_question()
main_win.show()
app.exec()