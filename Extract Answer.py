"""
Author: Pratham Bhat
Github: PrathamBhatTech
"""

from bs4 import BeautifulSoup

#print("Paste the html code here")

html = open('PEScode.html', 'r+')
#html.write(input())

soup = BeautifulSoup(html, 'lxml')

nq = 5

# Contains all the questions and options
questionsAndAnswers = soup.find('div', class_='no-tab-h-gutter no-tab-v-gutter fade in')
answers = questionsAndAnswers.find_all('label', class_='text-muted')

for i in range(1, nq * 4):
    ans = answers[i].input['value']
    if ans == "true":
        print(str(i // 4 + 1) + ': ' + str(i % 4 + 1))

input("\n\n\n\nPress enter to exit")
