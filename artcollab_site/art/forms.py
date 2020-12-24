from django import forms
from .models import Skillset

class SignupForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    first_name = forms.CharField(label='First Name', max_length=50)
    last_name = forms.CharField(label='Last Name', max_length=50)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    gender_choices = (
        (u'M', u'Male'),
        (u'F', u'Female'),
        (u'O', u'Other'),
    )
    gender = forms.ChoiceField(label='Gender', choices=gender_choices)
    age = forms.IntegerField(label='Age')
    country = forms.CharField(label='Country', max_length=50)
    state = forms.CharField(label='State', max_length=50)
    city = forms.CharField(label='City', max_length=50)
    email = forms.CharField(label='Email', max_length=50)
    skill_set = forms.ModelMultipleChoiceField(queryset=Skillset.objects.all(), label="Skill set - D:Dance, M:Music, P:Photography, V:Videography, O:Other", widget=forms.CheckboxSelectMultiple, required=True)
    fb_link = forms.CharField(label='Facebook Link', max_length=200)
    instagram_link = forms.CharField(label='Instagram Link', max_length=200)
    youtube_link = forms.CharField(label='Youtube Link', max_length=200)
    other_link = forms.CharField(label='Other Links', max_length=200)
    phone_number = forms.IntegerField(label='Phone Number')
    bio = forms.CharField(label='Bio', widget=forms.Textarea, max_length=500)

class HomeForm(forms.Form):
    username = forms.CharField(label='Find by Username', max_length=100, required=False)
    skill_set = forms.ModelMultipleChoiceField(queryset=Skillset.objects.all(), label="Find by Skill set - D:Dance, M:Music, P:Photography, V:Videography, O:Other", widget=forms.CheckboxSelectMultiple, required=True)
    country = forms.CharField(label='Find by Country', max_length=50, required=False)
    state = forms.CharField(label='Find by State', max_length=50, required=False)
    city = forms.CharField(label='Find by City', max_length=50, required=False)