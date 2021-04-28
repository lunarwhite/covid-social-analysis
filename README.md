# covid19-sentiment-data-analysis

## 1 topic

## 2 structure

```
|_1_Spider：放置爬虫代码
	|__comment：评论数据
	|__topic：短微博数据
	|__Comment.py：评论爬虫代码(Use your Cookie)
	|__Topic.py：按话题爬取短微博代码(Use your Cookie)
|_2_Preprocessing：放置预处理代码
	|__data:放置关键词提取结果
	|__myTextRank:自己实现的关键词提取
	|__pre.py:微博文本预处理
|_3_Analysis：放置数据分析代码
	|__Clustering：聚类代码
		|__DBSCAN：DBSCAN聚类
			|__DBSCAN.py：DBSCAN聚类代码
		|__Kmeans：K均值聚类
			|__Kmeans.py：Kmeans聚类代码
		|__层次：层次聚类
			|__层次聚类.py：层次聚类代码
	|__EmotionDict：情感词典代码
		|__data：存放数据
		|__dict：存放词典
		|__result：存放短微博结果
		|__result_comment：存放评论分析结果
		|__SOPMI_data：存放SOPMI所需数据
		|__Calculate.py：计算情感值代码
		|__SO_PMI.py：SOPMI发现新词代码
	|__MultidimensionalEmotion：多维情感分析代码
		|__data：存放数据
		|__dict：存放多维词典
		|__result：存放结果
		|__deal：处理结果
		|__multi：计算结果
|_4_Visualization：放置可视化分析代码
	|__Clustering：层次聚类效果可视化
    |__EmotionDict：情感值计算可视化
    |__MultidimensionalEmotion：多维情感可视化
    |__NumberOfClusters：类数可视化
```

## 3 set-up

```python
conda create --name classds python=3.6

pip3 install jupyter
```
