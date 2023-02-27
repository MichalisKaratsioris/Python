from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)


@app.route('/index', methods=['GET'])
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/search/<product_id>', methods=['GET', 'POST'])
def search(product_id):
    if request.method == 'GET':
        try:
            file_name = "product.csv"
            with open(file_name) as file:
                for line in file:
                    elements = line.split(";")
                    if product_id == elements[1]:
                        name_id = product_id
                        price_id = elements[2]
                        qty_id = elements[3]
            return render_template('result.html', name=name_id, price=price_id, qty=qty_id)
        except FileNotFoundError:
            return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
