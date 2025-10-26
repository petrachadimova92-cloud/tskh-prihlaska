import streamlit as st

st.title("Registrační formulář")


col1, col2, col3 = st.columns([0.4, 0.4, 0.2])
with col1: 
    jmeno = st.text_input("Zadej jméno:", max_chars = 20, key="jmeno")
with col2:
    prijmeni = st.text_input("Zadej příjmení", max_chars= 50, key="prijmeni")
with col3:
    vek = st.number_input("Zadej věk", min_value= 3, max_value= 20, step= 1,key= "vek")

col4, col5 = st.columns(2)
with col4: 
    kontakt_1 = st.text_input("Zadej tel. číslo", key="kontakt_1")    
with col5: 
    kontakt_2 = st.text_input("Zadej email", key="kontakt_2")    
bydliste = st.text_input("Zadej trvalé bydliště", key="bydliste")

col6, col7 = st.columns(2)
with col6:
    jmeno_zakonneho_zastupce = st.text_input("Zadej jméno zakonného zástupce", key="jmeno_zakonneho_zastupce")
with col7:
    prijmeni_zakonneho_zastupce = st.text_input("Zadej příjmení zakonnného zástupce", key="prijmeni_zakonnaho_zastupce")

col8, col9 = st.columns(2) 
with col8:
    kontakt_zakonneho_zastupce_1 = st.text_input("Zadej tel. číslo na zakonnného zástupce", key="kontakt_zakonneho_zastupce_1")
with col9:
    kontakt_zakonneho_zastupce_2 = st.text_input("Zadej email na zakonnného zástupce", key="kontakt_zakonneho_zastupce_2")


if vek in [3, 4]:
    dostupne_hobby_skupiny = ["Štístka"]
elif vek in [5, 6]:
    dostupne_hobby_skupiny = ["Mravenečci"]
elif vek in [7]:
    dostupne_hobby_skupiny = ["Sedmikrásky"]
elif vek in [8]:
    dostupne_hobby_skupiny = ["Sedmikrásky", "Sněženky"]
elif vek > 8 and vek <= 10:
    dostupne_hobby_skupiny = ["Sněženky"]
else:
    dostupne_hobby_skupiny = []
hobby_skupiny = st.multiselect(
    "Hobby skupiny",
    dostupne_hobby_skupiny 
)

if vek in [6, 7]:
    dostupne_poloprofi_skupiny = ["Angels"]
elif vek in [8, 9]:
    dostupne_poloprofi_skupiny = ["Balet"]
elif vek in [10, 11, 12, 13, 14, 15]:
    dostupne_poloprofi_skupiny = ["Balet", "Danza"]  
elif vek in [16, 17, 18]:
    dostupne_poloprofi_skupiny = ["Danza"]
else:
    dostupne_poloprofi_skupiny = []
poloprofi_skupiny = st.multiselect(
    "Poloprofi skupiny",
    dostupne_poloprofi_skupiny
   )

if vek in [8, 9, 10]:
    dostupne_profi_skupiny = ["Stars"]
elif vek in [11, 12, 13, 14]:
    dostupne_profi_skupiny = ["Rebels"]
elif vek in [15, 16, 17, 18, 19, 20]:
    dostupne_profi_skupiny = ["Diamonds"]
else:
    dostupne_profi_skupiny = []
profi_skupiny = st.multiselect(
    "Profi skupiny",
    dostupne_profi_skupiny)


souhlas = st.checkbox("Souhlasím se zpracováním svých osobních údajů.", key="souhlas")


tlacitko_odeslat = st.button(label = "Odeslat", disabled= not souhlas,key="tlacitko_odeslat")
if tlacitko_odeslat:
    if not jmeno: 
        st.error("Musíte vyplnit jméno.")
        st.stop()
    if not prijmeni: 
        st.error("Musíte vyplnit příjmení.")
        st.stop()     
    if not vek: 
        st.error("Musíte vyplnit věk.")
        st.stop()    
    if not kontakt_1: 
        st.error("Musíte vyplnit tel. číslo.")
        st.stop()        
    if not kontakt_2: 
        st.error("Musíte vyplnit email.")
        st.stop()
    if not bydliste: 
        st.error("Musíte vyplnit trvalé bydliště.")
        st.stop()
    if not jmeno_zakonneho_zastupce and vek <18:
        st.error("Musíš vyplnit jméno zakonného zástupce.")
        st.stop()
    if not prijmeni_zakonneho_zastupce and vek <18:
        st.error("Musíš vyplnit příjmení zakonného zástupce.")
        st.stop()
    if not kontakt_zakonneho_zastupce_1 and vek <18:
        st.error("Musíš vyplnit tel. číslo zakonného zástupce.")
        st.stop()
    if not kontakt_zakonneho_zastupce_2 and vek <18:
        st.error("Musíš vyplnit email zakonného zástupce.")
        st.stop()
 

    st.write("Odesláno")










