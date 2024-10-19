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

#temperature selection conditions
if selected == "Accurate":
	temp = 0.0
if selected == "Medium":
	temp = 0.5
if selected == "Creative":
	temp = 1.0
	
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

#FIRST PARTY SECTION
st.subheader("Details of 1st Party")
sec1, sec2, sec3 = st.columns(3)
with sec1:
	name = st.text_input("Enter 1st Party Name",placeholder="SmartScribe Inc.")
with sec2:
	rep = st.text_input("Enter Party representative name",placeholder="Aryaneel Shivam")
with sec3:
	pos = st.text_input("Enter representative position",placeholder="Founder Director")
sec4, sec5, sec6 = st.columns(3)
with sec4:
	address = st.text_input("Enter 1st Party Address",placeholder="Sector 3, Pragati Enclave, New Delhi")
with sec5:
	Contact = st.text_input("Enter Party contact number",placeholder="+91 70991 xxxxx")
with sec6:
	email = st.text_input("Enter Party email address",placeholder="party1@gmail.com")
sec7, sec8, sec9 = st.columns(3)
with sec7:
	country = st.text_input("Enter Governing Country",placeholder="India")
with sec8:
	date = st.date_input("Enter date of signing")
with sec9:
	date2 = st.date_input("Enter date of drafting")
purpose1 = st.text_area("Enter purpose of this MOU", placeholder="Enter the purpose of this Memorandum of Understanding")
partyaclause = st.text_area("Enter your terms and clauses",placeholder="Write down your terms and clauses for the agreement", height=250)

#SECOND PARTY SECTION
st.subheader("Details of 2nd Party")
ss1, ss2, ss3 = st.columns(3)
with ss1:
	name2 = st.text_input("Enter 2nd Party Name",placeholder="TeenScript Inc.")
with ss2:
	rep2 = st.text_input("Enter Party representative name",placeholder="John Doe")
with ss3:
	pos2 = st.text_input("Enter representative position",placeholder="Managing Director")
ss4, ss5, ss6 = st.columns(3)
with ss4:
	address2 = st.text_input("Enter 2nd Party Address",placeholder="Sector 10, New Delhi")
with ss5:
	Contact2 = st.text_input("Enter Party contact number",placeholder="+91 93455 xxxxx")
with ss6:
	email2 = st.text_input("Enter Party email address",placeholder="party2@gmail.com")
ss7, ss8, ss9 = st.columns(3)
with ss7:
	country2 = st.text_input("Enter Governing Country",placeholder="India", key="Country")
with ss8:
	datesec = st.date_input("Enter date of signing", key="2ndparty")
with ss9:
	datesec2 = st.date_input("Enter date of drafting", key="party2")
purpose2 = st.text_area("Enter purpose of this MOU", placeholder="Enter the purpose of this Memorandum of Understanding", key="purpose2")
partybclause = st.text_area("Enter your terms and clauses",placeholder="Write down your terms and clauses for the agreement", height=250, key="partybclause")
generate = st.button("Draft Memorandum", type="primary", use_container_width=True)
if generate:
	try:
		with st.spinner("SmartScribe is drafting your Memorandum of Understanding..."):

			prompt = f"""
							First Party Details are: {name},{rep},{pos},{address},{Contact},{email},{country},{date},{date2}
							which are the name of party, party representative name, representative position, address, contact number
							email address, country of governing law, date of signing and date of drafting respectively.
							Their terms and clauses are {partyaclause}.
							Second Party Details are: {name2},{rep2},{pos2},{address2},{Contact2},{email2},{country2},{datesec},{datesec2}
							which are the name of party, party representative name, representative position, address, contact number
							email address, country of governing law, date of signing and date of drafting respectively.
							Their terms and clauses are {partybclause}.
							Draft a proper formatted and working memorandum of understanding between the two parties with Non Disclosure and terms of termination clauses added
							The purpose of this memorandum of understanding are {purpose1} and {purpose2}"""

			response = model.generate_content(prompt, generation_config=genai.types.GenerationConfig(temperature=temp))
			conv = st.write(response.text)

	except:
		st.error("Something went wrong while generating document", icon="⚠️")
