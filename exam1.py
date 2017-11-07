with open('book_file.txt') as f:
    f_books = f.read().split('\n')
    f_books = [book.split(';') for book in f_books]
    f_books.remove([''])

dz_books = [dict(zip(['id', 'author', 'name', 'year'], book)) for book in f_books]

books2 = []
# привожу id и год в число
for book in dz_books:
    res_id = int(book['id'])
    res_year = int(book['year'])
    book['id'] = res_id
    book['year'] = res_year
    books2.append(book)

sort_lst_books = []
sort_lst_books = sorted(books2, key=lambda x: x['id'])

# запись в файл
def write_to_file(books):
    str1 = ''
    with open('out_book.txt', 'w') as file_out:
        for book in books:
            str1 += '{};{};{};{}\n'.format(book['id'], book['author'], book['name'], book['year'])
        file_out.write(str1)

# создание новой записи
def create_new_rec(books):
    mx = max(list(book['id'] for book in books))

    new_auth = input('Введите автора книги\n')
    new_nam = input('Введите название книги\n')
    new_yea = int(input('Введите год издания книги\n'))

    dct = {"id": mx+1, "author": new_auth, "name": new_nam, "year": new_yea}
    books.append(dct)
    print("Новая книга добавлена в каталог")
    return books

#  изменение года издания книги
def change_attributes_by_year(books):
    ls = int(input('Введите ID книги для изменения названия \n'))
    chk = False
    for i in range(len(books)):
        if books[i]['id'] == ls:
            chk = True
            print("Книга с указанным ID найдена:", '\n',
                  "ID:", books[i]['id'], "\t", "Автор: ", books[i]['author'], "\t",
                  "Название: ", books[i]['name'], "\t", "Год издания: ", books[i]['year'])
            accept = int(input("Введите новое значение года издания книги для указанного ID (числом)\n"))
            books[i]['year'] = accept
            print("Поле года издания для указанного ID было изменено.\n")
            print("ID:", books[i]['id'], "\t", "Автор: ", books[i]['author'], "\t",
                  "Название: ", books[i]['name'], "\t", "Год издания: ", books[i]['year'])
        print("\n")
    if chk == False:
        print("Данного ID в каталоге нет")
    print("\n")

# изменение названия книги
def change_attributes_by_name(books):
    ls = int(input('Введите ID книги для изменения названия \n'))
    chk = False
    for i in range(len(books)):
        if books[i]['id'] == ls:
            chk = True
            print("Книга с указанным ID найдена:", '\n',
                  "ID:", books[i]['id'], "\t", "Автор: ", books[i]['author'], "\t",
                  "Название: ", books[i]['name'], "\t", "Год издания: ", books[i]['year'])
            accept = input("Введите новое значение названия книги для указанного ID \n")
            books[i]['name'] = accept
            print("Поле названия книги для указанного ID было изменено.\n")
            print("ID:", books[i]['id'], "\t", "Автор: ", books[i]['author'], "\t",
                  "Название: ", books[i]['name'], "\t", "Год издания: ", books[i]['year'])
        print("\n")
    if chk == False:
        print("Данного ID в каталоге нет")
    print("\n")

# изменение автора книги
def change_attributes_by_author(books):
    ls = int(input('Введите ID книги для изменения автора \n'))
    chk = False
    for i in range(len(books)):
        if books[i]['id'] == ls:
            chk = True
            print("Книга с указанным ID найдена:", '\n',
                  "ID:", books[i]['id'], "\t", "Автор: ", books[i]['author'], "\t",
                  "Название: ", books[i]['name'], "\t", "Год издания: ", books[i]['year'])
            accept = input("Введите новое значение автора книги для указанного ID \n")
            books[i]['author'] = accept
            print("Поле автора для указанного ID было изменено.\n")
            print("ID:", books[i]['id'], "\t", "Автор: ", books[i]['author'], "\t",
                  "Название: ", books[i]['name'], "\t", "Год издания: ", books[i]['year'])
        print("\n")
    if chk == False:
        print("Данного ID в каталоге нет")
    print("\n")

# удаление элемента книги
def remove_elem(books):
    id_key = int(input('Введите ID элемента для удаления из списка: \n'))
    i = 0
    chk = False
    for book in sort_lst_books:
        if book['id'] == id_key:
            number = i
            chk = True
            print("Книга с указанным ID найдена в списке: \n", book)
            accept = input("Подтвердите удаление элемента из каталога [Введите 'yes' в случае согласия \
             или иную комбинацию букв для отмены] \n")
            if accept == "yes":
                del sort_lst_books[number]
                print("Книга удалена из списка")
                print("С удаленным элментом: ", book)
                break
            else:
                print("Удаление книги по ID отменено пользователем \n")
        i += 1
    if chk == False:
        print("Указанный ID не найден")

# поиск по году
def search_by_year(books):
    ls = int(input('Введите год издания книги для поиска в каталоге формата 1991: \n'))
    chk = False
    for i in range(len(books)):
        if books[i]['year'] == ls:
            chk = True
            print("Книга(-и) с указанным годом издания найдена(-ы):", '\n',
            "ID:", books[i]['id'], "\n", "Автор: ", books[i]['author'], "\n",
            "Название: ", books[i]['name'], "\n", "Год издания: ", books[i]['year'])
        print("\n")
    if  chk == False:
        print("Книг с указанным годом издания в каталоге нет")
    print("\n")

# поиск по названию книги
def search_by_name(books):
    ls = input('Введите название книги: \n')
    chk = False
    ls = ls.lower()
    for i in range(len(books)):
        str2 = books[i]['name'].lower()
        if str2.find(ls)>=0:
            chk = True
            print("ID:", books[i]['id'], "\t", "Автор: ", books[i]['author'], "\t",
                  "Название: ", books[i]['name'], "\t", "Год издания: ", books[i]['year'])
    if chk == False:
        print("Книг с указанным названием в каталоге нет \n")

# поиск по автору книги
def search_by_author(books):
    ls = input('Введите имя автора книги: \n')
    chk = False
    ls = ls.lower()
    for i in range(len(books)):
        str1 = books[i]['author'].lower()
        if str1.find(ls) >= 0:
            chk = True
            print("ID:", books[i]['id'], "\t", "Автор: ", books[i]['author'], "\t",
              "Название: ", books[i]['name'], "\t", "Год издания: ", books[i]['year'])

    if chk == False:
        print("Книг с указанным автором в каталоге нет \n")

# показать все книги
def show_all_books(books):
    for i in range(len(books)):
        print("ID:", books[i]['id'], "\t", "Автор: ", books[i]['author'], "\t",
              "Название: ", books[i]['name'], "\t", "Год издания: ", books[i]['year'])
    print("\n")

# поиск по ID книги
def search_by_id(books):
    ls = int(input('Введите ID книги для поиска в каталоге \n'))
    chk = False
    for i in range(len(books)):
        if books[i]['id'] == ls:
            chk = True
            print("Книга с указанным ID найдена:", '\n', "ID:", books[i]['id'], "\n",
                  "Автор: ", books[i]['author'], "\n",
                        "Название: ", books[i]['name'], "\n", "Год издания: ", books[i]['year'])
            break
        print("\n")
    if chk == False:
        print("Данного ID в каталоге нет")
    print("\n")


def main(books):
    print("Выберите действие: \n",
          "1 -  показать все книги в каталоге\n",
          "2 -  поиск книг по ID\n",
          "3 -  поиск по автору\n",
          "4 -  поиск по названию\n",
          "5 -  поиск по году\n",
          "6 -  изменение автора книги\n",
          "7 -  изменение названия книги\n",
          "8 -  изменение изменение года издания книги\n",
          "9 -  удаление книги из каталага по ID\n",
          "10 - добавление новой записи книги\n",
          "11 - внесение изменений в файл \n"
          )
    n = int(input())
    if n == 1:
        show_all_books(sort_lst_books)
        main(books)
    elif n == 2:
        search_by_id(sort_lst_books)
        main(books)
    elif n == 3:
        search_by_author(sort_lst_books)
        main(books)
    elif n == 4:
        search_by_name(sort_lst_books)
        main(books)
    elif n == 5:
        search_by_year(sort_lst_books)
        main(books)
    elif n == 6:
        change_attributes_by_author(sort_lst_books)
        main(books)
    elif n == 7:
        change_attributes_by_name(sort_lst_books)
        main(books)
    elif n == 8:
        change_attributes_by_year(sort_lst_books)
        main(books)
    elif n == 9:
        remove_elem(sort_lst_books)
        main(books)
    elif n == 10:
        create_new_rec(sort_lst_books)
        main(books)
    elif n == 11:
        write_to_file(sort_lst_books)
        main(books)


main(sort_lst_books)
