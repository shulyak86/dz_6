def parse_parameters(query: str) -> dict:
    mydict = {}
    if query.find("?") > 0 and not query.endswith('?'):
        query = query[query.find("?") + 1:]
        i = query.split('&')
        listed = []
        for item in i:
            listed.append(item.split('='))
        for item2 in listed:
            mydict[str(item2[0])] = str(item2[1])
    else:
        print("there are no given parameters... or it's not a string you're passing")
    print(mydict)
    return mydict


def parse_cookies(query: str) -> dict:
    mydict = {}
    if type(query) == str and len(query) > 0:
        if query[-1] == ';':    #here just in case of misspelling like 'name=Dima;' - for not to be ruined
            query = query[:-2]
        for item in query.split(';'):
            mydict[str(item.split('=')[0])] = item.split('=')[1]
    else:
        print('pass string of cookies to function!')
    return mydict


if __name__ == '__main__':
# # Tests for function "parse_parameters"
    try:
        assert parse_parameters('http://example.com/?') == {}
        assert parse_parameters('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
        assert parse_parameters('https://rozetka.com.ua/search/?text=%D0%BD%D0%BE%D1%81%D0%BA%D0%B8&class=0&redirected=1')
        assert parse_parameters('https://rozetka.com.ua/search/?text=%D1%88%D1%83%D0%B1%D0%B0')
        assert parse_parameters('https://ru.wikipedia.org/wiki/Is_This_the_Life_We_Really_Want%3F')
    except AssertionError as msg:
        print(str(msg) + 'Something went wrong (AssertionError) - no parameters')

# Tests for function "parse_cookies"
    try:
        assert parse_cookies('') == {}
        assert parse_cookies('name=Dima;') == {'name': 'Dima'}
        assert parse_cookies('name=Dima; name3=Dima3; nam=Dim') == {'name': 'Dima', ' name3': 'Dima3', ' nam': 'Dim'}
        assert parse_cookies('text=%D0%BD%D0%BE%D1%81%D0%BA%D0%B8; class=0; redirected=1') == {'text': '%D0%BD%D0%BE%D1%81%D0%BA%D0%B8', ' class': '0', ' redirected': '1'}
        assert parse_cookies('session-id=132-3545307-1067335; ubid-main=131-0251619-4211802; clouddc=east2; AKA_A2=A; ak_bmsc=DC91D5B56119480B03F9039473ADC7+t8AQAA0tc0Lg0pj6IglAXScM4LIs1VodMGTpYy2sZyqT')
    except AssertionError as msg:
        print(str(msg) + 'Something went wrong (AssertionError) - no cookies')

