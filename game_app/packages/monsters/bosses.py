class Boss:
    def __init__(self, level, name):
        self.level = level
        self.name = name
        self.damage = 10 * self.level
        self.hit_points = 10 * self.level * 2
        self.dialogs = ['Не iнтересно', 'Слабенько', 'Ну таке на 3', 'Iди роби хiдер']
        self.block_skills_dialog = ['Не хочу я слухати цей бред', 'Перекур', 'Какой Курить нiякого курить', 'Тебе шо в гуглi забанили']
        self.quiz = [
            {
                'text': 'Шо таке полiморфiзм?',
                'questions': [
                    'Бред',
                    'Шось на бекендськом',
                    'це здатність обєкта використовувати методи похідного класу',
                    'це здатність обєкта використовувати методи класу'
                ],
                'good': 'це здатність обєкта використовувати методи похідного класу'
            },
            {
                'text': 'Шо таке ООП?',
                'questions': [
                    'Опорно Ональный Проход',
                    'Офiгенний Олексiйович Петро',
                    'Обєктно Орієнтоване Питання',
                    'Обєктно Орієнтоване Програмування',
                ],
                'good': 'Обєктно Орієнтоване Програмування'
            },
            {
                'text': 'Шо зробив Петро Порошенко для Українаи?',
                'questions': [
                    'Викопав чорне море i насыпав Карпати',
                    'Всього по трошку',
                    'Поставив ПВО',
                    'Нiчього',
                ],
                'good': 'Викопав чорне море i насыпав Карпати'
            },
        ]

    def get_damage(self, damage_value):
        if self.hit_points <= int(damage_value):
            self.hit_points = 0
        else:
            self.hit_points -= int(damage_value)

    def block_skills(self, attack_index):
        return self.block_skills_dialog[int(attack_index)]