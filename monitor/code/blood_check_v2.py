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

    def get_state(self, mark):
        result = {'state': 'Показатели в норме'}
        if mark in ['over_RBC', 'over_MCV', 'over_MCH', 'over_MCHC', 'over_RFV']:
            result = {'state': 'кислородное голодание организма,'
                               ' перенесенное обезвоживание и нарушение водно-солевого баланса,'
                               ' приобретенные пороки сердца, например,'
                               ' после перенесенного тяжелого инфекционного заболевания, '
                               'нарушение функции коры надпочечников, '
                               'передозировка препаратами из группы глюкокортикостероидов, эритремия'}

        if mark in ['under_RBC', 'under_MCV', 'under_MCH', 'under_MCHC', 'under_RFV']:
            result = {'state': 'железодефицитная анемия, беременность в 2 и 3 триместрах,'
                               'перенесенные кровопотери и снижение ОЦК (объема циркулирующей крови),'
                               'заболевания красного костного мозга, '
                               'хронические воспалительные заболевания в организме'}

        if mark == 'over_HGB':
            result = {'state': 'повышенное содержание тромбоцитов в крови, '
                               'нарушение водно-солевого баланса в организме в результате длительной диареи или рвоты,'
                               'сгущение крови вследствие нарушений функции свертывания,'
                               'передозировка противоанемическими лекарственными препаратами, эритремия'}
        if mark == 'under_HGB':
            result = {'state': 'железодефицитная анемия, внутренние кровотечения, онкологические новообразования,'
                               'поражение костного мозга, заболевания почек, характеризующиеся нарушением их функции'}

        if mark == 'over_HCT':
            result = {'state': 'обезвоживание организма, перитонит, тяжелые обширные ожоги, полицитемия'}
        if mark == 'under_HCT':
            result = {'state': 'анемия, связанная с дефицитом железа в организме, патологии сердца,'
                               'заболевания сосудов и патологии почек, хроническая гиперазотемия '
                               '(повышение уровня азота в крови)'}

        if mark == 'over_CP':
            result = {'state': 'недостаток в организме цианокобаламина, дефицит витамина В9, полипы в желудке,'
                               'опухолевые злокачественные заболевания'}
        if mark == 'under_CP':
            result = {'state': 'анемия у беременных,'
                               'увеличение ОЦК (во время беременности, '
                               'когда добавляется третий плацентарный круг кровообращения), отравление свинцом'}

        if mark == 'over_PLT':
            result = {'state': 'колит, туберкулез, остеомиелит, заболевания суставов, злокачественные новообразования,'
                               'цирроз печени, миелофиброз, период реабилитации после перенесенных '
                               'хирургических вмешательств'}
        if mark == 'under_PLT':
            result = {'state': 'лейкоз, СПИД, отравления алкоголем, лекарственными препаратами, химическими веществами,'
                               'длительная терапия антибиотиками, эстрогенами, гормональными средствами, '
                               'Нитроглицерином, антигистаминными препаратами, апластическая анемия, '
                               'заболевания костного мозга'}

        if mark == 'over_ESR':
            result = {'state': 'беременность, обострение хронических заболеваний, отравления, анемия,'
                               'заболевания соединительной ткани, инфекционно-воспалительные заболевания,'
                               'болезни печени и почек'}
        if mark == 'under_ESR':
            result = {'state': 'анафилактический шок, заболевания сердца, патологии сосудов'}

        if mark == 'over_MPV':
            result = {'state': 'сахарный диабет, системная красная волчанка,'
                               'период реабилитации после хирургического удаления селезенки, алкоголизм,'
                               'закупорка просветов кровеносных сосудов атеросклеротическими бляшками,'
                               'талассемия (генетическая патология, характеризующаяся нарушением строения гемоглобина),'
                               'тромбоцитодистрофия'}
        if mark == 'under_MPV':
            result = {'state': 'цирроз печени, анемия (мегалобластная и пластическая),'
                               'период реабилитации после лучевой терапии, синдром Вискота-Олдрича'}
        # Лейкоцитоз
        if mark == 'over_WBC':
            result = {'state': 'беременность, роды, период накануне менструации, усиленные физические нагрузки,'
                               'перегрев или переохлаждение, повышенное психоэмоциональное перенапряжение,'
                               'гнойные воспалительные заболевания, полученные тяжелые ожоги, '
                               'применение гормона инсулина, злокачественные опухоли в организме, эпилепсия, '
                               'сильное отравление, аллергические реакции'}
        # Лейкопения
        if mark == 'under_WBC':
            result = {'state': 'цирроз печени, системная красная волчанка, лимфогрануломатоз, лейкоз,'
                               'гипоплазия костного мозга, прием некоторых лекарственных препаратов,'
                               'лучевая болезнь, гепатит, малярия, акромегалия, корь'}

        return result

    # Ретикулоциты (%)
    RET = [0.4, 1.3]

    # Проверка общего анализа крови в зависимости от пола
    def get_blood_check(self):
        result = {'problem':False}
        marks = []
        ch_RBC = self.check_RBC()
        if ch_RBC['problem']:
            marks.append(ch_RBC['mark'])

        ch_MCV = self.check_MCV()
        if ch_MCV['problem']:
            marks.append(ch_MCV['mark'])

        ch_MCH = self.check_MCH()
        if ch_MCH['problem']:
            marks.append(ch_MCH['mark'])

        ch_MCHC = self.check_MCHC()
        if ch_MCHC['problem']:
            marks.append(ch_MCHC['mark'])

        ch_RFV = self.check_RFV()
        if ch_RFV['problem']:
            marks.append(ch_RFV['mark'])

        ch_ESR = self.check_ESR()
        if ch_ESR['problem']:
            marks.append(ch_ESR['mark'])

        ch_HCT = self.check_HCT()
        if ch_HCT['problem']:
            marks.append(ch_HCT['mark'])

        ch_HGB = self.check_HGB()
        if ch_HGB['problem']:
            marks.append(ch_HGB['mark'])

        ch_CP = self.check_CP()
        if ch_CP['problem']:
            marks.append(ch_CP['mark'])

        ch_PLT = self.check_PLT()
        if ch_PLT['problem']:
            marks.append(ch_PLT['mark'])

        ch_MPV = self.check_MPV()
        if ch_MPV['problem']:
            marks.append(ch_MPV['mark'])

        ch_WBC = self.check_WBC()
        if ch_WBC['problem']:
            marks.append(ch_WBC['mark'])

        result['check'] = ''

        # Проверяю, выявлены ли проблемы или список пуск, если проблемы выявлены, то добавляю индикатор проблемы
        # и возможные состояния в result
        if marks != []:
            result['problem'] = True
            result['marks'] = marks
            for i in marks:
                state = self.get_state(i)
                if state['state'] not in result['check']:
                    if result['check'] != '':
                        result['check'] += ', ' + state['state']
                    else:
                        result['check'] += state['state']

        return result

    # Проверка RBC
    def check_RBC(self):
        # Эритроциты (× 10х12/л)
        M_RBC = [4.1, 5.2]
        W_RBC = [3.6, 4.6]

        result = {'problem': False}

        if self.sex == 'Мужчина':
            if self.rbc > M_RBC[1]:
                result['mark'] = 'over_RBC'
            elif self.rbc < M_RBC[0]:
                result['mark'] = 'under_RBC'
        else:
            if self.rbc > W_RBC[1]:
                result['mark'] = 'over_RBC'
            elif self.rbc < W_RBC[0]:
                result['mark'] = 'under_RBC'

        if 'mark' in result:
            result['problem'] = 'True'

        return result

    # Проверка MCV
    def check_MCV(self):
        # Средний объем эритроцитов (фл или мкм3)
        M_MCV = [81, 95]
        W_MCV = [82, 98]

        result = {'problem': False}
        if self.sex == 'Мужчина':
            if self.mcv > M_MCV[1]:
                result['mark'] = 'over_MCV'
            elif self.mcv < M_MCV[0]:
                result['mark'] = 'under_MCV'
        else:
            if self.mcv > W_MCV[1]:
                result['mark'] = 'over_MCV'
            elif self.mcv < W_MCV[0]:
                result['mark'] = 'under_MCV'

        if 'mark' in result:
            result['problem'] = 'True'

        return result

    # Проверка MCH
    def check_MCH(self):
        # Средний уровень HGB в эритроците (пг)
        MCH = [26, 32]

        result = {'problem': False}

        if self.mch > MCH[1]:
            result['mark'] = 'over_MCH'
        elif self.mch < MCH[0]:
            result['mark'] = 'under_MCH'

        if 'mark' in result:
            result['problem'] = 'True'

        return result

    # Проверка MCHC
    def check_MCHC(self):
        # Средняя концентрация эритроцитов в гемоглобине (%)
        MCHC = [31, 38]

        result = {'problem': False}

        if self.mchc > MCHC[1]:
            result['mark'] = 'over_MCHC'
        elif self.mchc < MCHC[0]:
            result['mark'] = 'under_MCHC'

        if 'mark' in result:
            result['problem'] = 'True'

        return result

    # Проверка RFV
    def check_RFV(self):
        # Анизоцитоз эритроцитов (%)
        RFV = [11.3, 14.6]

        result = {'problem': False}

        if self.rfv > RFV[1]:
            result['mark'] = 'over_RFV'
        elif self.rfv < RFV[0]:
            result['mark'] = 'under_RFV'

        if 'mark' in result:
            result['problem'] = 'True'

        return result

    # Проверка ESR
    def check_ESR(self):
        # СОЭ (мм/ч)
        M_ESR = [2, 16]
        W_ESR = [2, 8]

        result = {'problem': False}
        if self.sex == 'Мужчина':
            if self.esr > M_ESR[1]:
                result['mark'] = 'over_ESR'
            elif self.esr < M_ESR[0]:
                result['mark'] = 'under_ESR'
        else:
            if self.esr > W_ESR[1]:
                result['mark'] = 'over_ESR'
            elif self.esr < W_ESR[0]:
                result['mark'] = 'under_ESR'

        if 'mark' in result:
            result['problem'] = 'True'

        return result

    # Проверка HCT
    def check_HCT(self):
        # Гематокрит (в % соотношении)
        M_HCT = [40, 50]
        W_HCT = [35, 44]

        result = {'problem': False}
        if self.sex == 'Мужчина':
            if self.hct > M_HCT[1]:
                result['mark'] = 'over_HCT'
            elif self.hct < M_HCT[0]:
                result['mark'] = 'under_HCT'
        else:
            if self.hct > W_HCT[1]:
                result['mark'] = 'over_HCT'
            elif self.hct < W_HCT[0]:
                result['mark'] = 'under_HCT'

        if 'mark' in result:
            result['problem'] = 'True'

        return result

    # Проверка HGB
    def check_HGB(self):
        # Гемоглобин (г/л)
        M_HGB = [128, 150]
        W_HGB = [122, 138]

        result = {'problem': False}
        if self.sex == 'Мужчина':
            if self.hgb > M_HGB[1]:
                result['mark'] = 'over_HGB'
            elif self.hgb < M_HGB[0]:
                result['mark'] = 'under_HGB'
        else:
            if self.hgb > W_HGB[1]:
                result['mark'] = 'over_HGB'
            elif self.hgb < W_HGB[0]:
                result['mark'] = 'under_HGB'

        if 'mark' in result:
            result['problem'] = 'True'

        return result

    # Проверка CP
    def check_CP(self):
        # Цветной показатель
        CP = [0.8, 1.2]

        result = {'problem': False}
        if self.cp > CP[1]:
            result['mark'] = 'over_CP'
        elif self.cp < CP[0]:
            result['mark'] = 'under_CP'

        if 'mark' in result:
            result['problem'] = 'True'

        return result

    # Проверка PLT
    def check_PLT(self):
        # Тромбоциты (× 10х9/л)
        PLT = [178, 318]

        result = {'problem': False}
        if self.plt > PLT[1]:
            result['mark'] = 'over_PLT'
        elif self.plt < PLT[0]:
            result['mark'] = 'under_PLT'

        if 'mark' in result:
            result['problem'] = 'True'

        return result

    # Проверка MPV
    def check_MPV(self):
        # Средний объем тромбоцитов (фл или мкм3)
        MPV = [8, 12]
        result = {'problem': False}
        if self.mpv > MPV[1]:
            result['mark'] = 'over_MPV'
        elif self.mpv < MPV[0]:
            result['mark'] = 'under_MPV'

        if 'mark' in result:
            result['problem'] = 'True'

        return result

    # Проверка WBC
    def check_WBC(self):
        # Лейкоциты (× 10х9/л)
        WBC = [4, 10]

        result = {'problem': False}
        if self.wbc > WBC[1]:
            result['mark'] = 'over_WBC'
        elif self.wbc < WBC[0]:
            result['mark'] = 'under_WBC'

        if 'mark' in result:
            result['problem'] = 'True'

        return result

# bc = BloodCheck(mcv=1, mch=1)
# print(bc.get_blood_check())
