from django.contrib import admin

from group.models import Teacher, Student, Group

# Register your models here.

admin.site.register(Teacher)
# admin.site.register(Student)
# admin.site.register(Group)

@admin.register(Student)
class Students(admin.ModelAdmin):
    list_display = ('student_name', 'groups_list',)

    def student_name(self,obj):
        return obj

    def groups_list(self, obj):
        # print(obj.id, obj.name, obj.last_name, obj.age, obj.contacts)
        # print(obj.groups.all(), '!!!!!!!!!!!!')
        return [x for x in obj.groups.all()]



@admin.register(Group)
class Groups(admin.ModelAdmin):
    list_display = ('title', 'teacher','count_students','list_of_students')

    def count_students(self,obj):
        qt = obj.students.count()
        return qt

    def list_of_students(self, obj):
        ls = [x for x in obj.students.all()]
        return ls
