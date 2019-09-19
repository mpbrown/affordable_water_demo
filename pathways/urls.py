from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='pathways-home'),
    path('about/', views.about,name='pathways-about'),
    path('apply/', views.HouseholdView.as_view(),
        name='pathways-apply'),
    path('apply/household-eligible/', views.AutoEligibleView.as_view(),
        name='pathways-apply-household-eligible'),
    path('apply/income-methods/', views.IncomeMethodsView.as_view(),
        name='pathways-apply-income-methods'),
    path('apply/exact-income/', views.ExactIncomeView.as_view(),
        name='pathways-apply-exact-income'),
    path('apply/hourly-income/', views.HourlyIncomeView.as_view(),
        name='pathways-apply-hourly-income'),
    path('apply/estimate-income/', views.EstimateIncomeView.as_view(),
        name='pathways-apply-estimate-income'),
    path('apply/review-eligibility/', views.ReviewEligibilityView.as_view(),
        name='pathways-apply-review-eligibility'),
    path('apply/eligibility/', views.EligibilityView.as_view(),
        name='pathways-apply-eligibility'),
    path('debug/', views.debugsessionview, name='pathways-debug'),
]