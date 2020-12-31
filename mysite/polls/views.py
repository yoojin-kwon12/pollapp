

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template import loader

from .models import Question

# 색인 -> 최근 질문들을 표시
def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")

    #
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

    # loader 와 HttpResponse를 import한 방식.
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list' : latest_question_list
    # }
    # return HttpResponse(template.render(context,request))

    # loader 와 HttpResponse를 import하지 않아도 된다.
    # (만약 detail, results, vote에서 stub 메소드를 가지고 있다면, HttpResponse를 유지해야 할 것)
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list' : latest_question_list
    }
    
    # httpresponse 객체를 반환 
    return render(request,'polls/index.html',context)


# 세부 -> 질문 내용, 투표할 수 있는 서식 표시
def detail(request, question_id):

    # return HttpResponse("You're looking at question %s." % question_id)
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/detail.html', {'question': question})


# 결과 -> 특정 질문에 대한 결과를 표시
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


# 투표기능 -> 특정 질문에 대해 특정 선택을 할 수 있는 기능 제공
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
