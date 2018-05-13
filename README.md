# wechat_analyze

偶然间看到一篇题为“[我用 Python 爬取微信好友，最后发现一个大秘密](https://mp.weixin.qq.com/s?__biz=MzI5OTY0MTMyMg==&mid=2247488236&idx=1&sn=d63533371417c54ab23c5062a9cc3a22&chksm=ec922269dbe5ab7f41372156afc928a4ac78a7f7b1ebb9baa9d564afcbed243c053d9e6dd316&mpshare=1&scene=23&srcid=0512KEQLKRticMNgNNw0c9HJ#rd)”的公众号文章，觉得很有意思。于是就照着作者的思路实现了一遍，但是每次获取数据的时候都需要扫码登录显得很繁琐，索性就将第一次获取到的数据保存到文本，之后需要的数据就从文本读取。

我的男女比例还是比较均衡的：

![运行效果](https://github.com/wmltyq/wechat_analyze/blob/master/img/run.jpg)

![男女比例](https://github.com/wmltyq/wechat_analyze/blob/master/img/male_female_rate.jpg)

根据词云显示的效果来看，整体还是比较积极向上的：

![运行效果](https://github.com/wmltyq/wechat_analyze/blob/master/img/signature_wordcloud.jpg)