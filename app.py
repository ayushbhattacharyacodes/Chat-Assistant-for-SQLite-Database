import utils

import streamlit as st
from streamlit_chat import message

def initialize_session_state():

    st.session_state.setdefault('history',[])
    st.session_state.setdefault('generated',["Hello!! I am here to provide answers to questions fetched from the Database."])
    st.session_state.setdefault('past',["Hello Buddy!"])


def display_chat(conversation_chain,chain):
    reply_container = st.container()
    container = st.container()

    with container:
        with st.form(key='chat_form',clear_on_submit=True):
            user_input = st.text_input("Question:",placeholder="Ask me questions from the uploaded Database")
            submit_button = st.form_submit_button(label="Send🚀")
            
        if submit_button and user_input:
            generate_response(user_input, conversation_chain, chain)
    display_generated_responses(reply_container)


def generate_response(user_input, conversation_chain, chain):
    with st.spinner('Cooking an insightful response...'):
        output = conversation_chat(user_input,conversation_chain,chain,st.session_state['history'])
    
    st.session_state['past'].append(user_input)
    st.session_state['generated'].append(output)


def conversation_chat(user_input,conversation_chain,chain,history):
    response = conversation_chain.invoke(user_input)
    if len(response['result']) == 0 :
        response['result'] = 'Unfortunately, there is insufficient data to give an answer..'

    final_response = chain.invoke(f"Based on the following information generate human readable response {response['query'],response['result']}")
    history.append((user_input,final_response))  

    return final_response


def display_generated_responses(reply_container):
  if st.session_state['generated']:
      for i in range(len(st.session_state['generated'])):
          message(st.session_state['past'][i],is_user=True,key=f'{i}_user')
          message(st.session_state["generated"][i],key=str(i),avatar_style="bottts")



def main():
    initialize_session_state()
    
    st.title("DBCaretaker")

    hide_streamlit_style = """
      <style>
      MainMenu {visibility:hidden;}
      footer {visibility:hidden;}
      </style>
    """

    st.markdown(hide_streamlit_style,unsafe_allow_html=True)
    
    conversation_chain,chain = utils.create_conversational_chain()

    display_chat(conversation_chain,chain)

if __name__ =="__main__":
    main()
