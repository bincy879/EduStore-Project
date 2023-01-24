from django.urls import path
from Adminside import views

urlpatterns=[
    path('indexfn/',views.indexfn,name="indexfn"),
    path('add_admin/',views.add_admin,name="add_admin"),
    path('save_admin/',views.save_admin,name="save_admin"),
    path('view_admin/',views.view_admin,name="view_admin"),
    path('edit_admin/<int:dataid>/',views.edit_admin,name="edit_admin"),
    path('update_admin/<int:dataid>/',views.update_admin,name="update_admin"),
    path('add_catgry/',views.add_catgry,name="add_catgry"),
    path('save_catgry/',views.save_catgry,name="save_catgry"),
    path('view_catgry/',views.view_catgry,name="view_catgry"),
    path('del_admin/<int:dataid>/',views.del_admin,name="del_admin"),
    path('edit_category/<int:dataid>/',views.edit_category,name="edit_category"),
    path('update_category/<int:dataid>/',views.update_category,name="update_category"),
    path('del_category/<int:dataid>/',views.del_category,name="del_category"),
    path('add_product/',views.add_product,name="add_product"),
    path('save_pdt/',views.save_pdt,name="save_pdt"),
    path('view_product/',views.view_product,name="view_product"),
    path('edit_product/<int:dataid>/',views.edit_product,name="edit_product"),
    path('update_product/<int:dataid>/',views.update_product,name="update_product"),
    path('del_product/<int:dataid>/',views.del_product,name="del_product"),
    path('login_page/',views.login_page,name="login_page"),
    path('session/',views.session,name="session"),
    path('log_out/',views.log_out,name="log_out"),
    path('view_msg/',views.view_msg,name="view_msg"),
    path('del_msg/<int:dataid>/',views.del_msg,name="del_msg"),



]