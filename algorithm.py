from graph_v import GraphVisualization



class Qraf():
        #Qraf sinifinin yaradicisi (konstruktoru).
    def __init__(self, tepeler_s):
        
        #tepeler_s (int): Qrafın toplam təpə sayını təyin edir.
        self.V = tepeler_s
        self.qraf = [[0 for sutun in range(tepeler_s)]
                     for sira in range(tepeler_s)]
        
        #``self.qraf``(2D) matrisi, təpələr arasındakı 
        #kənarların ağırlıqlarını və varsa məsafələrini saxlayır.
        




    def cap_et(self, mesafe):
        #Görüntü üçün əlifba ilə təpə adların yazacağıq
        self.a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
        print("Təpə \t\t Ən qısa məsafə")
        for i in range(self.V): 
            print(self.a[i], "\t\t\t", mesafe[i])




    def minimum_mesafe(self, mesafe, spt):
        #başlanğıcda minimum dəyişəninə böyük bir ədəd təyin edirik
        minimum = 1e7
        # minimum dəyəri olan node indeksi
        min_index = None
        # Bütün təpələrdən keçərək, hələ işlənməmiş və ən kiçik
        # məsafəyə malik olan təpələri tapırıq.
        for v in range(self.V):
            if mesafe[v] < minimum and spt[v] == False:
                minimum = mesafe[v]
                min_index = v
        # Ən qısa yol məsafəsi olan təpənin indeksini qaytarırıq
        return min_index





    def dijkstra(self, src):
        # Bütün təpələr üçün sonsuz dəyərlə başlayırıq
        mesafe = [1e7] * self.V
        # Başlanğıc 0 olmalıdır
        mesafe[src] = 0
        # Spt, ən qısa yolu tapdığında True olacaq
        spt = [False] * self.V
        for sira in range(self.V):# Bütün təpələr üçün dövr başlatırıq
            # Hələki işlənməmiş ən kiçik məsafəli təpəni seçirik
            u = self.minimum_mesafe(mesafe, spt)
            spt[u] = True # Buranı işlənmiş olaraq yadda saxla
            # Seçilən təpənin qonşularını yoxlayırıq
            for v in range(self.V):
                # qonşusu olmalı, hələ işlənməmiş olmalı və
                #yeni yol daha qısa olmalıdır. Əgər hamısı True olsa:
                if (self.qraf[u][v] > 0 and
                        spt[v] == False and
                        mesafe[v] > mesafe[u] + self.qraf[u][v]):
                    # Daha qısa məsafəyə güncəllə
                    mesafe[v] = mesafe[u] + self.qraf[u][v]

        # Nəticələri çap et
        self.cap_et(mesafe)







matris = [
    [0, 3, 0, 0, 0, 0, 0, 5, 0],
    [3, 0, 5, 0, 0, 0, 0, 7, 0],
    [0, 5, 0, 4, 0, 3, 0, 0, 2],
    [0, 0, 4, 0, 6, 9, 0, 0, 0],
    [0, 0, 0, 6, 0, 7, 0, 0, 0],
    [0, 0, 3, 9, 7, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 5],
    [5, 7, 0, 0, 0, 0, 1, 0, 4],
    [0, 0, 2, 0, 0, 0, 5, 4, 0]
]



g = Qraf(len(matris[0]))
g.qraf = matris
g.dijkstra(0)
GraphVisualization(matris)
