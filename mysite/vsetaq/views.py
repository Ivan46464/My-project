from django.shortcuts import render, redirect, get_object_or_404
from .forms import IncomeForm, ExpensesForm, GoalsForm, Side_incomeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Income, Goals, Expenses, Side_income
import pandas as pd
from plotly.offline import plot
import plotly.express as px
import math
from datetime import datetime


# Create your views here.

def side_income(response):
    form = Side_incomeForm
    if response.method == "POST":
        form = Side_incomeForm(response.POST)
        if form.is_valid():
            passive_income = form.save(commit=False)
            passive_income.user = response.user
            passive_income.save()
            form.save()
            return redirect('/')
    context = {"form": form}
    return render(response, 'side_income.html', context)


def no_income(response):
    return render(response, 'no_income.html')


def choose_input(response):
    return render(response, 'choose_input.html')


def choose_chart(response):
    return render(response, 'charts.html')


def check(response):
    return render(response, 'check.html')


def income(response):
    income = Income.objects.filter(user=response.user)

    # income = get_object_or_404(Income, user=response.user)
    form = IncomeForm()
    if response.method == "POST":
        form = IncomeForm(response.POST)
        if form.is_valid():
            income1 = form.save(commit=False)
            income1.user = response.user
            income1.save()
            return redirect('/')
    context = {
        "form": form,
        'income_exists': True if income else False
    }
    return render(response, "income.html", context)


def home(response):
    try:
        income = Income.objects.get(user=response.user)
    except Income.DoesNotExist:
        income = 0
    now = datetime.now()
    current_month = now.month
    current_year = now.year
    side_income = Side_income.objects.filter(user=response.user,
                                             updated__month=current_month,
                                             updated__year=current_year)
    side_income_for_month = 0
    for side in side_income:
        side_income_for_month += side.side_income

    expenses = Expenses.objects.filter(user=response.user,
                                       updated__month=current_month,
                                       updated__year=current_year)
    all_expenses = 0
    for expense in expenses:
        all_expenses += expense.expenses
    context = {

       'income': income,
       'all_expenses': all_expenses,
       'side_income': side_income_for_month,
            }
    return render(response, "home.html", context)


def expenses(response):
    form = ExpensesForm()
    if response.method == "POST":
        form = ExpensesForm(response.POST)
        if form.is_valid():
            expenses1 = form.save(commit=False)
            expenses1.user = response.user
            expenses1.save()
            form.save()
            return redirect('/')
    context = {"form": form}
    return render(response, "expenses.html", context)


def chart(response):
    host = response.user
    qs = Expenses.objects.filter(user=host)
    if not qs:
        is_there_data = True
        context = {"data": is_there_data}
    else:
        data = [
            {
                'expenses': x.expenses,
                'categories': x.categories,

            }
            for x in qs
        ]
        df = pd.DataFrame(data)
        fig = px.bar(df, y='expenses', color='categories', x='categories')
        # fig.update_yaxes(autorange="reversed")
        gantt_plot = plot(fig, output_type="div")
        context = {'plot_div': gantt_plot, 'expenses': expenses}
    return render(response, 'chart.html', context)


def chart_side_income(response):
    host = response.user
    qs = Side_income.objects.filter(user=host)

    if not qs:
        is_there_data = True
        context = {"data": is_there_data}
    else:
        data = [
            {
                'side-income': x.side_income,
                'categories': x.category,
            }
            for x in qs
        ]
        df = pd.DataFrame(data)
        fig = px.bar(df, y='side-income', color='categories', x='categories')
        # fig.update_yaxes(autorange="reversed")
        gantt_plot = plot(fig, output_type="div")
        context = {'plot_div': gantt_plot}
    return render(response, 'chart_side_income.html', context)


def pie_chart(response):
    host = response.user
    qs = Expenses.objects.filter(user=host)
    if not qs:
        is_there_data = True
        context = {"data": is_there_data}
    else:
        data = [
            {
                'expenses': x.expenses,
                'categories': x.categories,

            }
            for x in qs
        ]
        df = pd.DataFrame(data)
        fig = px.pie(df, values='expenses', names='categories', color='categories')
        # fig.update_yaxes(autorange="reversed")
        gantt_plot = plot(fig, output_type="div")
        context = {'plot_div': gantt_plot}
    return render(response, 'pie_chart.html', context)


def pie_chart_side_income(response):
    host = response.user
    qs = Side_income.objects.filter(user=host)
    if not qs:
        is_there_data = True
        context = {"data":is_there_data}
    else:
        data = [
            {
                'side-income': x.side_income,
                'categories': x.category,

            }
            for x in qs
        ]
        df = pd.DataFrame(data)
        fig = px.pie(df, values='side-income', names='categories', color='categories')
        # fig.update_yaxes(autorange="reversed")
        gantt_plot = plot(fig, output_type="div")
        context = {'plot_div': gantt_plot}
    return render(response, 'pie_chart_side_income.html', context)


def edit_income(response):
    income = Income.objects.get(user=response.user)
    form = IncomeForm(instance=income)
    if response.method == 'POST':
        form = IncomeForm(response.POST, instance=income)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(response, "income.html", context)


def goal(response):
    try:
        income = Income.objects.get(user=response.user)
    except Income.DoesNotExist:
        return render(response, "no_income.html")
    now = datetime.now()
    current_month = now.month
    current_year = now.year
    side_income = Side_income.objects.filter(user=response.user,
                                             updated__month=current_month,
                                             updated__year=current_year)
    year_income = income.income * 12
    side_income_for_month = 0
    for side in side_income:
        side_income_for_month += side.side_income

    expenses = Expenses.objects.filter(user=response.user,
                                       updated__month=current_month,
                                       updated__year=current_year)
    all_expenses = 0
    for expense in expenses:
        all_expenses += expense.expenses
    success = income.income + side_income_for_month - all_expenses
    form = GoalsForm()
    if response.method == "POST":
        form = GoalsForm(response.POST)
        if form.is_valid():
            goals1 = form.save(commit=False)
            goals1.user = response.user
            goals1.save()
            form.save()
    if form.is_valid():
        goals1 = form.save(commit=False)
        goals1.user = response.user
        goals1.save()
        wanted_money = form.cleaned_data.get('save_money', 0)
    else:
        wanted_money = 0
    if Goals.objects.filter(user=response.user).exists():
        check_goals1 = Goals.objects.filter(user=response.user).latest('id')
    else:
        check_goals1 = None
    how_many = math.ceil(wanted_money / success)
    context = {
        "form": form,
        "income": income,
        "amount": year_income,
        "expenses": all_expenses,
        "check_goals": check_goals1,
        "wanted_money": wanted_money,
        "how_many": how_many,
        "success": success,
        "side_income": side_income_for_month
    }
    return render(response, "goals.html", context)


def check_side_income(response):
    check_side_income1 = Side_income.objects.filter(user=response.user)
    context = {
        'check_side_income': check_side_income1
    }
    return render(response, "check_side_income.html", context)


def check_goals(response):
    check_goals1 = Goals.objects.filter(user=response.user).exclude(finished=True)
    context = {
        'check_goals': check_goals1
    }
    return render(response, "check_goals.html", context)


def side_income_detail(response, side_income_id):
    side_income = Side_income.objects.get(user=response.user, id=side_income_id)
    context = {
        "side_income": side_income
    }
    return render(response, "check_side_income_detail.html", context)


def side_income_edit(response, side_income_id):
    side_income1 = get_object_or_404(Side_income, id=side_income_id)
    form = Side_incomeForm(instance=side_income1)
    if response.method == 'POST':
        form = Side_incomeForm(response.POST, instance=side_income1)
        if form.is_valid():
            form.save()
            return redirect('/check_side_income')
    context = {'form': form}
    return render(response, "side_income.html", context)


def side_income_delete(response, side_income_id):
    side_income = get_object_or_404(Side_income, id=side_income_id)
    if response.method == 'POST':
        side_income.delete()
        return redirect('/check_side_income')
    else:
        return redirect('/side_income_detail', side_income_id=side_income.id)


def goal_detail(request, goal_id):
    goal = Goals.objects.get(id=goal_id)
    income = Income.objects.get(user=request.user)

    year_income = income.income * 12
    now = datetime.now()
    current_month = now.month
    current_year = now.year
    side_income = Side_income.objects.filter(user=request.user,
                                             updated__month=current_month,
                                             updated__year=current_year)

    side_income_for_month = 0
    for side in side_income:
        side_income_for_month += side.side_income
    expenses = Expenses.objects.filter(user=request.user,
                                       updated__month=current_month,
                                       updated__year=current_year)
    all_expenses = 0
    for expense in expenses:
        all_expenses += expense.expenses
    success = income.income + side_income_for_month - all_expenses
    wanted_money = goal.save_money
    how_many = wanted_money / success

    context = {
        "goal": goal,
        "income": income,
        "amount": year_income,
        "expenses": all_expenses,
        "wanted_money": wanted_money,
        "how_many": how_many,
        "success": success,
        "side_income": side_income_for_month
    }
    return render(request, 'goal_detail.html', context)


def delete_goal(response, goal_id):
    goal = get_object_or_404(Goals, id=goal_id)
    if response.method == 'POST':
        goal.delete()
        return redirect('/check_goals')
    else:
        return redirect('/goal_detail', goal_id=goal.id)


def edit_goal(response, goal_id):
    goal = get_object_or_404(Goals, id=goal_id)
    form = GoalsForm(instance=goal)
    if response.method == 'POST':
        form = GoalsForm(response.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect('/check_goals')
    context = {'form': form}
    return render(response, "goals.html", context)


def check_expenses(response):
    expenses = Expenses.objects.filter(user=response.user)
    context = {
        "expenses": expenses
    }
    return render(response, "check_expenses.html", context)


def expenses_detail(response, expense_id):
    expenses = Expenses.objects.get(user=response.user, id=expense_id)
    context = {
        "expenses": expenses
    }
    return render(response, 'expenses_detail.html', context)


def delete_expense(response, expense_id):
    expenses = get_object_or_404(Expenses, id=expense_id)
    if response.method == 'POST':
        expenses.delete()
        return redirect('/check_expenses')
    else:
        return redirect('/expenses_detail', goal_id=expenses.id)


def edit_expenses(response, expense_id):
    expenses = get_object_or_404(Expenses, id=expense_id)
    form = ExpensesForm(instance=expenses)
    if response.method == 'POST':
        form = ExpensesForm(response.POST, instance=expenses)
        if form.is_valid():
            form.save()
            return redirect('/check_expenses')
    context = {'form': form}
    return render(response, "expenses.html", context)


def user_profile(response):
    host = response.user
    income = Income.objects.get(user=host)
    amount = income.income
    context = {
        "amount": amount
    }
    return render(response, "user_profile.html", context)


def finish_detail(response, goal_id):
    host = response.user
    goal = get_object_or_404(Goals, id=goal_id, user=host)
    goal.finished = True
    goal.save()
    return redirect('/check_goals', goal_id=goal_id)


def finished_goals(response):
    goal = Goals.objects.filter(finished=True, user=response.user)
    context = {'goal': goal}
    return render(response, 'check_finished_goals.html', context)
