from functions import load_random_word
from classes import Player


def main():
    game_is_on = True

    print("Введите имя игрока:")

    #имя игрока хранится в name_input
    name_input = input()
    print(f"Привет, {name_input}!")

    main_word = load_random_word()


    word = main_word.base_word
    word_count = main_word.subwords_len()
    print(f"Составьте {word_count} слов из слова {word.upper()}"
          f"\nСлова должны быть не короче 3 букв")
    print("Чтобы закончить игру, угадайте все слова или напишите 'stop'")


    player = Player(name_input)

    while game_is_on:

        print("Введите слово:")
        user_input = input()

        #проверка если инпут юзера в списке used_words, тогда print
        if player.has_used(user_input):
            print(f"Слово {user_input} уже было использовано.")

        #проверка если юзер инпут в списке допустимых подслов,
        #тогда его инпут добавляется в список used_words и выводится "верно"
        elif main_word.has_subword(user_input):

            player.add_word_to_used(user_input)
            print("Верно")

            # print(player.used_words)

        #проверка на длину слова если меньше 3 букв
        elif len(user_input) < 3:
            print("Слишком короткое слово")

        #проверка юзер инпута на стоп и stop. Остановка программы
        elif user_input == "stop" or user_input == "стоп":
            print(f"Завершение работы программы\nОтгаданное вами кол-во слов - {player.count_used_words()}...")

            game_is_on = False

        #если неверно отвечено слово
        else:
            print("Неверно.")

        #завершение работы цикла если отгаданное кол-во слов пользователем набрано
        #отгаданніе слова лежат в списке used_words
        if player.count_used_words() == word_count:
            print(f"Игра завершена, {player}. Отгаданное вами кол-во слов - {player.count_used_words()}!")
            game_is_on = False




main()










