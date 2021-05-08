from flask import Flask,request,render_template
import pickle

file = open('cancer.pkl','rb')
lr = pickle.load(file)
file.close()

"""file1 = open('kidney1.pkl','rb')
rf = pickle.load(file1)
file1.close()
"""

file2 = open('liver.pkl','rb')
lr1 = pickle.load(file2)
file2.close()

file3 = open('heart.pkl','rb')
lr3 = pickle.load(file3)
file3.close()


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/cancer',methods = ['GET','POST'])
def cancer():
    #if request == 'POST'
    if request.method == 'POST':
        my_dict = request.form
        meanrad = float(my_dict['meanrad'])
        meanper = float(my_dict['meanper'])
        meanarea = float(my_dict['meanarea'])
        meancon = float(my_dict['meancon'])
        concavemean= float(my_dict['concavemean'])
        concavepoints = float(my_dict['concavepoints'])
        radworst= float(my_dict['radworst'])
        perworst= float(my_dict['perworst'])
        concaveworst= float(my_dict['concaveworst'])
        input_features = [meanrad,meanper,meanarea,meancon,concavemean,concavepoints,radworst,perworst,concaveworst]
        inf = lr.predict([input_features])
        if inf == 1:
            inf = 'YES'
        else:
            inf = 'NO'
        return render_template('cancershow.html',inf = inf)
    
    return render_template('cancer.html')




"""<!-- age	bp	sg	al	su	bgr	bu	sc	hemo	pcv	htn	appet	pe	ane	 -->

    <!-- age - age
bp - blood pressure
sg - specific gravity
al - albumin
su - sugar
bgr - blood glucose random
bu - blood urea
sc - serum creatinine
hemo - hemoglobin
pcv - packed cell volume
htn - hypertension
appet - appetite
pe - pedal edema
ane - anemia
-->

"""



@app.route('/kidney',methods = ['GET','POST'])
def kidney():
    #if request == 'POST'
    if request.method == 'POST':
        my_dict1 = request.form
        age = int(my_dict1['age'])
        htn = float(my_dict1['htn'])
        sg = float(my_dict1['sg'])
        al = float(my_dict1['al'])
        su= float(my_dict1['su'])
        bgrk = float(my_dict1['bgrk'])
        bu= float(my_dict1['bu'])
        sc= float(my_dict1['sc'])
        hemo= float(my_dict1['hemo'])
        pcv= float(my_dict1['pcv'])
        input_features1 = [age,htn,sg,al,su,bgrk,bu,sc,hemo,pcv]
        inf = lr1.predict([input_features1])
        if inf == 1:
            inf = 'YES'
        elif inf == 2:
            inf = 'NO'
        return render_template('kidneyshow.html',inf = inf)
    
    return render_template('kidney.html')


@app.route('/heart',methods = ['GET','POST'])
def heart():
    #if request == 'POST'
    if request.method == 'POST':
        my_dict2 = request.form
        age1 = float(my_dict2['age1'])
        htn1 = float(my_dict2['htn1'])
        sg1 = float(my_dict2['sg1'])
        sg2 = float(my_dict2['sg2'])
        al1 = float(my_dict2['al1'])
        su1= float(my_dict2['su1'])
        bgrk1 = float(my_dict2['bgrk1'])
        bu1= float(my_dict2['bu1'])
        sc1= float(my_dict2['sc1'])
        hemo1= float(my_dict2['hemo1'])
        pcv1= float(my_dict2['pcv1'])
        pcv2= float(my_dict2['pcv2'])
        pcv3= float(my_dict2['pcv3'])
        input_features2 = [age1,htn1,sg1,sg2,al1,su1,bgrk1,bu1,sc1,hemo1,pcv1,pcv2,pcv3]
        inf = lr3.predict([input_features2])
        if inf == 1:
            inf = 'YES'
        elif inf == 0:
            inf = 'NO'
        return render_template('heartshow.html',inf = inf)
    
    return render_template('heart.html')

@app.route('/aboutcancer')
def aboutcancer():
    return render_template('aboutcancer.html')

@app.route('/aboutliver')
def aboutliver():
    return render_template('aboutliver.html')

@app.route('/aboutheart')
def aboutheart():
    return render_template('aboutheart.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug = True)