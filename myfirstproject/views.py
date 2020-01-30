from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request,'home.html' , {'heyaa' : 'this is first code'}) #this is the point that shows we can also write the python code in the brackets.

      
def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #already there soo increase
            worddictionary[word] += 1

        else:

            #not there add the word
            worddictionary[word] = 1
    
    return render(request,'count.html',{'fulltext' : fulltext , 'count' : len(wordlist) , 'worddictionary' : worddictionary.items()})