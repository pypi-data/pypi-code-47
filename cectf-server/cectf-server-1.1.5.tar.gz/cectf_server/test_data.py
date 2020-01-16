''' A user with the contestant role. '''
contestant = {
    'id': 1,
    'username': 'contestant',
    'email': 'contestant@ctf.chiquito.us',
    'password': 'contestant'
}
''' A user with the admin role. '''
admin = {
    'id': 2,
    'username': 'admin',
    'email': 'admin@ctf.chiquito.us',
    'password': 'admin'
}
''' A user with no fields in common with the other users. This user is not created in the test configuration. '''
new_user = {
    'username': 'n00b',
    'email': 'n00b@ctf.chiquito.us',
    'password': 'p4ssw0rd'
}
''' A list of challenges. The fourth challenge is not created in the test configuration. '''
challenges = [
    {
        'id': 1,
        'title': 'The First Challenge',
        'category': 'crypto',
        'author': 'ad4m',
        'body': 'The answer is CECTF{1}',
        'solution': 'CECTF{1}'
    },
    {
        'id': 2,
        'title': 'The Second Challenge',
        'category': 'reversing',
        'author': 'ev3',
        'body': 'The answer is CECTF{2}',
        'solution': 'CECTF{2}'
    },
    {
        'id': 3,
        'title': 'The Third Challenge',
        'category': 'web',
        'author':'c4rl0s',
        'body': 'The answer is CECTF{3}',
        'solution': 'CECTF{3}',
        'previousChallenge': 2
    },
    {
        'id': 4,
        'title': 'The Fourth Challenge',
        'category': 'binary',
        'author':'d4ni3l',
        'body': 'The answer is CECTF{4}',
        'solution': 'CECTF{4}'
    }
]
