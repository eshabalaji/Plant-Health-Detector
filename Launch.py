from pyngrok import ngrok

ngrok.set_auth_token("YOUR_NGROK_AUTH_TOKEN")  # Use your real token

port = 8501
public_url = ngrok.connect(port)
print(f"Access your app at: {public_url}")

!streamlit run app.py &
