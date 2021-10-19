from django.db import models


class Agent(models.Model):

    discord_username = models.CharField(max_length=37)
    github_username = models.CharField(max_length=39, blank=True, null=True)
    twitter_username = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.discord_username
