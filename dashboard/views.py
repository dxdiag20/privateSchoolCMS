from django.views.generic import TemplateView
from django.contrib.auth.models import User
from students.models import Student
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from .forms import SignUpForm, NoticeForm
from .models import Notice
import datetime
from django.utils import timezone
from payments.models import Payment
from attendance.models import Attendance
from django.http import JsonResponse

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('dashboard:index')
    else:
        form = SignUpForm()
    return render(request, 'components/signup.html', {'form': form})   

class NoticeView(TemplateView):
    def create(request):
        if request.method == 'GET':
            number = Notice.objects.all().count() + 1
            form = NoticeForm(initial={'number': number}) 
        else:
            form = NoticeForm(request.POST)
        return NoticeView.saveNoticeForm(request, form, 'dashboard/noticePartialCreate.html')

    def saveNoticeForm(request, form, template_name):
        html = {}
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                html['form_is_valid'] = True
                notices = Notice.objects.all()
                html['noticeList'] = render_to_string('dashboard/notice_notification.html', {
                'notices': notices })
                return redirect('dashboard:index')           
            else:
                html['form_is_valid'] = False
        context = {'form':form}
        html['html_form'] = render_to_string(template_name, context, request=request)           
        return JsonResponse(html)
    def delete(request, pk):
        html = {}
        notice = get_object_or_404(Notice, pk=pk)
        if request.method == 'POST':
            notice.delete()
            html['form_is_valid'] = True
            notices = Notice.objects.all()
            html['noticeList'] = render_to_string('dashboard/notice_notification.html', 
                {'notices': notices }, request=request)  
        else:
            context = {'notice':notice}
            html['html_form'] = render_to_string('dashboard/noticePartialDelete.html', context,
                request=request)
        return JsonResponse(html)        

class IndexView(TemplateView):
    template_name = "components/index.html"
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        try:
            human_students = Student.objects.filter(actState='HUMAN')
            payment_students = Student.objects.filter(isPayday='PAY')
            exceed_students = Student.objects.filter(exceedCount=0)
            today_sales = Payment.objects.filter(paymentDate=timezone.localtime(timezone.now()).date())
            total_todaySales = 0
            for sale in today_sales:
                total_todaySales = total_todaySales + sale.price

            attendanceList = Attendance.objects.filter(attendanceDate=timezone.localtime(timezone.now()).date())
            noticeList = Notice.objects.all()
            # render to string
            attendanceList = render_to_string('dashboard/notice_attendance.html',{'attendanceList':attendanceList})
            noticeList = render_to_string('dashboard/notice_notification.html',{'noticeList':noticeList})
            paymentList = render_to_string('dashboard/notice_paymentStudent.html',{'paymentList':payment_students})
            exceedList = render_to_string('dashboard/notice_paymentStudent2.html',{'exceedList':exceed_students})
            todaySales = render_to_string('dashboard/notice_payments.html',{'todaySales':today_sales})
            context.update({
                'is_valid': True,
                'human_students': human_students.count(),
                'payment_students': payment_students.count(),
                'exceed_students': exceed_students.count(),
                'total_todaySales': total_todaySales,
                'attendanceList': attendanceList,
                'noticeList': noticeList,
                'paymentList': paymentList,
                'exceedList': exceedList,
                'todaySales': todaySales,
                'loginUser': self.request.user 
            })
            return context
        except Exception as e:
            print("Error: "+str(e))
            context.update({
                'is_valid': False,
                'errorMsg': "Error: "+str(e) })
            return context
 
class BlankView(TemplateView):
    template_name = "components/blank.html"

    def get_context_data(self, **kwargs):
        context = super(BlankView, self).get_context_data(**kwargs)
        context.update({'title': "Blank Page"})
        return context


class ButtonsView(TemplateView):
    template_name = "components/buttons.html"

    def get_context_data(self, **kwargs):
        context = super(ButtonsView, self).get_context_data(**kwargs)
        context.update({'title': "Buttons"})
        return context


class FlotView(TemplateView):
    template_name = "components/flot.html"

    def get_context_data(self, **kwargs):
        context = super(FlotView, self).get_context_data(**kwargs)
        context.update({'title': "Flot Charts"})
        return context


class FormsView(TemplateView):
    template_name = "components/forms.html"

    def get_context_data(self, **kwargs):
        context = super(FormsView, self).get_context_data(**kwargs)
        context.update({'title': "Forms"})
        return context


class GridView(TemplateView):
    template_name = "components/grid.html"

    def get_context_data(self, **kwargs):
        context = super(GridView, self).get_context_data(**kwargs)
        context.update({'title': "Grid"})
        return context


class IconsView(TemplateView):
    template_name = "components/icons.html"

    def get_context_data(self, **kwargs):
        context = super(IconsView, self).get_context_data(**kwargs)
        context.update({'title': "Icons"})
        return context


class LoginView(TemplateView):
    template_name = "components/login.html"

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context.update({'title': "Log In"})
        return context


class MorrisView(TemplateView):
    template_name = "components/morris.html"

    def get_context_data(self, **kwargs):
        context = super(MorrisView, self).get_context_data(**kwargs)
        context.update({'title': "Morris Charts"})
        return context


class NotificationsView(TemplateView):
    template_name = "components/notifications.html"

    def get_context_data(self, **kwargs):
        context = super(NotificationsView, self).get_context_data(**kwargs)
        context.update({'title': "Notifications"})
        return context


class PanelsView(TemplateView):
    template_name = "components/panels-wells.html"

    def get_context_data(self, **kwargs):
        context = super(PanelsView, self).get_context_data(**kwargs)
        context.update({'title': "Panels and Wells"})
        return context


class TablesView(TemplateView):
    template_name = "components/tables.html"

    def get_context_data(self, **kwargs):
        context = super(TablesView, self).get_context_data(**kwargs)
        context.update({'title': "Tables"})
        return context


class TypographyView(TemplateView):
    template_name = "components/typography.html"

    def get_context_data(self, **kwargs):
        context = super(TypographyView, self).get_context_data(**kwargs)
        context.update({'title': "Typography"})
        return context

