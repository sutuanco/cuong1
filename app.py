from flask import Flask, render_template, request, flash
import solve
from sklearn.preprocessing import StandardScaler
import joblib           #savemodel
import data_shopee              #get_review
# a=solve.train()
filename = 'digits_classifier.joblib.pkl'
    #         #Save model
    # _ = joblib.dump(clf, filename, compress=9)
clf = joblib.load(filename)
app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"
@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')

standard_to = StandardScaler()

@app.route("/test", methods=['GET','POST'])
def test():
    if request.method == 'POST':        
        sentence = str(request.form['input'])
        b=solve.test_a_sentence(clf,sentence)
        if (b==1):
            flash('"{}" is predicted to be positive!'.format(sentence))
        else:
            flash('"{}" is predicted to be negative!'.format(sentence))
        return render_template('test.html')
    else:
        return render_template('test.html')

@app.route("/predict", methods=['POST'])
def predict():

    if request.method == 'POST':
        url = str(request.form['input'])
        b = solve.test_a_link_shopee(clf,url)
        a = data_shopee.getReview(url)
        return render_template('result.html', value1=b[0], value2=b[1], value3=a[0], value4=a[1], value5=round((b[0]/(b[0]+b[1]))*100, 2), value6=round((a[0]/(a[0]+a[1]))*100, 2), values1=a, values2=b)
    else:
        return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True)
