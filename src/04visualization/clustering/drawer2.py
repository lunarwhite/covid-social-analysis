from pyecharts.charts import *
from pyecharts import options as opts

x = ['疫情认知相关', '群众自我相关', '社会行为相关']
y = [91, 77, 33]  # 复工复产
y1 = [41, 60, 97]  # 对口支援
y2 = [110, 42, 56, ]  # 人传人
y3 = [119, 69, 15]  # 武汉封城

def pie_custom_radius(Y, stage_name):
    pie = Pie(init_opts=opts.InitOpts(theme='light', width='600px', height='400px'))
    pie.add(stage_name, [list(z) for z in zip(x, Y)], radius=["40%", "75%"])
    pie.set_global_opts(title_opts=opts.TitleOpts(title=stage_name+"事件", subtitle='聚类饼图'))
    pie.set_series_opts(label_opts=opts.LabelOpts(position='top', interval=1, formatter='{b}:{d}%'))
    return pie

chart1 = pie_custom_radius(y3, "武汉封城")
chart2 = pie_custom_radius(y2, "人传人")
chart3 = pie_custom_radius(y1, "对口支援")
chart4 = pie_custom_radius(y, "复工复产")
chart1.render('res\\output\\clustering\\image\\武汉封城-聚类分析饼图.html')
chart2.render('res\\output\\clustering\\image\\人传人-聚类分析饼图.html')
chart3.render('res\\output\\clustering\\image\\对口支援-聚类分析饼图.html')
chart4.render('res\\output\\clustering\\image\\复工复产-聚类分析饼图.html')
