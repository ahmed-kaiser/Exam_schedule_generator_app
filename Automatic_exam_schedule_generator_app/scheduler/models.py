from django.db import models

class Rooms(models.Model):
    room_no = models.IntegerField()
    room_capacity = models.IntegerField()

#....CSE.....

class CSE_eve_trimister(models.Model):
    dept = models.CharField(max_length = 5, null=True, blank=True)
    trimister =  models.IntegerField(primary_key=True)

class CSE_eve_batch_info(models.Model):
    batch_no = models.IntegerField()
    section = models.CharField(max_length = 10)
    st_number = models.IntegerField()
    trimister = models.ForeignKey(CSE_eve_trimister, on_delete=models.CASCADE, null=True)

    def save(self, force_insert=False, force_update=False):
        self.section = self.section.upper()
        super(CSE_eve_batch_info, self).save(force_insert=False, force_update=False)

class CSE_eve_course_list(models.Model):
    course_code = models.CharField(max_length = 20)
    course_name = models.CharField(max_length = 100)
    trimister = models.ForeignKey(CSE_eve_trimister, on_delete=models.CASCADE, null=True)

    def save(self, force_insert=False, force_update=False):
        self.course_code = self.course_code.upper()
        self.course_name = self.course_name.title()
        super(CSE_eve_course_list, self).save(force_insert=False, force_update=False)

class CSE_day_trimister(models.Model):
    dept = models.CharField(max_length = 5, null=True, blank=True)
    trimister =  models.IntegerField(primary_key=True)

class CSE_day_batch_info(models.Model):
    batch_no = models.IntegerField()
    section = models.CharField(max_length = 10)
    st_number = models.IntegerField()
    trimister = models.ForeignKey(CSE_day_trimister, on_delete=models.CASCADE, null=True)

    def save(self, force_insert=False, force_update=False):
        self.section = self.section.upper()
        super(CSE_day_batch_info, self).save(force_insert=False, force_update=False)

class CSE_day_course_list(models.Model):
    course_code = models.CharField(max_length = 20)
    course_name = models.CharField(max_length = 100)
    trimister = models.ForeignKey(CSE_day_trimister, on_delete=models.CASCADE, null=True)

    def save(self, force_insert=False, force_update=False):
        self.course_code = self.course_code.upper()
        self.course_name = self.course_name.title()
        super(CSE_day_course_list, self).save(force_insert=False, force_update=False)

#....EEE......

class EEE_eve_trimister(models.Model):
    dept = models.CharField(max_length = 5, null=True, blank=True)
    trimister =  models.IntegerField(primary_key=True)

class EEE_eve_batch_info(models.Model):
    batch_no = models.IntegerField()
    section = models.CharField(max_length = 10)
    st_number = models.IntegerField()
    trimister = models.ForeignKey(EEE_eve_trimister, on_delete=models.CASCADE, null=True)

    def save(self, force_insert=False, force_update=False):
        self.section = self.section.upper()
        super(EEE_eve_batch_info, self).save(force_insert=False, force_update=False)

class EEE_eve_course_list(models.Model):
    course_code = models.CharField(max_length = 20)
    course_name = models.CharField(max_length = 100)
    trimister = models.ForeignKey(EEE_eve_trimister, on_delete=models.CASCADE, null=True)

    def save(self, force_insert=False, force_update=False):
        self.course_code = self.course_code.upper()
        self.course_name = self.course_name.title()
        super(EEE_eve_course_list, self).save(force_insert=False, force_update=False)

class EEE_day_trimister(models.Model):
    dept = models.CharField(max_length = 5, null=True, blank=True)
    trimister =  models.IntegerField(primary_key=True)

class EEE_day_batch_info(models.Model):
    batch_no = models.IntegerField()
    section = models.CharField(max_length = 10)
    st_number = models.IntegerField()
    trimister = models.ForeignKey(EEE_day_trimister, on_delete=models.CASCADE, null=True)

    def save(self, force_insert=False, force_update=False):
        self.section = self.section.upper()
        super(EEE_day_batch_info, self).save(force_insert=False, force_update=False)

class EEE_day_course_list(models.Model):
    course_code = models.CharField(max_length = 20)
    course_name = models.CharField(max_length = 100)
    trimister = models.ForeignKey(EEE_day_trimister, on_delete=models.CASCADE, null=True)

    def save(self, force_insert=False, force_update=False):
        self.course_code = self.course_code.upper()
        self.course_name = self.course_name.title()
        super(EEE_day_course_list, self).save(force_insert=False, force_update=False)

#.....CEN.....

class CEN_eve_trimister(models.Model):
    dept = models.CharField(max_length = 5, null=True, blank=True)
    trimister =  models.IntegerField(primary_key=True)

class CEN_eve_batch_info(models.Model):
    batch_no = models.IntegerField()
    section = models.CharField(max_length = 10)
    st_number = models.IntegerField()
    trimister = models.ForeignKey(CEN_eve_trimister, on_delete=models.CASCADE, null=True)

    def save(self, force_insert=False, force_update=False):
        self.section = self.section.upper()
        super(CEN_eve_batch_info, self).save(force_insert=False, force_update=False)

class CEN_eve_course_list(models.Model):
    course_code = models.CharField(max_length = 20)
    course_name = models.CharField(max_length = 100)
    trimister = models.ForeignKey(CEN_eve_trimister, on_delete=models.CASCADE, null=True)

    def save(self, force_insert=False, force_update=False):
        self.course_code = self.course_code.upper()
        self.course_name = self.course_name.title()
        super(CEN_eve_course_list, self).save(force_insert=False, force_update=False)

class CEN_day_trimister(models.Model):
    dept = models.CharField(max_length = 5, null=True, blank=True)
    trimister =  models.IntegerField(primary_key=True)

class CEN_day_batch_info(models.Model):
    batch_no = models.IntegerField()
    section = models.CharField(max_length = 10)
    st_number = models.IntegerField()
    trimister = models.ForeignKey(CEN_day_trimister, on_delete=models.CASCADE, null=True)

    def save(self, force_insert=False, force_update=False):
        self.section = self.section.upper()
        super(CEN_day_batch_info, self).save(force_insert=False, force_update=False)

class CEN_day_course_list(models.Model):
    course_code = models.CharField(max_length = 20)
    course_name = models.CharField(max_length = 100)
    trimister = models.ForeignKey(CEN_day_trimister, on_delete=models.CASCADE, null=True)

    def save(self, force_insert=False, force_update=False):
        self.course_code = self.course_code.upper()
        self.course_name = self.course_name.title()
        super(CEN_day_course_list, self).save(force_insert=False, force_update=False)

#.....CEN.....

class BTE_eve_trimister(models.Model):
    dept = models.CharField(max_length = 5, null=True, blank=True)
    trimister =  models.CharField(primary_key=True, max_length = 15)

class BTE_eve_batch_info(models.Model):
    batch_no = models.IntegerField()
    section = models.CharField(max_length = 10)
    st_number = models.IntegerField()
    trimister = models.ForeignKey(BTE_eve_trimister, on_delete=models.CASCADE, null=True)

    def save(self, force_insert=False, force_update=False):
        self.section = self.section.upper()
        super(BTE_eve_batch_info, self).save(force_insert=False, force_update=False)

class BTE_eve_course_list(models.Model):
    course_code = models.CharField(max_length = 20)
    course_name = models.CharField(max_length = 100)
    trimister = models.ForeignKey(BTE_eve_trimister, on_delete=models.CASCADE, null=True)

    def save(self, force_insert=False, force_update=False):
        self.course_code = self.course_code.upper()
        self.course_name = self.course_name.title()
        super(BTE_eve_course_list, self).save(force_insert=False, force_update=False)

class BTE_day_trimister(models.Model):
    dept = models.CharField(max_length = 5, null=True, blank=True)
    trimister =  models.CharField(primary_key=True, max_length = 15)

class BTE_day_batch_info(models.Model):
    batch_no = models.IntegerField()
    section = models.CharField(max_length = 10)
    st_number = models.IntegerField()
    trimister = models.ForeignKey(BTE_day_trimister, on_delete=models.CASCADE, null=True)

    def save(self, force_insert=False, force_update=False):
        self.section = self.section.upper()
        super(BTE_day_batch_info, self).save(force_insert=False, force_update=False)

class BTE_day_course_list(models.Model):
    course_code = models.CharField(max_length = 20)
    course_name = models.CharField(max_length = 100)
    trimister = models.ForeignKey(BTE_day_trimister, on_delete=models.CASCADE, null=True)

    def save(self, force_insert=False, force_update=False):
        self.course_code = self.course_code.upper()
        self.course_name = self.course_name.title()
        super(BTE_day_course_list, self).save(force_insert=False, force_update=False)

#.....Routine.....

class EVE_routine(models.Model):
    course_code= models.CharField(max_length=10, null=True, blank=True)
    course_name = models.CharField(max_length=100, null=True, blank=True)
    dept = models.CharField(max_length=10, null=True, blank=True)
    batch = models.IntegerField(null=True, blank=True)
    section = models.CharField(max_length=5, null=True, blank=True)
    total_st = models.IntegerField(null=True, blank=True)
    st_number = models.IntegerField(null=True, blank=True)
    room = models.IntegerField(null=True, blank=True)
    exam_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    weekday = models.CharField(max_length=15, null=True, blank=True)
    exam_time = models.CharField(max_length=15, null=True, blank=True)

class DAY_routine(models.Model):
    course_code= models.CharField(max_length=10, null=True, blank=True)
    course_name = models.CharField(max_length=100, null=True, blank=True)
    dept = models.CharField(max_length=10, null=True, blank=True)
    batch = models.IntegerField(null=True, blank=True)
    section = models.CharField(max_length=5, null=True, blank=True)
    total_st = models.IntegerField(null=True, blank=True)
    st_number = models.IntegerField(null=True, blank=True)
    room = models.IntegerField(null=True, blank=True)
    exam_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    weekday = models.CharField(max_length=15, null=True, blank=True)
    exam_time = models.CharField(max_length=15, null=True, blank=True)

class publish(models.Model):
    batch = models.CharField(primary_key = True, max_length = 10, blank=True)
    trimister = models.CharField(max_length = 10, null=True, blank=True)
    term = models.CharField(max_length = 10, null=True, blank=True)
    pub_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)