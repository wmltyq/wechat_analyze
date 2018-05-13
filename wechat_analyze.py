import itchat, json, os, re, jieba
from matplotlib import pyplot as plt
from wordcloud import WordCloud

# 读写文件
friends_json = 'data/friends.json'
signature_txt = 'data/signature.txt'

# 读取微信朋友信息并保存到文件
def save_data():
    itchat.login()
    friends = itchat.get_friends(update=True)

    json_friends = json.dumps(friends, indent=4, ensure_ascii=False)
    print(json_friends)
    with open(friends_json, 'w', encoding='utf-8') as f:
        f.write(json_friends)


# 读取微信朋友信息文件
def read_data():
    with open(friends_json, encoding='utf-8') as f:
        friends = json.load(f)

    return friends


# 计算男女百分比
def parse_friends(friends):
    text = dict()
    male = 'male'
    female = 'female'
    other = 'other'
    # 排除第一条自己的信息
    for i in friends:
        sex = i['Sex']
        # 性别人数统计
        if sex == 1:
            text[male] = text.get(male, 0) + 1
        elif sex == 2:
            text[female] = text.get(female, 0) + 1
        else:
            text[other] = text.get(other, 0) + 1

    total = len(friends[1:])
    print('男性好友：%.2f%%' % (float(text[male]) / total * 100))
    print('女性好友：%.2f%%' % (float(text[female]) / total * 100))
    print('男性好友：%.2f%%' % (float(text[other]) / total * 100))

    draw(text)


# 男女比例柱状图
def draw(text):
    for key in text.keys():
        plt.bar(key, text[key])

    # plt.legend()
    plt.xlabel('sex')
    plt.ylabel('rate')
    plt.title('Gender of Alfred\'s friends')
    plt.savefig('img/male_female_rate.jpg')
    plt.show()


# 签名提取切分
def parse_signature(friends):
    siglist = []
    for friend in friends:
        signature = friend['Signature'].strip().replace('span', '').replace('class', '').replace('emoji', '')
        rep = re.compile('1f\d+\w*|[<>/=]')
        signature = rep.sub('', signature)
        siglist.append(signature)

    text = ''.join(siglist)
    # print(text)
    with open(signature_txt, 'w', encoding='utf-8') as f:
        wordlist = jieba.cut(text, cut_all=True)
        word_space_split = ' '.join(wordlist)
        f.write(word_space_split)


# 根据签名制作词云
def draw_signature():
    text = open(signature_txt, encoding='utf-8').read()
    my_wordcloud = WordCloud(background_color='white', max_words=2000, max_font_size=60, random_state=42, scale=2, font_path='font/simhei.ttf').generate(text)
    plt.imshow(my_wordcloud)
    plt.axis('off')
    plt.savefig('img/signature_wordcloud.jpg')
    plt.show()

if __name__ == '__main__':
    # 如果data目录不存在则创建
    if not os.path.exists('data'):
        os.makedirs('data')

    if not os.path.exists('img'):
        os.makedirs('img')

    # 是否重新读取并保存微信朋友信息
    re_save = False
    if re_save:
        save_data()

    friends = read_data()[1:]
    parse_friends(friends)

    if not os.path.exists(signature_txt):
        parse_signature(friends)

    draw_signature()

