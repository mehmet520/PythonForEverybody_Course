class araba:
    hiz = 0
    renk = 'siyah'
    tekersayisi = 4
    def hizlan(self):
        self.hiz = self.hiz +1

x = araba()
x.hiz = 100
x.renk = 'sari'
x.marka = 'bmw'
x.hizlan()
print ('x arabanin hizi', x.hiz, '\n x arabanin rengi: ', x.renk, '\nx araba marka: ', x.marka)

y = araba()
y.hizlan()
print('y arabanin hizi: ', y.hiz, '\n x arabanin rengi: ',y.renk)
