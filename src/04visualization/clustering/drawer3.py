from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.globals import CurrentConfig

CurrentConfig.ONLINE_HOST = "https://cdn.kesci.com/lib/pyecharts_assets/"

def line_with_custom_linestyle(X, Y1, Y2, Y3):
    line = Line(init_opts=opts.InitOpts(width='1200px', height='500px'))
    line.add_xaxis(X)
    line.add_yaxis('CH值/10', Y1, linestyle_opts=opts.LineStyleOpts(width=5, curve=0, type_='solid'))
    line.add_yaxis('轮廓系数', Y2, linestyle_opts=opts.LineStyleOpts(width=3, curve=0.5, type_='dashed'))
    line.add_yaxis('戴维森堡丁指数(DBI)',Y3, linestyle_opts=opts.LineStyleOpts(width=5, curve=1, type_='dotted'))
    return line

def readFile(type):
    file = open('res\\output\\clustering\\cluster-num\\'+type+'.txt', 'r', encoding='utf-8')
    l = file.readlines()
    X = []
    Y1 = []
    Y2 = []
    Y3 = []
    for x in l:
        li = x.split()
        X.append(float(li[0]))
        Y1.append(float(li[1][0:6]) / 10)
        Y2.append(float(li[2][0:6]))
        Y3.append(float(li[3][0:6]))
    return X, Y1, Y2, Y3

itype = ['hierarchical', 'dbscan', 'kmeans']
for i in itype: 
    tmp_x, tmp_y1, tmp_y2, tmp_y3 = readFile(i)
    chart = line_with_custom_linestyle(tmp_x, tmp_y1, tmp_y2, tmp_y3)
    chart.render('res\\output\\clustering\\image2\\'+i+'-类数.html')
