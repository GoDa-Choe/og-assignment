from django import forms
from collection import models


class ArtistForm(forms.ModelForm):
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


class ArtWorkForm(forms.ModelForm):
    class Meta:
        model = models.Artwork
        fields = ('title', 'canvas_size', 'price', 'picture')
        labels = {
            'title': '제목',
            'canvas_size': "호수",
            'price': "가격",
            'picture': "사진",
        }


class ArtworkSearchForm(forms.Form):
    search_string = forms.CharField(max_length=40, label="",
                                    widget=forms.TextInput(attrs={"placeholder": "피카소"}))
