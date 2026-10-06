import streamlit as st
import random

questions = [
    {
        "question": "AI technology has made great ( ) lately.",
        "answer": "progress"
    },
    {
        "question": "( ) software also uses AI technology.",
        "answer": "translation"
    },
    {
        "question": "Smartphones which ( ) to voice commands are common these days.",
        "answer": "respond"
    },
    {
        "question": "In the near ( ), AI will help us communicate with people all over the world quite easily.",
        "answer": "future"
    },
    {
        "question": "For example, internet search engines use AI ( ).",
        "answer": "technology"
    },
    {
        "question": "It can come ( ) with the best translation by using AI technology.",
        "answer": "up"
    },
    {
        "question": "Robots ( ) automatically clean your house have become popular.",
        "answer": "which"
    },
    {
        "question": "It is becoming ( ).",
        "answer": "common"
    },

    {
        "question": "I have an uncle ( ) runs a Japanese restaurant.",
        "answer": "who"
    },
    {
        "question": "I don’t always want to rely ( ) a machine to communicate with people.",
        "answer": "on"
    },
    {
        "question": "Today’s discussion topic is AI technology for our ( ).",
        "answer": "future"
    },
    {
        "question": "Kota has a good ( ), but I think learning foreign languages is still important.",
        "answer": "point"
    },
    {
        "question": "If you can use translation software, do you still ( ) to learn foreign languages in school?",
        "answer": "need"
    },
    {
        "question": "In my ( ), AI devices can help with many languages, so learning foreign languages will not be so important anymore.",
        "answer": "opinion"
    },
    {
        "question": "I think translation software is very ( ).",
        "answer": "useful"
    },

    {
        "question": "I also ( ) communicating in English, so I want to study more.",
        "answer": "enjoy"
    },
    {
        "question": "Can I ( ) something?",
        "answer": "say"
    },
    {
        "question": "OK, I think everyone had valuable opinions to ( ).",
        "answer": "share"
    },
    {
        "question": "( ) about you, Tina?",
        "answer": "how"
    },
    {
        "question": "Learning each other’s language and culture helps us get a better ( ) of each other, too.",
        "answer": "understanding"
    },
    {
        "question": "( ) his uncle, we’ll use AI devices more, and that’ll be convenient for us.",
        "answer": "like"
    },
    {
        "question": "Learning a language is a valuable experience ( ) will help us broaden our world view.",
        "answer": "that"
    },
    {
        "question": "On the other ( ), I also agree with Hajin and Eri’s opinion.",
        "answer": "hand"
    }
]


# 全問題から正解単語だけを取り出す
all_answers = list(set(q["answer"] for q in questions))


st.title("3年生 Unit 4まとめ")


# 最初の設定
if "question_list" not in st.session_state:
    st.session_state.question_list = random.sample(
        questions,
        min(10, len(questions))
    )

    st.session_state.number = 0
    st.session_state.results = []
    st.session_state.finished = False
    st.session_state.show_results = False
    st.session_state.choices = {}


# クイズ終了後
if st.session_state.finished:

    st.success("10問終了！")

    score = 0

    for result in st.session_state.results:
        if result["answer"] == result["correct"]:
            score += 1

    st.write(
        "あなたの得点は",
        score,
        "/",
        len(st.session_state.results)
    )


    if st.button("今回の結果を見る"):

        st.session_state.show_results = True
        st.rerun()


    if st.session_state.show_results:

        st.write("### 今回の問題と結果")

        for i, result in enumerate(st.session_state.results):

            st.write("第", i + 1, "問")

            st.write("問題:", result["question"])

            st.write("あなたの答え:", result["answer"])

            st.write("正解:", result["correct"])

            if result["answer"] == result["correct"]:

                st.success("○ 正解")

            else:

                st.error("× 不正解")


    if st.button("もう一度挑戦"):

        st.session_state.question_list = random.sample(
            questions,
            min(10, len(questions))
        )

        st.session_state.number = 0
        st.session_state.results = []
        st.session_state.finished = False
        st.session_state.show_results = False
        st.session_state.choices = {}

        st.rerun()


# クイズ中
else:

    question_data = st.session_state.question_list[
        st.session_state.number
    ]

    question = question_data["question"]

    correct = question_data["answer"]


    st.write(
        "第",
        st.session_state.number + 1,
        "問"
    )

    st.write(question)


    # この問題の4択をまだ作っていなければ作る
    if st.session_state.number not in st.session_state.choices:

        choices = [correct]

        while len(choices) < 4:

            choice = random.choice(all_answers)

            if choice not in choices:
                choices.append(choice)

        random.shuffle(choices)

        st.session_state.choices[
            st.session_state.number
        ] = choices


    choices = st.session_state.choices[
        st.session_state.number
    ]


    answer = st.radio(
        "正しい答えを選んでください",
        choices,
        key="choice_" + str(st.session_state.number)
    )


    if st.button("回答"):

        if answer == correct:

            st.success("正解！")

        else:

            st.error(
                "不正解。正解は " + correct
            )


        st.session_state.results.append({
            "question": question,
            "answer": answer,
            "correct": correct
        })


        if st.session_state.number < 9:

            st.session_state.number += 1
            st.rerun()

        else:

            st.session_state.finished = True
            st.rerun()