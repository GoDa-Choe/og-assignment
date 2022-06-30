from django import forms
from exhibition import models


class ExhibitionForm(forms.ModelForm):
    class Meta:
        model = models.Exhibition
        fields = ('title', 'start_date', 'end_date', 'poster', 'artworks')
        labels = {
            'title': '제목',
            'start_date': "시작일",
            'end_date': "종료일",
            'poster': "대표 포스터(생략가능)",
            'artworks': "작품 선택",
        }

    def __init__(self, artist, *args, **kwargs):
        super(ExhibitionForm, self).__init__(*args, **kwargs)
        self.fields["artworks"].widget = forms.CheckboxSelectMultiple()
        self.fields["artworks"].queryset = models.Artwork.objects.filter(artist=artist)

    def clean_end_date(self):
        end_date = self.cleaned_data.get('end_date')
        start_date = self.cleaned_data.get('start_date')

        if start_date <= end_date:
            return end_date
        else:
            raise forms.ValidationError("종요일이 시작일보다 빠릅니다.")
