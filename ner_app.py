import streamlit as st
from ner_spacy import ner, pos_tagging


def main():
    st.title("named entity recognition".title())
    input_sent = st.text_input("Input Sentence", "")
    if input_sent:
        for res in ner(input_sent):
            st.write(res[0], "---->", res[1])
        for tag in pos_tagging(input_sent):
            st.write(tag[0], "-->", (tag[3], tag[4]))


if __name__ == "__main__":
    main()