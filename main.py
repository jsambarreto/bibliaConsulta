from freebible import read_web
import streamlit as st
from re import sub

book_=''
term_=''

def camel_case(s):
  s = sub(r"(_|-)+", " ", s).title()
  return ''.join([s[0].upper(), s[1:]])

st.text_input("Please, enter with Book", key="book")
st.text_input("Please, enter with term for find", key="term")

def find_term_bible(book: str, term: str):
    web = read_web()
    j = 0
    if book != '':
        for i in range(len(web[book][1])):
            find = str(web[book][1][i+1])
            if term in find:
                st.write(web[book][1][i+1])
                j+=1
        return f'Termo "{term}", ocorre {j} vezes no livro de {book}'
    else:
        return f'Informe os termos para busca'  
#if st.session_state.book!= '':
#    book_=camel_case(st.session_state.book)

st.write(find_term_bible(book=st.session_state.book,term=st.session_state.term))
st.write("List of Books")

books = read_web()

for j in range(len(books.books)):
    st.write(books.books[j].short_name)