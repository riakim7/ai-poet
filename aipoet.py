from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st

#from dotenv import load_dotenv
#load_dotenv()

llm = init_chat_model(model="gemini-2.5-flash", model_provider="google_genai")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "{input}")
])

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

# 제목
st.title("인공지능 시인")
st.title('_Streamlit_ is :blue[cool] :sunglasses:')

# 시 주제 필드 입력
content = st.text_input("시의 주제를 제시해주세요.")
st.write("시의 주제는", content)

# 시 작성 요청하기
if st.button("시 작성 요청하기"):
    with st.spinner("Wait for it..."):  # 로딩 메시지 출력
        result = chain.invoke({"input": content + "에 대한 시를 4단락으로 써줘."})
        st.write(result)
