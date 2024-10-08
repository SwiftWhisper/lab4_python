text = "Договір про Антарктику окреслив захист континенту та ефективно припинив напруженість над територіальними претензіями. Хоча договір не змушує будь-яку країну відмовитися від свого права на територіальні претензії або позбавляти суверенітет над цією землею, вона перешкоджає країнам-членам заявляти про ці вимоги через будь-яку мирну діяльність."
# Використана функція len для того щоб підрахувати кількість символів у тексті
charCount = len(text)
print("Кількість символів у тексті:", charCount)

# Використана функція split() для того щоб розділити речення на слова, щоб потім підрахувати їх.
words = text.split()
wordCount = len(words)
print("Кількість слів в тексті:", wordCount)

# Використана функція lower() для того, щоб увесь текст був у малому регістрі
lowRegText = text.lower()
print("Текст у малому регістрі: \n", lowRegText)

# Використана функція reversed() для тексту у зворотньому порядку
reversed_text = ''.join(reversed(text))
print("Текст в зворотньому порядку; \n", reversed_text)

# Використана функція upper() для тексту в великому регістрі
upRegText= text.upper()
print("Текст у великому регістрі: \n", upRegText)

# Використана функція join() для об'єднання символів рядка дефісом
joined_text = '-'.join(text)
print("Текст з об'єднаними символами рядків: \n", joined_text)