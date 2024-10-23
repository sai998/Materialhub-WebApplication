from django.contrib import admin
from django.urls import path

from app1 import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.loginn),
    path('login_post',views.login_post),
    path('complaintReplay/<id>',views.complaintReplay),
    path('complaintReplay_post/<id>',views.complaintReplay_post),
    path('dealer',views.dealer),
    path('dealerapprove',views.dealerapprove),
    path('editMaterial/<id>',views.editMaterial),
    path('editMaterial_post/<id>',views.editMaterial_post),
    path('materialAdd',views.materialAdd),
    path('materialAdd_post',views.materialAdd_post),
    path('adminHome',views.adminHome),
    path('viewMaterial',views.viewMaterial),
    path('viewRegisteredUser',views.viewRegisteredUser),
    path('viewComplaint',views.viewComplaint),
    path('viewFeedback',views.viewFeedback),
    path('delete_material/<id>',views.delete_material),
    path('approve/<id>',views.approve),
    path('reject/<id>',views.reject),
#     ============================================:::Dealer:::==========================================================

    path('addDriver',views.driver_add),
    path('driver_add_post',views.driver_add_post),
    path('register',views.register),
    path('register_post',views.register_post),
    path('allocate_Driver/<id>',views.allocate_driver),
    path('edit_driver/<id>',views.edit_driver),
    path('update_stock/<id>/<mid>',views.update_stock),
    path('view_driver',views.view_driver),
    path('view_material',views.view_material),
    path('view_order',views.view_order),
    path('view_orderSub/<id>',views.view_order_sub),
    path('view_profile',views.profile),
    path('view_reviews',views.view_reviews),
    path('dealer_home',views.dealer_home),
    path('view_payment',views.view_payment),
    path('update_stock_post/<id>/<mid>',views.update_stock_post),
    path('delete_driver/<id>',views.delete_driver),
    path('edit_driver_post/<id>',views.edit_driver_post),
    path('userInfo_view/<id>',views.userInfo_view),
    path('driver_allocation/<id>/<oid>',views.driver_allocation),
    path('report',views.report),
    path('search_post',views.search_post),


    #-------------------------DRIVER------------------------------

    path('driver_home',views.driver_home),
    path('view_allocated_order',views.view_allocated_order),
    path('payment/<oid>/<uid>',views.payments),
    path('payment_post/<oid>/<uid>',views.payment_post),
    path('driver_profile',views.driver_profile),
    path('item/<id>',views.item),

  #------------------------Client-------------------------

    path('client_register',views.client_register),
    path('client_register_post',views.client_register_post),
    path('home',views.home),
    path('client_view_profile',views.client_view_profile),
    path('client_view_dealears/<id>',views.client_view_dealears),
    path('client_view_material',views.client_view_material),
    path('change_password',views.change_password),
    path('change_psswd_post',views.change_psswd_post),
    path('quantity_request/<id>',views.quantity_request),
    path('quantity_req_post/<id>',views.quantity_req_post),
    path('send_complaint',views. send_complaint),
    path('compalint_Post',views.compalint_Post),
    path('send_feedBack',views.send_feedBack),
    path('feedback_post',views.feedback_post),
    path('send_Review/<id>',views.send_Review),
    path('send_Review_post/<id>',views.send_Review_post),
    path('view_dealerReview/<id>',views.view_dealerReview),
    path('view_Replay',views.view_Replay),
    path('view_request_status',views.view_request_status),
    path('view_requested_item/<id>',views.view_requested_item),
    path('cancel/<id>',views.cancel),
    path('remove/<id>',views.remove),
    path('remove_replay/<id>',views.remove_replay),
    path('payment_method/<id>/<amnt>',views.payment_method),
    path('payment_method_post/<id>',views.payment_method_post),
    path('payment_entry',views.payment_entry),


    #-------------------------OTP-------------------
    path('otp',views.otp),
    path('otp_post',views.otp_post),
    path('otp2_post/<oid>/<uid>',views.otp2_post),
    path('otp2/<oid>/<uid>',views.otp2),

    #---logout
    path('logout',views.logout),
    #--forget Password
    path('forget',views.forget),
    path('forget_post',views.forget_post),

]
