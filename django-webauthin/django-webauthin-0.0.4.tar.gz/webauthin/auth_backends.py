import base64

import webauthn
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site

from .models import AuthData

ICON = "https://example.com/"


class WebAuthinBackend:
    def get_user(self, user_id):
        """Get a user by their primary key."""
        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    def authenticate(self, request, credential_id, data=None):
        """Authenticate a user given a signed token."""
        challenge = request.session.get("challenge")
        if not challenge:
            return None

        auth_data = AuthData.objects.filter(credential_id=data["id"]).first()
        if not auth_data:
            return None

        site = get_current_site(request)

        webauthn_user = webauthn.WebAuthnUser(
            user_id=base64.b64encode(str(auth_data.user.id).encode()).decode(),
            username=auth_data.user.get_username(),
            display_name="User",
            icon_url=ICON,
            credential_id=auth_data.credential_id,
            public_key=auth_data.public_key,
            sign_count=auth_data.sign_count,
            rp_id=site.domain,
        )

        webauthn_assertion_response = webauthn.WebAuthnAssertionResponse(
            webauthn_user, data, challenge, "https://%s" % site.domain, uv_required=True
        )

        try:
            sign_count = webauthn_assertion_response.verify()
        except Exception:
            return None

        # TODO: Validate the sign count here (https://w3c.github.io/webauthn/#signature-counter)
        auth_data.set_sign_count(sign_count)
        return auth_data.user
