

def fight_process(hero_class, enemy_class):
    while enemy_class.hit_points != 0:
        print(f'{enemy_class.name} HP: {enemy_class.hit_points}')
        print('----------------------------------')
        print(f'{hero_class.name} HP: {hero_class.hit_points}')
        print('---  /  Actions  /  ---')
        for i, attack in enumerate(hero_class.attacks):
            print(f'{i}) Здiбностi {attack["name"]}')
        hero_action = str(input('Виберiть дiю: '))

        for i, attack in enumerate(hero_class.attacks):
            if str(i) == hero_action:
                if enemy_class.name == 'IGIBO':
                    if attack['name'] == 'Влупити (Default)':
                        print(f'Дiя {attack["name"]} - {hero_class.attack(i)} dmg')
                        enemy_class.get_damage(hero_class.attack(i))
                    else:
                        print(enemy_class.block_skills(i))
                else:
                    print(f'Дiя {attack["name"]} - {hero_class.attack(i)} dmg')
                    enemy_class.get_damage(hero_class.attack(i))

        if enemy_class.hit_points == 0:
            if enemy_class.name == 'IGIBO':
                quiz_index = 0
                while quiz_index <= 2:
                    print('-------------------------------------------')
                    print(f'{enemy_class.quiz[int(quiz_index)]["text"]}')
                    print('-------------------------------------------')
                    question_index = 0
                    for question in enemy_class.quiz[int(quiz_index)]['questions']:
                        print(f'{question_index}) {question}')
                        question_index = question_index + 1
                    print('-------------------------------------------')
                    hero_answer = input('Ответ: ')

                    print(enemy_class.quiz[int(quiz_index)]['questions'][int(hero_answer)])
                    print(enemy_class.quiz[int(quiz_index)]['good'])

                    if enemy_class.quiz[int(quiz_index)]['questions'][int(hero_answer)] == enemy_class.quiz[int(quiz_index)]['good']:
                        quiz_index = quiz_index + 1
                        continue
                    else:
                        print('Ти прогдав iди пиляй хiдер')
                        break
                else:
                    print('You Won!')
            else:
                hero_class.set_experience(enemy_class.drop_experience())
        else:
            enemy_class.hit()
            if hero_class.hit_points <= enemy_class.damage:
                print('You Die...')
                break
            else:
                hero_class.get_damage(enemy_class.damage)