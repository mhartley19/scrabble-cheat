from django.shortcuts import render
from ana_app.forms import Word_Form


def words_view(request):
    result = []
    if request.method == "POST":
        form = Word_Form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            typed_word = data['selection']
            result = find_anagrams(typed_word)
    form = Word_Form()
    return render(request, 'index.html', {"result":result,
                                          "form": form})


def find_anagrams(word):
    anagrams = []
    sorted_word = ''.join(sorted(word))
    for items in words:
        if ''.join(sorted(items)) == sorted_word:
            anagrams.append(items)
    return anagrams
