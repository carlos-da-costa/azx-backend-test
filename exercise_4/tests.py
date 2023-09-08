from . import token_manager

class TestJWTFunctions:

    def test_generate_token(self):
        user_id = 'test_user'
        token = token_manager.generate_token(user_id)

        assert isinstance(token, str)


    def test_verify_token_valid(self):
        user_id = 'test_user'
        token = token_manager.generate_token(user_id)
        verified_user_id = token_manager.verify_token(token)

        assert verified_user_id == user_id

    def test_verify_token_expired(self):
        # Create an expired token (for testing purposes only)
        user_id = 'test_user'
        expired_token = token_manager.generate_token(user_id)
        payload = token_manager.jwt.decode(expired_token, token_manager.SECRET_KEY, algorithms=['HS256'])
        payload['exp'] = 0
        expired_token = token_manager.jwt.encode(payload, token_manager.SECRET_KEY, algorithm='HS256')

        verified_user_id = token_manager.verify_token(expired_token)

        assert verified_user_id is None

    def test_verify_token_invalid(self):
        invalid_token = 'invalid_token'
        verified_user_id = token_manager.verify_token(invalid_token)

        assert verified_user_id is None
