from django.shortcuts import render
from ana_app.forms import Word_Form
from pathlib import Path
import os
import requests

BASE_DIR = Path(__file__).resolve().parent.parent

def words_view(request):
    result = []
    if request.method == "POST":
        form = Word_Form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            typed_word = data['selection']
            result = find_anagrams(typed_word)
            print(result)
    form = Word_Form()
    return render(request, 'index.html', {"result":result,
                                          "form": form})


def find_anagrams(word):
    word_list = word_list_helper()
    anagrams = []
    sorted_word = ''.join(sorted(word))
    for items in word_list:
        if ''.join(sorted(items)) == sorted_word:
            anagrams.append(items)
    return anagrams



def word_list_helper():
    word_list = []
    word_file = os.path.abspath('words.txt')
    with open(word_file, "r") as f:
        for line in f:
            fixed_line = line.strip('\n')
            word_list.append(fixed_line)
    return word_list




# word_sort()
# def word_list():
#     MW_api = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/?key=ee240777-9262-4129-abaf-49991628c1fd'
#     r = requests.get(MW_api).json()
#     print(r)
#     # breakpoint()
#     # words_list = r.json()
#     # print(words_list['meta'])

# word_list()