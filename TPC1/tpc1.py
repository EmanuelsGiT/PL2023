from pessoa import Pessoa

class tpc1:
    def __init__(self):
        self.data = []
        self.mins = {}
        self.maxs = {  }
        self.count = 0


    def add(self, pessoa):
        self.pessoas.__add__(pessoa)


    def parserFile(self,filename):
        file = open(filename)
        line = file.readline()
        while line:
            line = file.readline()
            if len(line)>0:
                content = line.replace('\n','').split(',')
                #print(content)
                idade      = int(content[0])
                sexo       = content[1]
                tensao     = int(content[2])
                colesterol = int(content[3])
                batimento  = int(content[4])
                temDoenca  = int(content[5])
                self.data.append(Pessoa(idade,sexo,tensao,colesterol,batimento,temDoenca))
        self.count = len(self.data)
        self.maxs['idade'] = max(self.data, key=lambda e: e.idade).idade
        self.mins['idade'] = min(self.data, key=lambda e: e.idade).idade
        self.maxs['colesterol'] = max(self.data, key=lambda e: e.colesterol).colesterol
        self.mins['colesterol'] = min(self.data, key=lambda e: e.colesterol).colesterol

        file.close()

    def distr_sexo(self):
        res = {
            'M': 0,
            'F': 0
        }
        for entry in self.data:
            if(entry.temDoenca == 1):
                res[entry.sexo]+=1
        res['M'] = (res['M'],res['M']/self.count)
        res['F'] = (res['F'],res['F']/self.count)
        return res

    def distr_etario(self):
        m = self.maxs['idade']
        i = self.mins['idade']
        aux = {}
        res = {}
        while i < m:
            t = (i,i+4)
            res[t] = 0
            for k in range(0,5):
                aux[i+k] = t
            i +=5
        for entry in self.data:
            t = aux[entry.idade]
            if(entry.temDoenca == 1):
                res[t] +=1
        for key in res.keys():
            resu = res[key]
            res[key] = (resu,resu/self.count)
        return res

    def distr_colesterol(self):
        m = self.maxs['colesterol']
        i = self.mins['colesterol']
        aux = {}
        res = {}
        while i < m:
            t = (i,i+9)
            res[t] = 0
            for k in range(0,10):
                aux[i+k] = t
            i +=10
        for entry in self.data:
            t = aux[entry.colesterol]
            if(entry.temDoenca == 1):
                res[t] +=1
        for key in res.keys():
            resu = res[key]
            res[key] = (resu,resu/self.count)
        return res