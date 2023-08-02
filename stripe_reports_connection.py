from streamlit.connections import ExperimentalBaseConnection
import streamlit as st

class StripeReportsConnection(ExperimentalBaseConnection):
    def _connect(self):
        import stripe

        stripe.api_key = st.secrets['STRIPE_SECRET_KEY']

        self.conn = stripe.reporting.ReportRun
    
    def query(self, report_type, interval_start, interval_end):
        @st.cache_data
        def _query(_report_type, _interval_start, _interval_end):
            return self.conn.create(
                report_type=_report_type,
                parameters={
                    'interval_start': _interval_start,
                    'interval_end': _interval_end
                }
            )
        return _query(report_type, interval_start, interval_end)

    def get(self, report_id):
        @st.cache_data
        def _get(report_id):
            return self.conn.retrieve(
                report_id
            )
        return _get(report_id)
