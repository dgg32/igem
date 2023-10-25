import streamlit as st
from streamlit_chat import message
import agents
import yaml

with open("config.yaml", "r") as stream:
    try:
        PARAM = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

st.set_page_config(layout="wide")
st.title(PARAM["title"])


def get_text():
    input_text = st.text_input(PARAM["subtitle"], "", key="input")
    return input_text

user_input = get_text()

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'user_input' not in st.session_state:
    st.session_state['user_input'] = []

if user_input:

    #prompt = f"Previous you answered {last_answer}. Now the user asks {user_input}"
    res = agents.ask_question(user_input)

    #last_answer = res

    #print (last_answer)
    # st.session_state.user_input.append(user_input)
    # st.session_state.cypher.append("")
    # st.session_state.database_results.append("")
    # st.session_state.generated.append(cypher)

    st.session_state.user_input.append(user_input)
    st.session_state.generated.append(res)



if st.session_state['generated']:
    size = len(st.session_state['generated'])
    # Display only the last four  exchanges

    for i in range(max(size-4, 0), size):
        if st.session_state['user_input'][i]:

            message(st.session_state['user_input'][i],is_user=True, key=str(i) + '_user')
        
        if st.session_state["generated"][i]:

            message(st.session_state["generated"][i], key=str(i))
