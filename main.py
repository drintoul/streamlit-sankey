import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Create the data
df = pd.DataFrame({'Source': ['A', 'A', 'B', 'C', 'C', 'D'],
                   'Target': ['B', 'C', 'B', 'C', 'D', 'D'],
                   'Value': [10, 20, 30, 40, 50, 60]})

# Create the Sankey diagram
fig = go.Figure(data=[go.Sankey(link=dict(source=df['Source'], target=df['Target'], value=df['Value']))])

# Update the layout
fig.update_layout(title='Sankey Diagram', font=dict(size=12))

# Display the diagram
st.plotly_chart(fig)
