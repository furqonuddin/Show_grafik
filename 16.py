from flask import Flask, render_template, request, send_from_directory
import numpy as np
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/hasil/', methods=['POST'])
def hasil():
    nilaix = request.form['nilaix']                          # name pada HTML
    nilaiy = request.form['nilaiy']

    x = nilaix.split(',')
    y = nilaiy.split(',')

    listx =[]
    listy =[]
    try:
        for i in x:
            listx.append(int(i))
        for a in y:
            listy.append(int(a))
        
        ar1 = np.array(listx)
        ar2 = np.array(listy)
        
        plt.clf()
        plt.figure('grafik')
        plt.subplot(111)        
        plt.plot(ar1,ar2)
        plt.title('Tes Matplotlib')
        plt.xlabel('Nilai x')
        plt.ylabel('Nilai y')
        plt.xticks(rotation = 90)               # atur rotasi dari value x dan y
        plt.yticks(rotation = 60)
        plt.grid(True)
        plt.legend(ar2, loc=0)           # loc => menentukan posisi legend
        
        i = 0
        while True:
            i += 1
            newname = '%s%s.png'%('filename', str(i))
            if os.path.exists('./storage/'+ newname):
                continue
            plt.savefig('./storage/'+ newname)
            break

        grafik = 'http://localhost:5000/storage/'+ newname
        nilaigrafik = {
            'sumbuX' : nilaix,
            'sumbuY' : nilaiy,
            'gambar' : grafik
        }
        return render_template('hasil.html', nilaigrafik=nilaigrafik)
    except:
        return render_template('salah.html')

@app.route('/storage/<namafile>')
def storage(namafile):
    return send_from_directory('./storage',namafile)

if __name__ == '__main__':
    app.run(debug=True)