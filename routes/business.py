# coding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import render_template, request, session, abort, redirect
from routes import app
from models import Business, User, Item, Order

@app.route('/myRestaurant/')
def showMyRestaurant():
    if not session.get('user', None):
        abort(400)

    b = Business.queryByUsername(session['user'])
    if not b:
        abort(400)

    info = {}
    fields = ('image', 'name', 'address', 'contact', 'describe')
    for f in fields:
        info[f] = getattr(b, f)

    print info
    foods = Item.queryBySupplier(b.id)
    return render_template('restaurantDetail.html', info=info, foods=foods)

@app.route('/restaurantDetail/')
def showRestaurantDetail():
    if not session.get('user', None):
        abort(400)

    info = Business.queryByName(session['user'])
    if not info:
        abort(400)
    # info = {}
    # info['name'] = '四海一家'
    # info['image'] = '/static/Enterprise_Information/siHaiYiJia/Images/siHaiYiJiaImage.png'
    # info['describe'] = '四海一家国际美食之都2005年成立于广州。以“集四海美食于一家”的饮食理念，云集星级中西厨师，接轨世界食尚风潮，制作超过20个系列800多款国际美食，囊括：巴西烤肉、日本刺身、铁板烧、港式烧腊、泰国美食、马来西亚经典菜式、粤式名厨“鲍罗万有”系列等，力求满足食客们无限的美食渴望。'
    # info['address'] = '广州番禺迎宾路万博中心四海一家'
    # info['contact'] = '020-34822266'

    foods = []
    tmpFood = {}
    tmpFood['name'] = '姜葱鸡'
    tmpFood['describe'] = '姜葱鸡介绍姜葱鸡介绍姜葱鸡介绍'
    tmpFood['price'] = 38
    tmpFood['image'] = '/static/images/guangZhouJiuJia_2.jpg'

    for i in range(0, 10):
      foods.append(tmpFood)

    return render_template('restaurantDetail.html', info=info, foods=foods)
