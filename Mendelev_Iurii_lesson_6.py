# Задание 1

FILENAME = 'nginx_logs.txt'
res = []
with open(FILENAME, 'r') as file:
    for i in file:
        remote_addr = i.split()[0]
        request_type = i.split()[5][1:]
        requested_resource = i.split()[6]
        res.append((remote_addr, request_type, requested_resource))
print (res)

with open('result.txt', 'w') as result:
    result.write(str(res))


# Задание 3
info = {}
with open('users.csv', 'r', encoding='utf-8') as users:
    with open('hobby.csv', 'r', encoding='utf-8') as hobby:
        for i in users:

            for j in hobby:
                info[i.replace(',', ' ').strip('\n')] = j.replace(',', ', ').strip('\n')
                break
print(info)
with open('user_info.txt', 'w', encoding='utf-8') as user_info:
    user_info.write(str(info))


