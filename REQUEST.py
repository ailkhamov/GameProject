import requests



def take_postcode(postcode):
    response_post_code = requests.get('http://api.postcodes.io/postcodes/' + postcode)
    print(type(response_post_code))
    retrieve_data = response_post_code.json()
    print(type(retrieve_data))
    my_postcode = retrieve_data ['result']['postcode']
    return str(my_postcode)

def write_to_file(file,postcode):
    try:
        with open(file, 'a') as opened_file:
            opened_file.write(postcode + '\n')
    except FileNotFoundError:
        print("File not found")

    return print(opened_file)

postcode = str(take_postcode("HA55NZ"))


write_to_file('postcode.txt',postcode)

