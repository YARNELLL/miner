# Index of columns in behaviors.tsv
Impression_ID = 0 # 印象的ID
USER_ID = 1 # 用户ID
Time = 2 # 印象记录时间
HISTORY = 3 # 该用户在此印象之前的新闻点击历史记录(已点击新闻的ID列表)。点击的新闻文章按时间排序。
BEHAVIOR = 4 # 该印象中显示的新闻列表及用户的点击行为(点击为1，未点击为0)。印象中的新闻顺序被打乱了。

# Index of columns in news.tsv
NEWS_ID = 0 # 新闻ID
CATEGORY = 1 # 分类
SubCategory = 2 # 子分类
TITLE = 3 # 标题 
SAPO = 4 # 摘要
URL = 5 # 链接
Title_Entities = 6 # 新闻标题中的实体
Abstract_Entities = 7 # 新闻摘要中的实体


# 实体字段中每个部分的含义
# Label 维基数据知识图谱中的实体名称
# Type 该实体在维基数据中的类型
# WikidataId 维基数据中的实体ID
# Confidence 实体链接的可信度
# OccurrenceOffsets 标题或摘要文本中字符级实体偏移量
# SurfaceForms 原文中的原始实体名称