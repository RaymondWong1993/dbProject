# coding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import render_template, request, session, abort, redirect, jsonify
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

    foods = Item.queryBySupplier(b.id)
    return render_template('myRestaurant.html', info=info, foods=foods)

@app.route('/restaurantDetail/', methods=['GET', 'POST'])
def showRestaurantDetail():
    if request.method == 'GET':
        info = Business.queryByName(request.args.get('name', None))
        if not info:
            abort(404)

        foods = Item.queryBySupplier(info.id)
        return render_template('restaurantDetail.html', info=info, foods=foods)
    else:
        foods = request.form.get('food', [])
        counts = request.form.get('count', [])
        prices = request.form.get('price', [])

        if not foods:
            return jsonify(resp=0)

        if len(foods) != len(counts) != len(prices):
            return jsonify(resp=0)

        totalPrice = reduce(lambda l, r: int(l) + int(r), prices, 0)
        try:
            Order(items=','.join(foods), counts=','.join(counts), totalPrice=totalPrice).save()
        except Exception, e:
            print str(e)
            return jsonify(resp=0)
        else:
            return jsonify(resp=1)

@app.route('/listDisplay/')
def listDisplay():
    bs = Business.queryByCategory(request.args.get('', None))
    b_datas = []
    if bs:
        fields = ('image', 'name', 'describe', )
        for b in bs:
            b_data = {}
            for k in fields:
                b_data[k] = b.__dict__.get(k)

            b_datas.append(b_data)

    return render_template('listDisplay.html', restaurants=b_datas)
