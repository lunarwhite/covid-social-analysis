from pyecharts.charts import *
from pyecharts import options as opts

x_data = ['3月10日', '3月11日', '3月12日', ]

y_data_1 = ['13.6843', '37.3377', '18.9978']
y_data_2 = ['14.150', '16.301', '20.844', ]

def bar_with_multiple_axis(stage_name):
    bar = Bar(init_opts=opts.InitOpts(theme='macarons', width='500px', height='300px'))
    bar.add_xaxis(x_data)
    bar.extend_axis(yaxis=opts.AxisOpts())
    bar.add_yaxis("'"+stage_name+"'事件下情感值", y_data_1, yaxis_index=0)
    bar.add_yaxis("当天平均情感值", y_data_2, yaxis_index=0)
    return bar

chart1 = bar_with_multiple_axis("武汉封城")
chart2 = bar_with_multiple_axis("人传人")
chart3 = bar_with_multiple_axis("对口支援")
chart4 = bar_with_multiple_axis("复工复产")

chart1.render('res\\output\\emotion-dict\\image\\武汉封城情感对比.html')
chart2.render('res\\output\\emotion-dict\\image\\人传人情感对比.html')
chart3.render('res\\output\\emotion-dict\\image\\对口支援情感对比.html')
chart4.render('res\\output\\emotion-dict\\image\\复工复产情感对比.html')
