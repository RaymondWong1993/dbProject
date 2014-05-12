#-*- coding: UTF-8 -*-
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

def test(request):
  return render_to_response('test.html')

def login(request):
  if request.method == 'POST':
    request.session['user'] = request.POST.get('email', '')
    request.session['type'] = request.POST.get('type', '')
    return HttpResponseRedirect('/home/')

def logout(request):
  if 'user' in request.session.keys():
    del request.session['user']
    del request.session['type']
  return HttpResponseRedirect('/home/')
    
def home(request):
  data = []
  data0 = []
  data1 = []
  data0.append({'image':'/static/Enterprise_Information/BurgerKing/Images/burgerKingLogo.jpg', 'name':'Burger King', 'describe':'汉堡王,旧译堡加敬,是美国起家的知名国际性速食连锁店.它的海外据点多为私人经营,即特许加盟店.其中,大部分的加盟业者只经营单一店家,少数则自行发展为大型企业.截至财政年度2011年为止,汉堡王已拥有超过12400家连锁据点,分布于73个国家.'})
  data0.append({'image':'/static/Enterprise_Information/qiaoJiangNan/Images/qiaoJiangNanLogo.jpg', 'name':'俏江南', 'describe':'俏江南集团由张兰女士创始于2000年，总部位于北京，旗下品牌包括俏江南品牌餐厅和SUBU两大高端品牌，是中国最具发展潜力、值得信赖的国际餐饮服务管理集团。'})
  tmp = {'image':'/static/Enterprise_Information/siHaiYiJia/Images/siHaiYiJiaLogo.png', 'name':'四海一家', 'describe':'四海一家国际美食之都2005年成立于广州。以“集四海美食于一家”的饮食理念，云集星级中西厨师，接轨世界食尚风潮，制作超过20个系列800多款国际美食，囊括：巴西烤肉、日本刺身、铁板烧、港式烧腊、泰国美食、马来西亚经典菜式、粤式名厨“鲍罗万有”系列等，力求满足食客们无限的美食渴'}
  data0.append(tmp)
  data1.append({'image':'/static/Enterprise_Information/guangZhouJiuJia/Images/guangZhouJiuJiaLogo.jpg', 'name':'广州酒家', 'describe':'广州酒家于1939年建立， 改革开放后，广州酒家积极开拓连锁经营，企业规模由原来的一间店发展为包括有6间高级酒家、1个大型食品生产基地及30多间连锁食品商场等在内的大型饮食企业集团，总资产与达4亿多元，在行业中位居全国前列。'})
  data1.append({'image':'/static/Enterprise_Information/jiYeJia/Images/jiYeJiaLogo.jpg', 'name':'吉野家', 'describe':'吉野家是一家享有百年历史的著名日本牛肉饭专门店，始创于1899年，在日本筑地鱼市场开设第一间分店。“吉野家”的名字来源于地名，日本的吉野山地区的牛肉饭最为著名，传说是12世纪时候日本名将源义经的爱妾静在掩护义经避难之时，在吉野山把制作牛肉饭的技巧教给了当地居民，于是牛肉饭成为当地的特产美味，“吉野家”之所以这样取名，也是为了说明自己的牛肉饭正宗。'})
  tmp = {'image':'/static/Enterprise_Information/zhenGongFu/Images/zhenGongFuLogo.jpg','name':'真功夫','describe':'真功夫的品牌形象代言人乃是李小龙宗师在死亡的游戏中的形象的动漫卡通版。真功夫是知名的中式快餐品牌，主打美味、营养的原盅蒸汤、蒸饭，其前身是蔡达标与潘宇海1994年创立于广东东莞的“168”蒸品店，1997年改名为“双种子”，04年改名为“真功夫”。'}
  data1.append(tmp)
  data.append(data0)
  data.append(data1)
  user = {}
  user['logined'] = False
  user['type'] = 'customer'
  if 'user' in request.session.keys():
    user['logined'] = True
    user['type'] = request.session['type']
  return render_to_response('home.html', {'restaurants': data, 'user': user})

def register(request):
  return render_to_response('register.html')

def myAccount(request):
  userInfo = {}
  userInfo['email'] = '549425036@qq.com'
  userInfo['phone'] = '13826478796'
  userInfo['address'] = '广东省广州市番禺区大学城中山大学至善园2号'
  userInfo['b_day'] = '1993-10-11'
  userInfo['name'] = '黄佳博'
  history = []
  tmpHistory = {}
  tmpHistory['name'] = '四海一家'
  tmpHistory['date'] = '2014-5-6'
  tmpHistory['price'] = '258'
  for i in range(0,10):
    history.append(tmpHistory)
  
  for h in history:
    h['foods'] = []

  return render_to_response('myAccount.html', {'userInfo':userInfo, 'history':history, 'order':history})

def myRestaurant(request):
  info = {}
  info['name'] = '四海一家'
  info['address'] = '广州市番禺迎宾路万博中心四海一家'
  info['contact'] = '020-123456'
  info['describe'] = '高端自助餐厅'
  info['mainFoods'] = '川菜，粤菜，湘菜，西餐，甜点'

  order = []
  tmpOrder = {}
  tmpOrder['id'] = '2890123782'
  tmpOrder['date'] = '2014-4-3'
  tmpOrder['price'] = '256'
  for i in range(0,10):
    order.append(tmpOrder)

  foods = []
  tmpFood = {}
  tmpFood['name'] = '姜葱鸡'
  tmpFood['price'] = '38'
  tmpFood['describe'] = '姜葱鸡介绍姜葱鸡介绍姜葱鸡介绍姜葱鸡介绍姜葱鸡介绍姜葱鸡介绍姜葱鸡介绍姜葱鸡介绍'
  for i in range(0, 10):
    foods.append(tmpFood)

  return render_to_response('myRestaurant.html',{'info': info, 'order': order, 'foods': foods})

def listDisplay(request):
  data = []
  data0 = []
  data1 = []
  data0.append({'image':'/static/Enterprise_Information/BurgerKing/Images/burgerKingLogo.jpg', 'name':'Burger King', 'describe':'汉堡王,旧译堡加敬,是美国起家的知名国际性速食连锁店.它的海外据点多为私人经营,即特许加盟店.其中,大部分的加盟业者只经营单一店家,少数则自行发展为大型企业.截至财政年度2011年为止,汉堡王已拥有超过12400家连锁据点,分布于73个国家.'})
  data0.append({'image':'/static/Enterprise_Information/qiaoJiangNan/Images/qiaoJiangNanLogo.jpg', 'name':'俏江南', 'describe':'俏江南集团由张兰女士创始于2000年，总部位于北京，旗下品牌包括俏江南品牌餐厅和SUBU两大高端品牌，是中国最具发展潜力、值得信赖的国际餐饮服务管理集团。'})
  tmp = {'image':'/static/Enterprise_Information/siHaiYiJia/Images/siHaiYiJiaLogo.png', 'name':'四海一家', 'describe':'四海一家国际美食之都2005年成立于广州。以“集四海美食于一家”的饮食理念，云集星级中西厨师，接轨世界食尚风潮，制作超过20个系列800多款国际美食，囊括：巴西烤肉、日本刺身、铁板烧、港式烧腊、泰国美食、马来西亚经典菜式、粤式名厨“鲍罗万有”系列等，力求满足食客们无限的美食渴'}
  data0.append(tmp)
  data1.append({'image':'/static/Enterprise_Information/guangZhouJiuJia/Images/guangZhouJiuJiaLogo.jpg', 'name':'广州酒家', 'describe':'广州酒家于1939年建立， 改革开放后，广州酒家积极开拓连锁经营，企业规模由原来的一间店发展为包括有6间高级酒家、1个大型食品生产基地及30多间连锁食品商场等在内的大型饮食企业集团，总资产与达4亿多元，在行业中位居全国前列。'})
  data1.append({'image':'/static/Enterprise_Information/jiYeJia/Images/jiYeJiaLogo.jpg', 'name':'吉野家', 'describe':'吉野家是一家享有百年历史的著名日本牛肉饭专门店，始创于1899年，在日本筑地鱼市场开设第一间分店。“吉野家”的名字来源于地名，日本的吉野山地区的牛肉饭最为著名，传说是12世纪时候日本名将源义经的爱妾静在掩护义经避难之时，在吉野山把制作牛肉饭的技巧教给了当地居民，于是牛肉饭成为当地的特产美味，“吉野家”之所以这样取名，也是为了说明自己的牛肉饭正宗。'})
  tmp = {'image':'/static/Enterprise_Information/zhenGongFu/Images/zhenGongFuLogo.jpg','name':'真功夫','describe':'真功夫的品牌形象代言人乃是李小龙宗师在死亡的游戏中的形象的动漫卡通版。真功夫是知名的中式快餐品牌，主打美味、营养的原盅蒸汤、蒸饭，其前身是蔡达标与潘宇海1994年创立于广东东莞的“168”蒸品店，1997年改名为“双种子”，04年改名为“真功夫”。'}
  data1.append(tmp)
  data.append(data0)
  data.append(data1)
  if 'user' in request.session.keys():
    user = {}
    user['logined'] = True
    user['type'] = request.session['type']
  return render_to_response('listDisplay.html', {'restaurants': data, 'user': user})

def restaurantDetail(request):
  info = {}
  info['name'] = '四海一家'
  info['image'] = '/static/Enterprise_Information/siHaiYiJia/Images/siHaiYiJiaLogo.png'
  info['describe'] = '四海一家国际美食之都2005年成立于广州。以“集四海美食于一家”的饮食理念，云集星级中西厨师，接轨世界食尚风潮，制作超过20个系列800多款国际美食，囊括：巴西烤肉、日本刺身、铁板烧、港式烧腊、泰国美食、马来西亚经典菜式、粤式名厨“鲍罗万有”系列等，力求满足食客们无限的美食渴望。'
  info['address'] = '广州番禺迎宾路万博中心四海一家'
  info['contact'] = '020-34822266'

  foods = []
  tmpFood = {}
  tmpFood['name'] = '姜葱鸡'
  tmpFood['describe'] = '姜葱鸡介绍姜葱鸡介绍姜葱鸡介绍'
  tmpFood['price'] = 38
  tmpFood['image'] = '/static/images/guangZhouJiuJia_2.jpg'

  for i in range(0, 10):
    foods.append(tmpFood)
  
  user = {}
  user['logined'] = False
  user['type'] = 'customer'
  if 'user' in request.session.keys():
    user['logined'] = True
    user['type'] = request.session['type']
  return render_to_response('restaurantDetail.html', {'info': info, 'foods': foods, 'user': user})

