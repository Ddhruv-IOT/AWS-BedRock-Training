import streamlit as st
import boto3
import uuid

client = boto3.client('bedrock-agent-runtime', region_name="us-east-1")

resp =''
s_id = "AI01" 
    
import streamlit as st
from dataclasses import dataclass


@dataclass
class Message:
    actor: str
    payload: str


USER = "user"
ASSISTANT = "ai"
MESSAGES = "messages"
if MESSAGES not in st.session_state:
    st.session_state[MESSAGES] = [Message(actor=ASSISTANT, payload="Hi! How can I help you?")]

msg: Message
for msg in st.session_state[MESSAGES]:
    st.chat_message(msg.actor).write(msg.payload)

prompt: str = st.chat_input("Enter a prompt here")

if prompt:
    st.session_state[MESSAGES].append(Message(actor=USER, payload=prompt))
    st.chat_message(USER).write(prompt)
    print(s_id)
    
    resp = client.invoke_agent(
        sessionId=s_id,
        # refer to the jupyer notebook for the agentAliasId
        agentAliasId='Agent-Alias-Id',
        enableTrace=False,
        endSession=False,
        # refer to the jupyer notebook for the agentId
        agentId='Agent-Id',
        inputText=prompt,)
    
    response_data = resp['completion']
    
    for d in response_data:
        print(d)
        
    ai_response = d['chunk']['bytes'].decode('utf-8')

    # Print the extracted text
    print(ai_response)
    
    response: str = f"D-AI: {ai_response}"
    st.session_state[MESSAGES].append(Message(actor=ASSISTANT, payload=response))
    st.chat_message(ASSISTANT).write(response) 
