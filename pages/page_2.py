import streamlit as st

#自動でリロードされないようにする
with st.form(key='profile_form'):


    #テキストボックス
    name = st.text_input('名前')
    address = st.text_input("住所")

    #セレクトボックス
    age_categoy = st.radio(
        '年齢層',
        ("こども","大人")
    )

    hobby = st.multiselect(
        "趣味",
        ("スポーツ","読書","プログラミング","アニメ","釣り")
    )


    #ボタン
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')

    if submit_btn:
        st.text(name+address)
        st.text(age_categoy)
        st.text(",".join(hobby))