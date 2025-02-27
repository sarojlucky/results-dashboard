import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

# Set page configuration
st.set_page_config(
    page_title="Test Case Metrics Visualizer",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .stNumberInput > div > div > input {
        color: #333;
    }
    .error-msg {
        color: #ff0000;
        font-size: 14px;
    }
    .metric-container {
        background-color: #f0f2f6;
        padding: 10px;
        border-radius: 8px;
        margin: 5px 0;
    }
    div.block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.title("Test Case Metrics Visualizer")
st.markdown("Enter test results for both Smoke Tests and End to End Tests to generate visualizations.", help="Input the test results to see the distribution")

# Create columns for both test types
smoke_col, regression_col = st.columns(2)

# Smoke Tests Section
with smoke_col:
    st.subheader("Smoke Tests")
    smoke_pass = st.number_input("Passed Smoke Tests", min_value=0, value=0, step=1)
    smoke_fail = st.number_input("Failed Smoke Tests", min_value=0, value=0, step=1)
    smoke_total = smoke_pass + smoke_fail
    if smoke_total > 0:
        smoke_pass_rate = (smoke_pass / smoke_total) * 100
        smoke_fail_rate = (smoke_fail / smoke_total) * 100

# End to End Tests Section
with regression_col:
    st.subheader("End to End Tests")
    regression_pass = st.number_input("Passed End to End Tests", min_value=0, value=0, step=1)
    regression_fail = st.number_input("Failed End to End Tests", min_value=0, value=0, step=1)
    regression_total = regression_pass + regression_fail
    if regression_total > 0:
        regression_pass_rate = (regression_pass / regression_total) * 100
        regression_fail_rate = (regression_fail / regression_total) * 100

# Display metrics and charts only if there's data
if smoke_total > 0 or regression_total > 0:
    # Daily Regression Report Section
    st.markdown("### Daily Regression Report")

    metrics_col1, metrics_col2 = st.columns(2)

    with metrics_col1:
        if smoke_total > 0:
            st.markdown("**Smoke Tests**")
            st.markdown(f"""
            • Total test cases: **{smoke_total}**
            • Passed: **{smoke_pass}** (**{smoke_pass_rate:.1f}%**)
            • Failed: **{smoke_fail}** (**{smoke_fail_rate:.1f}%**)
            """)

    with metrics_col2:
        if regression_total > 0:
            st.markdown("**End to End Tests**")
            st.markdown(f"""
            • Total test cases: **{regression_total}**
            • Passed: **{regression_pass}** (**{regression_pass_rate:.1f}%**)
            • Failed: **{regression_fail}** (**{regression_fail_rate:.1f}%**)
            """)

    # Create charts
    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        if smoke_total > 0:
            # Smoke Tests pie chart
            fig_smoke = go.Figure(data=[go.Pie(
                labels=['Passed', 'Failed'],
                values=[smoke_pass, smoke_fail],
                hole=.3,
                marker_colors=['#2ecc71', '#e74c3c'],
                textinfo='percent',
                textfont=dict(size=24),  # Increased font size for percentages
                textposition='inside',  # Force text inside the pie
                insidetextorientation='horizontal'  # Keep text horizontal
            )])

            fig_smoke.update_layout(
                title=dict(
                    text="Smoke Tests Results",
                    y=0.95
                ),
                annotations=[dict(text=f'Total: {smoke_total}', x=0.5, y=0.5, font_size=16, showarrow=False)],
                margin=dict(l=20, r=20, t=40, b=20),
                showlegend=True,
                legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="right",
                    x=1
                )
            )
            st.plotly_chart(fig_smoke, use_container_width=True)

    with chart_col2:
        if regression_total > 0:
            # End to End Tests pie chart
            fig_regression = go.Figure(data=[go.Pie(
                labels=['Passed', 'Failed'],
                values=[regression_pass, regression_fail],
                hole=.3,
                marker_colors=['#2ecc71', '#e74c3c'],
                textinfo='percent',
                textfont=dict(size=24),  # Increased font size for percentages
                textposition='inside',  # Force text inside the pie
                insidetextorientation='horizontal'  # Keep text horizontal
            )])

            fig_regression.update_layout(
                title=dict(
                    text="End to End Tests Results",
                    y=0.95
                ),
                annotations=[dict(text=f'Total: {regression_total}', x=0.5, y=0.5, font_size=16, showarrow=False)],
                margin=dict(l=20, r=20, t=40, b=20),
                showlegend=True,
                legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="right",
                    x=1
                )
            )
            st.plotly_chart(fig_regression, use_container_width=True)

# Footer with reduced margin
st.markdown("<div style='margin-top: 1rem;'><hr/></div>", unsafe_allow_html=True)
#st.markdown("*Test metrics visualization powered by Streamlit and Plotly*")