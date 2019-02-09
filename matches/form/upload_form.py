# -*- coding: utf-8 -*-
'''
Created on Sep 30, 2014

@author: mvgagliotti
'''
from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()
