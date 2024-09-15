import streamlit as st

#Set the App Title
st.title('My First StreamLit Test App')

#This is how you 'write'
st.write('This is a text')

st.button('Reset', type='primary')
if st.button('Say hello'):
    st.write('Why hello There')
    st.image('https://media.cnn.com/api/v1/images/stellar/prod/gettyimages-2161673894.jpg?c=16x9&q=h_653,w_1160,c_fill/f_webp')
    st.balloons()
else:
    st.write('GoodBye')
    st.balloons()