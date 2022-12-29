# Third party imports.
from rest_framework import serializers

# Local application imports
from blog.models.minister_models import Profile


class MinisterProfile(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'image')
