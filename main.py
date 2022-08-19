from freebible import read_web
import streamlit as st

#with st.echo():
st.text_input("Please, enter with Book", key="book")
st.text_input("Please, enter with term for find", key="term")

def find_term_bible(book: str, term: str):
    web = read_web()
    j = 0
    if book != '':
        for i in range(len(web[book][1])):
            find = str(web[book][1][i+1])
            if term in find:
                st.write(web['John'][1][i+1])
                j+=1
        return f'Termo "{term}", ocorre {j} vezes no livro de {book}'
    else:
        return f'Informe os termos para busca'  

st.write(find_term_bible(book=st.session_state.book,term=st.session_state.term))
