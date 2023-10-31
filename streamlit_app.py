import streamlit as st
from PIL import Image
import base64
import requests

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64(r"D:\HUKP\Desktop\Studia\DOKUMENTY\STRONA_CV\background.jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:image/png;base64,{img}");
background-size: 180%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)



with open("D:\HUKP\Desktop\Studia\DOKUMENTY\STRONA_CV\style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

####################
# Header 
st.write('''
##### *Curriculum Vitae* 
# Szymon Fabiański
''')

image = Image.open(r'D:\HUKP\Desktop\Studia\DOKUMENTY\STRONA_CV\foto.png')
st.image(image, width=200)


####################
# Navigation

#st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

#st.markdown("""
#<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
#  <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">Chanin Nantasenamat</a>
#  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
##    <span class="navbar-toggler-icon"></span>
#  </button>
#  <div class="collapse navbar-collapse" id="navbarNav">
#    <ul class="navbar-nav">
#      <li class="nav-item active">
#        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
#      </li>
#      <li class="nav-item">
#        <a class="nav-link" href="#education">Education</a>
#      </li>
#      <li class="nav-item">
#        <a class="nav-link" href="#work-experience">Work Experience</a>
#      </li>
#      <li class="nav-item">
#        <a class="nav-link" href="#bioinformatics-tools">Bioinformatics Tools</a>
#      </li>
#      <li class="nav-item">
#        <a class="nav-link" href="#social-media">Social Media</a>
#      </li>
#    </ul>
#  </div>
#</nav>
#""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Wykształcenie
''')

txt('**Magister**', '2020-2022')
st.markdown('''
- Uczelnia: Uniwersytet Łódzki
- Kierunek: Informatyka i Ekonometria
- Specjalność: Analityka gospodarcza
- Temat pracy: Wpływ stóp procentowych na Budżet Państwa
''')

txt('**Licencjat**' , '2017-2020')
st.markdown('''
- Uczelnia: Uniwersytet Łódzki
- Kierunek: Informatyka i Ekonometria
- Specjalność: Ekonometria
Temat pracy: Determinanty bezpośrednich inwestycji zagranicznych w Polsce w latach 1996 -2017
''')

#####################
st.markdown('''
## Doświadczenie zawodowe
''')

txt('**Starszy Specjalista ds. Analiz Metodologicznych w Departamencie Polityki Makroekonomicznej**',
'08.2023 - obecnie')
st.markdown('''
- Budowanie narzędzi analitycznych (streamilt, R-shiny),
- Współautor modelu makroekonomicznego NEMPF, służącego do przygotowanie prognoz dla gospodarki Polski (Eviews),
- Przygotowywanie średnio i długookresowych scenariuszowych analiz makroekonomicznych,
- Przygotowywanie, na potrzeby Aktualizacji Planu Konwergencji oraz Budżetu Państwa, prognoz kateogrii makroekonomicznych,
- Przygotowanie dokumentów i opracowań prezentujących wyniki analiz,
- Udział w spotkaniach oraz merytoryczna dyskusja z ekspertami zagranicznymi (ECB, IMF, KE),
- Projekty NLP (natural language processing),
- Przygotowywanie opracowań naukowych.
''')
txt('**Specjalista ds. Analiz Metodologicznych w Departamencie Polityki Makroekonomicznej**',
'12.2021 - 07.2023')
txt('**Stażysta w Departamencie Polityki Makroekonomicznej**',
'07.2021 - 10.2023')

txt('**Stażysta w zespole Analiz Ryzyka | PKO LEASING**',
'04-06.2021')
st.markdown('''
- Przygotowywanie raportów na podstawie dostępnych danych w celu szacowania ryzyka,
- Wsparcie utrzymania i rozwoju narzędzia bazodanowego,
- Utrzymanie i rozwój raportów na platformie Reporting Services.
''')

txt('**Praktykant w zespole Data Technology | EY (dawniej Ernst&Young)**',
'12.2019 - 10.2020')
st.markdown('''
- Analiza i wizualizacja danych finansowych (MS Excel, MS Access, MS SQL),
- Wykonywanie procedur audytowych, mających na celu weryfikację zapisów księgowych,
- Przygotowywanie raportów i tworzenie dokumentacji.
''')

txt('**Stażysta w zespole IT | ROSSMANN**',
'07-08.2019')
st.markdown('''
- Projektowanie systemów informatycznych,
- Prowadzenie dokumentacji projektowej,
- Przygotowywanie raportów,
- Praca z językiem T-SQL.
''')

#####################


# EMOS
url = "https://raw.githubusercontent.com/SzymonFabian/CV/main/cert/EMOS.pdf"
response = requests.get(url)
with open("EMOS.pdf", "wb") as f:
    f.write(response.content)
# MD
url = "https://raw.githubusercontent.com/SzymonFabian/CV/main/cert/MD.pdf"
response = requests.get(url)
with open("MD.pdf", "wb") as f:
    f.write(response.content)
# SPSS
url = "https://raw.githubusercontent.com/SzymonFabian/CV/main/cert/CertyfikatSPSS.pdf"
response = requests.get(url)
with open("CertyfikatSPSS.pdf", "wb") as f:
    f.write(response.content)
# ML
url = "https://raw.githubusercontent.com/SzymonFabian/CV/main/cert/MachineLearningAZ.pdf"
response = requests.get(url)
with open("MachineLearningAZ.pdf", "wb") as f:
    f.write(response.content)


st.markdown('''
## Kursy I Certyfikaty
''')
st.divider()
with open("EMOS.pdf", "rb") as pdf_file:
    EMOS = pdf_file.read()
with open("CertyfikatSPSS.pdf", "rb") as pdf_file:
    SPSS = pdf_file.read()
with open('MD.pdf', "rb") as pdf_file:
    MD = pdf_file.read()
with open("MachineLearningAZ.pdf", "rb") as pdf_file:
    ML = pdf_file.read()


colc1, colc2 = st.columns([3,1])
colc1.markdown('''
EMOS - EuropeanMaster in Official Statistics
''')
               
colc2.download_button(label="Pobierz Certyfikat",
                    data=EMOS,
                    file_name="SzF_EMOS.pdf",
                    mime='application/octet-stream')

st.divider()
colc3, colc4 = st.columns([3,1])

colc3.markdown('''
SPSS - Technology Junior Expert
''')

colc4.download_button(label="Pobierz Certyfikat",
                    data=SPSS,
                    file_name="SzF_SPSS.pdf",
                    mime='application/octet-stream')

st.divider()
colc5, colc6 = st.columns([3,1])

colc5.markdown('''
MacroeconomicDiagnostics
''')

colc6.download_button(label="Pobierz Certyfikat",
                    data=MD,
                    file_name="SzF_MD.pdf",
                    mime='application/octet-stream')

st.divider()
colc7, colc8 = st.columns([3,1])

colc7.markdown('''
MeachineLearning A-Z: AI, Python&R
''')

colc8.download_button(label="Pobierz Certyfikat",
                    data=ML,
                    file_name="SzF_ML.pdf",
                    mime='application/octet-stream')


st.divider()


#####################
st.markdown('''
## Umiejętności
''')
txt3('Programming', '`Python`, `R`, `VBA`, `C++`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`,`dplyr`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `ggplot2`')
txt3('Machine Learning', '`scikit-learn`,`huggingface`')
txt3('Model deployment', '`streamlit`, `R Shiny`, `Heroku`')
txt3('Econometrics', ' `EViews`')

#####################
st.markdown('''
## Przykładowe prace
''')
            
txt4('Streamlit', 'Porównania międzynarodowe', 'https://aggpkb.streamlit.app/')    

txt4('RShiny', 'Prognozy NEMPF', 'https://szfpriv.shinyapps.io/Publikowane/')   
st.markdown("Dane wygenerowane losowo. Login: abc; Hasło: 123")
