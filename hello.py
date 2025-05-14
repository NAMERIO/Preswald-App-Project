from preswald import connect, get_df, query, table, text, plotly
import plotly.express as px

connect()

df = get_df("sample_csv")

df.columns = df.columns.str.lower()

sql = "SELECT * FROM sample_csv WHERE type = 'TV Show'"
filtered_df = query(sql, "sample_csv")

text("# Netflix Data Analysis")
text("This app shows data about Netflix shows.")

table(filtered_df, title="Filtered Data")

fig = px.bar(filtered_df, x="title", y="show_id", title="Top Netflix Shows (TV Shows Only)", labels={'show_id': 'Show ID', 'title': 'Show Title'})

plotly(fig)
