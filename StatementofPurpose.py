import streamlit as st
import google.generativeai as genai
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="SmartScribe",
    page_icon="🧠",
    initial_sidebar_state="expanded",
)

Google = 'AIzaSyDtl-9-hd5-JIXTnrYhf57_lQKsXm3Ksp0'
genai.configure(api_key=Google)
model = genai.GenerativeModel('gemini-1.5-pro')

st.title(":orange[Smart]Scribe")
st.sidebar.info("In cases when error appears while drafting document(s) hit the draft button once more.",icon="💡")


#options menu
with st.sidebar:
	selected = option_menu(
		menu_title="Draft Mode",
		options=["Accurate","Medium","Creative"],
		menu_icon="chat-dots-fill",
		default_index=0,
		icons=["circle-fill","circle-half","circle"],
		#orientation="horizontal"
	)

#temperature selection for Gemini
if selected=="Accurate":
	temp = 0.0
if selected=="Medium":
	temp = 0.5
if selected=="Creative":
	temp= 1.0

col1,col2,col3 = st.columns(3)
with col1:
	st.page_link("StatementofPurpose.py", label="Statement of Purpose", icon="📝")
with col2:
	st.page_link("pages/Memorandum of Understanding.py", label="Memorandum", icon="📮")
with col3:
	st.page_link("pages/Privacy Policy.py", label="Privacy Policy", icon="🤫")
col4, col5, col6 = st.columns(3)
with col4:
    st.page_link("pages/Non Disclosure Agreement.py", label="Non Disclosure", icon="🚩")
sec1, sec2 = st.columns(2)
with sec1:
	name = st.text_input("Your name", placeholder="Aryaneel Shivam")
with sec2:
	university = st.text_input("Interested University", placeholder="University of Edinburgh")
sec3, sec4 = st.columns(2)
with sec3:
	country = st.text_input("Name of the country", placeholder="United Kingdom")
with sec4:
	city = st.text_input("Name of the city", placeholder="Edinburgh")
sec5, sec6, sec7 = st.columns(3)
with sec5:
	marks10 = st.number_input("Enter 10th percentage")
with sec6:
	marks11 = st.number_input("Enter 12th percentage")
with sec7:
	board = st.text_input("Name of the education board", placeholder="CBSE")
sec8, sec9, sec10 = st.columns(3)
with sec8:
	course = st.text_input("Name of the course", placeholder="Bsc(Hons) Computer Science")
with sec9:
	job = st.text_input("Intended future job", placeholder="Data analytics")
with sec10:
	option = st.selectbox("Education entry level", ("Undergraduate","Post Graduate","Masters"))
 
writestatement = st.button("Write My Statement", type="primary", use_container_width=True)
if writestatement:
	try:
		with st.spinner("SmartScribe is drafting your statement of purpose..."):
			prompt = f"Write a statement of purpose for {name} applying to {university} in the country {country} in {city}, academic background includes marks obtained in class 10 {marks10} and in class 12 {marks11} under {board}, wants to pursure {course} aiming to get a job in {job} applying for {option}."
			response = model.generate_content(prompt, generation_config=genai.types.GenerationConfig(temperature=temp))
			conv = st.write(response.text)

	except:
		st.error("Something went wrong while generating document", icon="⚠️")
