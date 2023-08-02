# Streamlit Stripe reports connection

Run reports with the Stripe Reporting API.

## Develop locally

First, install the requirements `pip install`. 

1. Add a folder `.streamlit` in the root directory.
2. Add a file `secrets.toml`.
3. Paste your Stripe secret key.

```
STRIPE_SECRET_KEY="sk_********"
```

4. streamlit run app.py

## Deploy to Streamlit Community Cloud

1. Create a new app at [https://share.streamlit.io/](https://share.streamlit.io/).
2. Set the Main file path to `app.py`
3. Deploy.
4. You should get an error that STRIPE_SECRET_KEY is undefined.
5. Go to your Streamlit app settings and paste the contents of your local `secrets.toml` file. 

```
STRIPE_SECRET_KEY="sk_********"
```