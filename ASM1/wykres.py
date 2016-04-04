import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
#from matplotlib import style
import database as db

db.connect('/var/www/demo/baza.db')
kompTab = ['C1','C2','C3','C4','C5','external_recycle']#,'inflow']
fracTab = ['so','sno','snd','snh','ss','si','xh','xa','xs','xnd','xp','xi']
layerTab = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10']
tp = 20 #db.selectLast('params','tp')
step = int(300/tp)
fig = plt.figure()
#style.use('fivethirtyeight') #styl wykresu

for komp in kompTab:
	table=komp
	last_id = db.selectLast(table,'id')
	for frac in fracTab:
		xTab = []
		yTab=[]
		fraction = frac
		for id in range(1,last_id,step):
			xs = id*tp/86400.0
			xTab.append(xs)
			yTab.append(db.selectFraction(table,fraction, str(id)))
		fig.clear()
		plt.plot(xTab,yTab,color='b',linewidth=2.0)
		plt.xlim(xTab[0],xTab[len(xTab)-1])
		plt.title(fraction)
		plt.savefig('/var/www/demo/ASM1/wyniki/' + table + '/' + table + fraction  + '.png')

table = 'settler'
for layer in layerTab:
	xTab = []
	yTab = []
	last_id = db.selectLast(table,'id')
	for id in range(1,last_id,150):
		xs = id*tp/86400.0
		xTab.append(xs)
		yTab.append(db.selectFraction(table,layer, str(id)))
	fig.clear()
	plt.plot(xTab,yTab,color='g',linewidth=2.0)
	plt.xlim(xTab[0],xTab[len(xTab)-1])
	plt.title(layer)
	plt.savefig('/var/www/demo/ASM1/wyniki/' + table + '/' + layer  + '.png')
