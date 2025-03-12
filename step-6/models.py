class CourseInfo(models.Model):
    user = models.ForeignKey(User, on_delete-models.CASCADE)
    course_name = models.CharField(max_length=1000)
    slug = models.SlugField(max_length=250, null = True, blank=True)
    course_category = (
        ('development', 'Development'),
        ('business', 'Business'),
        ('finance & accounting', 'Finance & Accounting'),
        ('it & software', 'IT & Software'),
        ('marketing', 'Marketing'),
    )
    category = models.CharField(max_length=1000, choices=course_category, default='development')
    
    def _str_(self):
        return self.course_name
    
def course_slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = course_slug(instance)

pre_save.connect(course_slug_generator, sender = CourseInfo)
