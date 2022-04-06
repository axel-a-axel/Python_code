import pickle

game_data = {
'позиция-игрока' : 'С23 В45',
'карманы' : ['ключи', 'карманный нож', 'гладкий камень'],
'рюкзак' : ['веревка', 'молоток', 'яблоко'],
'деньги' : 158.50
}
save_file1 = open('D:\\save.txt', 'wb')
save_file2 = open('D:\\save2.txt', 'w')
pickle.dump(game_data, save_file1)
for key, value in game_data.items():
    save_file2.write('%s:%s\n' % (key, value))
save_file1.close()
save_file2.close()

load_file1 = open('D:\\save.txt', 'rb')
loaded_data = pickle.load(load_file1)
load_file1.close()
load_file2 = open('D:\\save2.txt', 'r')
loaded_data2 = load_file2.read()
load_file2.close()

print(loaded_data, '\n')
print(loaded_data2)