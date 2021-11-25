from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.fields import RichTextField


class Skill(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    score = models.IntegerField(default=80, blank=True, null=True) 
    image = models.FileField(upload_to='skills', blank=True, null=True)
    is_key_skill = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
    
    def __str__(self):
        return self.name 


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar', blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True)
    cv = models.FileField(upload_to='cv', blank=True, null=True)

    class Meta:
        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfiles'
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}' 


class ContactProfile(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, verbose_name='Name')
    email = models.EmailField(verbose_name='Email')
    message = models.TextField(verbose_name='Message')

    class Meta:
        verbose_name = 'Contact Profile'
        verbose_name_plural = 'Contact Profiles'
        ordering = ['timestamp']
    
    def __str__(self):
        return f'{self.name}'


class Testemonial(models.Model):
    thumbnail = models.ImageField(upload_to='thumbnail', blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True) 
    role = models.CharField(max_length=200, blank=True, null=True) 
    quote = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Testemonial'
        verbose_name_plural = 'Testemonials'
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Media(models.Model):
    image = models.ImageField(upload_to='media')
    url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    is_image = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Media'
        verbose_name_plural = 'Media Files'
        ordering = ['name']
    
    def save(self, *args, **kwargs):
        if self.url:
            self.is_image = False
        super(Media, self).save(*args, **kwargs)


class Portfolio(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='portfolio', blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolio Profiles'
        ordering = ['name']
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Portfolio, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        # from django.core.urlresolvers import reverse
        # return reverse('', kwargs={'pk': self.pk})
        return f'/portfolio/{self.slug}'


class Certificate(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Certificate'
        verbose_name_plural = 'Certificates'
    
    def __str__(self):
        return self.name