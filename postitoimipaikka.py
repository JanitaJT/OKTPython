import json


def hae_parit():
    f = open('postcode.json',)
    postcode = json.load(f)

    return postcode


def etsi_haettava_postitoimipaikka():
    postinumero = input('Anna postinumero: ')
    numerot = hae_parit()
    if postinumero in numerot:
        print(numerot[postinumero].title())
    else:
        print('Postitoimipaikkaa ei löytynyt.')


if __name__ == '__main__':
    etsi_haettava_postitoimipaikka()
