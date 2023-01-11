import streamlit as st


st.header('Twitch.tv :blue[StoreCL]')
st.subheader('Calcule o valor ideal para items na twitch!')
horas = st.slider('Média de horas por live', 1, 24, 6)
dias = st.slider('Dias de Live na semana', 1, 7, 3)
horas_mensal = (horas * (dias * 4))
st.write(horas, f'h por dia e', horas_mensal, 'horas mensais')
pontos = st.number_input('Qtd de pontos a cada 10 min. Ex: 15, 20. Consulte no streamelements.com',
                         min_value=1, value=10)
pontuacao_mensal = (pontos * 6) * horas_mensal
valor_mensal = st.number_input('Insira o valor mensal em reais para resgate. Ex: 10$ Reais',
                               min_value=1, value=10)
st.write('Valor mensal para resgate', valor_mensal, '$Reais')
valor_skin = st.number_input('Insira o valor do item/Skin. Ex: 5,99$ Reais',
                             value=2.5)

calc = (pontuacao_mensal * valor_skin) / valor_mensal
tempo = (pontuacao_mensal * 30) / calc
if st.button('Calcular'):
    st.write('O item deverá ter o valor dê:')
    st.code(int(calc))
