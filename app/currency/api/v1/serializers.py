from rest_framework import serializers

from currency.models import Rate, Source, ContactUs


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = [
            'id',
            'buy',
            'sale',
            'created',
            'source',
            'currency',
        ]


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = [
            'id',
            'source_url',
            'name',
            'number',
        ]


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = [
            'id',
            'name',
            'email_from',
            'subject',
            'message',
        ]

    def create(self, validated_data):
        instance = super(ContactUsSerializer, self).create(validated_data)
        subject = 'User ContactUs'
        message = f'''
            Request from: {instance.name}.
            Reply to email: {instance.email_from}.
            Subject: {instance.subject}.
            Body: {instance.message}.
        '''
        from currency.tasks import send_mail
        send_mail.apply_async(
            kwargs={'subject': subject, 'message': message},
        )
        return instance
