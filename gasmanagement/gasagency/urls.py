from django.urls import path
from gasagency import views

urlpatterns = [
       path('', views.index, name='index'),
       path('register/',views.register,name='register'),
       path('loginPage/',views.loginPage,name='loginPage'),
       path('user/',views.user,name='user'),
       path('admin_home/',views.admin_home,name='admin_home'),
       path('zone/',views.zone,name='zone'),
       path('editzone/<int:id>/',views.editzone,name='editzone'),
       path('deleteZone/<int:id>/',views.deleteZone,name='deleteZone'),
       path('viewZone/',views.viewZone,name='viewZone'),
       path('booking/',views.booking,name='booking'),
       path('bookingView/',views.bookingView,name='bookingView'),
       path('feedback/',views.feedback,name='feedback'),
       path('logoutPage/',views.logoutPage,name='logoutPage'),
       path('addAgent/',views.addAgent,name='addAgent'),
       path('manageAgent/',views.manageAgent,name='manageAgent'),
       path('editAgent/<int:gas_id>/',views.editAgent,name='editAgent'),
       path('deleteAgent/<int:gas_id>/',views.deleteAgent,name='deleteAgent'),
       path('viewBooking/',views.viewBooking,name='viewBooking'),
       path('viewFeedback/',views.viewFeedback,name='viewFeedback'),
       path('agentPanel/',views.agentPanel,name='agentPanel'),
       path('assignAgent/<int:booking_id>/',views.assignAgent,name='assignAgent'),
       path('viewAssigned',views.viewAssigned,name='viewAssigned'),
       path('agent_accept/<id>/',views.agent_accept,name='agent_accept'),
       path('agent_reject/<id>/',views.agent_reject,name='agent_reject'),
       path('manageCylinder/',views.manageCylinder,name='manageCylinder'),
       path('viewCylinder/',views.viewCylinder,name='viewCylinder'),
       path('editcylinder/<int:id>/',views.editcylinder,name='editcylinder'),
       path('deletecylinder/<int:id>/',views.deletecylinder,name='deletecylinder'),
       path('bookingLink/<int:id>/',views.bookingLink,name='bookingLink'),
       path('acceptedOrder/',views.acceptedOrder,name='acceptedOrder'),
       path('complete_get/',views.complete_get,name='complete_get'),
       path('complete_post/<int:id>/',views.complete_post,name='complete'),
       path('feedbackView/',views.feedbackView,name='feedbackView'),
       
       

 ]