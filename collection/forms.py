from django.forms import ModelForm
from collection import models


class ArtistForm(ModelForm):
    class Meta:
        model = models.Artist
        fields = ('name', 'gender', 'birth', 'email', 'phone_number', 'picture')
        labels = {
            'name': '이름',
            'gender': "성별",
            'birth': "생년월일",
            'email': "이메일",
            'phone_number': "전화번호",
            'picture': "프로필 사진",
        }


class ArtWorkForm(ModelForm):
    class Meta:
        model = models.Artwork
        fields = ('title', 'canvas_size', 'price', 'picture')
        labels = {
            'title': '제목',
            'canvas_size': "호수",
            'price': "가격",
            'picture': "사진",
        }
