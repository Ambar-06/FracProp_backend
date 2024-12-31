from notification.models.email_template import EmailTemplate
from common.helpers.smtp import send_email
from common.helpers.constants import EmailTypes


class EmailHelper:
    def __init__(self):
        self.email_template_model = EmailTemplate

    def send_template_email(self, template_type, **kwargs):
        template = self.email_template_model.objects.filter(template_type=template_type).first()
        if not template:
            return None
        user = kwargs.get("user")
        email = user.email
        if template.template_type == EmailTypes().OTP:
            otp = kwargs.get("otp")
            content = template.template.replace("{{ otp_code }}", str(otp))
            subject = "Email Verification OTP"
        elif template.template_type == EmailTypes().RESET_PASSWORD:
            link = kwargs.get("link")
            content = template.template.replace("{{ reset_link }}", link)
            subject = "Reset Password Link"
        send_email(subject=subject, body=content, to_email=email)
        return True
