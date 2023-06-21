from django.urls import path, include
from . import views


urlpatterns = [
    path("income/", views.income, name="income"),
    path("", views.home, name="home"),
    path("expenses/", views.expenses, name="expenses"),
    path('chart/', views.chart, name="chart"),
    path('pie_chart/', views.pie_chart, name="pie_chart"),
    path('edit_income/', views.edit_income, name="edit_income"),
    path('goals/', views.goal, name="goal"),
    path('check_goals/', views.check_goals, name="check_goals"),
    path('goal/int:<goal_id>/', views.goal_detail, name='goal_detail'),
    path('goals/<int:goal_id>/delete/', views.delete_goal, name='delete_goal'),
    path('goals/<int:goal_id>/edit/', views.edit_goal, name='edit_goal'),
    path('check_expenses/', views.check_expenses, name='check_expenses'),
    path('expense/int:<expense_id>/', views.expenses_detail, name='expenses_detail'),
    path('expenses/int:<expense_id>/delete/', views.delete_expense, name='delete_expense'),
    path('expenses/<int:expense_id>/edit/', views.edit_expenses, name='edit_expenses'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('finish_detail/int:<goal_id>', views.finish_detail, name='finish_detail'),
    path('check_finished_goals/', views.finished_goals, name='finished_goals'),
    path('choose_input/', views.choose_input, name="choose_input"),
    path('no_income/', views.no_income, name="no_income"),
    path('side_income/', views.side_income, name="side_income"),
    path('chart_side_income/', views.chart_side_income, name="chart_side_income"),
    path('pie_chart_side_income/', views.pie_chart_side_income, name="pie_chart_side_income"),
    path('choose_chart/', views.choose_chart, name="choose_chart"),
    path('check/', views.check, name="check"),
    path('check_side_income/', views.check_side_income, name="check_side_income"),
    path("side_income_detail/int:<side_income_id>", views.side_income_detail, name="side_income_detail"),
    path("side_income/int:<side_income_id>/edit/", views.side_income_edit, name="side_income_edit"),
    path('side_income/int:<side_income_id>/delete/', views.side_income_delete, name='side_income_delete'),




]