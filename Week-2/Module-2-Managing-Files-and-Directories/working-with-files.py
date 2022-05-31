import os
def created():
    with open('novel.txt') as file:
        file.write('This was a dark and stormy night.')

if __name__ == '__main__':
    if os.path.exists('novel.txt'):
        # os.remove('novel.txt')
        os.rename('novel.txt', 'novel_edited.txt')
    else:
        created()
