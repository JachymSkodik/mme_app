import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


# Kosmetika rámečků
box_style = """
    border: 0.5px solid #41444C;
    padding: 10px;
    border-radius: 5px;
    text-align: justify;
    background-color: #131720;
"""

# Renderování LaTeXu
latex_img = 'https://latex.codecogs.com/svg.latex?'
latex_style = 'filter: invert(100%);'

# Kosmetika grafů
plt.rcParams.update({
    'figure.facecolor': 'none',
    'axes.facecolor': 'none',
    'axes.edgecolor': 'white',
    'axes.labelcolor': 'white',
    'xtick.color': 'white',
    'ytick.color': 'white',
    'text.color': 'white',
    'grid.color': '#2C2C2B',
    'grid.linestyle': '--',
    'grid.linewidth': 0.5,
})

backslash = '\\'




def scroll_top():
    st.markdown("""
                <style>
                a#linkto_top {
                    color: white;
                    text-decoration: none;
                    border: 0.5px solid #41444C;
                    padding-top: 7px;
                    padding-bottom: 10px;
                    padding-left: 12px;
                    padding-right: 12px;
                    border-radius: 7px;
                    background-color: #131720;
                }
                </style>

                <center><a href='#linkto_top' id='linkto_top'>↑ Zpět nahoru</a></center>
                """, unsafe_allow_html=True)



def marshall():
    st.markdown("<div id='linkto_top'></div>", unsafe_allow_html=True)

    left_button, right_button = st.columns([2.82, 1])

    with left_button:
        if st.button('← Domů', key='1'):
            st.session_state.page = 'uvod'
            st.rerun()

    with right_button:
        if st.button('1.2 Hicksova úloha →', key='2'):
            st.session_state.page = 'hicks'
            st.rerun()


    st.markdown('---')


    st.subheader('1.1 Marshallova úloha')
    st.markdown(f"""
        <div style="text-align: justify"> 
        Základním problémem, který budeme v rámci teorie spotřebitele řešit, je Marshallova
        úloha. Při této úloze uvažujeme spotřebitele, který má určité (konstantní a exogenně
        dané) množství peněžních prostředků a ty chce utratit za zboží a služby.
        <br>
        <br>  
        Pro zjednodušení budeme pracovat s předpokladem, že spotřebitel se rozhoduje mezi
        dvěma druhy zboží neboli statků – statkem <img src="{latex_img}{'X'}" style="{latex_style}" />
        a statkem <img src="{latex_img}{'Y'}" style="{latex_style}" />.
        <br>
        <br>
        </div>
        """, unsafe_allow_html=True)



    marshall_definice = f"""
    <div style="{box_style}">
        <b>Definice Marshallovy úlohy</b>: Marshallovou úlohou myslíme maximalizaci spotřebitelova užitku při konstantním
        a pevně daném důchodu (jehož výši označujeme jako
        <img src="{latex_img}{'I'}" style="{latex_style}" />), tj.
            <div style="padding: 15px; padding-left: 20px;">
                <img src="{latex_img}{backslash + 'max_{X, Y} U(X, Y)'}" style="{latex_style}" />
            </div>
        za podmínky
            <div style="padding: 15px; padding-left: 20px;">
                <img src="{latex_img}{'P_X' + backslash + 'cdot X + P_Y' + backslash + 'cdot Y = I'}" style="{latex_style}" />,
            </div>
        kde <img src="{latex_img}{'X'}" style="{latex_style}" /> a <img src="{latex_img}{'Y'}" style="{latex_style}" />
        jsou množství poptávaných statků, <img src="{latex_img}{'P_X'}" style="{latex_style}" /> a <img src="{latex_img}{'P_Y'}" style="{latex_style}" />
        jsou jejich ceny, <img src="{latex_img}{'U'}" style="{latex_style}" /> je spotřebitelova užitková funkce a
        <img src="{latex_img}{'I'}" style="{latex_style}" /> je spotřebitelův důchod.
    </div>
    """

    st.markdown(marshall_definice, unsafe_allow_html=True)


    st.html('<br>')


    marshall_poptavka = f"""<div style="{box_style}">
                        <b>Definice Marshallovy poptávky</b>: Marshallova poptávka spotřebitele po
                        statku <img src="{latex_img}{'X'}" style="{latex_style}" /> je množství peněžních prostředků
                        spotřebitele a cen <img src="{latex_img}{'P_X'}" style="{latex_style}" /> a
                        <img src="{latex_img}{'P_Y'}" style="{latex_style}" /> a udává množství
                        statku <img src="{latex_img}{'X'}" style="{latex_style}" />, které spotřebitel poptává,
                        jestliže minimalizuje své peněžní výdaje.
                        </div>"""

    st.markdown(marshall_poptavka, unsafe_allow_html=True)


    st.markdown('---')


    st.markdown(f"""<div style="text-align: justify">
                Nyní budeme optimalizovat užitek spotřebitele s konkrétní užitkovou funkcí. V bočním panelu si nastavte
                ceny poptávaných statků, důchod spotřebitele a jeho preference (parametry užitkové funkce). Budeme zjišťovat, jaká
                množství statků <img src="{latex_img}{'X'}" style="{latex_style}" /> a <img src="{latex_img}{'Y'}" style="{latex_style}" />
                by měl spotřebitel zvolit, aby maximalizoval svůj užitek.
                <br>
                <br>
                </div>""", unsafe_allow_html=True)

    st.markdown(f"""<div style="text-align: justify">
                Budeme uvažovat Cobb-Douglasovu užitkovou funkci ve tvaru
                <div style="padding: 10px; padding-left: 20px;">
                <img src="{latex_img}{'U(X, Y) = X^c ' + backslash + 'cdot Y^d'}" style="{latex_style}" />
                </div>
                </div>""", unsafe_allow_html=True)

    st.markdown('s parametry $c$ a $d$, přičemž $c+d=1$ a zároveň $c, d > 0$. Zadejte tyto parametry pro užitkovou funkci daného spotřebitele.')


    st.markdown('---')


    # Boční panel pro zadání parametrů
    P_x = st.sidebar.slider('Cena statku $P_X$', min_value=1.0, max_value=10.0, value=5.0, step=0.1)

    P_y = st.sidebar.slider('Cena statku $P_Y$', min_value=1.0, max_value=10.0, value=5.0, step=0.1)

    I = st.sidebar.slider('Důchod spotřebitele $I$', min_value=100, max_value=1000, value=500, step=1)

    c = st.sidebar.slider('Parametry $c$ a $d$', min_value=0.01, max_value=0.99, value=0.5, step=0.01)
    d = round(1 - c, 2)


    # Shrnutí zadaných parametrů
    parameters = f"""<div style="{box_style}">
                    <img src="{latex_img}{'P_X='}{P_x}" style="{latex_style}" />
                    <br>
                    <img src="{latex_img}{'P_Y='}{P_y}" style="{latex_style}" />
                    <br>
                    <img src="{latex_img}{'I='}{I}" style="{latex_style}" />
                    <br>
                    <img src="{latex_img}{'c='}{c}" style="{latex_style}" />
                    <br>
                    <img src="{latex_img}{'d='}{d}" style="{latex_style}" />
                </div>"""
    st.sidebar.markdown(parameters, unsafe_allow_html=True)


    # Graf užitkové funkce
    st.markdown(f"""<div style="text-align: justify">
                Graf užitkové funkce s indiferenční křivkou <img src="{latex_img}{'U'}" style="{latex_style}" />, jež označuje optimum
                spotřebitele vypočítané na základě zadaných parametrů:
                <br>
                <br>
                </div>""", unsafe_allow_html=True)

    # Rozsah grafu
    scope = int(round(I/min(P_x, P_y), 0))
    x = np.linspace(0, scope*1.5, scope*5)
    y = np.linspace(0, scope*1.5, scope*5)

    # Vytvoříme graf
    fig, ax = plt.subplots()

    # Funkce Marshallovy poptávky
    ax.plot(x, (I - P_x*x)/P_y, color='#6473AC')

    # Cobb-Douglasova užitková funkce
    X, Y = np.meshgrid(x, y)
    U = X**c * Y**d

    # Optimum spotřebitele
    X_optimal = (c * I) / P_x
    Y_optimal = (d * I) / P_y
    U_optimal = X_optimal**c * Y_optimal**d

    # Indiferenční křivka
    ax.contour(X, Y, U, levels=[U_optimal], colors='white', linestyles='dashed')
    ax.contour(X, Y, U, levels=[U_optimal + x*(scope/6) for x in range(-8, 9) if x != 0], colors='#4D4D4D', linestyles='dashed', alpha=0.75)

    # Vyznačení optima
    if c == 0:
        text_fix_x = 0
        text_fix_y = 0.1*Y_optimal
    elif d == 0:
        text_fix_x = 0.05*X_optimal
        text_fix_y = 0
    else:
        text_fix_x = 0
        text_fix_y = 0
    ax.scatter(X_optimal, Y_optimal, color='red')
    ax.text(X_optimal + 0.1*Y_optimal + text_fix_x, Y_optimal + 0.1*X_optimal + text_fix_y, f'({X_optimal:.2f}, {Y_optimal:.2f})',
            color='white', fontsize=10)

    # Prvky grafu
    font_properties = {'fontsize': 12, 'fontweight': 'bold', 'fontfamily': 'sans-serif'}

    ax.set_xlabel('X', fontdict=font_properties)
    ax.set_ylabel('Y', fontdict=font_properties, rotation=0)
    plt.gca().xaxis.set_label_coords(1, -0.075)
    plt.gca().yaxis.set_label_coords(-0.05, 1.02)
    ax.grid(True)
    ax.set_xlim(0, scope*1.5)
    ax.set_ylim(0, scope*1.5)

    handles = [plt.Line2D([], [], color='#6473AC', label='$P_X ' + backslash + 'cdot X + P_Y ' + backslash + 'cdot Y = I$'),
               plt.Line2D([], [], linestyle='dashed', color='white', label='$U(X, Y) = X^c ' + backslash + 'cdot Y^d$'),
               plt.scatter([], [], color='red', label=f'Optimum spotřebitele\nmax $U(X, Y)$ = {round(U_optimal, 2)}')]
    ax.legend(handles=handles, loc='upper right', fontsize=9, facecolor='#0E1117')

    st.pyplot(fig)


    st.markdown('---')


    st.markdown(f"""<div style="text-align: justify">
                V následujících krocích si ukážeme, jak jsme se k tomuto výsledku dostali.
                <br>
                <br>
                <ol>
                <li>Nejprve sestavíme Langrangeovu funkci, jež má tvar
                <div style="padding: 10px; padding-left: 20px;">
                <img src="{latex_img}{backslash + 'mathcal{L} = U(X, Y) + ' + backslash + 'lambda(P_X ' + backslash + 'cdot X + P_Y ' + backslash + 'cdot Y - I)'}" style="{latex_style}" /> ,
                </div>
                přičemž <img src="{latex_img}{backslash + 'lambda'}" style="{latex_style}" /> je Lagrangeův multiplikátor.
                </li>
                <br>
                <li>Uvažujeme Cobb-Douglasovu užitkovou funkci, kterou můžeme zapsat tímto způsobem
                <div style="padding: 10px; padding-left: 20px;">
                <img src="{latex_img}{'U(X, Y) = X^c ' + backslash + 'cdot Y^d'}" style="{latex_style}" />
                </div>
                a dále ji zlogaritmovat, což úlohu zjednoduší:
                <div style="padding: 10px; padding-left: 20px;">
                <img src="{latex_img}{backslash + 'ln U(X, Y) = c ' + backslash + 'cdot ' + backslash + 'ln X + d ' + backslash + 'cdot ' + backslash + 'ln Y'}" style="{latex_style}" />.
                </div>
                </li>
                <br>
                <li>Lagrangeovu funkci pro tuto úlohu tedy můžeme zapsat jako
                <div style="padding: 10px; padding-left: 20px;">
                <img src="{latex_img}{backslash + 'mathcal{L} = c ' + backslash + 'cdot ' + backslash + 'ln X + d ' + backslash + 'cdot ' + backslash + 'ln Y + ' + backslash + 'lambda(P_X ' + backslash + 'cdot X + P_Y ' + backslash + 'cdot Y - I)'}" style="{latex_style}" /> .
                </div>
                </li>
                <br>
                <li>Určíme si parciální derivace této funkce a položíme je rovny nule
                <div style="padding: 10px; padding-left: 20px; padding-top: 15px;">
                    <img src="{latex_img}{backslash + 'frac{' + backslash + 'partial ' + backslash + 'mathcal{L} (X, Y, ' + backslash + 'lambda)}{' + backslash + 'partial X} = ' + backslash + 'frac{c}{X} + ' + backslash + 'lambda ' + backslash + 'cdot P_X = 0'}" style="{latex_style}" />
                <br>
                <br>
                    <img src="{latex_img}{backslash + 'frac{' + backslash + 'partial ' + backslash + 'mathcal{L} (X, Y, ' + backslash + 'lambda)}{' + backslash + 'partial Y} = ' + backslash + 'frac{d}{Y} + ' + backslash + 'lambda ' + backslash + 'cdot P_Y = 0'}" style="{latex_style}" />
                <br>
                <br>
                    <img src="{latex_img}{backslash + 'frac{' + backslash + 'partial ' + backslash + 'mathcal{L} (X, Y, ' + backslash + 'lambda)}{' + backslash + 'partial ' + backslash + 'lambda} = P_X ' + backslash + 'cdot X + P_Y ' + backslash + 'cdot Y - I = 0'}" style="{latex_style}" /> .
                </div>
                </li>
                <br>
                <li>Vyjádříme Lagrangeův multiplikátor
                <div style="padding: 10px; padding-left: 20px; padding-top: 15px; padding-bottom: 15px;">
                <img src="{latex_img}{backslash + 'lambda = -' + backslash + 'frac{d}{P_Y ' + backslash + 'cdot Y} = -' + backslash + 'frac{c}{P_X ' + backslash + 'cdot X}'}" style="{latex_style}" />
                </div>
                a z této rovnosti vyjádříme
                <div style="padding: 10px; padding-left: 20px; padding-top: 15px;">
                <img src="{latex_img}{'Y = ' + backslash + 'frac{d ' + backslash + 'cdot P_X ' + backslash + 'cdot X}{c ' + backslash + 'cdot P_Y}'}" style="{latex_style}" /> .
                </div>
                </li>
                <br>
                <li>Dosadíme do rozpočtové rovnice
                <div style="padding: 10px; padding-left: 20px; padding-top: 15px; padding-bottom: 15px;">
                <img src="{latex_img}{'P_X ' + backslash + 'cdot X + P_Y ' + backslash + 'cdot ' + backslash + 'frac{d ' + backslash + 'cdot P_X ' + backslash + 'cdot X}{c ' + backslash + 'cdot P_Y} = I'}" style="{latex_style}" />
                </div>
                a vyjádříme
                <div style="padding: 10px; padding-left: 20px; padding-top: 15px;">
                    <img src="{latex_img}{'X = ' + backslash + 'frac{c ' + backslash + 'cdot I}{P_X ' + backslash + 'cdot (c + d)} = ' + backslash + 'frac{c ' + backslash + 'cdot I}{P_X}'}" style="{latex_style}" />
                <br>
                <br>
                    <img src="{latex_img}{'Y = ' + backslash + 'frac{I - c ' + backslash + 'cdot I}{P_Y} = ' + backslash + 'frac{d ' + backslash + 'cdot I}{P_Y}'}" style="{latex_style}" /> .
                </div>
                </li>
                <br>
                <li>Nyní pouze dosadíme zadané hodnoty, vypočítáme optimální množství <img src="{latex_img}{'X'}" style="{latex_style}" /> a 
                optimální množství <img src="{latex_img}{'Y'}" style="{latex_style}" /> (optimum spotřebitele) a nakonec i maximalizovaný
                užitek pomocí užitkové funkce.
                </li>
                </ol>
                </div>""", unsafe_allow_html=True)
    

    st.markdown('---')


    scroll_top()



def hicks():
    st.markdown("<div id='linkto_top'></div>", unsafe_allow_html=True)

    left_button, right_button = st.columns([7.07, 1])

    with left_button:
        if st.button('← 1.1 Marshallova úloha', key='1'):
            st.session_state.page = 'marshall'
            st.rerun()

    with right_button:
        if st.button('Domů →', key='2'):
            st.session_state.page = 'uvod'
            st.rerun()


    st.markdown('---')


    st.subheader('1.2 Hicksova úloha')
    st.markdown(f"""
        <div style="text-align: justify"> 
        Alternativou k Marshallově úloze je Hicksova úloha. Přesněji řečeno, Hicksova úloha
        je duální úlohou k Marshallově úloze. Zatímco v případě Marshallovy úlohy jsme maximalizovali
        užitek spotřebitele při daném fixním příjmu, u Hicksovy úlohy minimalizujeme výdaje
        spotřebitele na dosažení určité požadované (a fixní) hodnoty užitku.
        <br>
        <br>
        </div>
        """, unsafe_allow_html=True)



    hicks_definice = f"""
    <div style="{box_style}">
        <b>Definice Hicksovy úlohy</b>: Hicksovou úlohou myslíme minimalizaci výdajů na nákup zboží při
        dané požadované úrovni užitku, tj.
            <div style="padding: 15px; padding-left: 20px;">
                <img src="{latex_img}{backslash + 'min_{X, Y}   P_X ' + backslash + 'cdot X + P_Y ' + backslash + 'cdot Y'}" style="{latex_style}" />
            </div>
        za podmínky
            <div style="padding: 15px; padding-left: 20px;">
                <img src="{latex_img}{'U(X, Y) = C'}" style="{latex_style}" />,
            </div>
        kde <img src="{latex_img}{'X'}" style="{latex_style}" /> a <img src="{latex_img}{'Y'}" style="{latex_style}" />
        jsou množství poptávaných statků, <img src="{latex_img}{'P_X'}" style="{latex_style}" /> a <img src="{latex_img}{'P_Y'}" style="{latex_style}" />
        jsou jejich ceny, <img src="{latex_img}{'U'}" style="{latex_style}" /> je spotřebitelova užitková funkce a
        <img src="{latex_img}{'C'}" style="{latex_style}" /> je spotřebitelův užitek.
    </div>
    """

    st.markdown(hicks_definice, unsafe_allow_html=True)


    st.html('<br>')


    hicks_poptavka = f"""<div style="{box_style}">
                        <b>Definice Hicksovy poptávky</b>: Hicksova poptávka spotřebitele po
                        statku <img src="{latex_img}{'X'}" style="{latex_style}" /> je funkcí požadované
                        úrovně užitku spotřebitele a cen <img src="{latex_img}{'P_X'}" style="{latex_style}" /> a
                        <img src="{latex_img}{'P_Y'}" style="{latex_style}" /> a udává množství
                        statku <img src="{latex_img}{'X'}" style="{latex_style}" />, které spotřebitel poptává,
                        jestliže minimalizuje své peněžní výdaje.
                        </div>"""

    st.markdown(hicks_poptavka, unsafe_allow_html=True)


    st.markdown('---')


    st.markdown(f"""<div style="text-align: justify">
                Nyní budeme minimalizovat výdaje spotřebitele s konkrétní užitkovou funkcí. V bočním panelu si nastavte
                ceny poptávaných statků, požadovaný užitek spotřebitele a jeho preference (parametry užitkové funkce). Budeme zjišťovat, jaká
                množství statků <img src="{latex_img}{'X'}" style="{latex_style}" /> a <img src="{latex_img}{'Y'}" style="{latex_style}" />
                by měl spotřebitel zvolit, aby minimalizoval své výdaje při zachování požadovaného užitku.
                <br>
                <br>
                </div>""", unsafe_allow_html=True)

    st.markdown(f"""<div style="text-align: justify">
                Budeme uvažovat Cobb-Douglasovu užitkovou funkci ve tvaru
                <div style="padding: 10px; padding-left: 20px;">
                <img src="{latex_img}{'U(X, Y) = X^c ' + backslash + 'cdot Y^d'}" style="{latex_style}" />
                </div>
                </div>""", unsafe_allow_html=True)

    st.markdown('s parametry $c$ a $d$, přičemž $c+d=1$ a zároveň $c, d > 0$. Zadejte tyto parametry pro užitkovou funkci daného spotřebitele.')


    st.markdown('---')


    # Boční panel pro zadání parametrů
    P_x = st.sidebar.slider('Cena statku $P_X$', min_value=1.0, max_value=10.0, value=5.0, step=0.1)

    P_y = st.sidebar.slider('Cena statku $P_Y$', min_value=1.0, max_value=10.0, value=5.0, step=0.1)

    C = st.sidebar.slider('Užitek spotřebitele $C$', min_value=1.0, max_value=10.0, value=5.0, step=0.1)

    c = st.sidebar.slider('Parametry $c$ a $d$', min_value=0.01, max_value=0.99, value=0.5, step=0.01)
    d = round(1 - c, 2)


    # Shrnutí zadaných parametrů
    parameters = f"""<div style="{box_style}">
                    <img src="{latex_img}{'P_X='}{P_x}" style="{latex_style}" />
                    <br>
                    <img src="{latex_img}{'P_Y='}{P_y}" style="{latex_style}" />
                    <br>
                    <img src="{latex_img}{'C='}{C}" style="{latex_style}" />
                    <br>
                    <img src="{latex_img}{'c='}{c}" style="{latex_style}" />
                    <br>
                    <img src="{latex_img}{'d='}{d}" style="{latex_style}" />
                </div>"""
    st.sidebar.markdown(parameters, unsafe_allow_html=True)


    # Graf užitkové funkce
    st.markdown(f"""<div style="text-align: justify">
                Graf Hicksovy poptávkové funkce s indiferenční křivkou <img src="{latex_img}{'U'}" style="{latex_style}" />, jež označuje
                zadaný užitek, jehož se snažíme dosáhnout s minimálními výdaji:
                <br>
                <br>
                </div>""", unsafe_allow_html=True)

    # Rozsah grafu
    scope = int(round((22/(P_x*P_y))*C*np.mean([P_x, P_y]), 0))
    x = np.linspace(0, scope, scope*20)
    y = np.linspace(0, scope, scope*20)

    # Vytvoříme graf
    fig, ax = plt.subplots()

    # Cobb-Douglasova užitková funkce
    X, Y = np.meshgrid(x, y)
    U = X**c * Y**d

    # Indiferenční křivka
    ax.contour(X, Y, U, levels=[C], colors='white', linestyles='dashed')
    ax.contour(X, Y, U, levels=[C + x*(scope/9) for x in range(-8, 9) if x != 0], colors='#4D4D4D', linestyles='dashed', alpha=0.75)

    # Optimum spotřebitele
    X_optimal = C * ((c*P_y) / (d*P_x))**d
    Y_optimal = C * ((d*P_x) / (c*P_y))**c

    # Funkce Hicksovy poptávky
    slope = -P_x / P_y
    line_equation = lambda x: slope * (x - X_optimal) + Y_optimal
    ax.plot(x, line_equation(x), color='#EE7708')
    
    # Vyznačení optima
    I = P_x * X_optimal + P_y * Y_optimal
    ax.scatter(X_optimal, Y_optimal, color='red')
    ax.text(X_optimal + 0.1*Y_optimal, Y_optimal + 0.1*X_optimal, f'({X_optimal:.2f}, {Y_optimal:.2f})', color='white', fontsize=10)

    # Prvky grafu
    font_properties = {'fontsize': 12, 'fontweight': 'bold', 'fontfamily': 'sans-serif'}

    ax.set_xlabel('X', fontdict=font_properties)
    ax.set_ylabel('Y', fontdict=font_properties, rotation=0)
    plt.gca().xaxis.set_label_coords(1, -0.075)
    plt.gca().yaxis.set_label_coords(-0.05, 1.02)
    ax.grid(True)
    ax.set_xlim(0, scope)
    ax.set_ylim(0, scope)
    
    handles = [plt.Line2D([], [], color='#EE7708', label='$P_X ' + backslash + 'cdot X + P_Y ' + backslash + 'cdot Y = I$'),
               plt.Line2D([], [], linestyle='dashed', color='white', label='$U(X, Y) = X^c ' + backslash + 'cdot Y^d$'),
               plt.scatter([], [], color='red', label=f'Minimální výdaje\n{'min $P_X ' + backslash + 'cdot X + P_Y ' + backslash + 'cdot Y$'} = {round(I, 2)}')]
    ax.legend(handles=handles, loc='upper right', fontsize=9, facecolor='#0E1117')

    st.pyplot(fig)


    st.markdown('---')


    st.markdown(f"""<div style="text-align: justify">
                V následujících krocích si ukážeme, jak jsme se k tomuto výsledku dostali.
                <br>
                <br>
                <ol>
                <li>Nejprve sestavíme Langrangeovu funkci, jež má tvar
                <div style="padding: 10px; padding-left: 20px;">
                <img src="{latex_img}{backslash + 'mathcal{L} = P_X ' + backslash + 'cdot X + P_Y ' + backslash + 'cdot Y + ' + backslash + 'lambda(U(X, Y) - C)'}" style="{latex_style}" /> ,
                </div>
                přičemž <img src="{latex_img}{backslash + 'lambda'}" style="{latex_style}" /> je Lagrangeův multiplikátor.
                </li>
                <br>
                <li>Uvažujeme Cobb-Douglasovu užitkovou funkci, kterou můžeme zapsat tímto způsobem
                <div style="padding: 10px; padding-left: 20px;">
                <img src="{latex_img}{'U(X, Y) = X^c ' + backslash + 'cdot Y^d'}" style="{latex_style}" /> .
                </div>
                </li>
                <br>
                <li>Lagrangeovu funkci pro tuto úlohu tedy můžeme zapsat jako
                <div style="padding: 10px; padding-left: 20px;">
                <img src="{latex_img}{backslash + 'mathcal{L} = P_X ' + backslash + 'cdot X + P_Y ' + backslash + 'cdot Y + ' + backslash + 'lambda(X^c ' + backslash + 'cdot Y^d - C)'}" style="{latex_style}" /> .
                </div>
                </li>
                <br>
                <li>Určíme si parciální derivace této funkce a položíme je rovny nule
                <div style="padding: 10px; padding-left: 20px; padding-top: 15px;">
                    <img src="{latex_img}{backslash + 'frac{' + backslash + 'partial ' + backslash + 'mathcal{L} (X, Y, ' + backslash + 'lambda)}{' + backslash + 'partial X} = P_X + ' + backslash + 'frac{' + backslash + 'lambda ' + backslash + 'cdot c ' + backslash + 'cdot Y^d}{X^d} = 0'}" style="{latex_style}" />
                <br>
                <br>
                    <img src="{latex_img}{backslash + 'frac{' + backslash + 'partial ' + backslash + 'mathcal{L} (X, Y, ' + backslash + 'lambda)}{' + backslash + 'partial Y} = P_Y + ' + backslash + 'frac{' + backslash + 'lambda ' + backslash + 'cdot d ' + backslash + 'cdot X^c}{Y^c} = 0'}" style="{latex_style}" />
                <br>
                <br>
                    <img src="{latex_img}{backslash + 'frac{' + backslash + 'partial ' + backslash + 'mathcal{L} (X, Y, ' + backslash + 'lambda)}{' + backslash + 'partial ' + backslash + 'lambda} = X^c ' + backslash + 'cdot Y^d - C = 0'}" style="{latex_style}" /> .
                </div>
                </li>
                <br>
                <li>Vyjádříme Lagrangeův multiplikátor
                <div style="padding: 10px; padding-left: 20px; padding-top: 15px; padding-bottom: 15px;">
                <img src="{latex_img}{backslash + 'lambda = -' + backslash + 'frac{P_X ' + backslash + 'cdot X^d}{c ' + backslash + 'cdot Y^d} = -' + backslash + 'frac{P_Y ' + backslash + 'cdot Y^c}{d ' + backslash + 'cdot X^c}'}" style="{latex_style}" />
                </div>
                a z této rovnosti vyjádříme
                <div style="padding: 10px; padding-left: 20px; padding-top: 15px;">
                <img src="{latex_img}{'Y = ' + backslash + 'frac{d ' + backslash + 'cdot P_X ' + backslash + 'cdot X}{c ' + backslash + 'cdot P_Y}'}" style="{latex_style}" /> .
                </div>
                </li>
                <br>
                <li>Dosadíme do užitkové funkce
                <div style="padding: 10px; padding-left: 20px; padding-top: 15px; padding-bottom: 15px;">
                <img src="{latex_img}{'X^c ' + backslash + 'cdot ' + backslash + 'left( ' + backslash + 'frac{d ' + backslash + 'cdot P_X ' + backslash + 'cdot X}{c ' + backslash + 'cdot P_Y} ' + backslash + 'right)^d = C'}" style="{latex_style}" />
                </div>
                a vyjádříme
                <div style="padding: 10px; padding-left: 20px; padding-top: 15px;">
                    <img src="{latex_img}{'X = C ' + backslash + 'cdot ' + backslash + 'left( ' + backslash + 'frac{c ' + backslash + 'cdot P_Y}{d ' + backslash + 'cdot P_X} ' + backslash + 'right)^d'}" style="{latex_style}" />
                <br>
                <br>
                    <img src="{latex_img}{'Y = C ' + backslash + 'cdot ' + backslash + 'left( ' + backslash + 'frac{d ' + backslash + 'cdot P_X}{c ' + backslash + 'cdot P_Y} ' + backslash + 'right)^c'}" style="{latex_style}" /> .
                </div>
                </li>
                <br>
                <li>Nyní pouze dosadíme zadané hodnoty, vypočítáme optimální množství <img src="{latex_img}{'X'}" style="{latex_style}" /> a 
                optimální množství <img src="{latex_img}{'Y'}" style="{latex_style}" /> a nakonec i minimální výdaje spotřebitele
                potřebné pro dosažení požadovaného užitku.
                </li>
                </ol>
                </div>""", unsafe_allow_html=True)
    

    st.markdown('---')


    scroll_top()



def prod_fun():
    st.markdown("<div id='linkto_top'></div>", unsafe_allow_html=True)

    left_button, right_button = st.columns([2.098, 1])

    with left_button:
        if st.button('← Domů', key='1'):
            st.session_state.page = 'uvod'
            st.rerun()

    with right_button:
        if st.button('2.2 Minimalizace nákladů →', key='2'):
            st.session_state.page = 'min_naklady'
            st.rerun()


    st.markdown('---')


    st.subheader('2.1 Produkční funkce firmy')
    st.markdown(f"""
        <div style="text-align: justify"> 
        Produkční funkce firmy udává maximální možný objem výroby při daném množství výrobních faktorů.
        V této kapitole budeme uvažovat dva výrobní faktory: práci <img src="{latex_img}{'L'}" style="{latex_style}" />
        a kapitál <img src="{latex_img}{'K'}" style="{latex_style}" /> (kapitálový statek).
        <br>
        <br>  
        Může existovat tzv. neefektivní firma, která se stejným objemem výrobních faktorů vyrobí menší množství zboží než efektivní firma.
        V následujících úlohách budeme ale předpokládat efektivní firmu, pro kterou platí, že hodnota produkční funkce je rovná
        skutečně vyrobenému množství zboží.
        <br>
        <br>
        Dále budeme předpokládat, že firma vyrábí jeden druh finálního produktu a všechny vyrobené kusy jsou homogenní.
        Uvažujeme, že i nakupované výrobní faktory se mezi sebou kvalitativně neliší.
        <br>
        <br>
        </div>
        """, unsafe_allow_html=True)



    mrts_definice = f"""
    <div style="{box_style}">
        <b>Definice mezní míry technické substituce</b>: 
        Mezní míra technické substituce (MRTS) udává, o kolik jednotek musí firma zvýšit použití jednoho výrobního faktoru,
        aby zachovala objem výstupu, pokud sníží použití druhého výrobního faktoru. Tato míra je definována vztahem
            <div style="padding: 15px; padding-left: 20px;">
                <img src="{latex_img}{'MR' + backslash + 'hspace{2pt}TS = -' + backslash + 'frac{MP_L}{MP_K} = -' + backslash + 'frac{' + backslash + 'frac{' + backslash + 'partial Q(L, K)}{' + backslash + 'partial L}}{' + backslash + 'frac{' + backslash + 'partial Q(L, K)}{' + backslash + 'partial K}}'}" style="{latex_style}" /> ,
            </div>
        kde <img src="{latex_img}{'MP_L'}" style="{latex_style}" /> je mezní produktivita práce (tj. o kolik se zvýší zisk, když firma
        zaměstná o jednotku práce více), <img src="{latex_img}{'MP_K'}" style="{latex_style}" /> je mezní produktivita kapitálu
        (tj. o kolik se zvýší zisk, když firma navýší náklady o jednotku kapitálu) a <img src="{latex_img}{'Q(L, K)'}" style="{latex_style}" />
        je produkční funkce firmy.
    </div>
    """

    st.markdown(mrts_definice, unsafe_allow_html=True)


    st.markdown('---')


    st.markdown(f"""<div style="text-align: justify">
                Nyní budeme počítat mezní míru technické substituce s konkrétní produkční funkcí. V bočním panelu si nastavte hodnoty
                vstupních výrobních atributů, tedy práce a kapitálu, a parametry produkční funkce.
                <br>
                <br>
                </div>""", unsafe_allow_html=True)

    st.markdown(f"""<div style="text-align: justify">
                Budeme uvažovat Cobb-Douglasovu produkční funkci ve tvaru
                <div style="padding: 10px; padding-left: 20px;">
                <img src="{latex_img}{'Q(L, K) = L^c ' + backslash + 'cdot K^d'}" style="{latex_style}" />
                </div>
                </div>""", unsafe_allow_html=True)

    st.markdown('s parametry $c$ a $d$, přičemž $c+d=1$ a zároveň $c, d > 0$. Zadejte tyto parametry pro produkční funkci dané firmy.')


    st.markdown('---')


    # Boční panel pro zadání parametrů
    L = st.sidebar.slider('Množství jednotek práce $L$', min_value=1.0, max_value=10.0, value=5.0, step=0.1)

    Q = st.sidebar.slider('Výstup firmy $Q$', min_value=1.0, max_value=10.0, value=5.0, step=0.1)

    c = st.sidebar.slider('Parametry $c$ a $d$', min_value=0.01, max_value=0.99, value=0.5, step=0.01)
    d = round(1 - c, 2)

    # Dopočítáme množství jednotek kapitálu na základě L a Q
    K = round((Q / L**c)**(1/d), 1)

    # Shrnutí zadaných parametrů
    parameters = f"""<div style="{box_style}">
                    <img src="{latex_img}{'L='}{L}" style="{latex_style}" />
                    <br>
                    <img src="{latex_img}{'K='}{K}" style="{latex_style}" />
                    <br>
                    <img src="{latex_img}{'Q='}{Q}" style="{latex_style}" />
                    <br>
                    <img src="{latex_img}{'c='}{c}" style="{latex_style}" />
                    <br>
                    <img src="{latex_img}{'d='}{d}" style="{latex_style}" />
                </div>"""
    st.sidebar.markdown(parameters, unsafe_allow_html=True)


    # Graf funkcí mezních výrobních faktorů
    st.markdown(f"""<div style="text-align: justify">
                Graf izokvanty pro výstup (produkci) <img src="{latex_img}{'Q'}" style="{latex_style}" /> dané firmy,
                jež vyznačuje potřebnou kombinaci výrobních faktorů <img src="{latex_img}{'L'}" style="{latex_style}" />
                a <img src="{latex_img}{'K'}" style="{latex_style}" /> pro dosažení výstupu
                <img src="{latex_img}{'Q'}" style="{latex_style}" />. Dále je zobrazena tečna pro daný bod
                <img src="{latex_img}{'(L, K)'}" style="{latex_style}" />, jejíž směrnice je právě
                <img src="{latex_img}{'MR' + backslash + 'hspace{2pt}TS'}" style="{latex_style}" />, tedy mezní míra technické substituce.
                <br>
                <br>
                </div>""", unsafe_allow_html=True)


    # Rozsah grafu
    scope = 30
    x = np.linspace(0.001, scope, 200)

    # Vytvoříme graf
    fig, ax = plt.subplots()

    # Izokvanta pro zadaný výstup firmy
    ax.plot(x, (Q / x**c)**(1/d), color='#EE7708')

    # Sklon tečny - MRTS
    m = -(c * K) / (d * L)
    ax.plot(x, m * (x - L) + K, color='#6473AC')

    # Vyznačení daného bodu
    if K < scope/1.5:
        ax.scatter(L, K, color='red')
        ax.text(L+0.1*K, K+0.1*L, f'({L:.2f}, {K:.2f})')
    elif scope/1.5 <= K <= scope:
        ax.scatter(L, K, color='red')
        ax.text(L+0.08*K, K-0.3*L, f'({L:.2f}, {K:.2f})')


    # Prvky grafu
    font_properties = {'fontsize': 12, 'fontweight': 'bold', 'fontfamily': 'sans-serif'}

    ax.set_xlabel('L', fontdict=font_properties)
    ax.set_ylabel('K', fontdict=font_properties, rotation=0)
    plt.gca().xaxis.set_label_coords(1, -0.075)
    plt.gca().yaxis.set_label_coords(-0.04, 1.03)
    ax.grid(True)
    ax.set_xlim(0, scope)
    ax.set_ylim(0, scope)

    # Legenda
    handles = [plt.Line2D([], [], color='#EE7708', label=f'Izokvanta $Q=${Q}'),
               plt.Line2D([], [], color='#6473AC', label=f'Tečna izokvanty'),
               plt.scatter([], [], color='red', label=f'$MRTS=${round(m, 3)}')]
    ax.legend(handles=handles, loc='upper right', fontsize=9, facecolor='#0E1117')

    st.pyplot(fig)


    st.markdown('---')


    st.markdown(f"""<div style="text-align: justify">
                V následujících krocích si ukážeme, jak jsme se k tomuto výsledku dostali.
                <br>
                <br>
                <ol>
                <li>Nejprve pomocí zadaného množství výrobního faktoru <img src="{latex_img}{'L'}" style="{latex_style}" /> (práce)
                a požadovaného výstupu firmy <img src="{latex_img}{'Q'}" style="{latex_style}" /> dopočítáme množství výrobního
                faktoru <img src="{latex_img}{'K'}" style="{latex_style}" /> (kapitál):
                <div style="padding: 10px; padding-left: 20px;">
                <img src="{latex_img}{'K = ' + backslash + 'left( ' + backslash + 'frac{Q}{L^c} ' + backslash + 'right)^{' + backslash + 'hspace{-1.5pt}' + backslash + 'frac{1}{d}} ='}{K}" style="{latex_style}" />
                </div>
                </li>
                <br>
                <li>Vypočítáme mezní produktivitu práce <img src="{latex_img}{'MP_L'}" style="{latex_style}" />
                a mezní produktivitu kapitálu <img src="{latex_img}{'MP_K'}" style="{latex_style}" /> :
                <div style="padding: 10px; padding-left: 20px; padding-top: 15px;">
                    <img src="{latex_img}{'MP_L = ' + backslash + 'frac{' + backslash + 'partial Q(L, K)}{' + backslash + 'partial L} = c ' + backslash + 'cdot ' + backslash + 'left( ' + backslash + 'frac{K}{L} ' + backslash + 'right)^{' + backslash + 'hspace{-1pt}d} ='}{round(c*(K/max(L, 10**-10))**d, 3)}" style="{latex_style}" />
                <br>
                <br>
                    <img src="{latex_img}{'MP_K = ' + backslash + 'frac{' + backslash + 'partial Q(L, K)}{' + backslash + 'partial K} = d ' + backslash + 'cdot ' + backslash + 'left( ' + backslash + 'frac{L}{K} ' + backslash + 'right)^{' + backslash + 'hspace{-1pt}c} ='}{round(d*(L/max(K, 10**-10))**c, 3)}" style="{latex_style}" />
                </div>
                </li>
                <br>
                <li>Nakonec tyto mezní veličiny vydělíme a získáme mezní míru technické substituce
                <img src="{latex_img}{'MR' + backslash + 'hspace{2pt}TS'}" style="{latex_style}" /> :
                <div style="padding: 10px; padding-left: 20px; padding-top: 15px;">
                <img src="{latex_img}{'MR' + backslash + 'hspace{2pt}TS = -' + backslash + 'frac{MP_L}{MP_K} ='}{round(m, 3)}" style="{latex_style}" />
                </div>
                </li>
                </ol>
                </div>""", unsafe_allow_html=True)
    

    st.markdown('---')


    st.markdown(f"""
        <div style="text-align: justify"> 
        Dalším pojmem souvisejícím s produkční funkcí firmy jsou výnosy z rozsahu. Hodnota výnosů z rozsahu nám může ukázat, do jaké míry
        se firmě vyplatí zvyšovat vstupy (náklady) za účelem zvýšení výstupů (produkce). Podmínkou pro určení výnosů z rozsahu je homogenita
        produkční funkce ve všech proměnných. Pokud máme homogenní funkci <img src="{latex_img}{'n'}" style="{latex_style}" />-tého stupně,
        znamená to, že když argument funkce vynásobíme libovolným kladným koeficientem, pak funkční hodnota se vynásobí
        <img src="{latex_img}{'n'}" style="{latex_style}" />-tou mocninou tohoto koeficientu.
        <br>
        <br>
        </div>
        """, unsafe_allow_html=True)


    vynosy_rozsah_definice = f"""
    <div style="{box_style}">
        <b>Určení výnosů z rozsahu</b>:
        Uvažujme produkční funkci homogenní stupně <img src="{latex_img}{'a'}" style="{latex_style}" /> ve všech proměnných.
        Potom výnosy z rozsahu jsou
        <ul style="margin: 0; padding: 0;">
        <li> rostoucí, pokud <img src="{latex_img}{'a > 1'}" style="{latex_style}" /> ,</li>
        <li> klesající, pokud <img src="{latex_img}{'a < 1'}" style="{latex_style}" /> ,</li>
        <li> konstantní, pokud <img src="{latex_img}{'a = 1.'}" style="{latex_style}" /></li>
        </ul>
    </div>
    """

    st.markdown(vynosy_rozsah_definice, unsafe_allow_html=True)


    st.markdown('---')


    st.markdown(f"""<div style="text-align: justify">
                Porovnáme výnosy z rozsahu u tří různých produkčních funkcí (pokud je lze určit):
                <div style="padding: 10px; padding-left: 20px; padding-top: 15px;">
                    <img src="{latex_img}{'Q_1(L, K) = L ' + backslash + 'cdot K'}" style="{latex_style}" />
                <br>
                <br>
                    <img src="{latex_img}{'Q_2(L, K) = L^{' + backslash + 'frac{1}{2}} ' + backslash + 'cdot K^{' + backslash + 'frac{1}{2}}'}" style="{latex_style}" />
                <br>
                <br>
                    <img src="{latex_img}{'Q_3(L, K) = L^{' + backslash + 'frac{1}{2}} + K^{' + backslash + 'frac{1}{2}}'}" style="{latex_style}" />
                </div>
                <br>
                Násobíme argumenty funkcí konstantou <img src="{latex_img}{'c'}" style="{latex_style}" /> :
                <div style="padding: 10px; padding-left: 20px; padding-top: 15px;">
                    <img src="{latex_img}{'Q_1(c ' + backslash + 'cdot L, c ' + backslash + 'cdot K) = (c ' + backslash + 'cdot L) ' + backslash + 'cdot (c ' + backslash + 'cdot K) = c^2 ' + backslash + 'cdot L ' + backslash + 'cdot K = c^2 ' + backslash + 'cdot Q_1(L, K)'}" style="{latex_style}" />
                <br>
                <br>
                    <img src="{latex_img}{'Q_2(c ' + backslash + 'cdot L, c ' + backslash + 'cdot K) = (c ' + backslash + 'cdot L)^{' + backslash + 'frac{1}{2}} ' + backslash + 'cdot (c ' + backslash + 'cdot K)^{' + backslash + 'frac{1}{2}} = c ' + backslash + 'cdot L^{' + backslash + 'frac{1}{2}} ' + backslash + 'cdot K^{' + backslash + 'frac{1}{2}} = c ' + backslash + 'cdot Q_2(L, K)'}" style="{latex_style}" />
                <br>
                <br>
                    <img src="{latex_img}{'Q_3(c ' + backslash + 'cdot L, c ' + backslash + 'cdot K) = (c ' + backslash + 'cdot L)^{' + backslash + 'frac{1}{2}} + (c ' + backslash + 'cdot K)^{' + backslash + 'frac{1}{2}} = c^{' + backslash + 'frac{1}{2}} ' + backslash + 'cdot ' + backslash + 'left( L^{' + backslash + 'frac{1}{2}} + K^{' + backslash + 'frac{1}{2}} ' + backslash + 'right) = c^{' + backslash + 'frac{1}{2}} ' + backslash + 'cdot Q_3(L, K)'}" style="{latex_style}" />
                </div>
                <br>
                Vidíme, že všechny tři produkční funkce jsou homogenní ve všech proměnných. Funkce
                <img src="{latex_img}{'Q_1'}" style="{latex_style}" /> je homogenní stupně <img src="{latex_img}{'2'}" style="{latex_style}" /> a
                funkce <img src="{latex_img}{'Q_2'}" style="{latex_style}" /> je homogenní stupně <img src="{latex_img}{'1'}" style="{latex_style}" /> a
                funkce <img src="{latex_img}{'Q_3'}" style="{latex_style}" /> je homogenní stupně <img src="{latex_img}{backslash + 'tiny{' + backslash + 'frac{1}{2}}'}" style="{latex_style}" /> .
                Podle výše uvedených pravidel můžeme tedy určit, že první produkční funkce má rostoucí výnosy z rozsahu, druhá funkce má konstantní
                výnosy z rozsahu a třetí funkce má klesající výnosy z rozsahu.
                </div>""", unsafe_allow_html=True)


    st.markdown('---')


    # Graf porovnávající produkční funkce
    st.markdown(f"""<div style="text-align: justify">
                Grafické porovnání výnosů z rozsahu u produkčních funkcí <img src="{latex_img}{'Q_1'}" style="{latex_style}" /> ,
                <img src="{latex_img}{'Q_2'}" style="{latex_style}" /> a <img src="{latex_img}{'Q_3'}" style="{latex_style}" /> :
                <br>
                <br>
                </div>""", unsafe_allow_html=True)

    # Rozsah grafu
    x2 = np.linspace(0.001, 8, 200)

    # Vytvoříme graf
    fig2, ax2 = plt.subplots()

    # Q1
    ax2.plot(x2, x2**2, color='#EE7708', label='$Q_1$')
    ax2.text(1.7, 6.7, '$a_1 = 2$', color='#EE7708')

    # Q2
    ax2.plot(x2, x2, color='#6473AC', label='$Q_2$')
    ax2.text(5.7, 6.7, '$a_2 = 1$', color='#6473AC')

    # Q3
    ax2.plot(x2, 2*x2**0.5, color='#F287D0', label='$Q_3$')
    ax2.text(5.7, 4.3, '$a_3 = ' + backslash + 'frac{1}{2}$', color='#F287D0')

    # Prvky grafu
    font_properties = {'fontsize': 12, 'fontweight': 'bold', 'fontfamily': 'sans-serif'}

    ax2.set_xlabel('L / K', fontdict=font_properties)
    ax2.set_ylabel('Q', fontdict=font_properties, rotation=0)
    plt.gca().xaxis.set_label_coords(0.975, -0.075)
    plt.gca().yaxis.set_label_coords(-0.04, 1.03)
    ax2.grid(True)
    ax2.set_xlim(0, 8)
    ax2.set_ylim(0, 8)

    ax2.legend(loc='lower right', fontsize=12, facecolor='#0E1117')

    st.pyplot(fig2)


    st.markdown('---')


    scroll_top()



def min_naklady():
    st.markdown("<div id='linkto_top'></div>", unsafe_allow_html=True)

    left_button, center_button, right_button = st.columns([1.5, 0.82, 1])

    with left_button:
        if st.button('← 2.1 Produkční funkce firmy', key='1'):
            st.session_state.page = 'prod_fun'
            st.rerun()

    with center_button:
        if st.button('↑ Domů', key='2'):
            st.session_state.page = 'uvod'
            st.rerun()

    with right_button:
        if st.button('2.3 Maximalizace zisku →', key='3'):
            st.session_state.page = 'max_zisk'
            st.rerun()


    st.markdown('---')


    st.subheader('2.2 Minimalizace nákladů')
    st.markdown(f"""
        <div style="text-align: justify"> 
        Každá efektivní firma se snaží minimalizovat své náklady. Nejprve si definujeme úlohu minimalizace nákladů a následně se podíváme
        na další pojmy související s minimalizací nákladů.
        <br>
        <br>
        </div>
        """, unsafe_allow_html=True)



    min_naklady_definice = f"""
    <div style="{box_style}">
        <b>Definice úlohy minimalizace nákladů firmy</b>: 
        Úloha minimalizace nákladů firmy znamená nalezení
            <div style="padding: 15px; padding-left: 20px;">
                <img src="{latex_img}{backslash + 'min_{L, K}   w ' + backslash + 'cdot L + r ' + backslash + 'cdot K'}" style="{latex_style}" />
            </div>
        za podmínky
            <div style="padding: 15px; padding-left: 20px;">
                <img src="{latex_img}{'Q(L, K) = Q_0'}" style="{latex_style}" /> ,
            </div>
        kde <img src="{latex_img}{'w'}" style="{latex_style}" /> je cena práce, <img src="{latex_img}{'r'}" style="{latex_style}" />
        je cena kapitálu, <img src="{latex_img}{'Q(L, K)'}" style="{latex_style}" /> je produkční funkce firmy a
        <img src="{latex_img}{'Q_0'}" style="{latex_style}" /> je dané množství zboží, které má firma vyrobit (tj. požadovaná produkce).
    </div>
    """

    st.markdown(min_naklady_definice, unsafe_allow_html=True)

    st.markdown(f"""
        <div style="text-align: justify">
        <br>
        Můžeme pozorovat, že z matematického hlediska se jedná o stejnou úlohu, jako je Hicksova úloha. Pouze zde figurují jiné
        proměnné, které se týkají firmy a ne spotřebitele. Firma minimalizuje své náklady a maximalizuje produkci, zatímco spotřebitel
        minimalizuje své výdaje a maximalizuje užitek. Optimální kombinaci množství výrobních faktorů lze tedy nalézt obdobně
        jako u Hicksovy úlohy pomocí metody Lagrangeových multiplikátorů. Zopakujeme stejný postup, jenom nahradíme proměnné a místo
        užitkové funkce použijeme produkční funkci.
        <br>
        <br>
        </div>
        """, unsafe_allow_html=True)


    min_naklady_veta = f"""
    <div style="{box_style}">
        <b>Věta</b>: 
        Firma minimalizuje náklady na výrobu, jestliže se poměr cen
        výrobních faktorů rovná poměru mezních produktivit výrobních faktorů, tj. musí platit
            <div style="padding: 15px; padding-left: 20px;">
                <img src="{latex_img}{backslash + 'frac{MP_L}{MP_K} = ' + backslash + 'frac{w}{r}'}" style="{latex_style}" /> ,
            </div>
        přičemž do této rovnosti lze zakomponovat i mezní míru technické substituce
            <div style="padding: 15px; padding-left: 20px;">
                <img src="{latex_img}{'MR' + backslash + 'hspace{2pt}TS = -' + backslash + 'frac{MP_L}{MP_K} = -' + backslash + 'frac{w}{r}'}" style="{latex_style}" /> .
            </div>
    </div>
    """

    st.markdown(min_naklady_veta, unsafe_allow_html=True)


    st.markdown('---')


    # Boční panel pro zadání parametrů
    w = st.sidebar.slider('Cena práce $w$', min_value=1.0, max_value=10.0, value=5.0, step=0.1)

    r = st.sidebar.slider('Cena kapitálu $r$', min_value=1.0, max_value=10.0, value=5.0, step=0.1)

    Q_0 = st.sidebar.slider('Výstup firmy $Q_0$', min_value=1.0, max_value=10.0, value=5.0, step=0.1)

    c = st.sidebar.slider('Parametry $c$ a $d$', min_value=0.01, max_value=0.99, value=0.5, step=0.01)
    d = round(1 - c, 2)


    # Shrnutí zadaných parametrů
    parameters = f"""<div style="{box_style}">
                    <img src="{latex_img}{'w='}{w}" style="{latex_style}" />
                    <br>
                    <img src="{latex_img}{'r='}{r}" style="{latex_style}" />
                    <br>
                    <img src="{latex_img}{'Q_0='}{Q_0}" style="{latex_style}" />
                    <br>
                    <img src="{latex_img}{'c='}{c}" style="{latex_style}" />
                    <br>
                    <img src="{latex_img}{'d='}{d}" style="{latex_style}" />
                </div>"""
    st.sidebar.markdown(parameters, unsafe_allow_html=True)


    # Graf produkční funkce
    st.markdown(f"""<div style="text-align: justify">
                V bočním panelu si nastavte ceny výrobních faktorů, požadovanou produkci firmy a parametry produkční funkce.
                Graf produkční funkce firmy, na němž je zobrazena optimální kombinace výrobních faktorů
                <img src="{latex_img}{'L'}" style="{latex_style}" /> a <img src="{latex_img}{'K'}" style="{latex_style}" />
                pro minimalizaci nákladů při pevně stanovených cenách práce a kapitálu –  <img src="{latex_img}{'w'}" style="{latex_style}" />,
                <img src="{latex_img}{'r'}" style="{latex_style}" /> :
                <br>
                <br>
                </div>""", unsafe_allow_html=True)

    # Rozsah grafu
    scope = int(round((22/(w*r))*Q_0*np.mean([w, r]), 0))
    x = np.linspace(0.001, scope, scope*50)

    # Vytvoříme graf
    fig, ax = plt.subplots()

    # Cobb-Douglasova produkční funkce
    ax.plot(x, (Q_0 / x**c)**(1/d), color='#EE7708', label='$Q_1$')

    # Kombinace výrobních faktorů minimalizující náklady
    L_optimal = Q_0 * ((c*r) / (d*w))**d
    K_optimal = Q_0 * ((d*w) / (c*r))**c

    # Tečna produkční funkce
    slope = -w / r
    line_equation = lambda x: slope * (x - L_optimal) + K_optimal
    ax.plot(x, line_equation(x), color='#6473AC')
    
    # Vyznačení optima
    C_min = w * L_optimal + r * K_optimal
    ax.scatter(L_optimal, K_optimal, color='red')
    ax.text(L_optimal + 0.1*K_optimal, K_optimal + 0.1*L_optimal, f'({L_optimal:.2f}, {K_optimal:.2f})', color='white', fontsize=10)

    
    # Prvky grafu
    font_properties = {'fontsize': 12, 'fontweight': 'bold', 'fontfamily': 'sans-serif'}

    ax.set_xlabel('L', fontdict=font_properties)
    ax.set_ylabel('K', fontdict=font_properties, rotation=0)
    plt.gca().xaxis.set_label_coords(1, -0.075)
    plt.gca().yaxis.set_label_coords(-0.05, 1.02)
    ax.grid(True)
    ax.set_xlim(0, scope)
    ax.set_ylim(0, scope)
    
    handles = [plt.Line2D([], [], color='#EE7708', label='$Q(L, K) = L^c ' + backslash + 'cdot K^d$'),
               plt.Line2D([], [], color='#6473AC', label='$w ' + backslash + 'cdot L + r ' + backslash + 'cdot K = TC$'),
               plt.scatter([], [], color='red', label=f'Minimální náklady\n{'min $TC$'} = {round(C_min, 2)}')]
    ax.legend(handles=handles, loc='upper right', fontsize=9, facecolor='#0E1117')

    st.pyplot(fig)


    st.markdown('---')


    podmin_poptavka_definice = f"""
    <div style="{box_style}">
        <b>Definice podmíněné poptávky</b>:
        Podmíněná poptávka firmy po výrobním faktoru <img src="{latex_img}{'X'}" style="{latex_style}" />
        udává množství výrobního faktoru <img src="{latex_img}{'X'}" style="{latex_style}" /> nakupovaného firmou v závislosti na
        ceně všech výrobních faktorů firmy a požadovaném objemu produkce. 
    </div>
    """

    st.markdown(podmin_poptavka_definice, unsafe_allow_html=True)

    st.markdown(f"""
        <div style="text-align: justify">
        <br>
        Na základě této definice vidíme, že podmíněná poptávka je obdobou Hicksovy poptávky, přičemž se jedná o poptávku z pohledu firmy,
        nikoliv spotřebitele.
        </div>
        """, unsafe_allow_html=True)


    st.markdown('---')


    st.markdown(f"""
        <div style="text-align: justify">
        Na základě údajů nastavených v bočním panelu si nyní spočítáme podmíněné poptávky po výrobních faktorech
        <img src="{latex_img}{'K'}" style="{latex_style}" /> a <img src="{latex_img}{'L'}" style="{latex_style}" /> .
        <br>
        <br>
        Budeme opět uvažovat Cobb-Douglasovu produkční funkci ve tvaru
        <div style="padding: 10px; padding-left: 20px;">
        <img src="{latex_img}{'Q(L, K) = L^c ' + backslash + 'cdot K^d'}" style="{latex_style}" />
        </div>
        </div>""", unsafe_allow_html=True)

    st.markdown('s parametry $c$ a $d$, přičemž $c+d=1$ a zároveň $c, d > 0$.')


    st.markdown('---')


    st.markdown(f"""<div style="text-align: justify">
                V následujících krocích si ukážeme, jak probíhá výpočet podmíněných poptávek.
                <br>
                <br>
                <ol>
                <li>Nejprve sestavíme Langrangeovu funkci, jež má tvar
                <div style="padding: 10px; padding-left: 20px;">
                <img src="{latex_img}{backslash + 'mathcal{L} = w ' + backslash + 'cdot L + r ' + backslash + 'cdot K + ' + backslash + 'lambda(L^c ' + backslash + 'cdot K^d - Q_0)'}" style="{latex_style}" /> .
                </div>
                </li>
                <br>
                <li>Určíme si parciální derivace této funkce a položíme je rovny nule
                <div style="padding: 10px; padding-left: 20px; padding-top: 15px;">
                    <img src="{latex_img}{backslash + 'frac{' + backslash + 'partial ' + backslash + 'mathcal{L} (L, K, ' + backslash + 'lambda)}{' + backslash + 'partial L} = w + ' + backslash + 'frac{' + backslash + 'lambda ' + backslash + 'cdot c ' + backslash + 'cdot K^d}{L^d} = 0'}" style="{latex_style}" />
                <br>
                <br>
                    <img src="{latex_img}{backslash + 'frac{' + backslash + 'partial ' + backslash + 'mathcal{L} (L, K, ' + backslash + 'lambda)}{' + backslash + 'partial K} = r + ' + backslash + 'frac{' + backslash + 'lambda ' + backslash + 'cdot d ' + backslash + 'cdot L^c}{K^c} = 0'}" style="{latex_style}" />
                <br>
                <br>
                    <img src="{latex_img}{backslash + 'frac{' + backslash + 'partial ' + backslash + 'mathcal{L} (L, K, ' + backslash + 'lambda)}{' + backslash + 'partial ' + backslash + 'lambda} = L^c ' + backslash + 'cdot K^d - Q_0 = 0'}" style="{latex_style}" /> .
                </div>
                </li>
                <br>
                <li>Vyjádříme Lagrangeův multiplikátor
                <div style="padding: 10px; padding-left: 20px; padding-top: 15px; padding-bottom: 15px;">
                <img src="{latex_img}{backslash + 'lambda = -' + backslash + 'frac{w ' + backslash + 'cdot L^d}{c ' + backslash + 'cdot K^d} = -' + backslash + 'frac{r ' + backslash + 'cdot K^c}{d ' + backslash + 'cdot L^c}'}" style="{latex_style}" />
                </div>
                a z této rovnosti vyjádříme
                <div style="padding: 10px; padding-left: 20px; padding-top: 15px;">
                <img src="{latex_img}{'K = ' + backslash + 'frac{d ' + backslash + 'cdot w ' + backslash + 'cdot L}{c ' + backslash + 'cdot r}'}" style="{latex_style}" /> .
                </div>
                </li>
                <br>
                <li>Dosadíme do užitkové funkce
                <div style="padding: 10px; padding-left: 20px; padding-top: 15px; padding-bottom: 15px;">
                <img src="{latex_img}{'L^c ' + backslash + 'cdot ' + backslash + 'left( ' + backslash + 'frac{d ' + backslash + 'cdot w ' + backslash + 'cdot L}{c ' + backslash + 'cdot r} ' + backslash + 'right)^d = Q_0'}" style="{latex_style}" />
                </div>
                a vyjádříme
                <div style="padding: 10px; padding-left: 20px; padding-top: 15px;">
                    <img src="{latex_img}{'L = Q_0 ' + backslash + 'cdot ' + backslash + 'left( ' + backslash + 'frac{c ' + backslash + 'cdot r}{d ' + backslash + 'cdot w} ' + backslash + 'right)^d ='}{round(L_optimal, 2)}" style="{latex_style}" />
                <br>
                <br>
                    <img src="{latex_img}{'K = Q_0 ' + backslash + 'cdot ' + backslash + 'left( ' + backslash + 'frac{d ' + backslash + 'cdot w}{c ' + backslash + 'cdot r} ' + backslash + 'right)^c ='}{round(K_optimal, 2)}" style="{latex_style}" />
                </div>
                </li>
                <br>
                <li> Podmíněná poptávka po práci je <img src="{latex_img}{round(L_optimal, 2)}" style="{latex_style}" />
                a podmíněná poptávka po kapitálu je <img src="{latex_img}{round(K_optimal, 2)}" style="{latex_style}" /> pro danou firmu.
                </li>
                </ol>
                </div>""", unsafe_allow_html=True)


    st.markdown('---')


    stezka_produktu_definice = f"""
    <div style="{box_style}">
        <b>Definice dlouhodobé stezky expanze produktu</b>:
        Dlouhodobá stezka expanze produktu je množina optimálních kombinací výrobních faktorů firmy při jejich
        konstantních cenách a při různých úrovních výstupu.
    </div>
    """

    st.markdown(stezka_produktu_definice, unsafe_allow_html=True)

    st.markdown(f"""
        <div style="text-align: justify">
        <br>
        Expanze produktu znamená, že se zvyšuje vyráběné množství tohoto produktu (tj. produkce). Jednotlivé úrovně produkce můžeme znázornit
        jako izokvanty v grafu, přičemž izokvanta je křivka zahrnující všechny možné kombinace množství výrobních faktorů pro konkrétní
        úroveň produkce neboli požadovaný výstup firmy. Dlouhodobá stezka expanze produktu je tedy přímka procházející všemi optimálními
        kombinacemi množství výrobních faktorů na každé izokvantě.
        </div>
        """, unsafe_allow_html=True)


    st.markdown('---')


    # Graf dlouhodobé stezky expanze produktu
    st.markdown(f"""<div style="text-align: justify">
                V bočním panelu si nastavte ceny výrobních faktorů, jednu konkrétní úroveň produkce firmy a parametry
                Cobb-Douglasovy produkční funkce.
                Graf dlouhodobé stezky expanze produktu, na němž jsou zobrazeny optimální kombinace výrobních faktorů
                <img src="{latex_img}{'L'}" style="{latex_style}" /> a <img src="{latex_img}{'K'}" style="{latex_style}" />
                pro minimalizaci nákladů při pevně stanovených cenách práce a kapitálu –  <img src="{latex_img}{'w'}" style="{latex_style}" />,
                <img src="{latex_img}{'r'}" style="{latex_style}" /> – pro různé úrovně produkce:
                <br>
                <br>
                </div>""", unsafe_allow_html=True)

    # Vypnutí a zapnutí popisků
    _, align_switch = st.columns([3.5, 1])
    with align_switch:
        labels_switch = st.toggle('Zobrazit údaje')

    y = np.linspace(0, scope, scope*20)

    # Vytvoříme graf
    fig2, ax2 = plt.subplots()

    # Cobb-Douglasova produkční funkce
    L, K = np.meshgrid(x, y)
    Q = L**c * K**d

    # Izokvanty
    izo = [Q_0 + x*(scope/9) for x in range(-8, 9)]
    ax2.contour(L, K, Q, levels=izo, colors='#7A7A7A', linestyles='dashed', alpha=0.75)

    # Optimální kombinace výrobních faktorů pro různé izokvanty
    L_optimals = np.array(izo) * ((c*r) / (d*w))**d
    K_optimals = np.array(izo) * ((d*w) / (c*r))**c

    # Dlouhodobá stezka expanze produktu
    slope2 = (d*w) / (c*r)
    ax2.plot(x, slope2*x, color='#6473AC')
    
    # Vyznačení optima
    Q_levels = w * L_optimals + r * K_optimals
    ax2.scatter(L_optimals, K_optimals, color='red')

    for i, C_min in enumerate(Q_levels):
        if C_min >= 0 and L_optimals[i] < scope and K_optimals[i] < scope and labels_switch:
            add_label = f'({round(L_optimals[i], 2)}, {round(K_optimals[i], 2)})\n$Q=${round(L_optimals[i]**c * K_optimals[i]**d, 2)}\n$TC=${round(C_min, 2)}'
            ax2.text(L_optimals[i], K_optimals[i], add_label, color='white', fontsize=5.5, bbox=dict(facecolor='#0E1117', edgecolor='grey', linewidth=0.3, alpha=0.6))

    # Prvky grafu
    font_properties = {'fontsize': 12, 'fontweight': 'bold', 'fontfamily': 'sans-serif'}

    ax2.set_xlabel('L', fontdict=font_properties)
    ax2.set_ylabel('K', fontdict=font_properties, rotation=0)
    plt.gca().xaxis.set_label_coords(1, -0.075)
    plt.gca().yaxis.set_label_coords(-0.05, 1.02)
    ax2.grid(True)
    ax2.set_xlim(0, scope)
    ax2.set_ylim(0, scope)
    
    handles = [plt.Line2D([], [], color='#6473AC', label='Dlouhodobá stezka\nexpanze produktu'),
               plt.Line2D([], [], linestyle='dashed', color='#7A7A7A', alpha=0.75, label='Izokvanty pro $Q ' + backslash + 'in ' + backslash + 'mathbb{R}^{+}_0$'),
               plt.scatter([], [], color='red', label=f'Minimální náklady\nmin {'$w ' + backslash + 'cdot L + r ' + backslash + 'cdot K$'} pro {'$Q ' + backslash + 'in ' + backslash + 'mathbb{R}^{+}_0$'}')]
    legend_pos = 'upper left' if slope2 < 1.5 else 'lower right'
    ax2.legend(handles=handles, loc=legend_pos, fontsize=9, facecolor='#0E1117')

    st.pyplot(fig2)


    st.markdown('---')


    st.markdown(f"""<div style="text-align: justify">
                Rovnici dlouhodobé stezky expanze produktu pro danou firmu určíme následujícím způsobem:
                <br>
                <br>
                <ol>
                <li>Využijeme již odvozené podmíněné poptávky po výrobních faktorech
                <div style="padding: 10px; padding-left: 20px; padding-top: 15px;">
                    <img src="{latex_img}{'L = Q_0 ' + backslash + 'cdot ' + backslash + 'left( ' + backslash + 'frac{c ' + backslash + 'cdot r}{d ' + backslash + 'cdot w} ' + backslash + 'right)^d'}" style="{latex_style}" />
                <br>
                <br>
                    <img src="{latex_img}{'K = Q_0 ' + backslash + 'cdot ' + backslash + 'left( ' + backslash + 'frac{d ' + backslash + 'cdot w}{c ' + backslash + 'cdot r} ' + backslash + 'right)^c'}" style="{latex_style}" /> .
                </div>
                </li>
                <br>
                <li>Vyjádříme z obou rovnic produkci <img src="{latex_img}{'Q_0'}" style="{latex_style}" />
                <div style="padding: 10px; padding-left: 20px; padding-top: 15px;">
                    <img src="{latex_img}{'Q_0 = L ' + backslash + 'cdot ' + backslash + 'left( ' + backslash + 'frac{d ' + backslash + 'cdot w}{c ' + backslash + 'cdot r} ' + backslash + 'right)^d'}" style="{latex_style}" />
                <br>
                <br>
                    <img src="{latex_img}{'Q_0 = K ' + backslash + 'cdot ' + backslash + 'left( ' + backslash + 'frac{c ' + backslash + 'cdot r}{d ' + backslash + 'cdot w} ' + backslash + 'right)^c'}" style="{latex_style}" /> .
                </div>
                </li>
                <br>
                <li>Máme rovnost
                <div style="padding: 10px; padding-left: 20px; padding-top: 15px; padding-bottom: 15px;">
                <img src="{latex_img}{'L ' + backslash + 'cdot ' + backslash + 'left( ' + backslash + 'frac{d ' + backslash + 'cdot w}{c ' + backslash + 'cdot r} ' + backslash + 'right)^d = K ' + backslash + 'cdot ' + backslash + 'left( ' + backslash + 'frac{c ' + backslash + 'cdot r}{d ' + backslash + 'cdot w} ' + backslash + 'right)^c'}" style="{latex_style}" />
                </div>
                a z této rovnosti vyjádříme <img src="{latex_img}{'K'}" style="{latex_style}" />
                <div style="padding: 10px; padding-left: 20px; padding-top: 15px;">
                <img src="{latex_img}{'K = L ' + backslash + 'cdot ' + backslash + 'left( ' + backslash + 'frac{d ' + backslash + 'cdot w}{c ' + backslash + 'cdot r} ' + backslash + 'right)^{d+c} = ' + backslash + 'frac{L ' + backslash + 'cdot d ' + backslash + 'cdot w}{c ' + backslash + 'cdot r}'}" style="{latex_style}" /> .
                </div>
                </li>
                <br>
                <li>Získali jsme rovnici dlouhodobé stezky expanze produktu
                <div style="padding: 10px; padding-left: 20px; padding-top: 15px;">
                <img src="{latex_img}{'K = ' + backslash + 'frac{L ' + backslash + 'cdot d ' + backslash + 'cdot w}{c ' + backslash + 'cdot r}'}" style="{latex_style}" /> .
                </div>
                </li>
                </ol>
                </div>""", unsafe_allow_html=True)


    st.markdown('---')


    LAC_definice = f"""
    <div style="{box_style}">
        <b>Definice funkce průměrných nákladů</b>:
        Funkci průměrných nákladů určíme ze vztahu
        <div style="padding: 10px; padding-left: 20px; padding-top: 15px;">
        <img src="{latex_img}{'LAC(w, r, Q) = ' + backslash + 'frac{LTC(w, r, Q)}{Q}'}" style="{latex_style}" /> ,
        </div>
        kde <img src="{latex_img}{'Q'}" style="{latex_style}" /> je objem produkce a
        <img src="{latex_img}{'LTC(w, r, Q)'}" style="{latex_style}" /> jsou celkové náklady.
    </div>
    """

    st.markdown(LAC_definice, unsafe_allow_html=True)

    st.html('<br>')

    LMC_definice = f"""
    <div style="{box_style}">
        <b>Definice funkce mezních nákladů</b>:
        Funkci mezních nákladů určíme ze vztahu
        <div style="padding: 10px; padding-left: 20px; padding-top: 15px;">
        <img src="{latex_img}{'LMC(w, r, Q) = ' + backslash + 'frac{' + backslash + 'partial LTC(w, r, Q)}{' + backslash + 'partial Q}'}" style="{latex_style}" /> ,
        </div>
        kde <img src="{latex_img}{'Q'}" style="{latex_style}" /> je objem produkce a
        <img src="{latex_img}{'LTC(w, r, Q)'}" style="{latex_style}" /> jsou celkové náklady.
    </div>
    """

    st.markdown(LMC_definice, unsafe_allow_html=True)


    st.markdown('---')


    scroll_top()



def max_zisk():
    st.markdown("<div id='linkto_top'></div>", unsafe_allow_html=True)

    left_button, right_button = st.columns([7.07, 1])

    with left_button:
        if st.button('← 2.2 Minimalizace nákladů', key='1'):
            st.session_state.page = 'min_naklady'
            st.rerun()

    with right_button:
        if st.button('Domů →', key='2'):
            st.session_state.page = 'uvod'
            st.rerun()


    st.markdown('---')


    st.subheader('2.3 Maximalizace zisku')
    st.markdown(f"""
        <div style="text-align: justify"> 
        Při úloze maximalizace zisku musíme o vyráběném objemu zboží rozhodnout. Stále
        však máme na paměti naše úvahy o minimalizaci nákladů a tento objem zboží chceme
        vyrobit co nejlevněji.
        <br>
        <br>
        </div>
        """, unsafe_allow_html=True)



    funkce_zisk_definice = f"""
    <div style="{box_style}">
        <b>Definice funkce zisku</b>: 
        Funkce zisku <img src="{latex_img}{backslash + 'pi'}" style="{latex_style}" /> udává zisk firmy v závislosti na
        ceně práce <img src="{latex_img}{'w'}" style="{latex_style}" />, ceně kapitálu
        <img src="{latex_img}{'r'}" style="{latex_style}" /> a prodejní ceně zboží <img src="{latex_img}{'P'}" style="{latex_style}" /> .           
    </div>
    """

    st.markdown(funkce_zisk_definice, unsafe_allow_html=True)

    st.markdown(f"""
        <div style="text-align: justify">
        <br>
        Existují dva způsoby, jak řešit úlohu maximalizace zisku:
        </div>
        """, unsafe_allow_html=True)
                
    metoda = st.radio('x', ['Dvoustupňová metoda', 'Přímá metoda'], label_visibility='hidden')
        
    st.markdown(f"""
        <div style="text-align: justify">
        Dvoustupňová metoda předpokládá, že nejprve budeme řešit úlohu minimalizace nákladů (nebo využijeme již existující řešení této úlohy)
        a teprve potom se zaměříme na maximalizaci zisku. Naopak přímá metoda předpokládá, že při řešení maximalizace zisku se přímo
        řídíme produkční funkcí. Dvoustupňová metoda je tedy náročnější výpočetně, ale přímá metoda nám neposkytne informace o
        nákladové funkci <img src="{latex_img}{'LTC(w, r, Q)'}" style="{latex_style}" />. Probereme obě metody.
        </div>
        """, unsafe_allow_html=True)


    st.markdown('---')


    # Boční panel pro zadání parametrů
    if metoda == 'Dvoustupňová metoda':
        P = st.sidebar.slider('Prodejní cena $P$', min_value=500, max_value=5000, value=2500, step=1)

        LFC = st.sidebar.slider('Fixní náklady $LFC$', min_value=10, max_value=1000, value=500, step=1)

        LVC = st.sidebar.slider('Variabilní náklady $LVC$', min_value=10, max_value=1000, value=500, step=1)

        c = st.sidebar.slider('Parametr $c$', min_value=2.0, max_value=5.0, value=3.0, step=0.01)


        # Shrnutí zadaných parametrů
        parameters = f"""<div style="{box_style}">
                        <img src="{latex_img}{'P='}{P}" style="{latex_style}" />
                        <br>
                        <img src="{latex_img}{'LFC='}{LFC}" style="{latex_style}" />
                        <br>
                        <img src="{latex_img}{'LVC='}{LVC}" style="{latex_style}" />
                        <br>
                        <img src="{latex_img}{'c='}{c}" style="{latex_style}" />
                    </div>"""
        st.sidebar.markdown(parameters, unsafe_allow_html=True)

        
        metoda2_definice = f"""
        <div style="{box_style}">
            <b>Definice dvoustupňové metody</b>: 
            Dvoustupňová metoda maximalizace zisku firmy předpokládá nejprve minimalizaci nákladů (tj. odvození funkce
            <img src="{latex_img}{'LTC'}" style="{latex_style}" />). Poté řešíme úlohu
                <div style="padding: 15px; padding-left: 20px;">
                    <img src="{latex_img}{backslash + 'max_Q   ' + backslash + 'pi = P ' + backslash + 'cdot Q - LTC(w, r, Q)'}" style="{latex_style}" />
                </div>
            za podmínky
                <div style="padding: 15px; padding-left: 20px;">
                    <img src="{latex_img}{'Q ' + backslash + 'geq 0'}" style="{latex_style}" /> ,
                </div>
            kde <img src="{latex_img}{backslash + 'pi'}" style="{latex_style}" /> je funkce zisku, <img src="{latex_img}{'P'}" style="{latex_style}" />
            je prodejní cena zboží, <img src="{latex_img}{'Q'}" style="{latex_style}" /> je výstup (produkce) a
            <img src="{latex_img}{'LTC(w, r, Q)'}" style="{latex_style}" /> je nákladová funkce určená ještě pomocí cen výrobních faktorů
            <img src="{latex_img}{'w, '}" style="{latex_style}" /> .
        </div>
        """

        st.markdown(metoda2_definice, unsafe_allow_html=True)


        zisk = round(P*(P/(c*LVC))**(1/(c-1)) - LFC - LVC*(P/(c*LVC))**(c/(c-1)), 2)
        st.markdown(f"""<div style="text-align: justify">
                    <br>
                    Budeme uvažovat jednoduchou nákladovou funkci
                    <div style="padding: 15px; padding-left: 20px;">
                    <img src="{latex_img}{'LTC = LFC + LVC ' + backslash + 'cdot Q^c'}" style="{latex_style}" /> ,
                    </div>
                    kde <img src="{latex_img}{'LFC'}" style="{latex_style}" /> jsou fixní náklady,
                    <img src="{latex_img}{'LVC'}" style="{latex_style}" /> jsou variabilní náklady na jednotku zboží a
                    <img src="{latex_img}{'c'}" style="{latex_style}" /> je parametr produkce.
                    Po dosazení tedy máme funkci zisku v tomto tvaru
                    <div style="padding: 15px; padding-left: 20px;">
                    <img src="{latex_img}{backslash + 'pi(Q) = P ' + backslash + 'cdot Q - LFC - LVC ' + backslash + 'cdot Q^c'}" style="{latex_style}" /> .
                    </div>
                    V bočním panelu si nastavte prodejní cenu, parametr <img src="{latex_img}{'c'}" style="{latex_style}" />,
                    fixní náklady a variabilní náklady. Následně hledáme optimální vyráběné množství <img src="{latex_img}{'Q'}" style="{latex_style}" />.
                    Určíme první derivaci funkce zisku a položíme ji rovnou <img src="{latex_img}{'0'}" style="{latex_style}" />
                    <div style="padding: 15px; padding-left: 20px;">
                    <img src="{latex_img}{backslash + 'frac{' + backslash + 'partial ' + backslash + 'pi}{' + backslash + 'partial Q} = P - c ' + backslash + 'cdot LVC ' + backslash + 'cdot Q^{c-1} = 0'}" style="{latex_style}" /> ,
                    </div>
                    potom vyjádříme <img src="{latex_img}{'Q'}" style="{latex_style}" />
                    <div style="padding: 15px; padding-left: 20px;">
                    <img src="{latex_img}{'Q = ' + backslash + 'left( ' + backslash + 'frac{P}{c ' + backslash + 'cdot LVC} ' + backslash + 'right)^{' + backslash + 'frac{1}{c-1}}'}" style="{latex_style}" /> ,
                    </div>
                    dosadíme optimální množství vyrobeného zboží do funkce zisku a vypočítáme zisk firmy
                    <div style="padding: 15px; padding-left: 20px;">
                    <img src="{latex_img}{backslash + 'pi(Q) = P ' + backslash + 'cdot ' + backslash + 'left( ' + backslash + 'frac{P}{c ' + backslash + 'cdot LVC} ' + backslash + 'right)^{' + backslash + 'frac{1}{c-1}} - LFC - LVC ' + backslash + 'cdot ' + backslash + 'left( ' + backslash + 'frac{P}{c ' + backslash + 'cdot LVC} ' + backslash + 'right)^{' + backslash + 'frac{c}{c-1}} ='}{zisk}" style="{latex_style}" />
                    </div>
                    </div>""", unsafe_allow_html=True)

    else:

        P = st.sidebar.slider('Prodejní cena $P$', min_value=500, max_value=5000, value=2500, step=1)

        w = st.sidebar.slider('Cena práce $w$', min_value=10, max_value=1000, value=500, step=1)

        r = st.sidebar.slider('Cena kapitálu $r$', min_value=10, max_value=1000, value=500, step=1)

        c = st.sidebar.slider('Parametry $c$ a $d$', min_value=0.01, max_value=0.99, value=0.5, step=0.01)
        d = round(1 - c, 2)


        # Shrnutí zadaných parametrů
        parameters = f"""<div style="{box_style}">
                        <img src="{latex_img}{'P='}{P}" style="{latex_style}" />
                        <br>
                        <img src="{latex_img}{'w='}{w}" style="{latex_style}" />
                        <br>
                        <img src="{latex_img}{'r='}{r}" style="{latex_style}" />
                        <br>
                        <img src="{latex_img}{'c='}{c}" style="{latex_style}" />
                        <br>
                        <img src="{latex_img}{'d='}{d}" style="{latex_style}" />
                    </div>"""
        st.sidebar.markdown(parameters, unsafe_allow_html=True)

        metoda1_definice = f"""
        <div style="{box_style}">
            <b>Definice přímé metody</b>: 
            Přímou metodou při maximalizaci zisku firmy máme na mysli řešení následující úlohy
                <div style="padding: 15px; padding-left: 20px;">
                    <img src="{latex_img}{backslash + 'max_{K, L}   ' + backslash + 'pi = P ' + backslash + 'cdot Q(L, K) - w ' + backslash + 'cdot L - r ' + backslash + 'cdot K'}" style="{latex_style}" />
                </div>
            za podmínek
                <div style="padding: 15px; padding-left: 20px;">
                    <img src="{latex_img}{'L ' + backslash + 'geq 0'}" style="{latex_style}" /> , <img src="{latex_img}{'K ' + backslash + 'geq 0'}" style="{latex_style}" /> ,
                </div>
            kde <img src="{latex_img}{backslash + 'pi'}" style="{latex_style}" /> je funkce zisku, <img src="{latex_img}{'P'}" style="{latex_style}" />
            je prodejní cena zboží, <img src="{latex_img}{'Q'}" style="{latex_style}" /> je produkční funkce,
            <img src="{latex_img}{'L'}" style="{latex_style}" /> je práce, <img src="{latex_img}{'K'}" style="{latex_style}" /> je kapitál,
            <img src="{latex_img}{'w'}" style="{latex_style}" /> a <img src="{latex_img}{'r'}" style="{latex_style}" /> jsou ceny těchto výrobních faktorů.
        </div>
        """

        st.markdown(metoda1_definice, unsafe_allow_html=True)


        zisk = round(P - w*((c*r)/(d*w))**d - r*((d*w)/(c*r))**c, 2)
        st.markdown(f"""<div style="text-align: justify">
                    <br>
                    Budeme uvažovat jednoduchou Cobb-Douglasovu produkční funkci
                    <div style="padding: 15px; padding-left: 20px;">
                    <img src="{latex_img}{'Q(L, K) = L^c ' + backslash + 'cdot K^d'}" style="{latex_style}" /> ,
                    </div>
                    </div>""", unsafe_allow_html=True)
        
        st.markdown("""s parametry $c$ a $d$, přičemž $c+d=1$ a $c, d > 0$.""")
        st.markdown(f"""<div style="text-align: justify">
                    Po dosazení tedy máme funkci zisku v tomto tvaru
                    <div style="padding: 15px; padding-left: 20px;">
                    <img src="{latex_img}{backslash + 'pi(L, K) = P ' + backslash + 'cdot L^c ' + backslash + 'cdot K^d - w ' + backslash + 'cdot L - r ' + backslash + 'cdot K'}" style="{latex_style}" /> .
                    </div>
                    V bočním panelu si nastavte prodejní cenu, ceny výrobních faktorů a parametry
                    <img src="{latex_img}{'c'}" style="{latex_style}" /> a <img src="{latex_img}{'d'}" style="{latex_style}" />. Následně
                    hledáme optimální množství jednotek práce a optimální množství jednotek kapitálu.
                    Určíme parciální derivace funkce zisku a položíme je rovny <img src="{latex_img}{'0'}" style="{latex_style}" />
                    <div style="padding: 15px; padding-left: 20px;">
                        <img src="{latex_img}{backslash + 'frac{' + backslash + 'partial ' + backslash + 'pi(L, K)}{' + backslash + 'partial L} = c ' + backslash + 'cdot P ' + backslash + 'cdot ' + backslash + 'left( ' + backslash + 'frac{K}{L} ' + backslash + 'right)^d - w = 0'}" style="{latex_style}" />
                    <br>
                    <br>
                        <img src="{latex_img}{backslash + 'frac{' + backslash + 'partial ' + backslash + 'pi(L, K)}{' + backslash + 'partial K} = d ' + backslash + 'cdot P ' + backslash + 'cdot ' + backslash + 'left( ' + backslash + 'frac{L}{K} ' + backslash + 'right)^c - r = 0'}" style="{latex_style}" /> ,
                    </div>
                    potom vyjádříme <img src="{latex_img}{'P'}" style="{latex_style}" />
                    <div style="padding: 15px; padding-left: 20px;">
                    <img src="{latex_img}{'P = ' + backslash + 'frac{w}{c} ' + backslash + 'cdot ' + backslash + 'left( ' + backslash + 'frac{L}{K} ' + backslash + 'right)^d = ' + backslash + 'frac{r}{d} ' + backslash + 'cdot ' + backslash + 'left( ' + backslash + 'frac{K}{L} ' + backslash + 'right)^c'}" style="{latex_style}" /> ,
                    </div>
                    vyjádříme <img src="{latex_img}{'K'}" style="{latex_style}" />
                    <div style="padding: 15px; padding-left: 20px;">
                    <img src="{latex_img}{'K = ' + backslash + 'frac{L ' + backslash + 'cdot d ' + backslash + 'cdot w}{c ' + backslash + 'cdot r}'}" style="{latex_style}" /> ,
                    </div>
                    dosadíme do produkční funkce a vyjádříme <img src="{latex_img}{'L'}" style="{latex_style}" />
                    <div style="padding: 15px; padding-left: 20px;">
                        <img src="{latex_img}{'Q(L, K) = L^c ' + backslash + 'cdot ' + backslash + 'left( ' + backslash + 'frac{L ' + backslash + 'cdot d ' + backslash + 'cdot w}{c ' + backslash + 'cdot r} ' + backslash + 'right)^d'}" style="{latex_style}" />
                    <br>
                    <br>
                        <img src="{latex_img}{'L = ' + backslash + 'left( ' + backslash + 'frac{c ' + backslash + 'cdot r}{d ' + backslash + 'cdot w} ' + backslash + 'right)^d'}" style="{latex_style}" /> ,
                    </div>
                    dopočítáme <img src="{latex_img}{'K'}" style="{latex_style}" />
                    <div style="padding: 15px; padding-left: 20px;">
                    <img src="{latex_img}{'K = ' + backslash + 'left( ' + backslash + 'frac{d ' + backslash + 'cdot w}{c ' + backslash + 'cdot r} ' + backslash + 'right)^c'}" style="{latex_style}" /> ,
                    </div>
                    dosadíme optimální výrobní faktory do funkce zisku a vypočítáme zisk firmy
                    <div style="padding: 15px; padding-left: 20px;">
                    <img src="{latex_img}{backslash + 'pi(L, K) = P ' + backslash + 'cdot ' + backslash + 'left( ' + backslash + 'frac{c ' + backslash + 'cdot r}{d ' + backslash + 'cdot w} ' + backslash + 'right)^{d ' + backslash + 'cdot c} ' + backslash + 'cdot ' + backslash + 'left( ' + backslash + 'frac{d ' + backslash + 'cdot w}{c ' + backslash + 'cdot r} ' + backslash + 'right)^{c ' + backslash + 'cdot d} - w ' + backslash + 'cdot ' + backslash + 'left( ' + backslash + 'frac{c ' + backslash + 'cdot r}{d ' + backslash + 'cdot w} ' + backslash + 'right)^d - r ' + backslash + 'cdot ' + backslash + 'left( ' + backslash + 'frac{d ' + backslash + 'cdot w}{c ' + backslash + 'cdot r} ' + backslash + 'right)^c ='}{zisk}" style="{latex_style}" />
                    </div>
                    </div>""", unsafe_allow_html=True)


    st.markdown('---')


    scroll_top()



def uvod():

    st.title('1 Teorie spotřebitele')
    st.markdown("""
        <div style="text-align: justify"> 
        V rámci teorie spotřebitele se zaměříme na zkoumání toho, jak spotřebitelé jednají na trzích s výrobním zbožím a službami. 
        Naše pozornost se bude soustředit na parciální rovnováhu, což znamená, že se budeme snažit najít rovnovážný stav na jednom z trhů.
        Tento rovnovážný stav se nazývá optimum spotřebitele a jedná se o rozložení investic spotřebitele do jednotlivých statků za účelem
        maximalizace užitku nebo minimalizace výdajů. Ke hledání optima spotřebitele slouží následující úlohy.
        </div>
        <br>
        """, unsafe_allow_html=True)

    left_button, right_button = st.columns([1.035, 2.5])

    with left_button:
        if st.button('1.1 Marshallova úloha', key='1'):
            st.session_state.page = 'marshall'
            st.rerun()

    with right_button:
        if st.button('1.2 Hicksova úloha', key='2'):
            st.session_state.page = 'hicks'
            st.rerun()


    st.markdown('---')


    st.title('2 Teorie firmy')
    st.markdown("""
        <div style="text-align: justify"> 
        V předchozí kapitole jsme zkoumali rozhodování spotřebitele, který je poptávajícím na trzích zboží a služeb.
        Nyní se zaměříme na výrobce, který na těchto trzích své produkty nabízí. V případě teorie firmy budeme mít dva různé typy úloh:
        <ul style="margin-top: 10px; margin-bottom: 10px;">
        <li>minimalizaci nákladů, kdy má firma pevně stanovený objem produkce a řeší, jak tento objem vyrobit s minimálními náklady,</li>
        <li>maximalizaci zisku, kdy firma volí objem vyrobeného zboží a způsob, jak tento objem vyrobit, aby při tom dosáhla
        co nejvyššího zisku.</li>
        </ul> 
        Úloha minimalizace nákladů je významná především z toho důvodu, že její výsledek můžeme dále použít při řešení
        úlohy maximalizace zisku. Nejprve se ale budeme zabývat produkční funkcí firmy, která je základem neoklasického
        popisu firmy a je klíčovou součástí všech následujících úloh.
        </div>
        <br>
        """, unsafe_allow_html=True)
    
    left_button, center_button, right_button = st.columns([1.035, 1, 1])

    with left_button:
        if st.button('2.1 Produkční funkce firmy', key='3'):
            st.session_state.page = 'prod_fun'
            st.rerun()

    with center_button:
        if st.button('2.2 Minimalizace nákladů', key='4'):
            st.session_state.page = 'min_naklady'
            st.rerun()

    with right_button:
        if st.button('2.3 Maximalizace zisku', key='5'):
            st.session_state.page = 'max_zisk'
            st.rerun()



def run_app():

    if 'page' not in st.session_state:
        st.session_state.page = 'uvod'

    if st.session_state.page == 'uvod':
        uvod()
    elif st.session_state.page == 'marshall':
        marshall()
    elif st.session_state.page == 'hicks':
        hicks()
    elif st.session_state.page == 'prod_fun':
        prod_fun()
    elif st.session_state.page == 'min_naklady':
        min_naklady()
    elif st.session_state.page == 'max_zisk':
        max_zisk()



run_app()