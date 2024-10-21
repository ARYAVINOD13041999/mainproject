from django.urls import path

from momo_app import views

urlpatterns = [

path('',views.index,name='index'),

path('index1',views.index1,name='index1'),

path('index2',views.index2,name='index2'),

path('adminbase',views.adminbase,name='adminbase'),

path('customerbase',views.customerbase,name='customerbase'),

path('managerbase',views.managerbase,name='managerbase'),

path('login_view',views.login_view,name='login_view'),

path('customer_reg',views.customer_reg,name='customer_reg'),

path('registration',views.registration,name='registration'),

path('worker_reg',views.worker_reg,name='worker_reg'),

path('customer_view',views.customer_view,name='customer_view'),

path('worker_view',views.worker_view,name='worker_view'),

path('delete/<int:id>/', views.delete, name='delete'),

path('update/<int:id>/', views.update, name='update'),

path('delete1/<int:id>/', views.delete1, name='delete1'),

path('update1/<int:id>/', views.update1, name='update1'),

path('complaint',views.feedback,name='complaint'),

# path('feedback',views.feedback,name='feedback'),(eganeyum ezhutham appol/fedback)

path('soorya',views.complaint_adview,name='soorya'),

path('arya',views.complaint_cusview,name='arya'),

path('replay/<int:id>/',views.replay,name='replay'),

path('add',views.notification,name='add'),

path('view',views.notificationview,name='view'),

path('delete3/<int:id>/', views.delete3, name='delete3'),

path('leo',views.seen,name='leo'),

path('leno',views.seenworker,name='leno'),

path('a',views.addschedule,name='a'),

path('b', views.view_schedule, name='b'),

path('c', views.view_scheduleADMIN, name='c'),

path('delete4/<int:id>/', views.delete_schedule, name='delete4'),

path('appointment/<int:id>/',views.take_appointment,name='appointment'),

path('d',views.view_appointment,name='d'),

path('view_appointment',views.view_appointment,name='view_appointment'),

path('view_user_appointment',views.view_user_appointment,name='view_user_appointment'),

path('manager_view_appointment',views.manager_view_appointment,name='manager_view_appointment'),

path('accept/<int:id>/',views.accept,name='accept'),

path('reject/<int:id>/',views.reject,name='reject'),





]