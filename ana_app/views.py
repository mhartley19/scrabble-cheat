from django.shortcuts import render
from ana_app.forms import Word_Form
from pathlib import Path
import os
import requests

BASE_DIR = Path(__file__).resolve().parent.parent

score_dictoinary = {
'1':['a', 'e', 'i', 'l', 'n', 'o', 'r', 's', 't', 'u'],
'2':['d', 'g'],
'3':['b','c','m','p'],
'4':['f','h','v','w','y'],
'5':['k'],
'8':['j', 'x'],
'10':['z', 'q']
}


def words_view(request):
    result = None
    result_dict = {}
    sorted_list = {}
    score = 0
    if request.method == "POST":
        form = Word_Form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            typed_word = data['selection']
            result = find_anagrams(typed_word)
            if result == []:
                result = "NO"
            else:
                for each in result:
                    for letter in each:
                        for key, value in score_dictoinary.items():
                            if letter in value:
                                score += int(key)
                            result_dict[each] = score
                    score = 0
            sorted_list = sorted(result_dict.items(), key=lambda x:x[1], reverse=True)
    form = Word_Form()
    return render(request, 'index.html', {"result":result,
                                          "sorted_list": sorted_list,
                                          "form": form})


def find_anagrams(word):
    word_list = word_list_helper()
    anagrams = []
    sorted_word = ''.join(sorted(word))
    for items in word_list:
        if ''.join(sorted(items)) in sorted_word:
            print(sorted_word)
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

def split_word(word):
    return [y for y in word]



