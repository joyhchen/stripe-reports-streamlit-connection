from stripe_reports_connection import StripeReportsConnection
import streamlit as st
from datetime import datetime
from dateutil.relativedelta import relativedelta

six_months_ago = datetime.now() - relativedelta(months=6)
six_months_ago_int = int(six_months_ago.timestamp())

two_days_ago = datetime.now() - relativedelta(days=2)
two_days_ago_int=int(two_days_ago.timestamp())

st.header('Show me the balance summary report for the interval starting 6 months ago and ending two days ago')
st.write('Start time', six_months_ago)
st.write('End time', two_days_ago)

conn = st.experimental_connection("stripe_reports_connection", type=StripeReportsConnection)

# reporting API params
# https://stripe.com/docs/reports/api#report-runs
report_type = 'balance.summary.1'
interval_start = six_months_ago_int
interval_end = two_days_ago_int

report_run = conn.query(report_type=report_type, interval_start=interval_start, interval_end=interval_end)

st.write("Ran report...")
st.write(report_run)

st.write("Paste your report run to verify its status")

query_id = st.text_input("Report run ID (frr_***)")
if query_id:
    retrieved_report = conn.get(query_id)
    st.write(retrieved_report)