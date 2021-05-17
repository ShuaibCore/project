from django.urls import path
from . import views, testfile, upload, gets, traindata, inserts, extracts


urlpatterns = [
    path('', views.index, name="home"),
    path('test/', testfile.testing, name="home"),
    path('upload/', upload.upload, name="uploader"),
    path('file_uploads/', gets.file_uploads, name="file_uploads"),
    path('file_extract/', extracts.file_extract, name="file_extract"),

    path('summarize/', inserts.summarize, name="summarize"),
    path('savesummary/', inserts.savesummary, name="savesummary"),
    path('listsummary/', gets.listsummary, name="listsummary"),
    path('list_dataset/', gets.get_dataset, name="get_dataset"),
    path('train_data/', traindata.train_data, name="train_data"),
    path('modelanalysis/', traindata.model_analysis, name="model_analysis"),
]
