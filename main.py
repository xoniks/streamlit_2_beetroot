import streamlit as st 


st.title('Hello to our wage app :sunglasses:')

hours = st.number_input('Insert a hours', step=1)
rates = st.number_input('Insert a rate')


def calculate_wage(hour, rate):
    return hour * rate


if st.button('Calculate wage!'):
    result = calculate_wage(hours,rates)
    st.write('The current number is ', result)