from django.urls import path
from .views import *
from .ajax import *


urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('group',GroupView.as_view(),name='group'),
    path('child',ChildView.as_view(),name='child'),
    path('cash/',CashView.as_view(), name='cash'),
    path('tarif',TarifCompanyView.as_view(),name='tarif'),
    path('teacher/',TeacherView.as_view(),name='teacher'),
    path('payment/',PaymentView.as_view(), name='payment'),
    path('transfer/',TransferView.as_view(), name='transfer'),
    path('settings/',SettingsView.as_view(), name='settings'),
    path('payment-cost/',PaymentCostView.as_view(), name='payment_cost'),
    path('payment-create/',PaymentCreateView.as_view(), name='payment-create'),
    path('transfer-create/',TransferCreateView.as_view(), name='transfer_create'),
    path('update-payment/', UpdatePaymenntView.as_view(), name='update-payment'),
    path('teacher/<int:pk>/',TeacherDetailView.as_view(),name='teacher_detail'),
    path('group-detail/<int:pk>/',GroupDetailView.as_view(),name='group_detail'),
    path('update-attendance-child/', UpdateAttendanceChildView.as_view(), name='update-attendance'),
    path('update-attendance-teacher/', UpdateAttendanceTeacherView.as_view(), name='update-attendance-teacer'),
    path('add_teacher/',add_teacher,name='add_teacher'),
    path('working_day/',working_day, name='working_day'),
    path('search-child/',search_child, name='search-child'),
    path('search-payment/',search_payment, name='search_payment'),
    path('search-transfer/',search_transfer, name='search_transfer'),
    path('get-teacher-cash/', get_teacher_cash, name='get_teacher_cash'),
    path('search-payment-cost/',search_payment_cost, name='search_payment_cost'),
    path('edit-tarif/<int:pk>/',edit_tarif,name='edit_tarif'),
    path('edit-amount/<int:pk>/',salary,name='edit_amount'),
    path('chaild-edit/<int:pk>/',chaild_edit,name='chaild_edit'),
    path('delete-chaild/<int:pk>/',delete_chaild,name='delete_chaild'),
    path('payment/child/<int:pk>/',payment_child,name='payment_child'),
    path('calendar/child/<int:pk>/',calendar_child,name='calendar_child'),
    path('calendar/teacher/<int:pk>/',calendar_teacher,name='calendar_teacher'),
    path('teacher-password/<int:pk>/',password,name='edit_password'),
    path('chaild-edit-tarif/<int:pk>/',chaild_edit_tarif,name='chaild_edit_tarif'),
    

]
