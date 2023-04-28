import socket
import threading
import random
import queue

def start_server():
    messages = queue.Queue() # Создаем очередь сообщений, в которую будут добавляться входящие сообщения от клиентов.
    clients = [] # Создаем список клиентов, которые подключены к серверу.
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Создаем UDP сокет для сервера.
    admin = False
    port = 0
    name = input("Nickname: ") # Запрашиваем у пользователя ввод никнейма и сохраняем его в переменную 

    print("type /new *index* or /connect *index*")
    while True:
        msg = input()
        words = msg.split() # Запрашиваем у пользователя ввод команды и сохраняем ее 

        if words[0] == "/new":
            admin = True
            port = int(words[1])
            server.bind(("localhost", port)) # Связываем серверный сокет с адресом "localhost" и портом
            print(f"Group created with ID: {port}")
            break

        elif words[0] == "/connect":
            client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            # Создается объект сокета server с использованием протокола UDP (SOCK_DGRAM).
            # Протокол UDP обеспечивает неупорядоченную и ненадежную доставку пакетов, 
            # но требует меньше ресурсов, чем протокол TCP, 
            # что может быть полезно в определенных ситуациях, таких как реализация чата.
            client.bind(("localhost", random.randint(1000, 9000)))

            def receive():
                while True:
                    try:
                        message, _ = client.recvfrom(1024)
                        #Функция recvfrom() является методом объекта сокета и используется 
                        #для приема данных из сокета с указанным максимальным размером данных (1024 в данном случае).
                        print(message.decode())
                    except:
                        pass

            t = threading.Thread(target=receive)
            t.start()

            client.sendto(f"SIGNUP_TAG:{name}".encode(), ("localhost", int(words[1])))
        #Данный код выполняет отправку данных с помощью сокета client на указанный адрес (("localhost", int(words[1]))) и порт. 
        #Функция sendto() является методом объекта сокета 
        #и используется для отправки данных через UDP (User Datagram Protocol).
        #Данные, которые отправляются, формируются с использованием форматирования строк (f-строк) 
        # и состоят из строки "SIGNUP_TAG:", за которой следует значение переменной name. 
        # Затем они кодируются в байты с помощью метода encode().
        #Адрес и порт, на которые данные отправляются, указываются в виде кортежа ("localhost", int(words[1])), 
        #где "localhost" - адрес хоста (в данном случае локального хоста), 
        # а int(words[1]) - порт, на который данные будут отправлены. Значение порта берется из words[1], 
        # которое должно быть предварительно преобразовано в целое число с помощью int().
            while True:
                message = input("")
                if message == "!q":
                    exit()
                else:
                    client.sendto(f"{name}: {message}".encode(), ("localhost", int(words[1])))

    def receive():
        while True:
            try:
                message, addr = server.recvfrom(1024)
                # Функция recvfrom() является методом объекта сокета и используется
                # для приема данных из сокета с указанным максимальным размером данных (1024 в данном случае).
                messages.put((message, addr))
            except:
                pass


    def broadcast():
        while True:
            while not messages.empty():  
                message, addr = messages.get()  
                print(message.decode())  # Вывод раскодированного сообщения в консоль
                if addr not in clients:  # Если адрес клиента не находится в списке clients, добавляем его
                    clients.append(addr)
                for client in clients:  # Отправляем сообщение всем клиентам из списка clients
                    try:
                        if message.decode().startswith("SIGNUP_TAG"):  # Если сообщение начинается с "SIGNUP_TAG"
                            name = message.decode()[message.decode().index(":") + 1:]  # Извлекаем имя из сообщения
                            if admin:  # Если администратор
                                
                                solution = input(f" Join {name} to the server? print /accept or /deny\n")  # Запрашиваем решение от администратора
                                if solution == "/accept":  # Если решение - "/accept", отправляем сообщение клиенту
                                    server.sendto(f"{name} Come to the server. Say hello.".encode(), client)
                                else:  # Иначе, отправляем отказ
                                    server.sendto(f"{name} denied. Good bye".encode(), client)
                            else:  # Если не администратор, отправляем отказ
                                server.sendto(f"{name} denied".encode(), client)
                        else:  # Если сообщение не начинается с "SIGNUP_TAG", отправляем его клиенту
                            server.sendto(message, client)
                    except:  # Обработка возможных ошибок
                        pass


    t1 = threading.Thread(target=receive)
    t2 = threading.Thread(target=broadcast)

    t1.start()
    t2.start()

def main():
    start_server_thread = threading.Thread(target=start_server)
    start_server_thread.start()

if __name__ == "__main__":
    main()

