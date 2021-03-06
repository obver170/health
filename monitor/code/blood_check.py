# Анализ крови
# источник - https://yandex.ru/health/turbo/articles?id=3811


class BloodCheck:

    def __init__(self, sex='Мужчина', rbc=4.1, mcv=81.0, mch=26.0, mchc=31.0, rfv=11.4, hgb=128.0, hct=40.0, cp=0.9,
                 plt=178.0, esr=2.0, mpv=8.0, wbc=4.0):
        self.sex = sex
        self.rbc = rbc
        self.mcv = mcv
        self.mch = mch
        self.mchc = mchc
        self.rfv = rfv
        self.hgb = hgb
        self.hct = hct
        self.cp = cp
        self.plt = plt
        self.esr = esr
        self.mpv = mpv
        self.wbc = wbc

    # Эритроциты (× 10х12/л)
    M_RBC = [4.1, 5.2]
    W_RBC = [3.6, 4.6]
    # Средний объем эритроцитов (фл или мкм3)
    M_MCV = [81, 95]
    W_MCV = [82, 98]
    # Средний уровень HGB в эритроците (пг)
    MCH = [26, 32]
    # Средняя концентрация эритроцитов в гемоглобине (%)
    MCHC = [31, 38]
    # Анизоцитоз эритроцитов (%)
    RFV = [11.3, 14.6]

    over_RBC = ["кислородное голодание организма", "перенесенное обезвоживание и нарушение водно-солевого баланса",
                "приобретенные пороки сердца, например, после перенесенного тяжелого инфекционного заболевания",
                "нарушение функции коры надпочечников", "передозировка препаратами из группы глюкокортикостероидов",
                "эритремия"]
    under_RBC = ["железодефицитная анемия", "беременность в 2 и 3 триместрах",
                 "перенесенные кровопотери и снижение ОЦК (объема циркулирующей крови)",
                 "заболевания красного костного мозга", "хронические воспалительные заболевания в организме"]

    # Гемоглобин (г/л)
    M_HGB = [128, 150]
    W_HGB = [122, 138]

    over_HGB = ["повышенное содержание тромбоцитов в крови",
                "нарушение водно-солевого баланса в организме в результате длительной диареи или рвоты",
                "сгущение крови вследствие нарушений функции свертывания",
                "передозировка противоанемическими лекарственными препаратами", "эритремия"]
    under_HGB = ["железодефицитная анемия", "внутренние кровотечения", "онкологические новообразования",
                 "поражение костного мозга", "заболевания почек, характеризующиеся нарушением их функции"]

    # Гематокрит (в % соотношении)
    M_HCT = [40, 50]
    W_HCT = [35, 44]

    over_HCT = ["обезвоживание организма", "перитонит", "тяжелые обширные ожоги", "полицитемия"]
    under_HCT = ["анемия, связанная с дефицитом железа в организме", "патологии сердца",
                 "заболевания сосудов и патологии почек", "хроническая гиперазотемия (повышение уровня азота в крови)"]

    # Цветной показатель
    CP = [0.8, 1.2]

    over_CP = ["недостаток в организме цианокобаламина", "дефицит витамина В9", "полипы в желудке",
               "опухолевые злокачественные заболевания"]
    under_CP = ["анемия у беременных",
                "увеличение ОЦК (во время беременности, когда добавляется третий плацентарный круг кровообращения)",
                "отравление свинцом"]

    # Тромбоциты (× 10х9/л)
    PLT = [178, 318]

    over_PLT = ["колит", "туберкулез", "остеомиелит", "заболевания суставов", "злокачественные новообразования",
                "цирроз печени", "миелофиброз", "период реабилитации после перенесенных хирургических вмешательств"]
    under_PLT = ["лейкоз", "СПИД", "отравления алкоголем, лекарственными препаратами, химическими веществами",
                 "длительная терапия антибиотиками, эстрогенами, гормональными средствами, Нитроглицерином, "
                 "антигистаминными препаратами",
                 "апластическая анемия", "заболевания костного мозга"]

    # СОЭ (мм/ч)
    M_ESR = [2, 16]
    W_ESR = [2, 8]

    over_ESR = ["беременность", "обострение хронических заболеваний", "отравления", "анемия",
                "заболевания соединительной ткани", "инфекционно-воспалительные заболевания", "болезни печени и почек"]
    under_ESR = ["анафилактический шок", "заболевания сердца", "патологии сосудов"]

    # Средний объем тромбоцитов (фл или мкм3)
    MPV = [8, 12]
    over_MPV = ["сахарный диабет", "системная красная волчанка",
                "период реабилитации после хирургического удаления селезенки", "алкоголизм",
                "закупорка просветов кровеносных сосудов атеросклеротическими бляшками",
                "талассемия (генетическая патология, характеризующаяся нарушением строения гемоглобина)",
                "тромбоцитодистрофия"]
    under_MPV = ["цирроз печени", "анемия (мегалобластная и пластическая)", "период реабилитации после лучевой терапии",
                 "синдром Вискота-Олдрича"]

    # Лейкоциты (× 10х9/л)
    WBC = [4, 10]

    # Лейкоцитоз
    over_WBC = ["беременность", "роды", "период накануне менструации", "усиленные физические нагрузки",
                "перегрев или переохлаждение", "повышенное психоэмоциональное перенапряжение",
                "гнойные воспалительные заболевания", "полученные тяжелые ожоги", "применение гормона инсулина",
                "злокачественные опухоли в организме", "эпилепсия", "сильное отравление", "аллергические реакции"]
    # Лейкопения
    under_WBC = ["цирроз печени", "системная красная волчанка", "лимфогрануломатоз", "лейкоз",
                 "гипоплазия костного мозга", "прием некоторых лекарственных препаратов",
                 "лучевая болезнь", "гепатит", "малярия", "акромегалия", "корь"]

    # Ретикулоциты (%)
    RET = [0.4, 1.3]

    # Проверка общего анализа крови в зависимости от пола
    def get_blood_check(self):
        result = {}

        ch_ESR = self.check_ESR()
        if ch_ESR['problem']:

            result['problem'] = True
            result['check_ESR'] = ch_ESR['check']


        ch_HCT = self.check_HCT()
        if ch_HCT['problem']:

            result['problem'] = True
            result['check_HCT'] = ch_HCT['check']

        ch_HGB = self.check_HGB()
        if ch_HGB['problem']:

            result['problem'] = True
            result['check_HGB'] = ch_HGB['check']

        ch_RBC = self.check_RBC()
        if ch_RBC['problem']:

            result['problem'] = True
            result['check_RBC'] = ch_RBC['check']

        ch_CP = self.check_CP()
        if ch_CP['problem']:

            result['problem'] = True
            result['check_CP'] = ch_CP['check']

        ch_PLT = self.check_PLT()
        if ch_PLT['problem']:

            result['problem'] = True
            result['check_PLT'] = ch_PLT['check']

        ch_MPV = self.check_MPV()
        if ch_MPV['problem']:

            result['problem'] = True
            result['check_MPV'] = ch_MPV['check']

        ch_WBC = self.check_WBC()
        if ch_WBC['problem']:

            result['problem'] = True
            result['check_WBC'] = ch_WBC['check']

        if result == {}:
            result = {
                'problem': False,
            }

        return result

    # Проверка ESR
    def check_ESR(self):
        result = {'problem': False,
                  'check': 'Показатель в пределах нормы'}
        if self.sex == 'Мужчина':
            if self.esr > self.M_ESR[1]:
                result['problem'] = True
                result['check'] = self.over_ESR
            elif self.esr < self.M_ESR[0]:
                result['problem'] = True
                result['check'] = self.under_ESR
        else:
            if self.esr > self.W_ESR[1]:
                result['problem'] = True
                result['check'] = self.over_ESR
            elif self.esr < self.W_ESR[0]:
                result['problem'] = True
                result['check'] = self.under_ESR

        return result

    # Проверка HCT
    def check_HCT(self):
        result = {'problem': False,
                  'check': 'Показатель в пределах нормы'}
        if self.sex == 'Мужчина':
            if self.hct > self.M_HCT[1]:
                result['problem'] = True
                result['check'] = self.over_HCT
            elif self.hct < self.M_HCT[0]:
                result['problem'] = True
                result['check'] = self.under_HCT
        else:
            if self.hct > self.W_HGB[1]:
                result['problem'] = True
                result['check'] = self.over_CP
            elif self.hct < self.W_HGB[0]:
                result['problem'] = True
                result['check'] = self.under_CP

        return result

    # Проверка HGB
    def check_HGB(self):
        result = {'problem': False,
                  'check': 'Показатель в пределах нормы'}
        if self.sex == 'Мужчина':
            if self.hgb > self.M_HGB[1]:
                result['problem'] = True
                result['check'] = self.over_CP
            elif self.hgb < self.M_HGB[0]:
                result['problem'] = True
                result['check'] = self.under_CP
        else:
            if self.hgb > self.W_HGB[1]:
                result['problem'] = True
                result['check'] = self.over_CP
            elif self.hgb < self.W_HGB[0]:
                result['problem'] = True
                result['check'] = self.under_CP

        return result

    # Проверка RBC
    def check_RBC(self):
        result = {'problem': False,
                  'check': 'Показатель в пределах нормы'}
        if self.sex == 'Мужчина':
            if (self.mch > self.MCH[1] or self.mchc > self.MCHC[1] or self.rfv > self.RFV[1]
                    or self.rbc > self.M_RBC[1] or self.mcv > self.M_MCV[1]):
                result['problem'] = True
                result['check'] = self.over_RBC
            elif (self.mch < self.MCH[0] or self.mchc < self.MCHC[0] or self.rfv < self.RFV[0]
                  or self.rbc < self.M_RBC[0] or self.mcv < self.M_MCV[0]):
                result['problem'] = True
                result['check'] = self.under_RBC
        else:
            if (self.mch > self.MCH[1] or self.mchc > self.MCHC[1] or self.rfv > self.RFV[1]
                    or self.rbc > self.W_RBC[1] or self.mcv > self.W_MCV[1]):
                result['problem'] = True
                result['check'] = self.over_RBC
            elif (self.mch < self.MCH[0] or self.mchc < self.MCHC[0] or self.rfv < self.RFV[0]
                  or self.rbc < self.W_RBC[0] or self.mcv < self.W_MCV[0]):
                result['problem'] = True
                result['check'] = self.under_RBC

        return result

    # Проверка CP
    def check_CP(self):
        result = {'problem': False,
                  'check': 'Показатель в пределах нормы'}
        if self.cp > self.CP[1]:
            result['problem'] = True
            result['check'] = self.over_CP
        elif self.cp < self.CP[0]:
            result['problem'] = True
            result['check'] = self.under_CP
        return result

    # Проверка PLT
    def check_PLT(self):
        result = {'problem': False,
                  'check': 'Показатель в пределах нормы'}
        if self.plt > self.PLT[1]:
            result['problem'] = True
            result['check'] = self.over_PLT
        elif self.plt < self.PLT[0]:
            result['problem'] = True
            result['check'] = self.under_PLT
        return result

    # Проверка MPV
    def check_MPV(self):
        result = {'problem': False,
                  'check': 'Показатель в пределах нормы'}
        if self.mpv > self.MPV[1]:
            result['problem'] = True
            result['check'] = self.over_MPV
        elif self.mpv < self.MPV[0]:
            result['problem'] = True
            result['check'] = self.under_MPV
        return result

    # Проверка WBC
    def check_WBC(self):
        result = {'problem': False,
                  'check': 'Показатель в пределах нормы'}
        if self.wbc > self.WBC[1]:
            result['problem'] = True
            result['check'] = self.over_WBC
        elif self.wbc < self.WBC[0]:
            result['problem'] = True
            result['check'] = self.under_WBC
        return result


# bc = BloodCheck(mcv=1, mch=1)
# print(bc.get_blood_check())

