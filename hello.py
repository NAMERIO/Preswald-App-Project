from preswald import connect, get_df, query, table, text, plotly
import plotly.express as px

connect()

df = get_df("sample_csv")

sql = "SELECT * FROM sample_csv WHERE TYPE = 'TV Show'"
filtered_df = query(sql, "sample_csv") 

text("# Netflix Data Analysis")
text("This app shows data about Netflix shows.")

table(filtered_df, title="Filtered Data")

fig = px.bar(filtered_df, x="TITLE", y="SHOW_ID", title="Top Netflix Shows (TV Shows Only)", labels={'SHOW_ID': 'Show ID', 'TITLE': 'Show Title'})

plotly(fig)
