import pytest
from pgpy import PGPKey, PGPMessage
from pgpy.errors import PGPError

from django_pgpy.helpers import hash_password
from django_pgpy.models import Identity
from test_app.models import EncryptedMessage


@pytest.mark.django_db
class TestUserIdentity:
    def test_protect(self, user_test_data):
        test_data = user_test_data
        uid_1 = Identity.objects.create(test_data.user_1, None)

        assert uid_1.private_key.is_protected is False
        uid_1.protect('1234567890')
        assert uid_1.private_key.is_protected

        with uid_1.unlock('1234567890'):
            assert uid_1.private_key.is_unlocked

    def test_unlock(self, user_identity_test_data):
        test_data = user_identity_test_data

        with test_data.uid_1.unlock(test_data.pwd_user_1):
            assert test_data.uid_1.private_key.is_unlocked

    def test_private_key(self, user_identity_test_data):
        test_data = user_identity_test_data

        priv_key_1 = test_data.uid_1.private_key
        assert isinstance(priv_key_1, PGPKey)

        priv_key_2 = test_data.uid_1.private_key
        assert priv_key_1 == priv_key_2

    def test_public_key(self, user_identity_test_data):
        test_data = user_identity_test_data

        pub_key_1 = test_data.uid_1.public_key
        assert isinstance(pub_key_1, PGPKey)

        pub_key_2 = test_data.uid_1.public_key
        assert pub_key_1 == pub_key_2

    def test_set_secret(self, user_test_data):
        test_data = user_test_data

        uid_1 = Identity.objects.create(test_data.user_1, None)

        uid_1.set_secret('test')
        assert uid_1.secret_blob.startswith('-----BEGIN PGP ')

    def test_get_secret(self, user_identity_test_data):
        test_data = user_identity_test_data

        with test_data.uid_1.unlock(test_data.pwd_user_1):
            secret = test_data.uid_2.get_secret(test_data.uid_1)
            with test_data.uid_2.private_key.unlock(secret):
                assert test_data.uid_2.private_key.is_unlocked

    def test_decrypt(self, encrypted_message_test_data):
        test_data = encrypted_message_test_data

        assert test_data.uid_1.decrypt(test_data.enc_text_1, test_data.pwd_user_1) == test_data.text_1
        assert test_data.uid_1.decrypt(test_data.enc_text_3, test_data.pwd_user_1) == test_data.text_3

        # decrypt with protected key
        with pytest.raises(PGPError):
            test_data.uid_1.decrypt(test_data.enc_text_1)

        # decrypt a message with wrong UID
        with pytest.raises(PGPError):
            test_data.uid_1.decrypt(test_data.enc_text_2)

    def test_unlock_private_key(self, user_identity_test_data):
        test_data = user_identity_test_data

        assert test_data.uid_2.private_key.is_protected

        alg, password = hash_password(test_data.pwd_user_2, test_data.uid_2.hash_info)
        with test_data.uid_2.private_key.unlock(password):
            assert test_data.uid_2.private_key.is_unlocked

    def test_change_password(self, user_identity_test_data):
        test_data = user_identity_test_data

        old_password = test_data.pwd_user_2
        new_password = '1234567890'
        uid = test_data.uid_2

        with uid.unlock(old_password):
            assert uid.private_key.is_unlocked

        uid = Identity.objects.get(id=uid.id)
        uid.change_password(old_password, new_password)

        uid = Identity.objects.get(id=uid.id)
        with uid.unlock(new_password):
            assert uid.private_key.is_unlocked

        # fallback still works
        # uid_1 = test_data.uid_1
        # _, uid_1_password_hash = hash_password(test_data.pwd_user_1, uid_1.hash_info)
        # with test_data.uid_1.private_key.unlock(uid_1_password_hash):

    def test_password_reset(self, user_identity_test_data):
        test_data = user_identity_test_data

        new_password = '1234567890'
        uid_admin = test_data.uid_1
        uid_user = test_data.uid_2

        reset_request = uid_user.reset_password(new_password)

        uid_user = Identity.objects.get(id=uid_user.id)
        assert uid_user.can_decrypt is False

        reset_request.reset_password(uid_admin, test_data.pwd_user_1)

        uid_user = Identity.objects.get(id=uid_user.id)
        uid_admin = Identity.objects.get(id=uid_admin.id)

        assert uid_user.can_decrypt

        with uid_user.unlock(new_password):
            assert uid_user.private_key.is_unlocked

        with uid_admin.unlock(test_data.pwd_user_1):
            secret = uid_user.get_secret(uid_admin)

            with uid_user.private_key.unlock(secret):
                assert uid_user.private_key.is_unlocked

    def test_add_restorers(self, user_identity_test_data):
        test_data = user_identity_test_data

        uid_admin = test_data.uid_1
        uid_user = test_data.uid_2
        new_user =  test_data.uid_4


        uid_user = Identity.objects.get(id=uid_user.id)
        assert new_user not in uid_user.encrypters.all()

        uid_user.add_restorers(test_data.pwd_user_2, [new_user])
        assert new_user in uid_user.encrypters.all()
        assert uid_admin in uid_user.encrypters.all()

        with new_user.unlock(test_data.pwd_user_4):
            secret = uid_user.get_secret(new_user)

            with uid_user.private_key.unlock(secret):
                assert uid_user.private_key.is_unlocked

        with uid_admin.unlock(test_data.pwd_user_1):
            secret = uid_user.get_secret(uid_admin)

            with uid_user.private_key.unlock(secret):
                assert uid_user.private_key.is_unlocked

class TestEncryptedMessage:

    def test_create(self, user_identity_test_data):
        test_data = user_identity_test_data

        encrypters = [test_data.uid_1]
        enc_msg = EncryptedMessage.objects.create('1234567890', encrypters)
        assert enc_msg.text.startswith('-----BEGIN PGP MESSAGE-----')
        assert [e.id for e in enc_msg.encrypters.all()] == [e.id for e in encrypters]

        with test_data.uid_1.unlock(test_data.pwd_user_1):
            assert test_data.uid_1.private_key.is_unlocked

            m = test_data.uid_1.private_key.decrypt(PGPMessage.from_blob(enc_msg.text))
            assert m.message == '1234567890'

        with test_data.uid_2.unlock(test_data.pwd_user_2):
            assert test_data.uid_2.private_key.is_unlocked

            with pytest.raises(PGPError):
                test_data.uid_2.private_key.decrypt(PGPMessage.from_blob(enc_msg.text))

    def test_encrypt(self, user_identity_test_data):
        test_data = user_identity_test_data

        encrypters = [test_data.uid_1]
        enc_msg = EncryptedMessage()
        enc_msg.encrypt('1234567890', encrypters)

        assert enc_msg.text.startswith('-----BEGIN PGP MESSAGE-----')
        assert [e.id for e in enc_msg.encrypters.all()] == [e.id for e in encrypters]

        with test_data.uid_1.unlock(test_data.pwd_user_1):
            assert test_data.uid_1.private_key.is_unlocked

            m = test_data.uid_1.private_key.decrypt(PGPMessage.from_blob(enc_msg.text))
            assert m.message == '1234567890'

        with test_data.uid_2.unlock(test_data.pwd_user_2):
            assert test_data.uid_2.private_key.is_unlocked

            with pytest.raises(PGPError):
                test_data.uid_2.private_key.decrypt(PGPMessage.from_blob(enc_msg.text))

    def test_decrypt(self, encrypted_message_test_data):
        test_data = encrypted_message_test_data

        with test_data.uid_1.unlock(test_data.pwd_user_1):
            assert test_data.enc_text_1.decrypt(test_data.uid_1) == test_data.text_1
            assert test_data.enc_text_3.decrypt(test_data.uid_1) == test_data.text_3

            with pytest.raises(PGPError):
                test_data.enc_text_2.decrypt(test_data.uid_1)

        with test_data.uid_2.unlock(test_data.pwd_user_2):
            assert test_data.enc_text_2.decrypt(test_data.uid_2) == test_data.text_2
            assert test_data.enc_text_3.decrypt(test_data.uid_2) == test_data.text_3

            with pytest.raises(PGPError):
                test_data.enc_text_1.decrypt(test_data.uid_2)

    def test_add_encrypter(self, add_remove_encrypter_test_data):
        test_data = add_remove_encrypter_test_data

        with test_data.uid_2.unlock(test_data.pwd_user_2):
            with pytest.raises(PGPError):
                test_data.enc_text_1.decrypt(test_data.uid_2)

        test_data.enc_text_1.add_encrypters(test_data.uid_1,
                                            test_data.pwd_user_1,
                                            [test_data.uid_2])

        with test_data.uid_2.unlock(test_data.pwd_user_2):
            enc_msg = EncryptedMessage.objects.get(id=test_data.enc_text_1.id)
            assert enc_msg.decrypt(test_data.uid_2) == test_data.text_1

        assert test_data.enc_text_3.encrypters.filter(id=test_data.uid_3.id).exists() is False
        with test_data.uid_3.unlock(test_data.pwd_user_3):
            with pytest.raises(PGPError):
                test_data.enc_text_3.decrypt(test_data.uid_3)

        test_data.enc_text_3.add_encrypters(test_data.uid_2,
                                            test_data.pwd_user_2,
                                            [test_data.uid_3])

        with test_data.uid_3.unlock(test_data.pwd_user_3):
            enc_msg = EncryptedMessage.objects.get(id=test_data.enc_text_3.id)
            assert enc_msg.decrypt(test_data.uid_3) == test_data.text_3

            assert enc_msg.encrypters.filter(id=test_data.uid_3.id).exists()

    def test_remove_encrypter(self, add_remove_encrypter_test_data):
        test_data = add_remove_encrypter_test_data

        assert test_data.enc_text_3.encrypters.filter(id=test_data.uid_2.id).exists()

        test_data.enc_text_3.remove_encrypters([test_data.uid_2])

        with test_data.uid_2.unlock(test_data.pwd_user_2):
            enc_msg = EncryptedMessage.objects.get(id=test_data.enc_text_3.id)
            assert enc_msg.encrypters.filter(id=test_data.uid_2.id).exists() is False
            with pytest.raises(PGPError):
                assert enc_msg.decrypt(test_data.uid_2) == test_data.text_3
