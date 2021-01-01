# views.py vote 

### get_object_or_404(Question, pk=question_id) :
###           Question 객체의 pk가 question_id인 객체가 존재하지 않을 경우 404 에러를 발생 시킨다.
### render : httpresponse 객체를 반환하는 함수, request와 template_name은 필수 인자이다.
###            원하는 인자를 해당 html 파일로 넘길 수 있다.
### HttpResponseRedirect(reverse('polls:results' , args=(question.id,))) :
###           HttpResponseRedirect는 response를 반환하지 않고 지정된 템플릿으로 redirect 할 시 사용된다.
###           reverse를 사용하여 'polls:results'를 url화(HttpResponseRedirect는 url을 넘겨주어야한다) 해서 인자와 함께 넘겨준다. 
### Choice.DoesNotExist : Choice 객체가 존재하지 않으면 . except 에 쓰인다.

### --------------------------------------------------------------------------------------------------------------------

# views.py IndexView / DetailView / ResultsView

## genericView - ListView
### template_name : 해당 템플릿 파일위치지정
### context_object_name : 객체 리스트 이름 설정

## genericView - DetailView
### model : 테이블 설정
### template_name : 해당 템플릿 파일위치지정