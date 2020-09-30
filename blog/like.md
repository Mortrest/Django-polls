1. User implemention
2. Login System
3. Def Like in Views
4. Url Like in Views
5. Html

if User.objects.get(id=UserLoginded).question_set.get(id=pk).likes == 0:
    q = User.objects.get(id=UserLoginded).question_set.get(id=pk).likes
    q = 1
    q.save()

else:
    q = User.objects.get(id=UserLoginded).question_set.get(id=pk).likes
    q = 0
    q.save()

1. click on like button ---> url like/pk(id_question) ---> user.question_set.get(id=pk).likeStatus = 1 ---> user.question_set.get(id=pk).likes += 1
