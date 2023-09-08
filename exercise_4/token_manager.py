from flask import cli
import jwt
import datetime

import click

SECRET_KEY = 'TDwvUH65ls'
EXPIRATION_TIME_MINUTES = 30

def generate_token(user_id):
    '''
    Generates a JWT token for an authenticated user.

    :param user_id: Unique identifier for the user.
    :return: JWT token as a string.
    '''
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=EXPIRATION_TIME_MINUTES)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def verify_token(token):
    '''
    Verifies the validity of a JWT token.

    :param token: JWT token to be verified.
    :return: User ID if the token is valid, None if invalid.
    '''
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload.get('user_id')
    except jwt.ExpiredSignatureError:
        # Token has expired
        return None
    except jwt.DecodeError:
        # Token is invalid
        return None


@click.group()
def commands():
    pass

@click.command()
@click.argument('user_id')
def generate(user_id: str):
    generated_token = generate_token(user_id)
    click.echo(f'Generated Token: {generated_token}')


@click.command()
@click.argument('token')
def verify(token:str):
    verified_user_id = verify_token(token)
    if verified_user_id:
        click.echo(f'Verified User ID: {verified_user_id}')
    else:
        click.echo('Token is invalid or expired')


commands.add_command(generate)
commands.add_command(verify)

if __name__ == '__main__':
    # provides a full CLI to interact with the JWT funcions
    commands()