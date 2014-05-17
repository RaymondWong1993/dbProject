#-*- coding: utf-8 -*-
from datetime import datetime
from common.db import initDb
from models.business import Business
from models.user import User
from models.item import Item
from models.order import Order

def initDatabase():
    Business.init()
    User.init()
    Item.init()
    Order.init()

    businesses_data = [
        {'username': 'burder', 'hashpw': 'burder', 'image':'/static/Enterprise_Information/BurgerKing/Images/burgerKingLogo.jpg', 'name':'Burger King', 'describe':'汉堡王,旧译堡加敬,是美国起家的知名国际性速食连锁店.它的海外据点多为私人经营,即特许加盟店.其中,大部分的加盟业者只经营单一店家,少数则自行发展为大型企业.截至财政年度2011年为止,汉堡王已拥有超过12400家连锁据点,分布于73个国家.', 'category': '美国'},
        {'username': 'jiangnan', 'hashpw': 'jiangnan', 'image':'/static/Enterprise_Information/qiaoJiangNan/Images/qiaoJiangNanLogo.jpg', 'name':'俏江南', 'describe':'俏江南集团由张兰女士创始于2000年，总部位于北京，旗下品牌包括俏江南品牌餐厅和SUBU两大高端品牌，是中国最具发展潜力、值得信赖的国际餐饮服务管理集团。', 'category': '日本'},
        {'username': 'sihaiyijia', 'hashpw': 'sihaiyijia', 'image':'/static/Enterprise_Information/siHaiYiJia/Images/siHaiYiJiaLogo.png', 'name':'四海一家', 'describe':'四海一家国际美食之都2005年成立于广州。以“集四海美食于一家”的饮食理念，云集星级中西厨师，接轨世界食尚风潮，制作超过20个系列800多款国际美食，囊括：巴西烤肉、日本刺身、铁板烧、港式烧腊、泰国美食、马来西亚经典菜式、粤式名厨“鲍罗万有”系列等，力求满足食客们无限的美食渴', 'category': '川菜'},
        {'username': 'guangzhou', 'hashpw': 'guangzhou', 'image':'/static/Enterprise_Information/guangZhouJiuJia/Images/guangZhouJiuJiaLogo.jpg', 'name':'广州酒家', 'describe':'广州酒家于1939年建立， 改革开放后，广州酒家积极开拓连锁经营，企业规模由原来的一间店发展为包括有6间高级酒家、1个大型食品生产基地及30多间连锁食品商场等在内的大型饮食企业集团，总资产与达4亿多元，在行业中位居全国前列。', 'category': '粤菜'},
        {'username': 'jiyejia', 'hashpw': 'jiyejia', 'image':'/static/Enterprise_Information/jiYeJia/Images/jiYeJiaLogo.jpg', 'name':'吉野家', 'describe':'吉野家是一家享有百年历史的著名日本牛肉饭专门店，始创于1899年，在日本筑地鱼市场开设第一间分店。“吉野家”的名字来源于地名，日本的吉野山地区的牛肉饭最为著名，传说是12世纪时候日本名将源义经的爱妾静在掩护义经避难之时，在吉野山把制作牛肉饭的技巧教给了当地居民，于是牛肉饭成为当地的特产美味，“吉野家”之所以这样取名，也是为了说明自己的牛肉饭正宗。', 'category': '日本'},
        {'username': 'zhengongfu', 'hashpw': 'zhengongfu', 'image':'/static/Enterprise_Information/zhenGongFu/Images/zhenGongFuLogo.jpg','name':'真功夫','describe':'真功夫的品牌形象代言人乃是李小龙宗师在死亡的游戏中的形象的动漫卡通版。真功夫是知名的中式快餐品牌，主打美味、营养的原盅蒸汤、蒸饭，其前身是蔡达标与潘宇海1994年创立于广东东莞的“168”蒸品店，1997年改名为“双种子”，04年改名为“真功夫”。', 'category': '老人菜谱'},
    ]

    map(lambda x: Business(**x).save(), businesses_data)

    User(username='admin', hashpw='admin').save()
