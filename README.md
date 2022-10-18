# covid19-sentiment-data-analysis

![covid-social-analysis](https://socialify.git.ci/lunarwhite/covid-social-analysis/image?description=1&descriptionEditable=ML-based%20analysis%20of%20social%20media%20users%27%20attentiveness%20under%20the%20COVID-19.%20Data%20crawling%2C%20analysis%2C%20visualization.&font=Raleway&forks=1&issues=1&logo=https%3A%2F%2Fwww.un.org%2Fsites%2Fun2.un.org%2Ffiles%2F2020%2F04%2Fcovid-19.svg&name=1&owner=1&pattern=Brick%20Wall&pulls=1&stargazers=1&theme=Light)

ML-based analysis of social media users' attentiveness under the COVID-19. || 基于机器学习的COVID-19疫情背景下，分阶段的微博文本情感分析，先爬取数据，再用聚类、情感词典和多维情感分析，并可视化

```
├───.vscode # vscode 配置文件
├───res
│   ├───input
│   │   ├───comment # 评论数据
│   │   ├───dict # 词典
│   │   ├───hot # 热词
│   │   ├───SOPMI
│   │   ├───stage # 不同阶段微博数据
│   │   └───topic # 微博数据
│   └───output
│       ├───clustering
│       │   ├───cluster-num # 聚类数
│       │   ├───image1 # 聚类分析饼图
│       │   └───image2 # 聚类数
│       ├───comment-txt # 评论数据-txt
│       ├───emotion-dict
│       │   └───image # 情感对比图
│       ├───hot
│       ├───multi-emotion
│       │   └───image # 多维情感分析图
│       └───topic-txt # 微博数据-txt
└───src
    ├───01crawling # 爬取数据
    ├───02preprocessing # 预处理
    ├───03analysis #分析
    │   ├───clustering # 聚类
    │   ├───emotion-dict # 情感词典
    │   └───multi-emotion # 多维情感
    └───04visualization # 可视化
        ├───clustering
        ├───emotion-dict
        └───multi-emotion
```

## 1 概览

- 手动爬取疫情背景下微博文本与评论，进行情感分析
- 分别尝试聚类、情感词典和多维度情感分析
- 主要工具包版本为Python 3.6.10、scikit-learn 0.24.2

## 2 部署

- 克隆repo：`git clone https://github.com/lunarwhite/covid19-sentiment-data-analysis.git`
- 更新pip：`pip3 install --upgrade pip`
- 为项目创建虚拟环境：`conda create --name <env_name> python=3.6`
- 激活env：`conda activate <env_name>`
- 安装python库依赖：`pip3 install -r requirements.txt`

## 3 流程

- 数据获取
  - 爬取微博文本
  - 爬取微博评论
- 数据预处理
  - 数据清洗
  - 去停用词
  - jieba分词
  - textRank关键词分析
- 分析-情感词典
  - SO-PMI新词发现
  - 心态词典扩展
  - 心态值计算
- 分析-聚类
  - K-means聚类
  - DBSCAN聚类
  - 层次聚类
- 分析-多维度分析
  - 多维心态词典
  - 多维情感分析
- 可视化
  - pyecharts
  - matplotlib
