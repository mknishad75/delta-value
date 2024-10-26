import threading
import requests
from flask import Flask, jsonify
import streamlit as st
from flask import Flask, jsonify
from deltacalculate.maicall import DeltaValue, CreateToken

# Flask API Setup
app = Flask(__name__)
value = DeltaValue()
getToken = CreateToken()

@app.route('/api/data', methods=['GET'])
def get_data():
   
    data = {"message": "Hello from the integrated Flask API!, "}
    return jsonify(data)
# create token
@app.route('/createtoken', methods=['POST'])
def create_token():
    data = requests.get_json() 
    name= data.get('name')
    id= data.get('userId')
    token= data.get('token')
    msg =getToken.token(name,id,token)
    return msg

#get value
@app.route('/delta/<pe>', methods=['GET'])
def get_itemValue():
    print("i am in delta")
  
    item = value.calling(pe,ce,expirydate)
    print(item)
    #item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({"error": "Item not found"}), 404


# Function to run Flask app on a separate thread
def run_flask():
    app.run(port=5000)

# Start Flask app in a separate thread
threading.Thread(target=run_flask).start()

# Streamlit Interface
st.title("Streamlit with Integrated Flask API")

with st.form("user_form"):
 pe = st.number_input("Enter the first number", placeholder="Type PE here...")
 ce = st.number_input("Enter the second number", placeholder="Type CE here...")
 expirydate = st.text_input("Enter the second number",placeholder="Type expiry here...")
 submitted = st.form_submit_button("Submit")
 
if submitted:    
   if pe and ce and expirydate:
       item = value.calling(pe,ce,expirydate)
       
st.title("Fill the form to create the token")
with st.form("create_token"):
 name = st.text_input("Enter the username", placeholder="Type PE here...")
 id = st.text_input("Enter the code", placeholder="Type CE here...")
 token = st.text_input("Enter the token",placeholder="Type expiry here...")
 submitted = st.form_submit_button("Submit")
 
if submitted:    
   if name and id and token:
        msg =getToken.token(name,id,token)
        data = {"message": " {msg} "}
        st.success(f"Hello, {data}")
   else:
       st.error("error")    

if st.button("Get Data from Flask API"):
    try:
        # Call the Flask API
        response = requests.get("http://127.0.0.1:5000/api/data")
        if response.status_code == 200:
            data = response.json()
            st.write("API Response:", data)
        else:
            st.error("Failed to get data from the API.")
    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {e}")




