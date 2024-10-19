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

st.subheader("Privacy Policy")
sec1, sec2 = st.columns(2)
with sec1:
	cname = st.text_input("Enter Company Name",placeholder="SmartScribe")
with sec2:
	caddress = st.text_input("Enter Registered Address",placeholder="India, New Delhi, Sector-3")
sec3, sec4 = st.columns(2)
with sec3:
	clink = st.text_input("Enter Website Link", placeholder="www.examplewebsite.com")
with sec4:
	cemail = st.text_input("Enter Company Email",placeholder="examplecompany@gmail.com")
sec5, sec6 = st.columns(2)
with sec5:
	stat = st.selectbox("Information Collection Status",("Collects Personal Information","Does not collect Personal Information"))
with sec6:
	date = st.date_input("Enter Effective Date")
sec7, sec8 = st.columns(2)
with sec7:
	typeof= st.multiselect("Type(s) of information collected",["Personal Identification Information", "Demographic Information","Finincial Information","Usage Data","Other Information(s)"])
with sec8:
	Method = st.multiselect("Method of collection",["Third Party","Direct Interaction","Automated Technologies"])
useofinfo = st.multiselect("Enter the uses of collected information",["Maintain Service(s)","Personalize Service(s)", "Promotional Purposes","Legal and Compliance","Other Purposes"])
shareinfo = st.multiselect("Status of Sharing of Information",["With service providers", "Business transfers","Third Party","Affiliate sharing","Legal reason(s)","Does not share"])

ss1,ss2,ss3 = st.columns(3)
with ss1:
	cookies = st.selectbox("Do you use cookies?",("Using Cookies","Not using Cookies"))
with ss2:
	ageres = st.selectbox("Age restricted content(s)?",("Yes, age restricted content(s)","No, age restricted content(s)"))
with ss3:
	storage = st.selectbox("Data storage status",("On-site data storage","Cloud data storage"))
userrights = st.multiselect("User Right(s) status",["Access and Correction","Data Portability","Deletion and Erasure","Opt-Out willingly"])
desc = st.text_area("Describe your company in brief",placeholder="Eg: SmartScribe is an AI-powered LLM-based Legal and Academic Document drafting webapp.")

generate = st.button("Draft My Privacy Policy",type="primary", use_container_width=True)
if generate:
	try:
		with st.spinner("SmartScribe is drafting your Privacy Policy..."):

			prompt = f"""
							Draft a fully formatted privacy policy with the given informations.
							Name of the company {cname}
							Address of the company {caddress}
							Link to the website of the company {clink}
							Email to the company {cemail}
							information collection status {stat}
							effective date {date}
							Types of information collected {typeof}
							Method of collection of information {Method}
							uses of collected information {useofinfo}
							Status of sharing of information {shareinfo}
							Usage of cookies {cookies}
							Any age restricted content {ageres}
							data storage status {storage}
							Rights granted to users {userrights}
							About the company {desc}"""

			response = model.generate_content(prompt, generation_config=genai.types.GenerationConfig(temperature=temp))
			conv = st.write(response.text)

	except:
		st.error("Something went wrong while generating document", icon="⚠️")
