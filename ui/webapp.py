import logging
from json import JSONDecodeError

import streamlit as st

from utils import query
debug = False


def set_state_if_absent(key, value):
    if key not in st.session_state:
        st.session_state[key] = value


def main():
    set_state_if_absent("question", None)
    set_state_if_absent("answer", None)
    set_state_if_absent("results", None)
    set_state_if_absent("raw_json", None)

    st.set_page_config(
        page_title="Notion integrated in Haystack",
        page_icon="https://files.readme.io/1caa2c4-small-haystack-favicon-32.png"
    )

    # Title
    st.write("# Integration of Notion with Haystack RAG Pipelines")
    st.write("This application is a demo of a RAG Pipeline that uses Notion pages as a knowledge source.")
    st.write("Let's asks some questions!")

    # Search bar
    question = st.text_input(
        max_chars=100,
        label="question",
        label_visibility="hidden",
    )

    run_pressed = st.button("Run")

    # Get results for query
    if run_pressed and question:
        st.session_state.question = question

        with st.spinner(
                "🧠 &nbsp;&nbsp; Generating answer based on retrieved documents... \n "
        ):
            try:
                st.session_state.results, st.session_state.raw_json = query(question)
            except JSONDecodeError as je:
                st.error("👓 &nbsp;&nbsp; An error occurred reading the results. Is the document store working?")
                print(st.session_state.raw_json)
                return
            except Exception as e:
                logging.exception(e)
                if "The server is busy processing requests" in str(e) or "503" in str(e):
                    st.error("🧑‍🌾 &nbsp;&nbsp; All our workers are busy! Try again later.")
                else:
                    st.error("🐞 &nbsp;&nbsp; An error occurred during the request.")
                return

    if st.session_state.results:

        st.write("## Answer:")

        # Display the answer
        answer_str = st.session_state.results["answer"]["answer"] + "\n\n"
        cited_docs = st.session_state.results["cited_docs"]

        for i, doc in enumerate(cited_docs):
            answer_str += f"[Source {i+1}]({doc['meta']['url']})\n\n"

        st.success(answer_str)

        if debug:
            st.subheader("REST API JSON response")
            st.write(st.session_state.raw_json)


if __name__ == "__main__":
    main()