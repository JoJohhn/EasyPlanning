from django import forms



class AddedTask(forms.Form):
    task_name = forms.CharField(label='Название задачи', widget=forms.TextInput(attrs={'class': 'form-input'}))
    task_description = forms.CharField(label='Описание задачи', widget=forms.TextInput(attrs={'class': 'form-input'}))

    def save(self):
        pass
