""" Avatar utilities """

def generate_avatar_url(name: str):
    """ Generate avatar url """
    return str('https://avatar.oxro.io/avatar.svg?name={}&length=1&caps=1').format(
        name[0]
    )
