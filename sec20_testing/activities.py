def eat(food, is_healthy):
    healthy_foods = [
        'okra',
        'beans',
        'broccoli',
        'tomatoes',
        'cucumber',
        'carrots'
    ]
    if is_healthy and food in healthy_foods:
        return f"I am eating {food} because I want to keep in shape."
    else:
        return f"I am eating {food} because we only live once."


def sleep(hours):
    if hours < 6:
        return f'I am still tired after spelling for {4} hours.'
    elif hours > 8:
        return 'Ptz! I slept too much! I am late for work.'


def is_funny(person):
    funny_people = ['Tom Cavalcante', 'Leo Lins', 'Jim Carrey']
    not_funny_people = ['Sérgio Malandro']
    if person in funny_people:
        return True
    elif person in not_funny_people:
        return False
    else:
        return "I don't known if this person is funny."
