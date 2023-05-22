fig12 = go.Figure()
fig12.add_trace(go.Scatter(
    x=df11.index,
    y=df11['Hieu suat'],
    name="Hiệu suất inverter 3 "))
fig12.add_trace(go.Scatter(
    x=df11.index,
    y=y_pred,
    name="Hiệu suất tuyến tính inverter 3 "))
fig12.update_layout(yaxis_range=[60, 100])
fig12.update_xaxes(title_text="Ngày")
fig12.update_yaxes(title_text="Hiệu suất")
fig12.update_layout(height=900)
fig12.update_layout(width=1500)
fig12.add_annotation(
    text="y="+a+"*x+"+b,
    xref="paper",
    yref="paper",
    x=1,
    y=0.84,
    showarrow=False,
    font=dict(
        size=18,
        color="red"
    )
)
fig12.show()