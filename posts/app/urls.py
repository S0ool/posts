from django.contrib import admin
from django.template.context_processors import static
from django.urls import path

from app.views import (index, add_post, category, category_info, edit_category, category_delete, add_category,
                       edit_post, post_info, post_delete, add_comment)
from posts import settings

urlpatterns = [
                  path('', index, name='index'),
                  path('category', category, name='category_page'),
                  path('add_new_post', add_post, name='add_new_post'),
                  path('add_new_category', add_category, name='add_new_category'),
                  path('add_new_comment', add_comment, name='add_comment'),
                  path('category/info/<int:category_id>', category_info, name='category_info'),
                  path('category/edit/<int:category_id>', edit_category, name='edit_category'),
                  path('category/delete/<int:category_id>', category_delete, name='category_delete'),

                  path('post/edit/<int:post_id>', edit_post, name='edit_post'),
                  path('post/info/<int:post_id>', post_info, name='post_info'),
                  path('post/delete/<int:post_id>', post_delete, name='post_delete'),

              ]
